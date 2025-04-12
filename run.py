"""Run the Flask application instance"""

from mealyzer import create_app
from mealyzer.database.database_utils import create_database, database_exists


def main():
    """Launch the web app

    Checks if the databse exists, creates it if not.
    Then launches the web app.
    """

    if not database_exists():
        create_database()

    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()
