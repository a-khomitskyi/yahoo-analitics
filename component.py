import csv
from os import listdir
import sqlite3


FILES = [x.replace('.csv', '') for x in listdir('yahoo_data')]  # List of csv files names


def rename_headers():
	"""
	Need to rename column name in csv as one word ( for PostgreSQL )
	:return: *.csv with header 'Adj Close' that replaced on 'Adj_Close'
	"""
	for file in FILES:
		r_file = open(f'/yahoo_data/{file}.csv')
		lines = r_file.readlines()
		lines[0] = lines[0].replace('Adj Close', 'Adj_Close')
		with open(f'yahoo_data/{file}.csv', 'w') as f:
			f.writelines(lines)
		r_file.close()


def db_connect():
	"""Function connect to DB"""
	return sqlite3.connect('identifier.sqlite')


def create_db_tables():
	""" Creating tables in DB using sql-script """
	conn = db_connect()
	cur = conn.cursor()
	f = open('initialize.sql')
	script = f.read()
	f.close()
	try:
		cur.executescript(script)
	except:
		print('Tables exists!')


def insert_data_to_db():
	"""	Method to add data from existing *.csv files to the database tables	"""
	conn = db_connect()
	cur = conn.cursor()

	for file in FILES:
		cur.execute(f'SELECT 1 from {file.lower()}')
		if cur.fetchone() is None:
			with open(f'yahoo_data/{file}.csv', 'r') as f:
				reader = csv.DictReader(f)
				to_db = [(x['Date'], x['Open'], x['High'], x['Low'], x['Close'], x['Adj_Close'], x['Volume']) for x in reader]
				cur.executemany(f"INSERT INTO {file} VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
		else:
			print(f'Data from {file} already exists')
	# Close connection
	conn.commit()
	conn.close()