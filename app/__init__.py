from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # instance
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # app directory module
# from app import views, models

# app.config.from_object('config')
# db = SQLAlchemy(app)
