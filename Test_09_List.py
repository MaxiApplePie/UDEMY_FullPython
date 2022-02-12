# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0] 
nombre_dernier = nombres[-1]

# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
langages = ["Java", "Python", "C++"]
langage = langages[1]

# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
liste = ["Java", "Python", "C++"]
liste.remove('Python')
liste.append('Python')
# print(liste)

usrer_list = ['Utilisateur_01',
        'Utilisateur_02',
        'Utilisateur_03',
        'Utilisateur_04',
        'Utilisateur_05',
        'Utilisateur_06']

#print(usrer_list[:4])

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
print(trois_premiers)
trois_derniers = liste[3:]
print(trois_derniers)
milieu = liste[1:-1]
print(milieu)
premier_dernier = liste[::5]
print(premier_dernier)

pos_carlos = liste.index("Carlos")
print(f"Carlos est arrivé en position {pos_carlos}.")

print(sorted(nombres))

film = "le seigneur des anneaux"
film.title()
print(film)