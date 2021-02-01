from app import db
from app.models import User
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import ValidationError, DataRequired, NumberRange
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class TripForm(FlaskForm):
    tripname = StringField('tripname', validators=[DataRequired()])
    destination = StringField('destination', validators=[DataRequired()])
    ## TESTING
    friend_id = SelectField('friend_id', choices=[(r.id, r.username) for r in User.query.with_entities(User.id, User.username)], coerce=int)
    # friend_id = IntegerField('friend_id', validators=[NumberRange(min=1, max=2)])
    submit = SubmitField('Create Trip')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
