""" Script to start a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

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

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
