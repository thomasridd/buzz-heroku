from flask import render_template

from application.home import home_blueprint

@home_blueprint.route('/')
def index():
    return render_template('home.html')


