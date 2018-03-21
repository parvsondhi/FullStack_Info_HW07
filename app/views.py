from flask import render_template, redirect, url_for, flash
from app import app, db
from flask_login import current_user, login_user, login_required, logout_user

from app.forms import LoginForm, RegistrationForm
from app.models import User, Trip
from app.utils import inject_trip, current_user_has_access_to_trip

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
    current_user_id = current_user.id
    created_trips = Trip.query.filter_by(user_id=current_user_id).all()
    return render_template('trips.html', created_trips=created_trips)


@app.route('/trips/<id>')
@login_required
@inject_trip
@current_user_has_access_to_trip
def show_trip(trip):
    return str(trip.id)