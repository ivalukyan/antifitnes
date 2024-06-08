import psycopg2


conn = psycopg2.connect("dbname='bot' user='postgres' host='localhost' password='postgres'")
cursor = conn.cursor()
