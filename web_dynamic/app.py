""" Script to start a Flask web application """
<<<<<<< HEAD

=======
>>>>>>> e3689c0a715309dd5695eb7d7740e9327496bdd5
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False
<<<<<<< HEAD

@app.route('/index', strict_slashes=False)
def index():
    ''' return the home page '''
    return render_template('index.html')

@app.route('/login')
def login():
    ''' returns the login page '''
    return render_template('login.html')

@app.route('/logout')
def logout():
    ''' returns the logout page '''
    return 'logout'
=======
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
>>>>>>> e3689c0a715309dd5695eb7d7740e9327496bdd5

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
