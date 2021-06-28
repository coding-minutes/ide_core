import os


class Config:
    DEBUG = os.environ.get("DEBUG") in ["True", "true", "1", 1]
    SECRET_KEY = os.environ.get("SECRET_KEY", "abc")
    ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

    DB_NAME = os.environ.get("DB_NAME")
    DB_HOST = os.environ.get("DB_HOST")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")

    SOURCE_MAX_LIMIT = int(os.environ.get("SOURCE_MAX_LIMIT", 40 * 1024))
    INPUT_MAX_LIMIT = int(os.environ.get("INPUT_MAX_LIMIT", 1 * 1024))
