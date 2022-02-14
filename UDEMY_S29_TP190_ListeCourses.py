import sys

items_liste = list()

while True:

    # Affichage du menu
    print('\nChoisissez parmi les 5 options suivantes\n\
    1: Ajouter un element à la liste\n\
    2: Retirer un element de la liste\n\
    3: Afficher la liste\n\
    4: Vider la liste\n\
    5: Quitter')

    choice = input('Votre choix : ')
    # Action en fonction du choix
    if choice == '1':
        new_item = input('Element à ajouter : ')
        items_liste.append(new_item)
        print(f'Confirmation: element {new_item} ajouté !\n')
    elif choice == '2':
        old_item = input('Element à retirer : ')
        if old_item in items_liste:
            items_liste.remove(old_item)
            print(f'Confirmation: element {old_item} retiré !\n')
        else:
            print('Cet element n\'est pas present dans la liste')
    elif choice == '3':
        print('Voici le contenu de votre liste :\n')
        for i, element in enumerate(items_liste):
            print(f'{i+1} {element}')
    elif choice == '4':
        items_liste.clear()
        print(f'Confirmation: liste vidée !\n')
    elif choice == '5':
        sys.exit()
    else:
        print('Choix invalide, recommencez.')

    print('------------------------------------')