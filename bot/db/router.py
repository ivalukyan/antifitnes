import psycopg2
from env import Postgres

postgres = Postgres()

conn = psycopg2.connect(f"dbname={postgres.db} user={postgres.user} host={postgres.host} port={postgres.port} password={postgres.password}")
cursor = conn.cursor()
