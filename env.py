import os
from dotenv import load_dotenv


load_dotenv()

# BOT
TOKEN = os.getenv('TOKEN')
ADMINS = os.getenv('ADMIN')

# URLS
ALL_USERS_URL = os.getenv('ALL_USERS_URL')
ADMIN_PANEL = os.getenv('ADMIN_PANEL')
PROFILE_URL = os.getenv('PROFILE_URL')

# CRM
LOGIN = os.getenv('LOGIN')  # Логин  от системы в CRM
PASSWORD = os.getenv('PASSWORD')  # Пароль от системы в CRM
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
USER_TOKEN = os.getenv('USER_TOKEN')
CID = int(os.getenv('CID'))  # Form ID

# DJANGO
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
POSTGRES_ENGINE = os.getenv('POSTGRES_ENGINE')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
