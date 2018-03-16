from flask import render_template, redirect, request
from app import app, models, db
from flask_login import LoginManager, UserMixin
# from .forms import
# from .models import

# flask-login
# https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# user model
class User(UserMixin):

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.password = self.name + "_secret"

    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

    

# @app.route('/')
# def index():
    # return redirect('/login')

# @app.login('/login')
# def login():

# @app.trips('/trips')
# def show_trips():

# @app.route('/create_trip')
# def create_trip():

# @app.route('/delete_trip')
# def delete_trip():
