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
    friend_list = retrieve_friends()
    friend_tuple = list(zip(friend_list, friend_list))
    dest = StringField('dest', validators=[DataRequired()])
    trip_name = StringField('trip_name', validators=[DataRequired()])
    print(friend_tuple, file=sys.stderr)
    friend = SelectField('friend', choices=friend_tuple)
    """
    name_of_part = StringField('name_of_part', validators=[DataRequired()])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])
    """
