class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_user_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT username FROM users WHERE urname=?", (username))

        row = cursor.fechone()
        return row

    def create_user(self, user):
        already_existing = self.find_user_by_username(user)
        if already_existing:
            return False
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO users (username, password) values (?, ?)",
                       (user.username, user.password))
        self._connection.commit()

        return user
