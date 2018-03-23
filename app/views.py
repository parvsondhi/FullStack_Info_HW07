from flask import render_template, redirect, url_for, flash, request, jsonify
from app import app, db
from flask_login import current_user, login_user, login_required, logout_user

from app.forms import LoginForm, RegistrationForm, TripForm
from app.models import User, Trip, TripInvitation
from app.utils import inject_trip, current_user_has_access_to_trip, trip_owned_by_user, inject_trip_invitation

# =========================
# 0. Error Handler
# =========================

@app.errorhandler(404)
def page_not_found(e):
    error_code = 404
    error_message = 'Sorry, we can\'t find what you are looking for :-('
    return render_template('error.html', error_code=error_code, error_message=error_message), error_code

@app.errorhandler(403)
def page_not_found(e):
    error_code = 403
    error_message = 'Naughty! You are not allowed to access this resource!'
    return render_template('error.html', error_code=error_code, error_message=error_message), error_code


# =========================
# 1. Anonymously Accessible 
# =========================

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('trips'))
    else:
       return redirect(url_for('register')) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, firstname=form.firstname.data, lastname=form.lastname.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, we successfully registered your account!', 'info')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



# =========================
# 2. Login Required
# =========================

@app.route('/trips')
@login_required
def trips():
    created_trips = current_user.trips
    invited_trips = current_user.invited_trips
    return render_template('trips.html', created_trips=created_trips, invited_trips=invited_trips)

@app.route('/trips/create', methods=['GET', 'POST'])
@login_required
def create_trip():
    form = TripForm()
    if form.validate_on_submit():
        trip = Trip(title=form.title.data, destination=form.destination.data, user_id=current_user.id)
        db.session.add(trip)
        db.session.commit()
        flash('Congratulations, you successfully added a trip!', 'info')
        return redirect(url_for('trips'))
    return render_template('create-trip.html', title='Create a Trip', form=form)


@app.route('/trips/<id>')
@login_required
@inject_trip
@current_user_has_access_to_trip
def show_trip(trip):
    return render_template('trip-detail.html', trip=trip)

@app.route('/trips/<id>', methods = ['DELETE'])
@login_required
@inject_trip
@trip_owned_by_user
def delete_trip(trip):
    db.session.delete(trip)
    db.session.commit()
    flash('Trip was deleted!', 'info')
    return jsonify(
        redirect=True,
        redirect_url=url_for('trips')
    )

@app.route('/trips/<id>/edit', methods=['GET', 'POST'])
@login_required
@inject_trip
@trip_owned_by_user
def edit_trip(trip):
    #TODO: This should really be a PUT request.
    trip_form = TripForm(obj=trip)
    if trip_form.validate_on_submit():
        trip.title = trip_form.title.data
        trip.destination = trip_form.destination.data
        db.session.commit()
        return redirect(url_for('show_trip', id=trip.id))
    return render_template('edit_trip.html', trip=trip, form=trip_form)


@app.route('/trips/<id>/invitation/<user_id>', methods=['POST'])
@login_required
@inject_trip
@current_user_has_access_to_trip
def invite_to_trip(trip, user_id):
    filtered_users = [ user for user in trip.invitable_users() if user.id == int(user_id) ]
    if len(filtered_users) > 0:
        trip_invitation = TripInvitation(user_id=user_id, trip_id=trip.id)
        db.session.add(trip_invitation)
        db.session.commit()
        flash(filtered_users[0].fullName() + ' was added to the trip!', 'info')
    else:
        flash('The user is already part of this trip', 'info')
    
    return jsonify(
            redirect=True,
            redirect_url=url_for('show_trip', id=trip.id )
        )

@app.route('/trips/<id>/invitation', methods = ['DELETE'])
@login_required
@inject_trip_invitation
def delete_trip_invitation(trip_invitation):
    ''' Removes the current user from the trip if they are invited.'''
    db.session.delete(trip_invitation)
    db.session.commit()
    flash('Trip invitation was deleted!', 'info')
    return jsonify(
        redirect=True,
        redirect_url=url_for('trips')
    )

@app.route('/trips/<id>/invitation/<user_id>', methods = ['DELETE'])
@login_required
@inject_trip
@trip_owned_by_user
def withdraw_trip_invitation(trip, user_id):
    ''' Removes specified user from the trip's guest list '''
    user = User.query.filter_by(id=int(user_id)).first()
    trip_invitation = TripInvitation.query.filter_by(trip_id=trip.id, user_id=user.id).first()
    if user and trip_invitation:
        db.session.delete(trip_invitation)
        db.session.commit()
    flash(user.fullName() + ' was removed from trip!', 'info')
    return jsonify(
        redirect=True,
        redirect_url=url_for('show_trip', id=trip.id )
    )