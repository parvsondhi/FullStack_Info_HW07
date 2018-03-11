from flask import render_template, redirect, request, url_for
from app import app, models, db
from .forms import TripForm
from .models import *


@app.route('/')
def index():
    # return redirect('/create_trip')
    return render_template('home.html')

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        destination = form.destination.data
        friend = form.friend.data
        insert_trip(destination, friend)
        return redirect('/trip_detail') 

    return render_template('trips.html', form = form) # this is what gets called without form

@app.route('/trip_detail')
def display_trip():
    # trips = retrieve_trips()
    # return render_template('home.html', trips = trips)
    return render_template('TripDetail.html')

# @app.route('/create_order/<value>', methods=['GET', 'POST'])
# def create_order(value):
#     form = OrderForm()
#     if form.validate_on_submit():
#         name_of_part = form.name_of_part.data
#         manufacturer_of_part = form.manufacturer_of_part.data
#         insert_order(name_of_part, manufacturer_of_part, value)
#         order_id = retrieve_order_id()
#         insert_customer_order(value, order_id)
#         return redirect('/customers')
#     return render_template('order.html', form = form)
