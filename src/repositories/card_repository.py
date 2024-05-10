from database_connection import get_database_connection
from cards import Card
from repositories.user_repository import UserRepository


class CardRepository:
    """Luokka, joka vastaa tehtäväkortteihin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self):
        """Luokan konstruktori. Hakee luokalle tietokantayhteyden sekä kutsuu 
        luokkia Card ja UserRepository. 
        """
        self._connection = get_database_connection()
        self.variables = None
        self.correct_answer = None
        self.card = Card()
        self.user_repo = UserRepository()

    def list_all(self):
        """Listaa kaikki exercises -tietokantataulun rivit.

        Returns:
            rows: Exercises -tietokantataulun rivit.
        """
        cursor = self._connection.cursor()
        data = cursor.execute("SELECT id, category FROM exercises")
        rows = data.fetchall()
        return rows

    def get_all_info_from_exercise_with_id(self, exercise_id):
        """Hakee kaikki sarakkeet ecercises taulun riviltä, jonka id vastaa 
        parametrina olevaa exercise_id:tä.

        Args:
            exercise_id: tehtävän id

        Returns:
            row: löydetyn rivin tiedot SQLiten row formaatissa.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id, category, variables, question FROM exercises WHERE id=?", (exercise_id, ))
        row = cursor.fetchone()
        return row

    def get_all_review_exercises(self):
        """Hakee kaikkien rivien kaikki tiedot review_exercises taulusta.

        Returns:
            rows: löydettyjen rivien tiedot SQLite row formaatissa.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT exercise_id, category, variables, question FROM review_exercises")
        rows = cursor.fetchall()
        return rows

    def get_category_with_id(self, exercise_id):
        """Hakee rivin parametrina annetun id:n perusteella 
        exercises taulusta ja palauttaa tehtävän kategoria numeron.

        Args:
            exercise_id: Tehtävän id

        Returns:
            row[0]: Palauttaa kategorianumeron(row muuttujan ensimmäisen indeksin)
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT category FROM exercises WHERE id=?", (exercise_id, ))
        row = cursor.fetchone()
        return row[0]

    def find_category(self, category):
        """Etsii card_categories taulusta merkkijonona
        kategorian nimen kategorian numeron avulla.

        Args:
            category (int): kategoriaa vastaava numero

        Returns:
            row[0]: palauttaa kategorian merkkijonona 
            (row muuttujan ensimmäisen indeksin)
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT category_text FROM card_categories WHERE category=?", (category, ))
        row = cursor.fetchone()
        return row[0]

    def find_operation(self, exercise_id):
        """Hakee laskukaavan tehtävän ratkaisemiseen.

        Args:
            exercise_id: Tehtävän id

        Returns:
            row[0]: palauttaa kaavan merkkijonona 
            (row muuttujan ensimmäisen indeksin)
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT operation FROM correct_answers WHERE exercise_id=?", (exercise_id, ))
        row = cursor.fetchone()
        return row[0]

    def get_question(self, exercise_id, seed=None):
        """Luo kysymystekstin, johon on lisätty generoidut muuttujat.

        Args:
            exercise_id: Tehtävän id
            seed: Testatessa käytettävä seed. Defaults to None.

        Returns:
            question: Kysymys merkkijonona.
        """
        question = self.find_question_with_id(exercise_id)
        if seed is not None:
            variable_info = self.get_variables(exercise_id)
            self.variables = self.card.generate_variables(variable_info, seed)
            for key, value in self.variables.items():
                question = question.replace("{" + key + "}", str(value))
            return question
        variable_info = self.get_variables(exercise_id)
        self.variables = self.card.generate_variables(variable_info)
        for key, value in self.variables.items():
            question = question.replace("{" + key + "}", str(value))
        return question

    def find_question_with_id(self, exercise_id):
        """Hakee tehtävän id:tä vastaavan kysymyksen.

        Args:
            exercise_id: Tehtävän id

        Returns:
            row[0]: Palauttaa tehtävän merkkijonona alkuperäisellä muotoilulla 
            (row muuttujan ensimmäisen indeksin)
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT question FROM exercises WHERE id=?", (exercise_id, ))
        row = cursor.fetchone()
        return row[0]

    def get_variables(self, exercise_id):
        """Hakee exercises taulusta muuttujien minimi ja maksimi arvot 
        muuttujien generointia varten.

        Args:
            exercise_id: Tehtävän id

        Returns:
            variable_info: Palauttaa sanakirjan variable_info.
        """
        variable_info = {}
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT variables FROM exercises WHERE id=?", (exercise_id, ))
        row = cursor.fetchone()
        variables = row[0].split(";")
        for variable in variables:
            name, values = variable.split(":")
            values = values.split(",")
            variable_info[name.strip()] = {
                'min': float(values[0]),
                'max': float(values[1])
            }
        return variable_info

    def solve_exercise(self, exercise_id, answer):
        """Hakee oikean vastauksen ja tarkistaa, onko 
        käyttäjän vastaus oikein.

        Args:
            exercise_id: Tehtävän id
            answer: Käyttäjän antama vastaus

        Returns:
            True: vastaus on oikein
            False: vastaus on väärin
        """
        operation = self.find_operation(exercise_id)
        correct = self.card.solve(operation, self.variables)
        self.correct_answer = correct
        answer = float(answer)
        answer = round(answer, 2)
        if answer == correct:
            return True
        return False

    def get_correct_answer_text(self, exercise_id):
        """Hakee tehtävän mallivastauksen correct_answers taulusta.

        Args:
            exercise_id: Tehtävän id

        Returns:
            get_correct_answer: Mallivastaus merkkijonona, sisältää generoidut 
            muuttujat ja oikean vastauksen.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT correct_answer FROM correct_answers WHERE exercise_id=?", (exercise_id, ))
        row = cursor.fetchone()
        correct_answer_text = row[0]
        variables = self.variables
        correct = self.correct_answer
        get_correct_answer = self.card.show_solution(
            correct_answer_text, variables, correct)
        return get_correct_answer

    def save_to_review_exercises(self, exercise_id):
        """Tallentaa väärin menneet tehtävät review_exercises tauluun.
        """
        exercise = self.get_all_info_from_exercise_with_id(exercise_id)
        user = self.user_repo.user
        cursor = self._connection.cursor()
        cursor.execute("""INSERT INTO review_exercises (exercise_id, username, category,
                        variables, question) values (?, ?, ?, ?, ?)""",
                       (exercise[0], user, exercise[1], exercise[2], exercise[3]))
        self._connection.commit()
