def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if EXISTS users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id serial primary key,
            username text,
            password text
        );
    ''')

    connection.commit()
