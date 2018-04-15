from flask import render_template

from application.version_1 import version_1_blueprint

@version_1_blueprint.route('/')
def index():
    return render_template('version1.html')

