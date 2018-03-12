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

###############################################################################################################################################

@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    customerForm = CustomerForm()
    addressForm = AddressForm()
    if customerForm.validate_on_submit():
        # Get data from the customer form
        first_name = customerForm.first_name.data
        last_name = customerForm.last_name.data
        company = customerForm.company.data
        email = customerForm.email.data
        phone = customerForm.phone.data

        # Get data from the address form
        street_address = addressForm.street_address.data
        city = addressForm.city.data
        state = addressForm.state.data
        country = addressForm.country.data
        zip_code = addressForm.zip_code.data

        # Send data from form to Database
        customer_id = insert_customer(first_name, last_name, company, email, phone)
        insert_address(street_address, city, state, country, zip_code, customer_id)
        return redirect('/customers')
    return render_template('customer.html', customerForm=customerForm, addressForm=addressForm)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html', customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        # Get data from the order form
        name_of_part = orderForm.name_of_part.data
        manufacturer_of_part = orderForm.manufacturer_of_part.data
        order_id = insert_order(name_of_part, manufacturer_of_part, value)

        # Send data from form to Database
        insert_customer_order(value, order_id)
        return redirect('/customers')
    return render_template('order.html', orderForm=orderForm)
