from flask import render_template, redirect, request, Flask, url_for, escape, session
from app import app, models, db
from .forms import TripForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    if 'email_id' in session:
        trips = models.retrieve_trips(session['email_id'])
        return render_template('trip.html', email_id=escape(session['email_id']), trips=trips)
    return redirect(url_for('login'))
    # return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email_id = request.form['email_id']
        password = request.form['password']
        first = request.form['first_name']
        last = request.form['last_name']
        if request.form['action'] == 'login':
            if models.authenticate_user(email_id, password):
                session['email_id'] = email_id
                return redirect(url_for('index'))
            else:
                return render_template('login.html', message="Incorrect Password or Username(Email)")
        else:
            # if email_id == None or password == None or first == None or last == None:
                # return render_template('login.html', message="Please Fill out all the required Fields")
            if create_user(email_id, password, first, last):
                session['email_id'] = email_id
                return redirect(url_for('index'))
            else:
                return render_template('login.html', message="An Account Already Exists with the following Email!")

    return render_template('login.html', message=None)

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        print (request.form['friend'])
        res = models.insert_trip(name, location, session['email_id'], request.form['friend'])

        if(res == False):
            return render_template('/create_trip.html', email_id = escape(session['email_id']), users = models.get_users())

        return redirect(url_for('index'))

    return render_template('/create_trip.html', email_id = escape(session['email_id']), users = models.get_users())

@app.route('/remove_trip', methods=['GET', 'POST'])
def remove_trip():
    idd = request.args.get('trip_id')
    models.delete_trip(idd)
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('email_id', None)
    return redirect(url_for('index'))