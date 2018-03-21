from flask.ext.wtf import Form
from wtforms import StringField, IntegerField, SelectField, PasswordField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired, Required

class LoginForm(Form):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])

class SignupForm(Form):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])

class AddTripForm(Form):
    # Add order input form fields here
    trip_name = StringField("trip_name", validators=[DataRequired()])
    destination = StringField("destination", validators=[DataRequired()])
    friend = SelectField("friend", coerce=int)

