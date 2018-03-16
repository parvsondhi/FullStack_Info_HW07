import flask
from flask import Flask, render_template, redirect, request, url_for
from app import app, models, db
import flask_login
from flask_login import LoginManager, UserMixin
# from .forms import
# from .models import

##### flask-login #####
# https://flask-login.readthedocs.io/en/latest/
login_manager = LoginManager()
login_manager.init_app(app)

## TESTING - REPLACE WITH SECURE PASSWORD MATCHING
users = {'foobar': {'password': 'secret'}}

# user model
class User(UserMixin):
    """ Base User class inherited from UserMixin """
    pass

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@login_manager.user_loader
def user_loader(username):
    """ Creates the User object """
    if username not in users:
        return

    user = User()
    user.id = username
    return user

@login_manager.request_loader
def request_loader(request):
    """ Creates User object and validates password """
    username = request.form.get('username')
    if username not in users:
        return

    user = User()
    user.id = username

    ## TESTING - REPLACE WITH SECURE PASSWORD MATCHING
    user.is_authenticated = request.form['password'] == users[username]['password']

    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    """ Bad login handler """
    return 'Unauthorized'

###### ROUTES #####

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():

    ## Display form on request
    if flask.request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='username' id='username' placeholder='username'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    ## create user object and authenticate
    username = flask.request.form['username']
    if flask.request.form['password'] == users[username]['password']:
        user = User()
        user.id = username
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    ## else error
    return 'Bad login'

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

# @app.trips('/trips')
# def show_trips():

# @app.route('/create_trip')
# def create_trip():

# @app.route('/delete_trip')
# def delete_trip():
