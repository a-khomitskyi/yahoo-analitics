from os import listdir
import psycopg2


files = [x.replace('.csv', '') for x in listdir('yahoo_data')]  # get names of csv files


def rename_headers():
	"""
	Need to rename column name in csv as one word
	:return: *.csv with header 'Adj Close' that replaced on 'Adj_Close'
	"""
	for file in files:
		r_file = open(f'yahoo_data/{file}.csv')
		lines = r_file.readlines()
		lines[0] = lines[0].replace('Adj Close', 'Adj_Close')
		with open(f'yahoo_data/{file}.csv', 'w') as f:
			f.writelines(lines)
		r_file.close()


def insert_data_to_db():
	"""
	Method to add data from existing *.csv files to the database tables
	:return 1 if work finished correctly
	"""
	conn = psycopg2.connect(
		'host=chunee.db.elephantsql.com dbname=qdljldfw user=qdljldfw password=TPKALru4l7bcPn2hpOz4nhKNp2hmxOQi')
	cur = conn.cursor()

	for file in files:
		with open(f'/home/mizzantrop/Desktop/yahoo_data/{file}.csv', 'r') as f:
			next(f)  # Skip the header row.
			# f , <database name>, Comma-Seperated
			cur.copy_from(f, f'{file.lower()}', sep=',')
			conn.commit()
	# Close connection
	conn.close()
	return 1