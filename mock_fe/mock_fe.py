from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'


@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host=host, port=port)
