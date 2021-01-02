import os
# Import the base settings
from .base import *
from dotenv import find_dotenv, load_dotenv

DEBUG = True
load_dotenv(find_dotenv())
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ['DATABASE_NAME'],
        "USER": os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': "localhost",
        "PORT": "5432",
    }
}
