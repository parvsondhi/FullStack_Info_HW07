from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TripsForm(Form):
    trip_name =  StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = SelectField('friend', choices=[])
    # Add additional trip fields here
