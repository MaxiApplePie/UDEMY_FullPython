liste = [1, 2, 3, 4, 5]
liste.append(6)
if 6 in liste:
    print('Le nombre 6 a bien été ajouté à la liste.')


langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

python = langages[0][0]
deux = nombres[1][1][0]
print(deux)
sept = nombres[-1][-1][-1]
print(sept)