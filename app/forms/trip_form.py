from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from app.models import User

class TripForm(Form):
    name = StringField('Trip Name', render_kw={'class': 'form-control', 'placeholder': 'Spring Break Gppd Luck with Your Liver', 'required': True}, validators=[DataRequired('Please enter your trip name.')])
    destination = StringField('Destination', render_kw={'class': 'form-control', 'placeholder': 'Floripa', 'required': True}, validators=[DataRequired('Please enter your travel destination')])
    submit = SubmitField('Login', render_kw={'class': 'btn btn-primary btn-round'} )
