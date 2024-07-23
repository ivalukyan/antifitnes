import psycopg2
from env import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST


conn = psycopg2.connect(f"dbname={POSTGRES_DB} user={POSTGRES_USER} host='localhost' password={POSTGRES_PASSWORD}")
cursor = conn.cursor()
