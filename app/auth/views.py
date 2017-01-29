# third party imports
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

# local imports
from . import auth
from app import db
from ..models import User
from .forms import LoginForm, RegisterForm

@auth.route("/login", methods = ["GET", "POST"])
def login():
	form = LoginForm()

	if form.validate_on_submit():
		# check provided credentials
		user = User.query.filter_by(email = form.email.data).first()
		if user is not None and user.verify_password(form.password.data):

			login_user(user)

			return redirect(url_for("home.dashboard", id = user.id))

		flash("Incorrect email or password.")
		return render_template("auth/login.html", form = form)

	# render login template on a GET request
	return render_template("auth/login.html", form = form)


@auth.route("/register", methods = ["GET", "POST"])
def register():
	form = RegisterForm()

	if form.validate_on_submit():
		# add user to database
		user = User(name = form.name.data,
					email = form.email.data,
					password = form.password.data)

		db.session.add(user)
		db.session.commit()

		flash("Your account has been created successfully.")
		return redirect(url_for("auth.login"))

	return render_template("auth/register.html", form = form)

@auth.route("/logout")
@login_required
def logout():
	logout_user()

	flash("You have successfully been logged out.")

	return redirect(url_for("auth.login"))