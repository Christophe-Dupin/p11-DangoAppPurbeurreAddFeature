import os
from dotenv import find_dotenv, load_dotenv
from .base import *  # noqa: F401, F403

ALLOWED_HOSTS = ["*"]
load_dotenv(find_dotenv())
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv('DATABASE_NAME', default=""),
        "USER": os.getenv('DATABASE_USER', default=""),
        "PASSWORD": os.getenv('DATABASE_PASSWORD', default=""),
        'HOST': "localhost",
        "PORT": "5432",
    }
}
