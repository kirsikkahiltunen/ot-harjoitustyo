import random


class Card:
    def __init__(self, category, seed=None):
        self.category = category
        self.seed = seed
        self.force = None
        self.area = None
        self.mass = None
        self.velocity = None
        self.pressure = None
        self.kineticenergy = None

    def generate_variables(self):
        if self.seed is not None:
            random.seed(self.seed)
        if self.category == 1:
            self.force = random.randint(350, 750)  # force in newtons
            self.area = round(random.uniform(0.01, 0.022),
                              3)  # area in square meters
        if self.category == 2:
            self.mass = random.randint(300, 10000)  # mass in kilograms
            # velocity in meters per second
            self.velocity = random.randint(5, 30)

    def solve(self):
        if self.category == 1:
            self.pressure = self.force/self.area
            return f"{self.pressure:.2f}"
        if self.category == 2:
            self.kineticenergy = (1/2)*self.mass*self.velocity**2
            return f"{self.kineticenergy:.2f}"
        return None

    def show_solution(self):
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
