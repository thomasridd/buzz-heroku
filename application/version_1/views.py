from flask import render_template

from application.version_1 import version_1


@version_1.route('/')
def index():
    return render_template('version1.html')


@version_1.route('/register_click/<animal>/', methods=['POST'])
def register_click(animal):
    print(animal)
    return 'hello'
