from flask import Blueprint

home_blueprint = Blueprint('home', __name__, url_prefix='/')

from application.home.views import index
