from database_connection import get_database_connection


connection=get_database_connection()

def drop_tables():
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if EXISTS users;
    ''')

    connection.commit()


def create_tables():
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id serial primary key,
            username text,
            password text
        );
    ''')

    connection.commit()

drop_tables()
create_tables()