from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class UserForm(Form):
	# user form
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])


