from flask import Flask, render_template, redirect, request, session, escape, url_for
from app import app, models
from .forms import UserForm, TripForm
# Access the models file to use SQL functions
from .models import *

# index page
@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        username = escape(session['username'])
        return redirect('/trips')
    else:
        return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method=='POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    if request.method=='GET':
        return redirect(url_for('signup'))
    #if request.method=='GET':
    #    do something
    #    return redirect(url_for('index'))

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method=='POST':
        username = request.form['username']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        insert_user(username, password, first_name, last_name)
        session['username'] = username
        session['first_name'] = first_name
        session['last_name'] = last_name
        session['password'] = password
        return redirect(url_for('index'))
    return render_template('signup.html')
    #return redirect(url_for('index'))

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
    userForm = UserForm()

    return render_template('trips.html')

@app.route('/trips')
def display_trips():
    curr_user = session['username']
    #curr_user = "cy"
    trips = retrieve_trips(curr_user)
    return render_template('trips.html', trips=trips, name=curr_user)

@app.route('/create-trip', methods=['GET', 'POST'])
def create_trip():
    curr_user = session['username']
    friend_list = retrieve_friends(curr_user)
    friend_tuple = list(zip(friend_list, friend_list))
    form = TripForm()
    form.friend.choices=friend_tuple

    if form.validate_on_submit():
        dest = form.dest.data
        friend = form.friend.data
        trip_name = form.trip_name.data
        trip_owner = session['username']
        #trip_owner = "cy"
        insert_trip(trip_owner, dest, trip_name, friend)
        return redirect('/trips')
    return render_template('create-trip.html', form=form, name=curr_user)

@app.route('/remove-trip/<value>')
def remove_trip(value):
    delete_trip(value)
    return redirect('/trips')

# 404 errohandler
@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404
