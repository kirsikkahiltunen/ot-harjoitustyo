import random


class Card:
    """Luokka, joka vastaa tehtäväkortteihin liittyvistä operaatioista. 
    """

    def __init__(self, seed=None):
        """Luokan konstruktori, joka alustaa tehtäväkortin muuttujat.

        Args:
            category: Käyttäjän valitsema tehtäväkategoria
            seed: Parametri, jota käytetään luokan testaamiseen, 
            kun generoidaan satunnaiset muuttujat tehtäväpohjaan. Defaults to None.
        """
        self.seed = seed
        self.force = None
        self.area = None
        self.mass = None
        self.velocity = None
        self.pressure = None
        self.kineticenergy = None

    def generate_variables(self, variables):
        """Generoi uudet muuttujat, joilla tehtävä tulee ratkaista.
        """
        if self.seed is not None:
            random.seed(self.seed)
        generated_variables={}
        for variable, info in variables.items():
            generated_var=round(random.uniform(info["min"],info["max"]), 3)
            generated_variables[variable]=generated_var
        return generated_variables

    def solve(self):
        """Ratkaisee annetun tehtävän generoiduilla muuttujilla.

        Returns:
            palauttaa tehtäväkategorian mukaisen vastauksen f-string muodossa.
            Jos tehtäväkategoria ei ole mikään määritellyistä, palautetaann None.
        """
        if self.category == 1:
            self.pressure = self.force/self.area
            return f"{self.pressure:.2f}"
        if self.category == 2:
            self.kineticenergy = (1/2)*self.mass*self.velocity**2
            return f"{self.kineticenergy:.2f}"
        return None

    def give_hint(self):
        """Antaa käyttäjälle vihjeen tehtävän ratkaiemiseksi.

        Returns:
                Palauttaa merkkijonon, jossa kerrotaan kategorian mukainen vihje. 
        """
        if self.category == 1:
            return "Paine lasketaan kaavalla p=F/A"
        if self.category == 2:
            return "Liike-energia lasketaan kaavalla E=1/2mv^2"
        return None

    def show_solution(self):
        """Näyttää käyttäjälle oikean vastauksen.
        Returns:
                Palauttaa merkkijonon, jossa on oikea ratkaisu kysyttyyn tehtävään.
        """
        if self.category == 1:
            return f"""Paine lasketaan kaavalla p=F/A
              eli p={self.force}/{self.area} 
              oikea vastaus on siis {self.pressure:.2f} pascalia"""
        if self.category == 2:
            return f"""Liike-energia lasketaan
              kaavalla E=1/2mv^2 eli
                E=1/2*{self.mass}*{self.velocity}^2
                  oikea vastaus on siis {self.kineticenergy:.2f} joulea"""
        return None
