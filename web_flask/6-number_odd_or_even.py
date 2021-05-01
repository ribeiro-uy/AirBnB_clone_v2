#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
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


@app.route('/c/<text>')
def c(text=''):
    """
    Route:
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space
    """
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """
    Route:
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space
    """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number(n):
    """
    Route:
    display “n is a number” only if n is an integer
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Route:
    display “n is a number” only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def n_odd_or_even(n):
    """
    Route:
    display “n is a number” only if n is an integer
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(port=5000)
