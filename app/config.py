import os

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
sql_connect_string = os.getenv("SQL_CONNECT_STRING")

base_url = 'https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={item_id}'

timeout = 1800
# timeout = 2

admin_tg_id = 5312665858

