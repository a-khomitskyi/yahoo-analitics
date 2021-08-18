from flask import Flask, jsonify, make_response, request
import psycopg2
from main import files

app = Flask(__name__)

def get_content_from_DB(name):
	conn = psycopg2.connect('host=chunee.db.elephantsql.com dbname=qdljldfw user=qdljldfw password=TPKALru4l7bcPn2hpOz4nhKNp2hmxOQi')
	cur = conn.cursor()

	cur.execute(f"SELECT array_to_json(array_agg(row_to_json (r))) FROM (SELECT id, date, round(open::numeric, 6) as open, round(high::numeric, 6) as high, round(low::numeric, 6) as low, round(close::numeric, 6) as close, round(adj_close::numeric, 6) as adj_close, volume FROM {name}) r;")
	res = cur.fetchone()[0]
	# Close connection
	conn.close()
	return res


@app.route('/api/<string:comp>', methods=['GET'])
def get_route(comp):
	if comp.upper() in files:
		return jsonify(get_content_from_DB(comp))
	else:
		return make_response(jsonify({'error': 'Not correct route'}), 404)


if __name__ == '__main__':
	app.run(debug=True)