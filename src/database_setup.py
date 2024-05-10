from database_connection import get_database_connection
from initialize_database import InitializeDatabase


def initialize_database():
    connection = get_database_connection()
    init_db = InitializeDatabase(connection)
    init_db.drop_tables()
    init_db.create_tables()
    init_db.add_cards_to_exercises()
    init_db.add_categories_to_card_categories()
    init_db.add_correct_answers()

initialize_database()
