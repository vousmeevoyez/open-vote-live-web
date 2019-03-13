"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os

class Config:
    """ This is base class for configuration """
    DEBUG = False
    SENTRY_CONFIG = {}


    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER') or "mongodb", # sqlite // postgresql // mysql
        "HOST_NAME": os.getenv('DB_HOSTNAME') or "localhost",
        "DB_NAME"  : os.getenv('DB_NAME') or "live_count",
        "DB_PORT"  : os.getenv('DB_PORT') or "27017",
    }
    TIMEOUT = 10 # second time out
    #BASE_URL = "http://34.80.69.106:5000/api/v1"
    BASE_URL = os.getenv("API_URL") or "http://127.0.0.1:5000/api/v1"
    ROUTES = {
        "LOGIN"  : "/auth/login",
        "LOGOUT" : "/auth/logout",
        "CANDIDATES" : "/elections/{}/candidates/",
        "VOTE"       : "/votes/{}"
    }
#end class

class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}/{}_dev".format(DATABASE["DRIVER"],
                                       DATABASE["HOST_NAME"],
                                       DATABASE["DB_PORT"],
                                       DATABASE["DB_NAME"])
#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}/{}_testing".format(DATABASE["DRIVER"],
                                       DATABASE["HOST_NAME"],
                                       DATABASE["DB_PORT"],
                                       DATABASE["DB_NAME"])
#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = False

    DATABASE = Config.DATABASE
    MONGO_URI = "{}://{}:{}/{}_prod".format(DATABASE["DRIVER"],
                                       DATABASE["HOST_NAME"],
                                       DATABASE["DB_PORT"],
                                       DATABASE["DB_NAME"])

    SENTRY_CONFIG = Config.SENTRY_CONFIG
    SENTRY_CONFIG["dsn"] = os.environ.get("SENTRY_DSN")
#end class

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

