import os
from os import environ
from os import getenv

class Config(object):
        APP_ID = int(os.environ.get("APP_ID"))
        API_HASH = os.environ.get("API_HASH")
        BOT_TOKEN = os.environ.get("BOT_TOKEN")
        BOT_USERNAME = os.environ.get("BOT_USERNAME")
        BOT_NAME = os.environ.get("BOT_NAME")
        F_SUB_CHANNEL = os.environ.get("F_SUB_CHANNEL")
        STICKER_ID = os.environ.get("STICKER_ID")
