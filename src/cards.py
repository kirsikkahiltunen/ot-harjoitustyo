import random

class Card:
    def __init__(self, category, seed=None):
        self.category = category
        self.variables = []
        self.seed = seed
        


    
    def generate_variables(self):
        if self.seed is not None:
            random.seed(self.seed)
            if self.category == 1:
                force = random.randint(300, 2000) #force in newtons
                self.variables.append(force)
                area = random.randint(10, 1000) #area in square meters
                self.variables.append(area)

            
            elif self.category == 2:
                mass = random.randint(10, 1000) #mass in kilograms
                self.variables.append(mass)
                velocity = random.randint(5, 30) #velocity in meters per second
                self.variables.append(velocity)
        
    def solve(self):

        if self.category == 1:
            F = self.variables[0]
            A = self.variables[1]
            pressure = (F/A)
            return (f"Paine lasketaan kaavalla p=F/A eli p={F}/{A} oikea vastaus on siis {pressure} pascalia")
            
        elif self.category == 2:
            m = self.variables[0]
            v = self.variables[1]
            kineticenergy = ((1/2)*m*v**2)
            return (f"Liike-energia lasketaan kaavalla E=1/2mv^2 eli E=1/2*{m}*{v}^2 oikea vastaus on siis {kineticenergy} joulea")
        






        
    



    
    
        
