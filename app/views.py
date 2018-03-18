from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
from app import app, models, db
from .forms import UserForm, TripForm
from .models import *

import sys


@app.route('/index', methods = ['GET', 'POST'])
def index():
    if 'user_name' in session: #check if the user is already in session, if so, direct the user to trips.html
        user_name = session.get('user_name')
        return render_template('trips.html', name=user_name)
    else:
        user_form = UserForm()
        return render_template('login.html', user_form=user_form)

# @app.route('/create_user', methods=['GET', 'POST'])
# def create_user():
#     form = UserForm()
#     if form.validate_on_submit():
#         # Get data from the form
#         user_name = form.user_name.data
#         password = form.password.data
#         # Send data from form to Database
#         insert_user(user_name,password)
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

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    print("Trying to signup a user...", file = sys.stderr)
    user_form = UserForm()
    print("UserForm created...", file = sys.stderr)
    if user_form.validate_on_submit():
        # Get data from the form
        print("Validate on submit....", file = sys.stderr)
        user_name = user_form.user_name.data
        password = user_form.password.data
        # Send data from form to Database
        status = insert_user(user_name,password)
        print(status, file = sys.stderr)
        return redirect('/login')
    return render_template('login.html', user_form=user_form) 

@app.route('/users', methods=['GET', 'POST'])
def display_users():
    # Retreive data from database to display
    print("trying to display users...", file = sys.stderr)
    users = retrieve_users()
    print("users are..." + users, file = sys.stderr)
    print(users)
    return render_template('index.html',
                            users=users)

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


@app.route('/delete_trip', methods=['GET', 'POST'])
def delete_trip():
    print("Hi!", file = sys.stderr)
    trip = request.form["trip_id"]
    print("Trip id to delete:" + trip, file = sys.stderr)
    remove_trip(trip)
    return redirect(url_for('display_trips'))
