from flask import Flask # Flask Object
from config import Config # Config Object
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # database version control
from flask_login import LoginManager, UserMixin # login functions and userclass defaults

app = Flask(__name__) # instance
app.config.from_object(Config) # pulls values from config.py
db = SQLAlchemy(app) # db instance
migrate = Migrate(app, db) # migrate db version object
login = LoginManager(app) # login control for app
login.login_view = 'login'

from app import routes, models # app directory module

app.config.from_object('config')
