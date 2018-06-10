from flask import Blueprint

scanner_blueprint = Blueprint('scanner', __name__, url_prefix='/task-4')

from application.task_scanner.views import scanner_menu