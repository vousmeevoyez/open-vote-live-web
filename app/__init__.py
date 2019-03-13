"""
    Flask APP
"""
from flask  import Flask
from raven.contrib.flask import Sentry


from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler
from os import path

from app.config import config

sentry = Sentry()

def register_extensions(app):
    if not app.debug and not app.testing:
        sentry.init_app(app)
        
def register_blueprints(app):
    for module_name in ['vote']:
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)

def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())

def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='static')
    app.config.from_object(config.CONFIG_BY_NAME[config_name])

    register_extensions(app)
    register_blueprints(app)
    configure_logs(app)
    return app
