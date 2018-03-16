from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    

# class LoginForm(Form):

# class CreateTrip(Form):
