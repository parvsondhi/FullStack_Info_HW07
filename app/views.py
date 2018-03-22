from flask import render_template, redirect, request, session
from app import app, model
from .forms import CustomerForm,  NewUserForm, LoginForm, TripForm
from .model import *


@app.route('/')
def index():
    if 'username' in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session['username']
        return redirect('/trips')
    else:
        return redirect('/login')

@app.route('/create_newUser', methods=['GET', 'POST'])
def create_newUser():
    newUserForm = NewUserForm()
    if newUserForm.validate_on_submit():
        first_name = newUserForm.first_name.data
        last_name = newUserForm.last_name.data
        email = newUserForm.email.data
        username = newUserForm.username.data
        password = newUserForm.password.data
        

        # ADD PROPER PASSWORD FIELD
        # ADD SHA HASHING
        # ADD CRYPTO DB TO SAVE DECRYPTION KEYS


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
    friendChoices = []
    for friend in friends:
        row = {}
        row['Username'] = friend['Username']
        # row['last_name'] = friend['Last']
        boomlist.append(row)  
        
    if tripForm.validate_on_submit():
        trip_title = tripForm.trip_title.data
        trip_destination = tripForm.trip_destination.data
        trip_friend = tripForm.trip_friend.data

        # need to add both the user currently signed in, as well as the submitted friend
        participants = []
        participants.append(session['username'])
        participants.append(trip_friend)
        collection = chooseCollection('trips')
        insertTrip(collection, trip_title, trip_destination, participants)

        return redirect('/trips')
    return render_template('trip.html', tripForm=tripForm, friends=boomlist, user=session['username'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    wrong = 'none'

    # instantiate an object for the user collection
    collection = chooseCollection('users')
    #instantiate a friends object for users within users collection
    friends = findUsers(collection)
    
    # create a list to hold friends
    Flist = []
    
    # enter if there is at least one friend in the users collection
    if friends.count() is 0:
        return redirect('/create_newUser')

    else: 
        # for every friend, add the 'Username' and 'Password' to the friends list array
        for friend in friends:
            # print(friend['Username'])
            Flist.append({ friend['Username'] : friend['Password'] })

    # enter on validate
    if loginForm.validate_on_submit():
        # submitted username
        u = loginForm.username.data
        #submitted password
        p = loginForm.password.data

        # enter if entries in friend list, adding usernames and passwords to session
        if {u:p} in Flist:
            session['username'] = loginForm.username.data
            session['password'] = loginForm.password.data
            return redirect('/trips')
        # else, render login and push 'block' as wrong
        else:
            wrong = 'block'            
            return render_template('login.html', loginForm=loginForm, wrong=wrong)

    return render_template('login.html', loginForm=loginForm, wrong=wrong)


# @app.route('/friends')
# def friends():
    
    
#     collection = chooseCollection('users')
#     friends = findUsers(collection)

#     boomlist = []

#     for friend in friends:
#         print(friend['First'])
#         row = {}
#         row['first_name'] = friend['First']
#         row['last_name'] = friend['Last']
        
#         boomlist.append(row)        


#     return render_template('friends.html', friends=boomlist, session=session)

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
    
        boomlist = []

        for trip in trips:
            row = {}
            row['trip_title'] = trip['Title']
            row['trip_destination'] = trip['Destination']
        
            boomlist.append(row)    

    return render_template('home.html',trips=boomlist, user=session['username'])
