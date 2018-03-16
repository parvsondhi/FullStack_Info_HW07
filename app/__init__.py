from flask import Flask
from config import Config
# from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) # instance
app.config.from_object(Config)

from app import routes # app directory module
# from app import views, models

# app.config.from_object('config')
# db = SQLAlchemy(app)
