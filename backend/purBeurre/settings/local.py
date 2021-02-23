import os

# Import the base settings
from .base import *
from dotenv import find_dotenv, load_dotenv

DEBUG = True
load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": "5432",
    }
}
