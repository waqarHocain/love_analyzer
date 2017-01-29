# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

# local imports
from config import app_config


# initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
	app = Flask(__name__, instance_relative_config = True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile("config.py")

	db.init_app(app)

	login_manager.init_app(app)
	login_manager.login_message = "You need to log in to access this page"
	login_manager.login_view = "auth.login"

	Bootstrap(app)

	from app import models

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix="/auth")

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	return app
