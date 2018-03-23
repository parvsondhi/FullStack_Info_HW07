from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class UserForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])

class TripForm(Form):
	trip = StringField('trip', validators=[DataRequired()])
	destination = StringField('destination', validators=[DataRequired()])
	friend = StringField('friend', validators=[DataRequired()])