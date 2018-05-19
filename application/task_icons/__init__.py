from flask import Blueprint

icons_blueprint = Blueprint('icons', __name__, url_prefix='/task-1')

from application.task_icons.views import icon_menu
