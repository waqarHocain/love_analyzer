# third party imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Local imports
from app import db, login_manager


class User(UserMixin, db.Model):
	"""
	User model
	"""
	__tablename__ = "user"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60))
	email = db.Column(db.String(60), unique = True)
	password_hash = db.Column(db.String(128))
	responses = db.relationship("Response", backref = "owner", lazy = "dynamic")

	@property
	def password(self):
		# prevent password from accessing
		raise AttributeError("Password is not a readable attribute")

	@password.setter
	def password(self, password):
		# store password as hashed string
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		# check if hashed password matches actual password
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return "<User : {}".format(self.email)


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class Response(db.Model):
	"""
	Table for storing a users responses
	"""
	__tablename__ = "response"

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60))
	response1 = db.Column(db.String(60))
	response2 = db.Column(db.String(60))
	response3 = db.Column(db.String(60))
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

