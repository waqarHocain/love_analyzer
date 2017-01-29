# Third party imports
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ResponseForm(FlaskForm):
	"""
	Form to store a user victim's response
	"""
	name = StringField("Enter Your Name", validators=[DataRequired()])
	response1 = StringField("Your crush 1 name", validators=[DataRequired()])
	response2 = StringField("Your crush 2 name", validators=[DataRequired()])
	response3 = StringField("Your crush 3 name", validators=[DataRequired()])
	submit = SubmitField("Analyze")
	