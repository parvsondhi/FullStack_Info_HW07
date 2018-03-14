from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
    company = StringField('company', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    fname = StringField('fname', validators=[DataRequired()])
    lname = StringField('lname', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])

class AddressForm(Form):
    street_address = StringField('street_address', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    zip_code = IntegerField('zip_code', validators=[DataRequired()])

class OrderForm(Form):
    part_name = StringField('part_name', validators=[DataRequired()])
    manufacturer = StringField('manufacturer', validators=[DataRequired()])
