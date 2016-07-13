from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired

class RegistrationForm(Form):
	username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
	email = StringField('Email Address', [validators.DataRequired(), validators.Length(min=6, max=35)])
	password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
	confirm = PasswordField('Repeat Password')
	accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
	Username = StringField('Username', [validators.DataRequired()])
	Password = PasswordField('Password', [validators.DataRequired()])
	remember_me = BooleanField('remember_me', default = False)

