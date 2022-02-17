class Voiture:

    def __init__(self, essence=100):
        self.essence = essence
    
    def afficher_reservoir(self):
        # print(f"La voiture est une {self.marque}")
        print(f"La voiture contient {self.essence}L d'essence.")


    def faire_le_plein(self):
        self.essence += 100
        print("Vous pouvez repartir !")

    def roule(self, nb_kms:int):
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        else: 
            self.essence -= nb_kms * 0.05
            if self.essence < 10:
                print("Vous n'avez bientôt plus d'essence")
            self.afficher_reservoir()

v = Voiture()
v.afficher_reservoir()
v.roule(25)

class Voituree:
    prix = 30000
    def __init__(self, prix):
        self.prix = prix
 
Peugeot = Voituree(prix=20000)
print(Peugeot.prix)