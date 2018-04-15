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