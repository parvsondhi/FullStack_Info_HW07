from flask.ext.wtf import Form
from wtforms import StringField
# from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired


class TripForm(Form):
    destination = StringField('destination', validators=[DataRequired()])
    friend = StringField('friend', validators=[DataRequired()])