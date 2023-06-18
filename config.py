from pathlib import Path
from os import getenv
from dotenv import load_dotenv

env_path = Path(__file__).parents[1].joinpath('env')
load_dotenv(env_path)


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_FOLDER = 'app/templates'

    # ##### настройка Flask-Mail #####
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = getenv('MAIL_USERNAME') or 'YOU_MAIL@gmail.com'
    # MAIL_DEFAULT_SENDER = MAIL_USERNAME
    # MAIL_PASSWORD = getenv('MAIL_PASSWORD') or 'password'


class DevelopementConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = getenv('DEVELOPMENT_DATABASE_URI')


class TestingConfig(BaseConfig):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = getenv('TESTING_DATABASE_URI')


class ProductionConfig(BaseConfig):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = getenv('PRODUCTION_DATABASE_URI')
