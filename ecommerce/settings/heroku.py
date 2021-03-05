import environ

from ecommerce.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)

SECRET_KEY = ENV('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db(),
}