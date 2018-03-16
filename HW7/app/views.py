from flask import Flask, render_template, redirect, request, session
from app import app, models, db
from forms import UserForm, TripForm, AddressForm
# Access the models file to use SQL functions
from models import *

# index page
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        username = escape(session['username'])
        return render_template('trips.html', name=username)
    else:
        return render_template('login.html')

@app.route('login', methods = ['GET', 'POST'])
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

@app.route('/register/', methods=['GET', 'POST'])
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
    return render_template('create-user.html')

@app.route('/trips')
def display_trips():
    return render_template('trip.html')

@app.route('/create-trip/<value>', methods=['GET', 'POST'])
def create_trip(value):
    return None

# 404 errohandler
@myapp.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
