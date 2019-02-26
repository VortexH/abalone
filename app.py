#!/usr/bin/env python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/login')
def login():
    return 'login'

@app.route('/logout')
def logout():
    return 'logout'

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
