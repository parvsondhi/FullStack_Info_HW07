from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, PasswordField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired
from .models import retrieve_friends

class userForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class tripForm(Form):
    friend_list = retrieve_friends()
    dest = StringField('dest', validators=[DataRequired()])
    trip_name = StringField('trip_name', validators=[DataRequired()])
    friend = SelectField('friend', choices=friend_list)
    """
    name_of_part = StringField('name_of_part', validators=[DataRequired()])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])
    """
