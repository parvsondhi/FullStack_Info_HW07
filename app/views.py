# Importing flask library
from app import app
from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    username = ''
    if 'username' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['username']
        "Logged in as " + username + "<br>" + \
        "<b><a href = '/logout'>Click here to log out</a></b>"
        return render_template('survey.html', name=username)
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST', 'GET']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == 'POST':
        session['username'] = request.form['name']
        session['email'] = request.form['email']
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('email', None)
	return redirect(url_for('index'))

@app.route('/trips')
def view_trips():
    
    return render_template('trips.html')

@app.route('/create-trip', methods=['GET', 'POST'])
def create_trips():
    username = ''
    if'username' in session: #check if user in session
        username = session.get('username')
        surveyResponse = {}
        surveyResponse['trip_name'] = request.form.get('trip_name')
        surveyResponse['destination'] = request.form.get('destination')
        return render_template('trips.html', trip_name=trip_name , destination=destination) # pass in variables to the template
    else:
        return render_template('create_trip.html')
    
    # return render_template('create_trip.html')

@app.route('/submit-survey', methods=['GET', 'POST'])
def submitSurvey():
    username = ''
    email = ''
    if'username' in session: #check if user in session
        username = session.get('username')
        surveyResponse = {}
        surveyResponse['color'] = request.form.get('color')
        surveyResponse['food'] = request.form.get('food')
        surveyResponse['vacation'] = request.form.get('vacation')
        #get the rest o responses from users using request library Hint: ~3 lines of code
        surveyResponse['fe-before'] = request.form.get('feBefore')
        surveyResponse['fe-after'] = request.form.get('feAfter')
        return render_template('results.html', name=username, surveyResponse=surveyResponse) # pass in variables to the template
    else:
        return render_template('login.html')


@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
