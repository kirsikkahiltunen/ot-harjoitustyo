import unittest
from cards import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(1, 43)

    def test_variables_is_empty_list_after_test_setUp(self):
        self.assertEqual(self.card.variables, [])

    def test_seed_is_None_if_there_is_only_1_parameter_for_class_Card(self):
        self.card2 = Card(1)
        self.assertEqual(self.card2.seed, None)

    def test_generate_variables_appends_variables_to_the_variables_list_when_category_is_1(self):
        self.card.generate_variables()
        self.assertNotEqual(self.card.variables, [])

        