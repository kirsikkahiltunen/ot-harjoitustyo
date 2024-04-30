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

    def test_give_hint_returns_correct_hint_when_category_is_1(self):
        self.card.generate_variables()
        self.assertEqual(str(self.card.give_hint()),
                         "Paine lasketaan kaavalla p=F/A")

    def test_give_hint_returns_correct_hint_when_category_is_2(self):
        self.card3.generate_variables()
        self.assertEqual(str(self.card3.give_hint()),
                         "Liike-energia lasketaan kaavalla E=1/2mv^2")

    def test_seed_is_not_None_if_there_are_2_parameters_for_class_Card(self):
        self.assertNotEqual(self.card.seed, None)

    def test_solve_function_calculate_answer_and_saves_it_to_variable_pressure_when_category_is_1(self):
        self.card.generate_variables()
        self.card.solve()
        self.assertNotEqual(self.card.pressure, None)

    def test_solve_function_calculate_answer_and_saves_it_to_variable_pressure_when_category_is_2(self):
        self.card3.generate_variables()
        self.card3.solve()
        self.assertNotEqual(self.card3.kineticenergy, None)
