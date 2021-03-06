""" Script to start a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

@app.route('/')
def index():
    ''' return the home page '''
    return render_template('login.html')

@app.route('/index')
def login():
    ''' returns the login page '''
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
