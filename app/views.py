from flask import render_template, redirect, url_for
from app import app, db
from flask_login import current_user

from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('trips'))
    else:
       return redirect(url_for('register')) 

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
        return redirect(url_for('trips'))
    return render_template('register.html', title='Register', form=form)

@app.route('/trips')
def trips():
    return render_template('trips.html')