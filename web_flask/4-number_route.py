#!/usr/bin/python3
"""Flask framework"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """home
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """c text
    """
    display_text = text.replace('_', ' ')
    return "C {}".format(display_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ pyhon text
    """
    display_text = text.replace('_', ' ')
    return f"Python {display_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def check_number(n):
    """integer number"""
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
