from flask import Blueprint

tree_blueprint = Blueprint('tree', __name__, url_prefix='/task-3')

from application.task_tree.views import tree_menu