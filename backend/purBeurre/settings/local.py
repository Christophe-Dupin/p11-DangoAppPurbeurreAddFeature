import os

# Import the base settings
from .base import *

DEBUG = True
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": {
        "ENGINE": os.environ["POSTGRES_ENGINE"],
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": os.environ["POSTGRES_HOST"],
        "PORT": os.environ["POSTGRES_PORT"],
    }
}
