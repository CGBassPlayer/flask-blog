import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nzKEV_6DH2HQsmMb6wj-zw'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    HUMAN_LOGFILE = os.path.join('logs/flask.log')
    MACHINE_LOGFILE = os.path.join('logs/ingest/flask.json.log')
    LOG_BACKTRACE = False
    LOG_LEVEL = 'INFO'


class ProductionConfig(Config):
    """ PASSWORD RESET MAILING """
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get('EMAIL_USER')
    # MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    """ MYSQL DATABASE SERVER """
    # MYSQL_HOST = os.environ.get('DB_HOST')
    # MYSQL_USER = os.environ.get('DB_USER')
    # MYSQL_PASSWORD = os.environ.get('DB_PASS')
    # MYSQL_DB = os.environ.get('DB')


class TestingConfig(Config):
    """ MYSQL DATABASE TESTING SERVER """
    # MYSQL_HOST =
    # MYSQL_USER =
    # MYSQL_PASSWORD =
    # MYSQL_DB =


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    TEMPLATE_AUTO_RELOAD = True
    """ SQLITE DEVELOPMENT FILE """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    LOG_BACKTRACE = True
    LOG_LEVEL = 'DEBUG'
