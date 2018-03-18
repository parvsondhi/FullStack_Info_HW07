from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TripForm(Form):
    trip_title = StringField('trip_title', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    # Add additional Address fields here

# class OrderForm(Form):
#     # Add order input form fields here
#     part_name = StringField('part_name', validators=[DataRequired()])
#     manufacturer = StringField('manufacturer', validators=[DataRequired()])
