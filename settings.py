import os
import dotenv

dotenv.load_dotenv('.env')

DEVMAN_TOKEN = os.environ['DEVMAN_TOKEN']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

