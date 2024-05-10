import random


class Card:
    """Luokka, joka vastaa tehtäväkortteihin liittyvistä operaatioista. 
    """

    def __init__(self, seed=None):
        """Luokan konstruktori, joka alustaa tehtäväkortin muuttujat.

        Args:
            seed: Parametri, jota käytetään luokan testaamiseen, 
            kun generoidaan satunnaiset muuttujat tehtäväpohjaan. Defaults to None.
        """
        self.seed = seed

    def generate_variables(self, variables, seed=None):
        """Generoi uudet muuttujat, joilla tehtävä tulee ratkaista.
        """
        if seed is not None:
            self.seed = seed
            random.seed(self.seed)
            generated_variables = {}
            for variable, info in variables.items():
                generated_var = round(random.uniform(
                    info["min"], info["max"]), 3)
                generated_variables[variable] = generated_var
            return generated_variables
        generated_variables = {}
        for variable, info in variables.items():
            generated_var = round(random.uniform(info["min"], info["max"]), 3)
            generated_variables[variable] = generated_var
        return generated_variables

    def solve(self, operation, variables):
        """Ratkaisee tehtävän generoiduilla muuttujilla.

        Returns:
            palauttaa tehtävän oikean vastauksen.
        """
        for key, value in variables.items():
            operation = operation.replace("{" + key + "}", str(value))
        solved = eval(operation)
        result = round(solved, 2)
        return result

    def show_solution(self, correct_answer_text, variables, correct):
        """Luo merkkijono muotoisen oikean vastauksen.
        Returns:
                Palauttaa merkkijonon, jossa on oikea ratkaisu kysyttyyn tehtävään.
        """
        for key, value in variables.items():
            correct_answer_text = correct_answer_text.replace(
                "{" + key + "}", str(value))
        correct_answer_text = correct_answer_text.replace(
            "{answer}", str(correct))
        return correct_answer_text
