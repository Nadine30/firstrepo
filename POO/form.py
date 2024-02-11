from math import pow
class Form:
    def __init__(self):
        print("une forme a été crée")
class Cercle(Form):
    def __init__(self,rayon):
        super().__init__()
        self.rayon=rayon
    def Surface(self):
        print(self.rayon*pow(3,14^2))
class Rectangle(Form):
    def __init__(self,longueur,largeur):
        super().__init__()
        self.longueur=longueur
        self.largeur=largeur
    def Aire(self):
        print(self.longueur*self.largeur)

rect=Rectangle(4,2)
rect.Aire()