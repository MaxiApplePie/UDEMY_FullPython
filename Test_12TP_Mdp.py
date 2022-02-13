liste_nb = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_positif = list()
for elt in liste_nb:
    if elt >= 0:
        liste_positif.append(elt)

print(liste_positif)

liste_nb2 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
liste_positif2 = [elt for elt in liste_nb if elt >= 0]

print(liste_positif2)

for i in range(1, 11):
    print(f'Utilisateur {str(i)}')

mot = 'Python'
for letter in reversed(mot):
    print(letter) 

nombre = 7
for mult in range(11):
    print(f'{mult} x 7 = {mult * 7}')


continuer = "o"
while continuer == "o":
    if continuer == 'n':
        break
    print("On continue !")
    input("Voulez-vous continuer ? o/n ")