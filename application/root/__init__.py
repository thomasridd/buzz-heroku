from flask import Blueprint

root_blueprint = Blueprint('root', __name__)

from application.root.views import index
