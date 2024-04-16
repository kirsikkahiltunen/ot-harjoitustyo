import unittest
from cards import Card


class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(1, 43)
        self.card2 = Card(1)
        self.card3 = Card(2, 40)

    def test_generate_variables_set_value_to_force_if_category_is_1(self):
        self.card.generate_variables()
        self.assertEqual(self.card.force, 369)

    def test_generate_variables_set_value_to_area_if_category_is_1(self):
        self.card.generate_variables()
        self.assertEqual(self.card.area, 0.013)

    def test_generate_variables_set_value_to_velocity_if_category_is_2(self):
        self.card3.generate_variables()
        self.assertEqual(self.card3.velocity, 23)

    def test_generate_variables_set_value_to_mass_if_category_is_2(self):
        self.card3.generate_variables()
        self.assertEqual(self.card3.mass, 7813)

    def test_seed_is_None_if_there_is_only_1_parameter_for_class_Card(self):
        self.assertEqual(self.card2.seed, None)
