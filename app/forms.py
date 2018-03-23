from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class TripForm(Form):
    trip_title = StringField('trip_title', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    friend = SelectField('friend', validators=[DataRequired()])
  
    # company = StringField('company', validators=[DataRequired()])
    # email = EmailField('email', validators=[DataRequired()])
    # phone_number = StringField('phone_number', validators=[DataRequired()])
    # street_address = StringField('street_address', validators=[DataRequired()])
    # city = StringField('city', validators=[DataRequired()])
    # state = StringField('state', validators=[DataRequired()])
    # country = StringField('country', validators=[DataRequired()])
    # zip_code = IntegerField('zip_code', validators=[DataRequired()])

# class UserForm(Form):
#     # Add order input form fields here
#     name_of_part = StringField('name_of_part', validators=[DataRequired()])
#     manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])