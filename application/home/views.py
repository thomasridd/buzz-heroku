from application.home import home_blueprint

@home_blueprint.route('/')
def index():
    return 'home'

