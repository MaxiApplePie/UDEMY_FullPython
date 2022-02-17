class Livre:
    def __init__(self, n:str, nb:int, p:float):
        self.nom = n 
        self.nombre_de_pages = nb
        self.prix = p

livre_HP = Livre("Harry Potter", 300, 10.99)
livre_LOTR = Livre("Le signeur des anneaux", 400, 11.99)

