
while True:

    # Saisie des nombre
    nombre_a = input('Entrer un premier nombre : ')
    nombre_b = input('Entrer un deuxieme nombre : ')

    # Controle de la saisie
    if not nombre_a.isdigit() or not nombre_b.isdigit():
        print('Veuillez entrer deux nombres valides.')
    else:
        print(f'Le résultat de l\'addition de {nombre_a} avec {nombre_b} est égal à {int(nombre_a) + int(nombre_b)}')
        break  

