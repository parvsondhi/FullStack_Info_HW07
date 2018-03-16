from flask import render_template, redirect, request
from app import app, models, db
from .forms import *
from .models import *

# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_customer')

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    form = CustomerForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = form.first_name.data
        last_name = form.last_name.data
        company = form.company.data
        email = form.email.data
        phone = form.phone.data
        customer_data = [first_name,last_name,company,email,phone]

        # add address info as well
        street_address = form.street_address.data
        city = form.city.data
        state = form.state.data
        country = form.country.data
        zip_code = form.zip_code.data
        #customer_id = get_customer_id()
        address_data = [street_address, city, state, country, zip_code]
        insert_data(customer_data, address_data)
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    customers = retrieve_customers()
    orders = retrieve_orders()
    return render_template('home.html',
                            customers=customers, orders=orders)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    form = OrderForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        order_data = [name_of_part, manufacturer_of_part, value]
        order_id = insert_order(order_data)
        insert_customer_order(order_id, value)
        return redirect('/customers')
    return render_template('order.html', form=form)
