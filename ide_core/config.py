import os


class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost").split(",")

    DB_NAME = os.environ.get("POSTGRES_DB")
    DB_HOST = os.environ.get("POSTGRES_HOST")
    DB_USER = os.environ.get("POSTGRES_USER")
    DB_PASS = os.environ.get("POSTGRES_PASSWORD")

    SOURCE_MAX_LIMIT = int(os.environ.get("SOURCE_MAX_LIMIT", 40 * 1024))
    INPUT_MAX_LIMIT = int(os.environ.get("INPUT_MAX_LIMIT", 1 * 1024))
