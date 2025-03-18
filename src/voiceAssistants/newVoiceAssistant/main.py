from os import getenv
from pyWrkspPackage import *

# General Setup
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
if AI_KEY is None:
    raise ValueError('AI_TOKEN is not set')

AI_MODEL = 'mistral-large-latest'
AI_URL = 'http://192.168.86.4:4001'
