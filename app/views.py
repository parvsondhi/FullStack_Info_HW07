from flask import render_template, redirect, request
from app import app, models, db
from .forms import TripForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/home')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    # customerForm = CustomerForm()
    # addressForm = AddressForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data # getting data from html 
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone_number = form.phone_number.data
        # insert into models.py
        customer_id = insert_customer(first_name,last_name,company,email,phone_number)
        
        
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        insert_address(street_address,city,state,country,zip_code, customer_id)
        
        return redirect('/customers')
    return render_template('customers.html', form=form)

@app.route('/home')
def display_trips():
    # Retreive data from database to display
    trip = retrieve_trips()
    return render_template('home.html',
                            trip=trip)

@app.route('/addtrip', methods=['GET', 'POST'])
def add_trip(value):
    # Get data from the form
    # Send data from form to Database
    tripForm = TripForm()
    if tripForm.validate_on_submit():
        uid = value
        trip_title = orderForm.trip_title.data
        destination = orderForm.destination.data
        trip_id = insert_trip(trip_title, destination)
        insert_trip_user(trip_id, uid)
        return redirect('/home')
    return render_template('addtrip.html', form=tripForm)