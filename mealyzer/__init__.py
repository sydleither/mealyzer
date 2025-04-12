"""Flask application instance

Import app to create a Flask application instance for the given module.
"""

from flask import Flask

from mealyzer import views


def create_app():
    """Create Flask app instance.

    :return: app
    :rtype: Flask object
    """
    app = Flask(__name__)
    app.register_blueprint(views.bp)
    return app
