import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

ENV = os.getenv('ENV', 'dev')
HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 6666))
