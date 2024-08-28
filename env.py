import os
from dotenv import load_dotenv


load_dotenv()


# BOT
class BotEnv:
    def __init__(self):
        self.token = os.getenv("TOKEN")
        self.admin = os.getenv("ADMIN")


# URL
class Urls:
    def __init__(self):
        self.all_users = os.getenv("ALL_USERS_URL")
        self.admin_panel = os.getenv("ADMIN_PANEL")
        self.profile_url = os.getenv("PROFILE_URL")


# CRM
class Crm:
    def __init__(self):
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")
        self.bearer = os.getenv("BEARER_TOKEN")
        self.company_id = os.getenv("CID")
        self.user = os.getenv("USER_TOKEN")


# DJANGO
class Django:
    def __init__(self):
        self.secret_key = os.getenv("SECRET_KEY")
        self.debug = os.getenv("DEBUG")


# POSTGRES
class Postgres:
    def __init__(self):
        self.engine = os.getenv("POSTGRES_ENGINE")
        self.db = os.getenv("POST_DB")
        self.user = os.getenv("POST_USER")
        self.password = os.getenv("POST_PASSWORD")
        self.host = os.getenv("POST_HOST")
        self.port = os.getenv("POST_PORT")


HOST_PROD = os.getenv('HOST_PROD')
