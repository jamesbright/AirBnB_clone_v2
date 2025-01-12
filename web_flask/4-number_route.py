#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
# create an instance of flask app
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Display Hello HBNB!"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Display HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display C followed by text"""

    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """Display Python followed by text"""

    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Displays: "n is a  number". only if it is"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
