import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_default_secret_key")
    DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///my_database.db")

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    SECRET_KEY = os.environ.get("SECRET_KEY")
