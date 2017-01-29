# Third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email
from wtforms import ValidationError

# Local imports
from ..models import User

class LoginForm(FlaskForm):
	"""
	Form for users to login
	"""
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField("Password", validators = [DataRequired()])
	remember_me = BooleanField("Remember me")
	submit = SubmitField("Login")


class RegisterForm(FlaskForm):
	"""
	Form for users to create new account
	"""
	name = StringField("Name", validators = [DataRequired()])
	email = StringField("Email", validators = [DataRequired(), Email()])
	password = PasswordField("Password", validators = [DataRequired()])
	submit = SubmitField("Register")

	def validate_email(self, field):
		"""
		Prevent users from creating two accounts with same email
		"""
		if User.query.filter_by(email = field.data).first():
			raise ValidationError("Email is already in use.")

