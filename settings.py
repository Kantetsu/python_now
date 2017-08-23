import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = os.path.join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

LINE_ACCESS_TOKEN = os.environ.get("LINE_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")
