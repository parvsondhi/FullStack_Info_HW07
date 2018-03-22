from app import app
import models
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
from forms import TripForm
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index' )
def index():
    username = ''
    if 'username' in session: #check if the user is already in session, if so, direct the user to trips.html Hint: render_template with a variable
        username = session['username']
        "Logged in as " + username + "<br>" + \
        "<b><a href = '/logout'>Click here to log out</a></b>"
        return render_template('trips.html', username=username)
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST', 'GET']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

#users can create trips
@app.route('/createTrip')
def create_trip():
    form = TripForm()
    username = session['username']
    # if'username' in session:
    #     trip_name = form.trip_name.data
    #     destination = form.destination.data
    #     models.insert_trip(trip_name, destination)
    #
    #     # surveyResponse = {}
    #     # surveyResponse['trip_name'] = request.form.get('trip_name')
    #     # surveyResponse['destination'] = request.form.get('destination')
    #     return redirect(url_for('trips'))
    return render_template('create_trip.html', form=form, username=username)

#cancel from create trips
@app.route('/trips')
def cancel_create_trip():
    return render_template('trips.html')

#display users trips
@app.route('/trips')
def display_trip():
    # Retreive data from database to display
    trips = models.retrieve_trips()
    return render_template('trips.html')


@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
