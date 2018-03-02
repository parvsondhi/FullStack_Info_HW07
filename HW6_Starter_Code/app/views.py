from flask import render_template, redirect, request
from app import app, models, db
from .forms import CustomerForm
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
        return redirect('/customers')
    return render_template('customer.html', form=form)

@app.route('/customers')
def display_customer():
    # Retreive data from database to display
    return render_template('home.html',
                            customers=customers)

@app.route('/create_order/<value>', methods=['GET', 'POST'])
def create_order(value):
        # Get data from the form
        # Send data from form to Database
        return redirect('/customers')
    return render_template('order.html', form=orderForm)
