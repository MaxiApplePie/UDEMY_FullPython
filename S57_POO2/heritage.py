projets = ['pr_HP', 'Avengers', 'pr_GOT']

class Utilisateur:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def __str__(self):
        return f"Utilisateur {self.prenom} {self.nom}"

    def afficher_projets(self):
        for projet in projets:
            print(projet)

class Junior(Utilisateur):
    def __init__(self, nom, prenom):
        super().__init__(nom, prenom)

    def afficher_projets(self):
        for projet in projets:
            if not projet.startswith('pr_'):
                print(projet)


Paul = Junior('Durant', 'Paul')
Paul.afficher_projets()