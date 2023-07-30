from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "9583161"
API_HASH = "aecf9e2b7c655c4f916564ab6d598a73"
BOT_TOKEN = "6223135275:AAHdvscM8m9QQrc9Ol8Qu4HmaYKJ8HAMWng"
BOT_UN = "GGGGGGGGGGGG88888888888888888BOT"

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
