from flask import render_template, redirect, request, session
from app import app, models, db
from .forms import *
from .models import *

# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/new_user')

@app.route('/new_user', methods=['POST'])
def new_user():
    form = UserForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        username = form.username.data
        password = form.password.data

        insert_user(username, password)
        return redirect('/users')
    return render_template('signup.html', form=form)

@app.route('/users')
def display_user():
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
