from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm, AddressForm, OrderForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    customerForm = CustomerForm()
    addressForm = AddressForm()
    if customerForm.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = customerForm.first_name.data
        last_name = customerForm.last_name.data
        company = customerForm.company.data
        email = customerForm.email.data
        phone_number = customerForm.phone_number.data
        insert_customer(first_name,last_name,company,email,phone_number)

        street_address = addressForm.street_address.data
        city = addressForm.city.data
        state = addressForm.state.data
        country = addressForm.country.data
        zipcode = addressForm.zipcode.data
        customer_id = retrieve_customer_id()
        insert_address(street_address,city,state,country,zipcode, customer_id) # need to add customer_id

        return redirect('/customers')
    return render_template('customer.html', customerForm=customerForm, addressForm=addressForm)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    orderForm = OrderForm()
    if orderForm.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = orderForm.name_of_part.data
        manufacturer_of_part = orderForm.manufacturer_of_part.data
        customer_id = value # not sure if the value carries over ??
        insert_orders(name_of_part, manufacturer_of_part, customer_id)

        order_id = retrieve_order_id()
        insert_order_detail(customer_id,order_id)
        return redirect('/customers')
    return render_template('order.html', orderForm=orderForm)
