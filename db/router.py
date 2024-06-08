import psycopg2


conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'")
cursor = conn.cursor()
