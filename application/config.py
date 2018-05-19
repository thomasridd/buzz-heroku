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
    SECRET_KEY = os.environ['SECRET_KEY']
    WTF_CSRF_ENABLED = True

    CHOICES = [
        {'item': 'Fish', 'value': 'Fish', 'image': 'fish.png'},
        {'item': 'Wasp', 'value': 'Wasp', 'image': 'Wasp.png'},
        {'item': 'Elephant', 'value': 'Elephant', 'image': 'Elephant.png'},
        {'item': 'Dolphin', 'value': 'Dolphin', 'image': 'Dolphin.png'},
        {'item': 'Horse', 'value': 'Horse', 'image': 'Horse.png'},
        {'item': 'Swan', 'value': 'Swan', 'image': 'Swan.png'},
        {'item': 'Koala', 'value': 'Koala', 'image': 'Koala.png'},
        {'item': 'Camel', 'value': 'Camel', 'image': 'Camel.png'},
        {'item': 'Antelope', 'value': 'Antelope', 'image': 'Antelope.png'},
        {'item': 'Bee', 'value': 'Bee', 'image': 'Bee.png'},
        {'item': 'Goose', 'value': 'Goose', 'image': 'Goose.png'},
        {'item': 'Fox', 'value': 'Fox', 'image': 'Fox.png'},
        {'item': 'Bear', 'value': 'Bear', 'image': 'Bear.png'},
        {'item': 'Walrus', 'value': 'Walrus', 'image': 'Walrus.png'},
        {'item': 'Dragonfly', 'value': 'Dragonfly', 'image': 'Dragonfly.png'},
        {'item': 'Sheep', 'value': 'Sheep', 'image': 'Sheep.png'},
        {'item': 'Zebra', 'value': 'Zebra', 'image': 'Zebra.png'},
        {'item': 'Pigeon', 'value': 'Pigeon', 'image': 'Pigeon.png'},
        {'item': 'Deer', 'value': 'Deer', 'image': 'Deer.png'},
        {'item': 'Pig', 'value': 'Pig', 'image': 'Pig.png'},
        {'item': 'Gnat', 'value': 'Gnat', 'image': 'Gnat.png'},
        {'item': 'Dog', 'value': 'Dog', 'image': 'Dog.png'},
        {'item': 'Eagle', 'value': 'Eagle', 'image': 'Eagle.png'},
        {'item': 'Frog', 'value': 'Frog', 'image': 'Frog.png'},
    ]

    TREE = [
        {'item': 'Animal', 'is_leaf': False, 'tree': [
            {'item': 'Land', 'is_leaf': False, 'tree': [
                {'item': 'Elephant', 'is_leaf': True},
                {'item': 'Horse', 'is_leaf': True},
                {'item': 'Koala', 'is_leaf': True},
                {'item': 'Camel', 'is_leaf': True},
                {'item': 'Antelopes', 'is_leaf': True},
            ]},
            {'item': 'Water', 'is_leaf': False, 'tree': [
                {'item': 'Frog', 'is_leaf': True},
                {'item': 'Walrus', 'is_leaf': True},
                {'item': 'Hippo', 'is_leaf': True},
            ]},
        ]},
        {'item': 'Fish', 'is_leaf': False, 'tree': [
            {'item': 'Salmon', 'is_leaf': True},
            {'item': 'Shark', 'is_leaf': True},
            {'item': 'Whale', 'is_leaf': True},
            {'item': 'Dolphin', 'is_leaf': True},
        ]},
        {'item': 'Insects', 'is_leaf': False, 'tree': [
            {'item': 'Bee', 'is_leaf': True},
            {'item': 'Wasp', 'is_leaf': True},
            {'item': 'Gnat', 'is_leaf': True},
        ]},
        {'item': 'Birds', 'is_leaf': False, 'tree': [
            {'item': 'Goose', 'is_leaf': True},
            {'item': 'Eagle', 'is_leaf': True},
            {'item': 'Pigeon', 'is_leaf': True},
        ]}
    ]


class DevConfig(Config):
    DEBUG = True
    PUSH_ENABLED = False
    FETCH_ENABLED = False
    ENVIRONMENT = 'DEV'
    SESSION_COOKIE_SECURE = False
    SERVER_NAME = 'localhost:5000'
