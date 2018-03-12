import os
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO: Environment variables should be read from an .env file

SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
