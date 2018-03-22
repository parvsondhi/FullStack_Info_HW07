from flask import render_template, redirect, request
from app import app, model, forms, views
from .forms import UserForm, TripForm
from .model import *
# Access the models file to use SQL functions

@app.route('/')
@app.route('/index')
def index():
    # username = ''
    if 'username' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['username']
        return render_template('trip.html')
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST']) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    # session dictionary
    if request.method == 'POST':
        print('hello')
        session['username'] = request.form['password']
        session['password'] = request.form['password']
    return redirect(url_for('index'))
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))



@app.route('/trip', methods=['GET', 'POST'])
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        title = form.title.data
        destination = form.destination.data
        participants = form.participants.data
        
        insertTrip(title, destination, participants)

        return redirect('/trip')
    return render_template('trip.html', form=form)

@app.route('/trips')
def display_trip():
    # Retreive data from database to display
    trips = findTrips(session['username'])

    # Construct the object that is used to display orders on homepage

    stuff = []

    i=0
    for trip in trips:
        row = {}
        row['title'] = trip['title']
        row['Destination'] = order['Destination']
        
        stuff.append(row)    

    return render_template('trips.html', trips=stuff)


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        
        # Get data from the form
        email = form.email.data
        username = form.username.data
        password = form.password.data
        first = form.first.data
        last = form.last.data
        
        insertUser(email, username, password, first, last)

        return redirect('/trips')
    
