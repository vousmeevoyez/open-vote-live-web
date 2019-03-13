from os import environ
from sys import exit

from app import create_app

app = create_app(environ.get('ENVIRONMENT', 'dev'))