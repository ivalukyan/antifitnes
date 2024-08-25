import os
from dotenv import load_dotenv


load_dotenv()


# DJANGO
class Django:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        self.debug = os.getenv("DEBUG")


# POSTGRES
class Postgres:
    def __init__(self):
        self.engine = os.getenv("POSTGRES_ENGINE")
        self.db = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self.host = os.getenv("POSTGRES_HOST")
        self.port = os.getenv("POSTGRES_PORT")


HOST_PROD = os.getenv('HOST_PROD')
