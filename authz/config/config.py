from os import environ
from pickle import NONE


class Config:
    ############### Application Config ###############
    ENV = environ.get("TECHLAND_AUTHZ_ENV", "production")
    DEBUG = bool(int(environ.get("TECHLAND_AUTHZ_DEBUG", "0")))
    TESTING = bool(int(environ.get("TECHLAND_AUTHZ_TESTING", "0")))
    SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY","HARD-HARD-HARD-SECRET-KEY")
    TIMEZONE = environ.get("TECHLAND_AUTHZ_TIMEZONE", "Asia/Tehran")
    
    ############### Database Config ###############
    SQLALCHEMY_DATABASE_URI =  environ.get("TECHLAND_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

    ############### User Config ###############
    USER_DEFAULT_ROLE = environ.get("TECHLAND_AUTH_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("TECHLAND_AUTH_USER_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(environ.get("TECHLAND_AUTH_USER_DEFAULT_STATUS", "3"))