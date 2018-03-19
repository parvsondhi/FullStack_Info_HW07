from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user, login_required
from app.models import User, Trip
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    user_id = current_user.id
    user_trips = current_user.trips.all()
    all_trips = Trip.query.all()
    return render_template('index.html', trips=user_trips)

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

@app.route('/create-trip', methods=['GET', 'POST'])
@login_required
def create_trip():
    ## Get form Element
    # form = TripForm()
    ## Form Processing
    # if form.validate_on_submit():
        ## Create Trip object

        ## Write Trip object to database

        ## Redirect to index page

    ## Render page and form
    return render_template('create_trip.html', form=form)




# @app.route('/delete_trip')
# @flask_login.login_required
# def delete_trip():
