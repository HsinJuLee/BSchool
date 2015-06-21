import os

class Config(object):
    DEBUG = False
    SECRET_KEY = 'it_is_going_to_be_changed'
    DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
