class InitializeDatabase:
    """Luokka, joka vastaa tietokantatauluista.
    """
    def __init__(self, connection):
        self.connection = connection

    def drop_tables(self):
        """Poistaa jo olemassaolevat tietokantataulut:
        users, exercises, review_exercises,
        card_categories ja correct_answers.
        """
        cursor = self.connection.cursor()

        cursor.execute('''
            DROP TABLE if EXISTS users;
        ''')
        cursor.execute('''
            DROP TABLE if EXISTS exercises;
        ''')
        cursor.execute('''
            DROP TABLE if EXISTS review_exercises;
        ''')

        cursor.execute('''
            DROP TABLE if EXISTS card_categories;
        ''')

        cursor.execute('''
            DROP TABLE if EXISTS correct_answers;
        ''')

        self.connection.commit()

    def create_tables(self):
        """Luo uudet tietokantataulut 
        users, exercises, review_exercises,
        card_categories ja correct_answers.
        """
        cursor = self.connection.cursor()
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
            CREATE TABLE review_exercises (
                exercise_id int,
                username text,
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
        cursor.execute('''
            CREATE TABLE correct_answers (
                exercise_id int,
                hint text,
                correct_answer text,
                operation text
            );
        ''')
        self.connection.commit()

    def add_cards_to_exercises(self):
        """Lisää exercises-tietokantatauluun tehtäviä.
        """
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO exercises (category, variables, question) values (?, ?, ?)""",
                       (1, "variable1:0.01, 0.022; variable2:350, 750",
                        """Emma seisoo yhdellä jalalla,hänen kengän 
                        pintaala on {variable1} neliömetriä ja hänen kengän
                        alueelle kohdistuva voima on {variable2} newtonia,
                        laske kuinka suuren paineen Emma aiheuttaa maahan."""))
        cursor.execute("""INSERT INTO exercises (category, variables, question) values (?, ?, ?)""",
                       (2, "variable1:5, 30; variable2:300, 10000",
                        """Laske ajoneuvon liike-energia
                        kun sen nopeus on {variable1} metriä 
                        sekunnissa ja massa {variable2} kilogrammaa"""))
        self.connection.commit()

    def add_correct_answers(self):
        """Lisää correct_answers-tietokantatauluun tehtävien ratkaisuja.
        """
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO correct_answers
                    (exercise_id, hint, correct_answer, operation) 
                    values (?, ?, ?, ?)""",
                       (1, "Paine lasketaan kaavalla p=F/A",
                        """Paine lasketaan kaavalla p=F/A eli p={variable2}/{variable1}
                        oikea vastaus on siis {answer} pascalia""", "{variable2}/{variable1}"))
        cursor.execute("""INSERT INTO correct_answers
                    (exercise_id, hint, correct_answer, operation)
                        values (?, ?, ?, ?)""",
                       (2, "Liike-energia lasketaan kaavalla E=1/2mv^2", """Liike-energia lasketaan
                        kaavalla E=1/2mv^2 eli E=1/2*{variable2}*{variable1}^2
                    oikea vastaus on siis {answer} joulea""", "1/2*{variable2}*{variable1}**2"))
        self.connection.commit()

    def add_categories_to_card_categories(self):
        """Lisää card_categories-tietokantatauluun tehtävien kategoriat.
        """
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO card_categories (category, category_text) values (?, ?)""",
                       (1, 'Paine'))
        cursor.execute("""INSERT INTO card_categories (category, category_text) values (?, ?)""",
                       (2, 'Liike-energia'))
        self.connection.commit()
