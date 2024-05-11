import sqlite3
from config import DATABASE_FILE_PATH

def get_database_connection():
    """Hakee tietokannalle polun ja luo tietokantayhteyden

    Returns:
        Palauttaa tietokantayhteyden
    """
    db_connection = sqlite3.connect(DATABASE_FILE_PATH)
    db_connection.row_factory = sqlite3.Row

    return db_connection
