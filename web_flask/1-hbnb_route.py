#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Routes: / display “Hello HBNB!”
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Route: /hbnb display “HBNB”
    """
    return 'HBNB'

if __name__ == '__main__':
    app.run(port=5000)
