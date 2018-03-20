from flask import request, Flask, session, redirect, url_for, escape, request, render_template
from app import app, models, db
# Access the models file to use SQL functions
import app.models as models  

@app.route('/')
def index():
    if 'username' in session:
        trips = models.get_trips(session['username'])
        return render_template('trip.html', username=escape(session['username']), trips=trips)
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if request.form['action'] == 'login':
            if models.check_login(username, password):
                session['username'] = username
                return redirect(url_for('index'))
            else:
                return render_template('login.html', message="Incorrect username or password")
        else:
            if models.create_user(username, password):
                session['username'] = username
                return redirect(url_for('index'))
            else:
                return render_template('login.html', message="User already exists")

    return render_template('login.html', message=None)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/create_trip', methods=['GET', 'POST'])
def create_trip():
    if request.method == 'POST':
        title = request.form['title']
        dest = request.form['dest']
        models.add_trip(title, dest, session['username'], request.form['otheruser'])
        return redirect(url_for('index'))
    return render_template('create_trip.html', username=escape(session['username']), users=models.get_users())

@app.route('/remove_trip', methods=['GET', 'POST'])
def remove_trip():
    trip_id = request.args.get('trip_id')
    print trip_id
    models.remove_trip(trip_id)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
