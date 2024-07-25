import psycopg2
from env import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST


# conn = psycopg2.connect(f"dbname={POSTGRES_DB} user={POSTGRES_USER} host={POSTGRES_HOST} password={POSTGRES_PASSWORD}")
conn = psycopg2.connect('postgresql://gen_user:W%2CMkd)Q4VPm0X%3C@147.45.247.128:5432/default_db')
cursor = conn.cursor()
