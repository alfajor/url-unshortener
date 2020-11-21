from os import environ

# set key for session cookie signing
SECRET_KEY = environ.get('SECRET_KEY')