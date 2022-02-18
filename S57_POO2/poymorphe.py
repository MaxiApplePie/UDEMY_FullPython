class Vehicule:
    def avance(self):
        print('Le vehicule avance')

class Voiture(Vehicule):
    def roule(self):
        super().avance()
        print('La voiture roule')

class Avion(Vehicule):
    def vole(self):
        super().avance()
        print('L\'avion vole')


a = Avion()
a.vole()

