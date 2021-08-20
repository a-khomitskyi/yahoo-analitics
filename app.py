from flask import Flask, jsonify, make_response
from component import *


app = Flask(__name__)


def get_content_from_table(name):
	"""
	:param name: Must be name of existing table in our DB
	:return: All the data that collected from current DB table
	"""
	conn = db_connect()
	conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
	cur = conn.cursor()
	# Correction of accuracy of floating point numbers
	rows = cur.execute(f"SELECT * FROM {name};").fetchall()
	conn.commit()
	# Close connection
	conn.close()
	return [dict(ix) for ix in rows]


# Forming json response with all the data from DB (list(dict<table_name: table_data>))
@app.route('/api/', methods=['GET'])
def json_response_all_data():
	content = []
	for i in FILES:
		name = i
		content.append({
			name: get_content_from_table(name)
		})
	return jsonify(content)


# Forming json response with all the data from table (list(dict<column_name: column_data>))
@app.route('/api/<string:comp>/', methods=['GET'])
def current_json_response(comp):
	# route exist
	if comp.upper() in FILES:
		return jsonify(get_content_from_table(comp.upper()))
	# route not exist
	else:
		return make_response(jsonify({'error': 'Not correct route!'}), 404)


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not correct route!'}), 404)


if __name__ == '__main__':
	create_db_tables()
	insert_data_to_db()
	app.run(debug=False)