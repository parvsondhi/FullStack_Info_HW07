from flask import Flask, render_template, redirect, request, session
from app import app, models, db
from forms import UserForm, TripForm, AddressForm
# Access the models file to use SQL functions
from models import *

@app.route('/index')
@app.route('/')
def index():
    if 'username' in session:
        return redirect('/trips')
    else:
        return render_template('login.html')

@app.route('login', methods = ['GET', 'POST'])
def login():
    return None

@app.route('/logout')
def logout():
    return None

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
