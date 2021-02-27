import os

# Import the base settings
from .base import *

DEBUG = os.environ["DEBUG"]
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = ["157.245.249.94"]
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
