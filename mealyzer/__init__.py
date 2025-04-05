"""Flask application instance

Import app to create a Flask application instance for the given module.
"""

from flask import Flask

from mealyzer import views


app = Flask(__name__)
app.register_blueprint(views.bp)
