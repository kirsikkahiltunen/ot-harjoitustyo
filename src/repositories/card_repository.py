from database_connection import get_database_connection

class CardRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def list_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT category FROM exercises")
        rows=cursor.fetchall()
        return rows