from database_connection import get_database_connection


class UserRepository:
    """Luokka, joka vastaa käyttäjään liittyvistä tietokantaoperaatioista.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo luokalle tietokantayhteyden.
        """
        self._connection = get_database_connection()
        self.user = None

    def find_user_by_username(self, username):
        """Etsii käyttäjän users -taulusta.

        Args:
            username: Käyttäjätunnus, jonka tiedot etsitään taulusta.

        Returns:
            row: palauttaa rivin, joka vastaa annettua käyttäjätunnusta.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT username, password FROM users WHERE username=?", (username,))

        row = cursor.fetchone()
        return row

    def list_all(self):
        """Palauttaa kaikki tiedot users -taulusta.

        Returns:
            rows: Palauttaa taulun kaikki rivit.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT username, password FROM users")
        rows = cursor.fetchall()
        return rows

    def create_user(self, user, password):
        """Lisää uuden käyttäjän users -tauluun, mikäli käyttäjätunnusta ei ole vielä varattu.

        Args:
            user: Luotu käyttäjätunnus.
            password: Luotu salasana.

        Returns:
            True: jos käyttäjätunnusta ei ole varattu ja tietojen lisääminen tietokantaan onnistui.
            False: jos käyttäjätunnus on jo users -taulussa.
        """
        already_existing = self.find_user_by_username(user)
        if already_existing:
            return False
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) values (?, ?)",
                       (user, password))
        self._connection.commit()

        return True

    def login(self, user, password):
        """Annetun käyttäjätunnuksen ja salasanan tarkistus ja käyttäjän sisään kirjaaminen.

        Args:
            user: Käyttäjän antama käyttäjätunnus.
            password: Käyttäjän antama salasana.

        Returns:
            True: jos käyttäjätunnus löytyy tietokannasta ja salasana täsmää.
            False: jos käyttäjänimi tai salasana virheellinen.
        """
        user_row = self.find_user_by_username(user)
        self.user = user

        if user_row is None or password != user_row[1]:
            return False

        return True

    def logout(self):
        """Kirjaa käyttäjän ulos sovelluksesta.
        """
        self.user = None

    def delete_all_users(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()
