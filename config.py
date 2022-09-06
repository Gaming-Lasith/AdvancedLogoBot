from os import environ

class Config(object):
        API_ID = int(environ.get("API_ID"))
        API_HASH = environ.get("API_HASH")
        BOT_TOKEN = environ.get("BOT_TOKEN")
        BOT_USERNAME = environ.get("BOT_USERNAME")
        BOT_NAME = environ.get("BOT_NAME")
        F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")
