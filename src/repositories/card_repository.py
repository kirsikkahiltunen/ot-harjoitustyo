from database_connection import get_database_connection


class CardRepository:
    """Luokka, joka vastaa tehtäväkortteihin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self):
        """Luokan konstruktori. Luo luokalle tietokantayhteyden. 
        """
        self._connection = get_database_connection()

    def list_all(self):
        """Listaa kaikki exercises -tietokantataulun rivit.

        Returns:
            rows: Exercises -tietokantataulun rivit.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT category FROM exercises")
        rows = cursor.fetchall()
        return rows
