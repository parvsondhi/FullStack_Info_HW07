from flask import render_template, redirect, request, session
from app import app, models, model
from .forms import CustomerForm, OrderForm, NewUserForm, LoginForm, TripForm
from .models import *
from .model import *


@app.route('/')
def index():
    if 'username' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['username']
        return render_template('trip.html')
    else:
        return redirect('/create_newUser')

@app.route('/create_newUser', methods=['GET', 'POST'])
def create_newUser():
    newUserForm = NewUserForm()
    if newUserForm.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        first_name = newUserForm.first_name.data
        last_name = newUserForm.last_name.data
        email = newUserForm.email.data
        username = newUserForm.username.data
        password = newUserForm.password.data
        
        collection = chooseCollection('users')
        insertUser(collection, email, username, password, first_name, last_name)

        session['username'] = username
        session['password'] = password

        return redirect('/trips')
    return render_template('register.html', newUserForm=newUserForm)

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    tripForm = TripForm()
    
    collection = chooseCollection('users')
    friends = findUsers(collection)

    boomlist = []

    for friend in friends:
        print(friend['First'])
        row = {}
        row['first_name'] = friend['First']
        row['last_name'] = friend['Last']
        
        boomlist.append(row)  

    # return render_template('trip.html', tripForm=tripForm, friends=boomlist)

    if tripForm.validate_on_submit():
        trip_title = tripForm.trip_title.data
        trip_destination = tripForm.trip_destination.data
        
        # DUMMY VALUE
        #participants = []
        #participants.append(session['username'])
        participants = session['username']
        collection = chooseCollection('trips')
        insertTrip(collection, trip_title, trip_destination, participants)

        return redirect('/trips')
    return render_template('trip.html', tripForm=tripForm, friends=boomlist)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    wrong = 'none'

    collection = chooseCollection('users')
    friends = findUsers(collection)
    
    Flist = []
    
    if friends.count() is not 0:
        
        for friend in friends:
            Flist.append({friend['Username']:friend['Password']})

    if loginForm.validate_on_submit():
        
        u = loginForm.username.data
        p = loginForm.password.data

        if {u:p} in Flist:
            session['username'] = loginForm.username.data
            session['password'] = loginForm.password.data
            return redirect('/trips')
        else:
            wrong = 'block'            
            return render_template('login.html', loginForm=loginForm, wrong=wrong)

    return render_template('login.html', loginForm=loginForm, wrong=wrong)

@app.route('/friends')
def friends():
    # Retreive data from database to display
    
    collection = chooseCollection('users')
    friends = findUsers(collection)

    boomlist = []

    for friend in friends:
        print(friend['First'])
        row = {}
        row['first_name'] = friend['First']
        row['last_name'] = friend['Last']
        
        boomlist.append(row)        


    return render_template('friends.html', friends=boomlist, session=session)

@app.route('/trips')
def trips():
    # Retreive data from database to display
    

    collection = chooseCollection('trips')
    trips = findTrips(collection, session['username'])
    
    boomlist = []

    if trips.count() is not 0:
        print('Trips:')
        print(trips)
        print(trips[0])
    
        boomlist = []

        for trip in trips:
            row = {}
            row['trip_title'] = trip['Title']
            row['trip_destination'] = trip['Destination']
        
            boomlist.append(row)    

    return render_template('home.html',trips=boomlist, user=session['username'])


@app.route('/tripsrem/<value>', methods=['GET', 'POST'])
def tripsrem(value):
    # Retreive data from database to display

    print(value)    

    collection = chooseCollection('trips')

    removeTrip(collection,value)
    
    trips = findTrips(collection, session['username'])
    
    boomlist = []

    if trips.count() is not 0:
        print('Trips:')
        print(trips)
        print(trips[0])
    
        boomlist = []

        for trip in trips:
            row = {}
            row['trip_title'] = trip['Title']
            row['trip_destination'] = trip['Destination']
        
            boomlist.append(row)    

    return render_template('home.html',trips=boomlist, user=session['username'])
