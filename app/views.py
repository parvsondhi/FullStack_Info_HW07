from __future__ import print_function
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
from app import app, models, db
from .forms import UserForm, TripForm
from .models import *

import sys


@app.route('/', methods = ['GET', 'POST'])
def index():
    if 'user_name' in session: #check if the user is already in session, if so, direct the user to trips.html
        #user_name = session.get('user_name')
        #return render_template('trips.html', name=user_name)
        return redirect(url_for('display_trips'))
    else:
        user_form = UserForm()
        return render_template('login.html', user_form=user_form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        validation = recognize_user(user_name, password)
        if validation is True:
            session['user_name'] = user_name
            session['password'] = password
            return redirect(url_for('display_trips'))
        else:
            error = 'Invalid username or password. Please try again!'
            user_form = UserForm()
        return render_template('login.html', user_form=user_form, error=error)
    return redirect(url_for('index'))

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
        session['user_name'] = user_form.user_name.data
        session['password'] = user_form.password.data
        # Send data from form to Database
        status = insert_user(session['user_name'], session['password'])
        print(status, file = sys.stderr)
        return redirect('/login')
    return render_template('login.html', user_form=user_form)


@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    # print("TRying to create a trip...", file = sys.stderr)
    trip_form = TripForm()
    users = retrieve_users()
    print("Form created...", file = sys.stderr)
    if trip_form.validate_on_submit():
        # Get data from the form
        # print("Validate on submit....", file = sys.stderr)
        trip_name = trip_form.trip_name.data
        destination = trip_form.destination.data
        users = [session['user_name'],
                trip_form.friend.data]  # myself and my friendss
        # Send data from form to Database
        status = insert_trips(trip_name,destination,users)
        print(status, file = sys.stderr)
        return redirect('/trips')
    return render_template('create_trip.html', trip_form=trip_form, users=users)

@app.route('/trips')
def display_trips():
    # Retreive data from database to display
    this_user_name = session.get('user_name')
    trips = []
    if this_user_name is None:
        print("Must have a user name to get access to trips!")
        # TODO: tell this to the user!
    else:
        trips = retrieve_trips(this_user_name)
        print(trips, file = sys.stderr)
        if trips is None:
            trips = []
    return render_template('trips.html',
                            trips=trips, user_name=this_user_name)


@app.route('/delete_trip', methods=['GET', 'POST'])
def delete_trip():
    # print("Hi!", file = sys.stderr)
    trip = request.form["trip_id"]
    # print("Trip id to delete:" + trip, file = sys.stderr)
    remove_trip(trip)
    return redirect(url_for('display_trips'))
