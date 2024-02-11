class Personne:
    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age
    def show(self):
        print("Salut je m'appelle",self.nom,"\t","j'ai",self.age,"ans") 
P1=Personne("Tch","Nado",18)
P1.show()