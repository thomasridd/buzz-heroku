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
        {'item': 'Banana', 'value': 'Banana', 'image': 'banana.png'},
        {'item': 'Beer can', 'value': 'Beer can', 'image': 'beercan.png'},
        {'item': 'Bottle cap', 'value': 'Bottle cap', 'image': 'bottlecap.png'},
        {'item': 'Cigarette', 'value': 'Cigarette', 'image': 'cigarette.png'},
        {'item': 'Coke', 'value': 'Coke', 'image': 'coke.png'},
        {'item': 'Costa', 'value': 'Costa', 'image': 'costa.png'},
        {'item': 'Crisp packet', 'value': 'Crisp packet', 'image': 'crisppacket.png'},
        {'item': 'Food', 'value': 'Food', 'image': 'food.png'},
        {'item': 'Juice carton', 'value': 'Juice carton', 'image': 'juicecarton.png'},
        {'item': 'McDonalds', 'value': 'McDonalds', 'image': 'mcdonalds.png'},
        {'item': 'Plastic bag', 'value': 'Plastic bag', 'image': 'plasticbag.png'},
        {'item': 'Plastic bottle', 'value': 'Plastic bottle', 'image': 'plasticbottle.png'},
        {'item': 'Redbull', 'value': 'Redbull', 'image': 'redbull.png'},
        {'item': 'Starbucks', 'value': 'Starbucks', 'image': 'starbucks.png'},
        {'item': 'Straw', 'value': 'Straw', 'image': 'straw.png'},
    ]

    TREE = [
        {'item': 'Recyclable', 'value': 'Recyclable', 'image': 'recyclable.png', 'subitems': [
            {'item': 'Plastic bottle', 'value': 'Plastic bottle', 'image': 'plasticbottle.png'},
            {'item': 'Plastic bag', 'value': 'Plastic bag', 'image': 'plasticbag.png'},
            {'item': 'Straw', 'value': 'Straw', 'image': 'straw.png'},
            {'item': 'Bottle cap', 'value': 'Bottle cap', 'image': 'bottlecap.png'},
            {'item': 'Juice carton', 'value': 'Juice carton', 'image': 'juicecarton.png'},
            {'item': 'Starbucks', 'value': 'Starbucks', 'image': 'starbucks.png'},
            {'item': 'Costa', 'value': 'Costa', 'image': 'costa.png'},
            {'item': 'Redbull', 'value': 'Redbull', 'image': 'redbull.png'},
            {'item': 'Coke', 'value': 'Coke', 'image': 'coke.png'},
            {'item': 'Beer can', 'value': 'Beer can', 'image': 'beercan.png'},
        ]},
        {'item': 'Non-recyclable', 'value': 'Non-recyclable', 'image': 'nonrecyclable.png', 'subitems': [
            {'item': 'Cigarette', 'value': 'Cigarette', 'image': 'cigarette.png'},
            {'item': 'Food', 'value': 'Food', 'image': 'food.png'},
            {'item': 'Crisp packet', 'value': 'Crisp packet', 'image': 'crisppacket.png'},
            {'item': 'McDonalds', 'value': 'McDonalds', 'image': 'mcdonalds.png'},
            {'item': 'Banana', 'value': 'Banana', 'image': 'banana.png'},
        ]},
    ]


class DevConfig(Config):
    DEBUG = True
    PUSH_ENABLED = False
    FETCH_ENABLED = False
    ENVIRONMENT = 'DEV'
    SESSION_COOKIE_SECURE = False
    SERVER_NAME = 'localhost:5000'
