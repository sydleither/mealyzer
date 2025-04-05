"""View functions

Defines the logic for executing client requests for a given URL.
All routes should pass in a title to render_template().
"""

from flask import Blueprint, render_template


bp = Blueprint("bp", __name__)


@bp.route("/", methods=["Get"])
def index() -> str:
    """Render home page.

    :return: The rendered HTML.
    :rtype: str
    """
    return render_template("index.html", title="Home Page")


# @bp.route("/add_recipe", methods=["Get", "Post"])
# def add_recipe() -> str:
#     '''Render page and save input to database.

#     :return: The rendered HTML.
#     :rtype: str
#     '''
#     return render_template("add_recipe.html", title="Add Recipe")
