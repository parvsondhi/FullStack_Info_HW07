from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TripForm(Form):
    trip_name = StringField('trip_name', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    travel_pal = SelectField('travel_pal', otherusers=[])
    # Add additional Address fields here
    # first_name = StringField('first_name', validators=[DataRequired()])
    # last_name = StringField('last_name', validators=[DataRequired()])
    # phone_number = StringField('phone_number', validators=[DataRequired()])
    # street_address = StringField('street_address', validators=[DataRequired()])
    # city = StringField('city', validators=[DataRequired()])
    # state = StringField('state', validators=[DataRequired()])
    # country = StringField('country', validators=[DataRequired()])
    # zipcode = StringField('zipcode', validators=[DataRequired()])

# class OrderForm(Form):
#     # Add order input form fields here
#     name_of_part = StringField('name_of_part', validators=[DataRequired()])
#     manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])
