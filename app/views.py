from flask import render_template, redirect, request, session
from app import app, models, db
from .forms import *
# Access the models file to use SQL functions
from .models import *

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        users = retrieve_username()
        user_id = check_up(username, password)
        if user_id:
            session['user_id'] = user_id
            return redirect('/trips')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        users = check_user(username);
        if not users:
            return render_template('signup.html', form=form)
        else:
            user_id = sign_up(username, password)
            session['user_id'] = user_id
            return redirect('/trips')
        
    return render_template('signup.html', form=form)

@app.route('/trips')
def trips():
    # Retreive trips for this user from DB
    if "user_id" in session:
        user_id = session["user_id"]

        trips = retrieve_trips(user_id)
        return render_template('trips.html', trips=trips)
    return redirect("/login")

@app.route('/add', methods=['POST', 'GET'])
def add():
    form = AddTripForm()
    form.friend.choices = [(user["userid"], user["username"]) for user in retrieve_users()]
    if form.validate_on_submit():
        trip_name = form.trip_name.data
        destination = form.destination.data
        friend = form.friend.data

        add_trip(trip_name, destination, session["user_id"], friend)
        return redirect('/trips')

    return render_template('add.html', form=form)


@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html', customers=customers, orders=orders)

@app.route('/remove/<value>', methods=['GET', 'POST'])
def remove(value):
    remove_trip(value)
    return redirect('/trips')
