from database_connection import get_database_connection

class UserRepository:
    def __init__(self):
        self._connection = get_database_connection()

    def find_user_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT username FROM users WHERE username=?", (username,))

        row = cursor.fetchone()
        return row
    
    def list_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows=cursor.fetchall()
        print(rows)


    def create_user(self, user, password):
        already_existing = self.find_user_by_username(user)
        if already_existing:
            return False
        else:
            cursor = self._connection.cursor()
            cursor.execute("INSERT INTO users (username, password) values (?, ?)",
                        (user, password))
            self._connection.commit()

        return True
