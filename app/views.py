from flask import Flask, redirect, make_response, render_template, url_for, session, request, escape, flash
from app import app, models, db
from .forms import UserForm, TripForm
from .models import *
import os
app.secret_key = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:  
    	return redirect('/user')
    # return render_template('trip.html', username=session['username'])
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST']) 
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        username = request.form['username']
        password = request.form['password']
        if check_user(username,password):
        	return redirect(url_for('index'))
        else:
        	return render_template('login.html')

@app.route('/login', methods=['GET']) 
def show_login():
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('password', None)
	return redirect(url_for('index'))

@app.route('/user')
def user():
	username = session['username']
	trips = retrieve_trips(username)
	return render_template('trip.html', username=session['username'],trips = trips)

@app.route('/create', methods=['GET', 'POST'])
def create():
	username = session['username']
	user_id = retrieve_user(username)
	form = TripForm()
	users = retrieve_allusers()
	if form.validate_on_submit():
		trip = form.trip.data
		destination = form.destination.data
		friend = request.form.get('friend')
		friend_id = retrieve_user(friend)
		insert_trip(user_id,trip,destination,friend,friend_id)
		insert_trip(friend_id,trip,destination,username,user_id)
		return redirect('/user')
	return render_template('create.html',username=session['username'],form = form,users=users)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
	trip = request.form.get('trip')
	delete_trip(trip)
	return redirect('/user')

@app.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	password = request.form['password']
	if check_username(username):
		insert_user(username,password)
		return render_template('login.html')
	else:
		return render_template('register.html',message="username already existed.")

@app.route('/register',methods=['GET'])
def show_register():
    return render_template('register.html')
