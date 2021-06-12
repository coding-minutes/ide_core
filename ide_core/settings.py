from dotenv import load_dotenv
from pathlib import Path
from ide_core.config import Config

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = Config.SECRET_KEY

DEBUG = Config.DEBUG

ALLOWED_HOSTS = Config.ALLOWED_HOSTS

INSTALLED_APPS = [
    "corsheaders",
    "rest_framework",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

ROOT_URLCONF = "ide_core.urls"

WSGI_APPLICATION = "ide_core.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer",]
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "https://ide.codingminutes.com",
]
