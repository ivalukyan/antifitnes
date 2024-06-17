import os
from dotenv import load_dotenv


load_dotenv()

# Переменные
TOKEN = os.getenv('TOKEN')
ADMINS = os.getenv('ADMIN')
ALL_USERS_URL = os.getenv('ALL_USERS_URL')
ADMIN_PANEL = os.getenv('ADMIN_PANEL')
PROFILE_URL = os.getenv('PROFILE_URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
USER_TOKEN = os.getenv('USER_TOKEN')
CID = int(os.getenv('CID'))
