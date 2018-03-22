from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
from .model import findUsers, chooseCollection

class CustomerForm(Form):
    first_name = StringField('firstName', validators=[DataRequired()])
    last_name = StringField('lastName', validators=[DataRequired()])
    company = StringField('company', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()]) # just making this a string field rather than using PhoneNumberField


class OrderForm(Form):
    # Add order input form fields here
    name_of_part = StringField('name_of_part', validators=[DataRequired()])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])


# MEGALAB

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class NewUserForm(Form):
    first_name = StringField('firstName', validators=[DataRequired()])
    last_name = StringField('lastName', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class TripForm(Form):
    trip_title = StringField('tripTitle', validators=[DataRequired()])
    trip_destination = StringField('tripDestination', validators=[DataRequired()])
    
    collection = chooseCollection('users')
    friends = findUsers(collection)
    friendChoices = []
    for friend in friends:
        friendChoices.append((friend['Last'],friend['First']))

    trip_friend  = SelectField('tripFriend', choices = friendChoices)
