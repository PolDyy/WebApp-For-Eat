import redis
from pathlib import Path
from os import getenv
from dotenv import load_dotenv

env_path = Path(__file__).parents[1].joinpath('env')
load_dotenv(env_path)


class BaseConfig:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TEMPLATES_FOLDER = 'app/templates'
    JSON_AS_ASCII = False

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

    SESSION_REDIS = redis.StrictRedis(host='0.0.0.0', port=6379, db=0)


class DevelopementConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

