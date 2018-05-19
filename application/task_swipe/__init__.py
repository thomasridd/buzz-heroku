from flask import Blueprint

swipe_blueprint = Blueprint('swipe', __name__, url_prefix='/task-2')

from application.task_swipe.views import swipe_menu