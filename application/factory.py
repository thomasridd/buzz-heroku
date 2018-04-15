
from flask import (
    Flask
)


def create_app(config_object):

    from application.home import home_blueprint
    from application.version_1 import version_1_blueprint

    app = Flask(__name__)

    app.register_blueprint(home_blueprint)
    app.register_blueprint(version_1_blueprint)

    return app
