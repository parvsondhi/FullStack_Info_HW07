from flask import render_template, redirect, request
from app import app, models, db
from .forms import AddressForm, CustomerForm, OrderForm
from .models import retrieve_addressess, retrieve_customers, retrieve_orders, insert_customer, insert_order, insert_address

@app.route('/')
def index():
    return redirect('/customers')

@app.route('/customers') # Redirects to home.html
def display_customer():

    ## Retreive data from database to display
    orders = retrieve_orders()
    customers = retrieve_customers()

    return render_template('home.html', customers=customers, orders=orders)

@app.route('/create_customer', methods=['GET', 'POST'])
def create_customer():
    ## WTF Form object
    customerForm = CustomerForm()
    addressForm = AddressForm()

    ## Submission Handler
    if customerForm.validate_on_submit():

        ## Get data from the customerForm
        company = customerForm.company.data
        email = customerForm.email.data
        fname = customerForm.fname.data
        lname = customerForm.lname.data
        phone = customerForm.phone.data

        ## Get data from addressForm
        street_address = addressForm.street_address.data
        city = addressForm.city.data
        state = addressForm.state.data
        country = addressForm.country.data
        zip_code = addressForm.zip_code.data

        ## Send customer data from form to Database
        ## NOTE: This runs function and gets last row, which is the customer id. Is there a better way?
        customer_id = insert_customer(company, email, fname, lname, phone)

        insert_address(customer_id, street_address, city, state, country, zip_code)

        return redirect('/customers')

    ## else render customer form for input
    return render_template('customer.html', customerForm=customerForm, addressForm=addressForm)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
    ## WTF Form object
    form = OrderForm()

    ## Get customer_id for order
    customer = value

    ## Submission Handler
    if form.validate_on_submit():
        part_name = form.part_name.data
        manufacturer = form.manufacturer.data

        ## Send data from form to Database
        insert_order(customer, part_name, manufacturer)

        ## redirect to homepage
        return redirect('/customers')

    return render_template('order.html', form=form)

@app.route('/add_address/<value>')
def add_address(value):
    ## WTF Form object
    form = AddressForm()

    ## Get customer_id for order
    customer = value

    return None
