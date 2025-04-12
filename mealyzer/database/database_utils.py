"""Functions supporting database creation and modification."""

import os
import sqlite3


PATH = "mealyzer/database/"
SCHEMA = "schema.sql"
DATABASE_NAME = "database.db"


def database_exists():
    """Check if the database file exists.

    :return: True if the database file exists, else False
    :rtype: bool
    """
    if os.path.isfile(os.path.join(PATH, DATABASE_NAME)):
        return True
    return False


def create_database():
    """Create the database if it does not already exist.
    
    Database schema should exist where defined by global vars PATH/SCHEMA.
    """
    if database_exists():
        print("ERROR: attempting to make a database when one already exists.")
        return
    schema_path = os.path.join(PATH, SCHEMA)
    if not os.path.isfile(schema_path):
        print("ERROR: schema not found.")
        return

    connection = sqlite3.connect(os.path.join(PATH, DATABASE_NAME))
    with open(schema_path, "r", encoding="UTF-8") as sql:
        connection.executescript(sql.read())

    connection.commit()
    connection.close()
