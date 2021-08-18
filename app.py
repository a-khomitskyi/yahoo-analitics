from flask import Flask, jsonify, make_response
import psycopg2
import main

app = Flask(__name__)

def get_content_from_table(name):
	"""
	:param name: Must be name of existing table in our DB
	:return: All the data that collected from current DB table
	"""
	conn = psycopg2.connect('host=chunee.db.elephantsql.com dbname=qdljldfw user=qdljldfw password=TPKALru4l7bcPn2hpOz4nhKNp2hmxOQi')
	cur = conn.cursor()
	# Correction of accuracy of floating point numbers
	cur.execute(f"SELECT array_to_json(array_agg(row_to_json (r))) FROM (SELECT date, round(open::numeric, 6) as open, round(high::numeric, 6) as high, round(low::numeric, 6) as low, round(close::numeric, 6) as close, round(adj_close::numeric, 6) as adj_close, volume FROM {name}) r;")
	# Get the result after executing sql query
	res = cur.fetchone()[0]
	# Close connection
	conn.close()
	return res


# Forming json response with all the data from DB (list(dict<table_name: table_data>))
@app.route('/api', methods=['GET'])
def json_responce_all_data():
	content = []
	for i in main.files:
		name = i
		content.append({
			name: get_content_from_table(i.lower())
		})
	return jsonify(content)


# Forming json response with all the data from table (list(dict<column_name: column_data>))
@app.route('/api/<string:comp>', methods=['GET'])
def current_json_responce(comp):
	# route exist
	if comp.upper() in main.files:
		return jsonify(get_content_from_table(comp))
	# route not exist
	else:
		return make_response(jsonify({'error': 'Not correct route'}), 404)


if __name__ == '__main__':
	# main.rename_headers()
	if main.insert_data_to_db() == 1:
		app.run(debug=True)
	else:
		raise Exception('Something wrong...')
