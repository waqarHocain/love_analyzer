# third party imports
from flask import render_template, redirect, url_for
from flask_login import login_required

# local imports
from . import home
from app import db
from .forms import ResponseForm
from ..models import User, Response


@home.route("/")
def homepage():
	return render_template("home/index.html")


@home.route("/<int:id>/dashboard")
@login_required
def dashboard(id):
	user = User.query.filter_by(id = int(id)).first()

	# if the given id doesn't belong to anyone, redirect to homepage
	if user is None:
		return redirect(url_for("home.homepage"))

	responses = Response.query.filter_by(owner = user).all()

	return render_template("home/dashboard.html", responses = responses)


@home.route("/<int:id>/analyzer", methods=["GET", "POST"])
def analyzer(id):
	form = ResponseForm()

	# check the given id
	user = User.query.filter_by(id = int(id)).first()
	if user is not None and form.validate_on_submit():
		response = Response(name = form.name.data,
							response1 = form.response1.data,
							response2 = form.response2.data,
							response3 = form.response3.data,
							owner = user)
		db.session.add(response)
		db.session.commit()

		form_submitted = True

		return render_template("home/oops.html", form_submitted = form_submitted, name = user.name)

	return render_template("home/analyze.html", form = form)