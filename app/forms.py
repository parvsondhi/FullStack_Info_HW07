from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, validators
# from wtforms_components import PhoneNumberField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class UserForm(Form):
	email = EmailField('email', validators=[DataRequired()])
	firstName = StringField('firstName', validators=[DataRequired()])
	lastName = StringField('lastName', validators=[DataRequired()])
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])

class TripForm(Form):
	title = StringField('title', validators=[DataRequired()])
	destination = StringField('destination', validators=[DataRequired()])
		