from flask import render_template, redirect, request, url_for, flash
from app import app, models, db, login
from .forms import TripForm, LoginForm, SignUpForm
from .models import *
from flask_login import current_user, login_user, logout_user
from app.models import User
from flask_login import login_required

@app.route('/')
def index():
    # return redirect('/create_trip')
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if check_username_exists(username):
            flash("Username already exists. Please pick a different one.")
            return render_template('signup.html', title = "Sign Up", form = form)
        create_user(username, email, password)
        login_user(user)
        return redirect(url_for('index'))
    return render_template('signup.html', title = "Sign Up", form = form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User(username)

        if user is None or not user.check_password(password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)


@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        destination = form.destination.data
        friend = form.friend.data
        insert_trip(destination, friend)
        return redirect('/trip_detail') 

    return render_template('trips.html', form = form) # this is what gets called without form

@app.route('/trip_detail')
def display_trip():
    # trips = retrieve_trips()
    # return render_template('home.html', trips = trips)
    return render_template('TripDetail.html')

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'

# @login.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized'

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/index')

# @app.route('/create_order/<value>', methods=['GET', 'POST'])
# def create_order(value):
#     form = OrderForm()
#     if form.validate_on_submit():
#         name_of_part = form.name_of_part.data
#         manufacturer_of_part = form.manufacturer_of_part.data
#         insert_order(name_of_part, manufacturer_of_part, value)
#         order_id = retrieve_order_id()
#         insert_customer_order(value, order_id)
#         return redirect('/customers')
#     return render_template('order.html', form = form)
