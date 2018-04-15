from flask import (
    Flask
)

from application.services.google_service import google_service

def create_app(config_object):

    from application.home import home_blueprint
    from application.version_1 import version_1

    app = Flask(__name__)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(version_1)

    google_service.init_service(config_object.OAUTH_CREDENTIALS)
    return app
