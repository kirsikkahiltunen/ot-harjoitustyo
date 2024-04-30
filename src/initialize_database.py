from database_connection import get_database_connection


connection = get_database_connection()


def drop_tables():
    """Poistaa jo olemassaolevat tietokantataulut users ja exercises.
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if EXISTS users;
    ''')
    cursor.execute('''
        DROP TABLE if EXISTS exercises;
    ''')

    connection.commit()


def create_tables():
    """Luo uudet tietokantataulut users ja exercises.
    """
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id serial primary key,
            username text,
            password text
        );
    ''')

    cursor.execute('''
        CREATE TABLE exercises (
            id serial primary key,
            category int,
            variables text,
            question text
        );
    ''')

    connection.commit()


def add_cards_to_exercises():
    """Lisää exercises-tietokantatauluun tehtäviä.
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO exercises (category, variables, question) values (?, ?, ?)",
                   (1, '"force":(350, 750); "area":(0.01, 0.022)',
                    '''Emma seisoo yhdellä jalalla,
                       hänen kengän pintaala on {area} neliömetriä
                         ja hänen kengän alueelle kohdistuva voima on {force} newtonia,
                           laske kuinka suuren paineen Emma aiheuttaa maahan.'''))

    cursor.execute("INSERT INTO exercises (category, variables, question) values (?, ?, ?)",
                   (2, '"mass":(300, 10000); "velocity":(5, 30)',
                    '''Laske ajoneuvon liike-energia
                       kun sen nopeus on {velocity} metriä 
                       sekunnissa ja massa {mass} kilogrammaa'''))

    connection.commit()


drop_tables()
create_tables()
add_cards_to_exercises()
