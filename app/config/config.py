import os
from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent.parent
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"


class DevConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", 
        f"sqlite:///{Config.BASE_DIR / 'instance/dev.db'}"
    )


class TestConfig(Config):
    FLASK_ENV = "testing"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL", 
        f"sqlite:///{Config.BASE_DIR / 'instance/test.db'}"
    )


class ProdConfig(Config):
    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", 
        f"sqlite:///{Config.BASE_DIR / 'instance/prod.db'}"
    )


config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProdConfig,
    "default": DevConfig
} 