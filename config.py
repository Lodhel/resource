import os
import pytz


TIMEZONE = pytz.timezone('Europe/Moscow')


class Configuration:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_URL = os.getenv('SERVER_URL')
