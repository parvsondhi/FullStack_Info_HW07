from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class CustomerForm(Form):
	first_name = StringField("first_name", validators=[DataRequired()])
	last_name = StringField("last_name", validators=[DataRequired()])
	company = StringField("company", validators=[DataRequired()])
	email = EmailField("email", validators=[DataRequired()])
	phone = IntegerField("phone", validators=[DataRequired()])
	address = StringField("address", validators=[DataRequired()])
	city = StringField("city", validators=[DataRequired()])
	state = StringField("state", validators=[DataRequired()])
	country = StringField("country", validators=[DataRequired()])
	zip_code = IntegerField("zip_code", validators=[DataRequired()])

class OrderForm(Form):
    # Add order input form fields here
    name_of_part = StringField("name_of_part", validators=[DataRequired()])
    manufacturer_of_part = StringField("manufacturer_of_part", validators=[DataRequired()])
