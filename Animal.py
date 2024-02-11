class Animal:
    def __init__(self,nom):
        self.nom=nom
    def faire_son_crie(self):
        print("l'animal fait son crie")
class Chat (Animal):
    def faire_son_crie(self):
        print("Miaouuuuuuu")
class Chien (Animal):
    def faire_son_crie(self):
        print(self.nom,"fait","wouuuuuuu")

max=Chien("max")
max.faire_son_crie()


