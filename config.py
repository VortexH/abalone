import os

class Config(object):
    APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY') or 'e4e6f3ac4014f9e5badshfkj79c0e69c8e'
    GOOGLE_LOGIN_CLIENT_ID = '753487899865-c2pln8bgpndo6pftsrjmaa4o62i1dqkr.apps.googleusercontent.com'
    GOOGLE_LOGIN_CLIENT_SECRET = 'jHfeVJTxe4pxYAP0x4MlsYk-'
