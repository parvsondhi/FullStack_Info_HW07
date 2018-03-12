from flask.ext.wtf import Form
from wtforms import PasswordField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class LoginForm(Form):
    email = EmailField('email', render_kw={'class': 'form-control', 'placeholder': 'john@doe.com', 'required': True}, validators=[DataRequired('Please enter a valid email address.')])
    password = PasswordField('password', render_kw={'class': 'form-control', 'placeholder': 'your secret password', 'required': True}, validators=[DataRequired('Please enter a password.')])