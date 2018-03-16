from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class userForm(Form):
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = EmailField('email', validators=[DataRequired()])


class tripForm(Form):
    """
    name_of_part = StringField('name_of_part', validators=[DataRequired()])
    manufacturer_of_part = StringField('manufacturer_of_part', validators=[DataRequired()])
    """
