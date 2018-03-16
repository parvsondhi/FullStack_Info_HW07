from flask import render_template, redirect, request
from app import app, models, db
from .forms import UserForm, TripForm, AddressForm
# Access the models file to use SQL functions
from .models import *

@app.route('/')
def index():

def login():

def logout():

# need this?
@app.route('/create_user', methods=['GET', 'POST'])
def create_user():

@app.route('/trips')
def display_trips():

@app.route('/create_trip/<value>', methods=['GET', 'POST'])
def create_trip(value):

# 404 errohandler
