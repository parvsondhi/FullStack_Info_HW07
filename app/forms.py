from flask_wtf import FlaskForm
# from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

# from flask.ext.wtf import Form
# from wtforms import StringField, IntegerField
# from flask_wtf.html5 import EmailField
# from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# class LoginForm(Form):

# class CreateTrip(Form):
