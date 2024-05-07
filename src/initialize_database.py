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
    cursor.execute('''
        DROP TABLE if EXISTS rewiev_exercises;
    ''')

    cursor.execute('''
        DROP TABLE if EXISTS card_categories;
    ''')

    connection.commit()


def create_tables():
    """Luo uudet tietokantataulut users ja exercises.
    """
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id integer primary key,
            username text,
            password text
        );
    ''')

    cursor.execute('''
        CREATE TABLE exercises (
            id integer primary key,
            category int,
            variables text,
            question text
        );
    ''')

    cursor.execute('''
        CREATE TABLE rewiev_exercises (
            id integer primary key,
            category int,
            variables text,
            question text
        );
    ''')

    cursor.execute('''
        CREATE TABLE card_categories (
            category int,
            category_text text
        );
    ''')

    connection.commit()


def add_cards_to_exercises():
    """Lisää exercises-tietokantatauluun tehtäviä.
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO exercises (category, variables, question) values (?, ?, ?)",
                   (1, 'variable1:0.01, 0.022; variable2:350, 750',
                    '''Emma seisoo yhdellä jalalla,
                       hänen kengän pintaala on {variable1} neliömetriä
                         ja hänen kengän alueelle kohdistuva voima on {variable2} newtonia,
                           laske kuinka suuren paineen Emma aiheuttaa maahan.'''))

    cursor.execute("INSERT INTO exercises (category, variables, question) values (?, ?, ?)",
                   (2, 'variable1:5, 30; variable2:300, 10000',
                    '''Laske ajoneuvon liike-energia
                       kun sen nopeus on {variable1} metriä 
                       sekunnissa ja massa {variable2} kilogrammaa'''))

    connection.commit()

def add_categories_to_card_categories():
    cursor = connection.cursor()
    cursor.execute("INSERT INTO card_categories (category, category_text) values (?, ?)",
                   (1, 'Paine'))
    
    cursor.execute("INSERT INTO card_categories (category, category_text) values (?, ?)",
                   (2, 'Liike-energia'))
    
    connection.commit()

drop_tables()
create_tables()
add_cards_to_exercises()
add_categories_to_card_categories()