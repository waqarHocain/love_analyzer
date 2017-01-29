# third party imports
from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views