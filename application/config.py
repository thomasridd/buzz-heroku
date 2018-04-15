import os
from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv

# Note this will fail with warnings, not exception
# if file does not exist. Therefore the config classes
# In Heroku, well... they are set in Heroku.


p = Path(dirname(__file__))
dotenv_path = join(str(p.parent), '.env')
load_dotenv(dotenv_path)


class Config:
    '''
    Right now we don't need any of this but let's keep it in the bag
    '''
    # GITHUB_ACCESS_TOKEN = os.environ['GITHUB_ACCESS_TOKEN']
    CONFIG_VAR = "config"
    BASE_DIRECTORY = dirname(dirname(os.path.abspath(__file__)))


class DevConfig(Config):
    DEBUG = None
    PUSH_ENABLED = False
    FETCH_ENABLED = False
    ENVIRONMENT = 'DEV'
    SESSION_COOKIE_SECURE = False
    SERVER_NAME = 'localhost:5000'