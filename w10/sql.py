import psycopg2

conn1=psycopg2.connect("dbname=postgres user=postgres password=superuser123")

'''def get_connection():
	try:
		return psycopg2.connect(
			database="postgres",
			user="postgres",
			password="Adventure",
			host="localhost",
			#port=5432,
		)
	except:
		return False

conn = get_connection()

if conn:
	print("Connection to the PostgreSQL established successfully.")
else:
	print("Connection to the PostgreSQL encountered and error.")
	'''
	#conn = psycopg2.connect(dbname='postgres', user='postgres', password='Adventure', host='localhost')

