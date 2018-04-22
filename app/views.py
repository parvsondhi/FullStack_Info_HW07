from flask import render_template, redirect, request, session, url_for, flash
from app import app, models, db
from .forms import TripsForm
# Access the models file to use SQL functions--done
from .models import *

@app.route('/')
def index():
    username = ''
    if "username" in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session["username"]
        # return "Logged in as " + username + '<br>' + \
        # "<b><a href = '/logout'> Click here to log out </a> </b>"
        trips =  retrieve_trips([1],[1],[1])
        companions = retrieve_companions([1],[1])
        return render_template('home.html', trips=trips, companions=companions, username=username)
    else:
        return render_template('login.html')

@app.route('/login', methods = ["POST", "GET"]) # You need to specify something here for the function to get requests
def login():
    # Here, you need to have logic like if there's a post request method, store the username and email from the form into
    if request.method == "POST":
        username = request.form["Name"]
        email = request.form["Email"]
    # session dictionary
        session['username'] = request.form["Name"]
        trips =  retrieve_trips([1],[1], [1])
        companions = retrieve_companions([1],[1])
        return render_template('home.html', trips=trips, companions=companions, username=username)
    if():
        pass
    return render_template('login.html')

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    username = session["username"]
    form = TripForm()
    form.friend.choices = [('Nolan', 'Nolan'), ('Eric', 'Eric'), ('David', 'David')]        
    for row in fetch_companions('Trips', 'username'):
        person = str(row[0])
        form.friend.choices += []
    if form.validate_on_submit():
        # Get data from the form -- done
        # Send data from form to Database -- done
        trip_name = form.trip_name.data
        destination = form.destination.data
        friend = form.friend.data
        username = username
        insert_data(trip_name, destination, friend, username)
        return redirect('/trips')
    else:
        return render_template('trips.html', form=form, username=username)
        
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/friends/<id>', methods=['GET', 'POST'])
def remove(id):
    with sql.connect("app.db") as con:
        cur = con.cursor()
        cur.execute('delete FROM Trips WHERE customer_id=?', (id,))
        con.commit()
        # con.row_factory = sql.Row
        # # above sets up connection to accept data in the form of row objects
        # cur = con.cursor()
        # result = cur.execute('DELETE FROM Trips WHERE Customer_ID=?', (id,))
    return redirect(url_for('index'))


@app.route('/trips')
def display_trips():
    if "username" in session: #check if the user is already in session, if so, direct the user to survey.html Hint: render_template with a variable
        username = session["username"]
        trips =  retrieve_trips([1],[1], [1])
        companions = retrieve_companions([1],[1]) 
        # Retreive data from database to display
        return render_template('home.html',
                            trips=trips, companions=companions, username=username)

