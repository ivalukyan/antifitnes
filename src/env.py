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
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
USER_TOKEN = os.getenv('USER_TOKEN')
CID = int(os.getenv('CID'))
