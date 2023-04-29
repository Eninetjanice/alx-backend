#!/usr/bin/env python3
"""
Basic flask application
"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate app object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap app with Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
