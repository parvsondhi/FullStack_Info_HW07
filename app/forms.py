from flask_wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TripForm(Form):
    trip_title = StringField('trip_title', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = StringField('friend', validators=[DataRequired()])
