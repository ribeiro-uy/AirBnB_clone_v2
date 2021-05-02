#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """
    Route:
    display “n is a number” only if n is an integer
    """
    states = storage.all('State')
    return render_template('6-number_odd_or_even.html', states=states.values())


@app.teardown_appcontext
def close(self):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()

if __name__ == '__main__':
    app.run(port=5000)
