from flask import Blueprint

tree_blueprint = Blueprint('tree', __name__, url_prefix='/task-3')

from application.task_swipe.views import swipe_menu