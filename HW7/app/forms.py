from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
from .models import retrieve_friends
import sys

class UserForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class TripForm(Form):
    dest = StringField('dest', validators=[DataRequired()])
    trip_name = StringField('trip_name', validators=[DataRequired()])
    friend = SelectField('friend', validators=[DataRequired()])

    # def __init__(self, friend_tuple):
        
