import os
from dotenv import find_dotenv, load_dotenv
from .base import *  # noqa: F401, F403

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "postgres",
        "PORT": "5432",
    }
}
