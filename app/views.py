from flask import render_template, redirect, request, session
from app import app, models
from .forms import *
from .models import *

# Access the models file to use SQL functions


@app.route('/')
def index():
    if 'username' in session:
        return redirect('/trips')
    else:
        return redirect('/new_user')

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        username = form.username.data
        password = form.password.data

        success = insert_user(username, password)
        if success:
            session['username'] = username
            return redirect('/trips')
        else:
            return redirect('/new_user')
    return render_template('signup.html', form=form)

@app.route('/trips')
def display_user():
    # Retreive data from database to display
    if 'username' not in session:
        redirect('/new_user')
    else:
        username = session['username']
        trips = get_trips(username)
        return render_template('trips.html',
                            username=username, trips=trips)

@app.route('/create_trip/<value>', methods=['GET', 'POST'])
def create_trip(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        order_data = [name_of_part, manufacturer_of_part, value]
        order_id = insert_order(order_data)
        insert_customer_order(order_id, value)
        return redirect('/customers')
    return render_template('create_trip.html', form=form)
