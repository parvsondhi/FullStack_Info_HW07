from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, TripForm
from flask_login import current_user, login_user, login_required, logout_user
from app.models import User, Trip
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    user_id = current_user.id
    user_trips = current_user.trips.all()
    invited_trips = Trip.query.filter_by(friend_id=user_id).all()
    # all_trips = Trip.query.all()
    return render_template('index.html', trips=user_trips, invited=invited_trips)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user) # TESTING: REMEBER TO ADD remember=form.remember_me.data
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    # flash('login fail')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('index'))

@app.route('/create_trip', methods=['GET', 'POST'])
@login_required
def create_trip():
    ## Create form object
    form = TripForm()

    ## Form Processing
    if form.validate_on_submit():
        ## Create Trip object
        trip = Trip(tripname=form.tripname.data, destination=form.destination.data, user_id=current_user.id)

        ## Write Trip object to database
        db.session.add(trip)
        db.session.commit()

        ## Redirect to index page
        # return redirect(url_for('index'))
        return redirect(url_for('index'))

    ## Render page and form
    return render_template('create_trip.html', form=form)

@app.route('/delete_trip/<value>')
@login_required
def delete_trip(value):
    trip_id = value
    # User.query.filter(User.id == 123).delete()
    Trip.query.filter(Trip.id == trip_id).delete()
    db.session.commit()

    return redirect(url_for('index'))
