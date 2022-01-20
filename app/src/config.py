import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

postgres_local_base =  os.getenv('PG_DATABASE_URL')
# postgres_local_base = os.environ['DATABASE_URL


class Config:

    SECRET_KEY = os.getenv('SECRET_KEY', 'siri-kali-sana-msee')
    DEBUG = False
    TOKEN_EXPIRE_HOURS = 1000
    CELERY_BROKER_URL = os.getenv('REDIS_URL')
    CELERY_RESULT_BACKEND = os.getenv('REDIS_URL')
    REDIS_URL = os.getenv('REDIS_URL')

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
