import psycopg2
from os import listdir
import json
import datetime

files = [x.replace('.csv', '') for x in listdir('yahoo_data')]


def rename_headers():
	for file in files:
		r_file = open(f'yahoo_data/{file}.csv')
		lines = r_file.readlines()
		lines[0] = lines[0].replace('Adj Close', 'Adj_Close')
		with open(f'yahoo_data/{file}.csv', 'w') as f:
			f.writelines(lines)
		r_file.close()


def insert_data_to_db():
	conn = psycopg2.connect(
		'host=chunee.db.elephantsql.com dbname=qdljldfw user=qdljldfw password=TPKALru4l7bcPn2hpOz4nhKNp2hmxOQi')
	cur = conn.cursor()

	for file in files:
		with open(f'/home/mizzantrop/Desktop/yahoo_data/{file}.csv', 'r') as f:
			next(f)  # Skip the header row.
			# f , <database name>, Comma-Seperated
			cur.copy_from(f, f'{file.lower()}', sep=',')
			# Add new column as PK with name ID
			cur.execute(f'ALTER TABLE {file.lower()} ADD COLUMN ID SERIAL PRIMARY KEY;')
			conn.commit()
	# Close connection
	conn.close()


if __name__ == '__main__':
	# rename_headers()
	insert_data_to_db()
	pass