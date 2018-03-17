from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
from app import app, models, db
from .forms import UserForm, TripForm
from .models import *

import sys


@app.route('/index')
def index():
    if 'user_name' in session: #check if the user is already in session, if so, direct the user to trips.html
        user_name = session.get('user_name')
        return render_template('trips.html', name=user_name)
    else:
        return render_template('login.html')

# @app.route('/create_user', methods=['GET', 'POST'])
# def create_user():
#     form = UserForm()
#     if form.validate_on_submit():
#         # Get data from the form
#         user_name = form.user_name.data
#         password = form.password.data
#         # Send data from form to Database
#         insert_users(user_name,password)
#         return redirect('/index')
#     return render_template('index.html', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user_name'] = request.form['user_name']
        session['password'] = request.form['password']
    return redirect(url_for('display_trips'))

@app.route('/logout')
def logout():
    session.pop('user_name', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/user')
def display_user():
    # Retreive data from database to display
    user = retrieve_users()
    print(user)
    return render_template('index.html',
                            user=user)

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    print("TRying to create a trip...", file = sys.stderr)
    trip_form = TripForm()
    print("Form created...", file = sys.stderr)
    if trip_form.validate_on_submit():
        # Get data from the form
        print("Validate on submit....", file = sys.stderr)
        trip_name = trip_form.trip_name.data
        destination = trip_form.destination.data
        # Send data from form to Database
        status = insert_trips(trip_name,destination)
        print(status, file = sys.stderr)
        return redirect('/trips')
    return render_template('create_trip.html', trip_form=trip_form)

@app.route('/trips')
def display_trips():
    # Retreive data from database to display
    trips = retrieve_trips()
    print(trips, file = sys.stderr)
    return render_template('trips.html',
                            trips=trips)



#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(data)
#         models.insert_customer(data['first_name'], data['last_name'], data['company'], data['email'], data['phone'])
#         print "jello"
#         form.validate_on_submit()
#         # Get data from the form
#         # Send data from form to Database
#         print "asdfasdfasdfasdf"
#         return redirect('/customers')
#     return render_template('customer.html', form=form)


# @app.route('/customers')
# def display_customer():
#     orders = models.retrieve_orders()
#     customers = models.retrieve_customers()
#     # Retreive data from database to display
#     return render_template('home.html',
#                             customers=customers,
#                             orders=orders,
#                             )

# @app.route('/create_order/<value>', methods=['GET', 'POST'])
# def create_order(value):
#     # Get data from the form
#     # Send data from form to Database
#     # return redirect('/customers')
#     form = OrderForm()
#     print(form)
#     print(form.errors)
#     if request.method == "POST":
#         data = request.form.to_dict()
#         print(data)
#         models.insert_order(data['name_of_part'], data['manufacturer_of_part'])
#         if form.is_submitted():
#             print "order form done"
#         return redirect('/customers')
#     return render_template('order.html', form=form)

# @app.route('/orders')
# def display_order():
#     customers = models.retrieve_customers()
#     orders = models.retrieve_orders()
#     # Retreive data from database to display
#     return render_template('home.html',
#                             orders=orders, customers=customers)