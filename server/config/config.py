import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'postgres://flasklogin:flasklogin@localhost/flasklogin'