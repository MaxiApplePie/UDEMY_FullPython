_username = 'Paul'
print(_username)
print(False + True)

l = [1, 2]
a = l.extend([3, 4])


class Voiture:
    roues = 4
    def afficher_roues(self):
        print(f"La voiture a {Voiture.roues} roues.")
 
voiture_01 = Voiture()
voiture_01.afficher_roues()