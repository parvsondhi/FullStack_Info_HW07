from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TripForm(FlaskForm):
    tripname = StringField('tripname', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    # friend_id = IntegerField('friend_id', validators=[NumberRange(min=1, max=3, message='DEBUG: Can only be 1 - 3')])# TESTING -- Replace with Drop down
    submit = SubmitField('Create Trip')
