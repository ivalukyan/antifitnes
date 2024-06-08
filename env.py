import os
from dotenv import load_dotenv


load_dotenv()

# Переменные
TOKEN = os.getenv('TOKEN')
ADMINS = os.getenv('ADMIN')
