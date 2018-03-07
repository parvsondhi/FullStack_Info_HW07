from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
    first_name = StringField('firstName', validators=[DataRequired()])
    last_name = StringField('lastName', validators=[DataRequired()])
    company = StringField('company', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone_number = StringField('phone_number', validators=[DataRequired()]) # just making this a string field rather than using PhoneNumberField

class AddressForm(Form):    
	street_address = StringField('street_address', validators=[DataRequired()])
	city = StringField('city', validators=[DataRequired()])
	state = StringField('state', validators=[DataRequired()])
	country = StringField('country', validators=[DataRequired()])
	zipcode = IntegerField('zipcode', validators=[DataRequired()])
    # Add additional Address fields here

class OrderForm(Form):
    # Add order input form fields here
    name_of_part = StringField('name_of_part', validators=[DataRequired()])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])
