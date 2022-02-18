class Voiture:

    voitures_crees = 0
    def __init__(self, marque, vitesse, prix):
        self.marque = marque
        self.vitesse = vitesse
        self.prix = prix
        Voiture.voitures_crees += 1

    @classmethod
    def lamborghini(cls):
        return cls(marque="Lamborghini", vitesse=250, prix=200000)

    @classmethod
    def volvo(cls):
        return cls(marque="Volvo", vitesse=250, prix=200000)

    @staticmethod
    def afficher_nombre_voitures():
        print(f"Vous avez {str(Voiture.voitures_crees)} voiture dans le garage.")

    def __str__(self):
        return f"Cette voiture {self.marque} coute {self.prix} et roule à {self.vitesse} km/h"

lambo = Voiture.lamborghini()
print(lambo.prix)
print(Voiture.afficher_nombre_voitures())
print(lambo)