import os
from .base import *  # noqa: F401, F403

ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = False
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": "postgres",
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": "5432",
    }
}