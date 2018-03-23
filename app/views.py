from flask import Flask, render_template, redirect, request, session, url_for
from app import app, models, db
from .forms import TripForm
from .models import *
import sys
# Access the models file to use SQL functions


@app.route('/')
@app.route('/index')
def index():
    #username = ''
    if 'username' in session:
        current_user = session['username']
        #print(current_user, file=sys.stderr)
        #return render_template('home.html')
        return redirect(url_for('display_trips'))
    else:
        return render_template('login.html')

@app.route('/login', methods = ['GET','POST']) 
def login():
    if request.method == 'POST':
        session['username'] = request.form['nm']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return ""

@app.route('/logout')
def logout():
	session.pop('username', None)
	session.pop('password', None)
	return redirect(url_for('index'))

# @app.route('/create_customer', methods=['GET', 'POST'])
# def create_customer():
#     form = CustomerForm()
#     # customerForm = CustomerForm()
#     # addressForm = AddressForm()
#     if form.validate_on_submit():
#         # Get data from the form
#         # Send data from form to Database
#         first_name = form.first_name.data # getting data from html 
#         last_name = form.last_name.data
#         company = form.company.data
#         email = form.email.data
#         phone_number = form.phone_number.data
#         # insert into models.py
#         customer_id = insert_customer(first_name,last_name,company,email,phone_number)
        
        
#         street_address = form.street_address.data
#         city = form.city.data
#         state = form.state.data
#         country = form.country.data
#         zip_code = form.zip_code.data
#         insert_address(street_address,city,state,country,zip_code, customer_id)
        
#         return redirect('/customers')
#     return render_template('customers.html', form=form)

@app.route('/home')
def display_trips():
    # Retreive data from database to display
    current_user = session['username']
    print(current_user, file=sys.stderr)
    ID = getID(current_user)
    print(ID, file=sys.stderr)
    trip = retrieve_trips(ID)
    return render_template('home.html',
                            trip=trip)

@app.route('/addtrip', methods=['GET', 'POST'])
def add_trip():
    current_user = session['username']
    friend_list = retrieve_friends(current_user) # create list of users
    friend_tuple = list(zip(friend_list, friend_list)) # put list into tuple form
    tripForm = TripForm() # instantiate the trip form
    tripForm.friend.choices = friend_tuple # add friend list to choices on form
    if tripForm.validate_on_submit():
        uid = getID(current_user) 
        # print(uid, file=sys.stderr)
        # Get data from the form
        trip_title = tripForm.trip_title.data  
        destination = tripForm.destination.data
        friend = tripForm.friend.data
        # Send data from form to Database
        trip_id = insert_trip(trip_title, destination, friend)
        friend_id = getID(friend)
        insert_trip_user(trip_id, uid, friend_id)
        return redirect('/home')
    return render_template('addtrip.html', form=tripForm)

@app.route('/remove_trip/<value>')
def remove_trip(value):
    delete_trip(value)
    return redirect(url_for('display_trips'))