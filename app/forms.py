from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class UserForm(Form):
    #user_id = IntegerField('user_id', validators=[DataRequired()])
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class TripForm(Form):
    #trip_id = IntegerField('trip_id', validators=[DataRequired()])
    trip_name = StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = StringField('friend')
