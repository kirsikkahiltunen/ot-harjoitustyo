import sqlite3
import os

connection = sqlite3.connect(os.path.join(
    os.path.dirname(__file__), "..", "data", "database.sqlite"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection
