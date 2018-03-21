from flask import Flask, render_template, redirect, request, session, escape, url_for
from app import app, models
from .forms import userForm, tripForm
# Access the models file to use SQL functions
from .models import *

# index page
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        username = escape(session['username'])
        return render_template('trips.html', name=username)
    else:
        return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
	"""Register Form"""
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'])
		db.session.add(new_user)
		db.session.commit()
		return render_template('login.html')
	return render_template('signup.html')

# need this?
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    userForm = userForm()
    # tripForm = tripForm()
    return render_template('trips.html')

@app.route('/trips')
def display_trips():
    return render_template('trips.html')

@app.route('/create-trip', methods=['GET', 'POST'])
def create_trip(value):
    form = TripForm()
    if form.validate_on_submit():
        dest = form.dest.data
        friend = form.dest.friend
        trip_name = form.trip_name.data
        trip_owner = session['username']
        insert_trip(dest, friend, trip_name, trip_owner)
    return None

# 404 errohandler
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
