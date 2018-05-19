from flask import (
    Flask
)
from flask_wtf import CSRFProtect

csrf = CSRFProtect()

from application.services.google_service import google_service


def create_app(config_object):
    from application.task_swipe import swipe_blueprint
    from application.task_icons import icons_blueprint
    from application.root import root_blueprint

    app = Flask(__name__)
    app.config.from_object(config_object)

    app.register_blueprint(swipe_blueprint)
    app.register_blueprint(icons_blueprint)
    app.register_blueprint(root_blueprint)
    csrf.init_app(app)

    google_service.init_service(config_object.OAUTH_CREDENTIALS)
    return app
