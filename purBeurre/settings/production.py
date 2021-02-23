import os

# Import the base settings
from .base import *
from dotenv import find_dotenv, load_dotenv

DEBUG = False
load_dotenv(find_dotenv())
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ["157.245.249.94"]
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT"),
    }
}
