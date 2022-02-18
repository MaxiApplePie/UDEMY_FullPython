import os
import json
import logging

from constants import DATA_DIR

LOGGER = logging.getLogger()

class Liste(list):

    def __init__(self, nom:str ="default"):
        self.nom = nom

    def ajouter(self, item):
        if not isinstance(item, str):
            raise ValueError("Vous ne pouvez ajouter que des chaines de caracteres.")

        if item in self:
            LOGGER.error(f"{item} est deja dans la liste.")    
            return False

        self.append(item)
        return True

    def afficher(self):
        print(f'La liste {self.nom} contient : {", ".join(self)}')

    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR, f"{self.nom}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)

        with open(chemin, 'w', encoding='utf-8') as f:
            json.dump(self, f, indent=4)

        return True

    def enlever(self, item):
        if item in self:
            self.remove(item)
            return True
        return False

if __name__ == "__main__":
    l1 = Liste("courses")
    print(l1)
    resultat = l1.ajouter('pomme')
    if resultat:
        # Possibilité d'aller dans une interface graphique
        pass
    resultat = l1.ajouter('banane')
    l1.sauvegarder()


