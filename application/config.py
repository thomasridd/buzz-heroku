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
    OAUTH_CREDENTIALS = {
        "type": "service_account",
        "project_id": "buzz-buzz-buzz",
        "private_key_id": os.environ['AUTH_PRIVATE_KEY_ID'],
        "private_key": os.environ['AUTH_PRIVATE_KEY'].replace('[BREAK]', '\n'),
        "client_email": os.environ['AUTH_CLIENT_EMAIL'],
        "client_id": os.environ['AUTH_CLIENT_ID'],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://accounts.google.com/o/oauth2/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ['AUTH_CERT_URL']
    }



class DevConfig(Config):
    DEBUG = None
    PUSH_ENABLED = False
    FETCH_ENABLED = False
    ENVIRONMENT = 'DEV'
    SESSION_COOKIE_SECURE = False
    SERVER_NAME = 'localhost:5000'