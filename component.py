from os import listdir
import psycopg2
from config import *


FILES = [x.replace('.csv', '') for x in listdir('yahoo_data')]  # List of csv files names


def rename_headers():
	"""
	Need to rename column name in csv as one word
	:return: *.csv with header 'Adj Close' that replaced on 'Adj_Close'
	"""
	for file in FILES:
		r_file = open(f'yahoo_data/{file}.csv')
		lines = r_file.readlines()
		lines[0] = lines[0].replace('Adj Close', 'Adj_Close')
		with open(f'yahoo_data/{file}.csv', 'w') as f:
			f.writelines(lines)
		r_file.close()


def db_connect():
	"""Function connect to DB"""
	return psycopg2.connect(f'host={host} dbname={dbname} user={user} password={password}')


def insert_data_to_db():
	"""	Method to add data from existing *.csv files to the database tables	"""
	conn = db_connect()
	cur = conn.cursor()

	for file in FILES:
		cur.execute(f'SELECT 1 from {file.lower()}')
		if cur.fetchone() is None:
			with open(f'/yahoo_data/{file}.csv', 'r') as f:
				next(f)  # Skip the header row.
				# f , <database name>, Comma-Seperated
				cur.copy_from(f, f'{file.lower()}', sep=',')
				conn.commit()
		else:
			print(f'Data from {file} already exists')
	# Close connection
	conn.close()