from flask import render_template

from application.version_1 import version_1
from application.services.google_service import google_service

@version_1.route('/')
def index():
    return render_template('version1.html')


@version_1.route('/register-click/<animal>/', methods=['POST'])
def register_click(animal):
    print(animal)
    google_service.add_row(['list menu', 'select', animal])
    return 'hello'
