from flask_wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    company = StringField('company', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    phone = StringField('phone', validators=[DataRequired()])

    street = StringField('street', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    state = StringField('state', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    zipcode = IntegerField('zipcode', validators=[DataRequired()])

class OrderForm(Form):
    # Add order input form fields here
    part_name = StringField('part_name', validators=[DataRequired()])
    manufacturer = StringField('manufacturer', validators=[DataRequired()])
