from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

# class LoginForm(Form):
    
#     email_id = EmailField('email_id', validators=[DataRequired()])
#     password = StringField('password', validators=[DataRequired()])

class TripForm(Form):
    # Add order input form fields here
    trip_title = StringField('trip_title', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired()])
    friend = StringField('friend', validators=[DataRequired()])
    # friend = SelectField('friend', validators=[DataRequired()])


