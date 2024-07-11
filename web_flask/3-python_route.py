#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Returns Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Returns HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def printTet(text):
    """Displays 'C' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ') if '_' in text else text
    return 'C ' + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays 'python' followed by the value of <text>.

    Replaces any underscores in <text> with slashes.
    """
    text = text.replace('_', ' ') if '_' in text else text
    return 'Python ' + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
