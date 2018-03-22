from __future__ import print_function
from app import app
import models
import sys
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
from forms import TripForm

#Make database sqlite3 app.db < schema.sql

app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'


@app.route('/')
@app.route('/index' )
def index():
    username = ''
    # username = session['username']
    if username in session: #check if the user is already in session, if so, direct the user to trips.html Hint: render_template with a variable
            trips = models.retrieve_trips()
            return render_template('trips.html')

        # return render_template('trips.html', username=username)
    else:
        # return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/login', methods=['POST', 'GET']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == 'POST':
        # username = session['username']
        # password = session['password']
        username = request.form['username']
        password = request.form['password']
        models.insert_users( username, password)
        return render_template('trips.html', username=username)
    else:
        return redirect(url_for('index'))
        # return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

#users can create trips
@app.route('/create_trip', methods=['POST', 'GET'])
def create_trip():
    # tripform = TripForm()
    if request.method == 'POST':
        trip_name  = request.form['trip_name']
        destination  = request.form['destination']
        models.insert_trip(trip_name, destination)
        # return render_template('trips.html')
        return redirect(url_for('display_trip'))
    return render_template('create_trip.html')

# @app.route('/trips', methods=['POST', 'GET'])
# def submit_trip():
#     # form = TripForm()
#     # if form.validate_on_submit:
#     #     trip_name = form.trip_name.data
#     #     destination = form.destination.data
#     #     travel_pal = form.pal.data

#     #     trip_id = insert_trip(trip_name, destination)
#     #     return redirect('trips')
#     return render_template('create_trip.html', form=form)

#display users trips
@app.route('/trips', methods=['POST', 'GET'])
def display_trip():
    if request.method == 'GET':
    # Retreive data from database to display
        trips = models.retrieve_trips()
        return render_template('trips.html', trips=trips)
    else:
        return render_template('trips.html')



@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
