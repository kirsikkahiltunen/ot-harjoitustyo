import unittest
from repositories.card_repository import CardRepository


class TestCardRepo(unittest.TestCase):
    def setUp(self):
        self.card_repo = CardRepository()

    def test_list_all_returns_all_rows_of_exercises_table(self):
        list_all = self.card_repo.list_all()
        self.assertEqual(len(list_all), 2)

    def test_get_question_returns_correct_question(self):
        question = self.card_repo.get_question(1, 30)
        self.assertEqual(question, """Emma seisoo yhdellä jalalla,hänen kengän 
                        pintaala on 0.016 neliömetriä ja hänen kengän
                        alueelle kohdistuva voima on 465.679 newtonia,
                        laske kuinka suuren paineen Emma aiheuttaa maahan.""")

    def test_get_question_returns_different_values_every_time(self):
        question1 = self.card_repo.get_question(1)
        question2 = self.card_repo.get_question(1)
        self.assertNotEqual(question1, question2)

    def test_solve_returns_true_when_correct_answer(self):
        question = self.card_repo.get_question(1, 30)
        is_correct = self.card_repo.solve_exercise(1, 29104.938)
        self.assertEqual(is_correct, True)

    def test_solve_returns_false_when_incorrect_answer(self):
        question = self.card_repo.get_question(1, 30)
        is_correct = self.card_repo.solve_exercise(1, 29503.938)
        self.assertEqual(is_correct, False)

    def test_get_correct_answer_text_returns_correct_answer(self):
        question = self.card_repo.get_question(1, 30)
        is_correct = self.card_repo.solve_exercise(1, 29104.938)
        correct_answer_text = self.card_repo.get_correct_answer_text(1)
        self.assertEqual(correct_answer_text, """Paine lasketaan kaavalla p=F/A eli p=465.679/0.016
                        oikea vastaus on siis 29104.94 pascalia""")

    def test_save_to_review_exercises_saves_exercise_to_review_exercises_table(self):
        self.card_repo.save_to_review_exercises(1)
        self.card_repo.save_to_review_exercises(2)
        get_all = self.card_repo.get_all_review_exercises()
        self.assertEqual(len(get_all), 2)

    def test_find_category_finds_correct_category(self):
        card_category = self.card_repo.find_category(1)
        self.assertEqual(card_category, "Paine")

    def test_get_category_with_id_get__correct_categorynumber(self):
        category = self.card_repo.get_category_with_id(1)
        self.assertEqual(category, 1)
