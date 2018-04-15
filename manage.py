#! /usr/bin/env python
import os

from flask_script import Manager, Server


from application.factory import create_app
from application.config import Config, DevConfig

env = os.environ.get('ENVIRONMENT', 'DEV')

app = create_app(DevConfig)

manager = Manager(app)
manager.add_command("server", Server())

if __name__ == '__main__':
    manager.run()
