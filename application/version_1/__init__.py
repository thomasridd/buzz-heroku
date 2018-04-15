from flask import Blueprint

version_1 = Blueprint('version_1', __name__, url_prefix='/v1')

from application.version_1.views import index
