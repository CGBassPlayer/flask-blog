import logging

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

from webapp.config import ProductionConfig

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def create_app(configuration=ProductionConfig):
    app = Flask(__name__)
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True
    app.config.from_object(configuration)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    logger.start(app.config['MACHINE_LOGFILE'],
                 level=app.config['LOG_LEVEL'],
                 backtrace=app.config['LOG_BACKTRACE'],
                 rotation='25 MB',
                 format="",
                 serialize=True)
    logger.start(app.config['HUMAN_LOGFILE'],
                 level=app.config['LOG_LEVEL'],
                 backtrace=app.config['LOG_BACKTRACE'],
                 format="{time} | {level.icon} | {name}:{line} - {function} | {message} | {extra}",
                 rotation='50 MB')
    app.logger.addHandler(InterceptHandler())

    from webapp.main.routes import main
    from webapp.users.routes import users
    from webapp.posts.routes import posts
    from webapp.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    return app
