from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

class TripForm(Form):
    title = StringField('Title', render_kw={'class': 'form-control', 'placeholder': 'Awesome Spring Break Trip', 'required': True}, validators=[DataRequired('How should be call you? Please enter a title for your trip.')])
    destination = StringField('Destination', render_kw={'class': 'form-control', 'placeholder': 'Brazil', 'required': True}, validators=[DataRequired('Please enter a destintion for your trip.')])
    submit = SubmitField('Submit', render_kw={'class': 'btn btn-primary btn-round'} )
