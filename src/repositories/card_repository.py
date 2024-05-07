from database_connection import get_database_connection
from cards import Card


class CardRepository:
    """Luokka, joka vastaa tehtäväkortteihin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self):
        """Luokan konstruktori. Luo luokalle tietokantayhteyden. 
        """
        self._connection = get_database_connection()
        self.card = Card()

    def list_all(self):
        """Listaa kaikki exercises -tietokantataulun rivit.

        Returns:
            rows: Exercises -tietokantataulun rivit.
        """
        cursor = self._connection.cursor()
        data = cursor.execute("SELECT id, category FROM exercises")
        rows = data.fetchall()
        return rows
    
    def get_category_with_id(self, id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT category FROM exercises WHERE id=?", (id, ))
        row = cursor.fetchone()
        return row[0]
    
    def find_category(self, category):
        cursor = self._connection.cursor()
        cursor.execute("SELECT category_text FROM card_categories WHERE category=?", (category, ))
        row = cursor.fetchone()
        return row[0]
    
    def get_question(self, id):
        question = self.find_question_with_id(id)
        variable_info = self.get_variables(id)
        variables=self.card.generate_variables(variable_info)
        for key, value in variables.items():
            question = question.replace("{" + key + "}", str(value))
        
        return question
    
    def find_question_with_id(self, id):
        cursor = self._connection.cursor()
        cursor.execute("SELECT question FROM exercises WHERE id=?", (id, ))
        row = cursor.fetchone()
        return row[0]
    
    def get_variables(self, id):
        variable_info={}
        cursor = self._connection.cursor()
        cursor.execute("SELECT variables FROM exercises WHERE id=?", (id, ))
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

    


        
