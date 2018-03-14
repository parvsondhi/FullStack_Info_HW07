from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired


class TripForm(Form):
	tripname = StringField('tripname', validators=[DataRequired()])
	destination = StringField('destination', validators=[DataRequired()])
	friend = StringField('friend', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class SignUpForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators = [DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')