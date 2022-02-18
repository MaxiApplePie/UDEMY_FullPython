import json
import sys

liste_courses_path = r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\S35_ListeCourese.txt'

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

        with open(liste_courses_path, 'r')  as f:
            content = json.load(f)

        content.append(new_item)

        with open(liste_courses_path, 'w')  as f:
           json.dump(content, f, indent=4)

        print(f'Confirmation: element {new_item} ajouté !\n')

    elif choice == '2':
        old_item = input('Element à retirer : ')

        with open(liste_courses_path, 'r')  as f:
            content = json.load(f)

        if old_item in content:
            content.remove(old_item)

            with open(liste_courses_path, 'w')  as f:
                json.dump(content, f, indent=4)
                
                print(f'Confirmation: element {old_item} retiré !\n')
        else:
            print('Cet element n\'est pas present dans la liste')

    elif choice == '3':
        print('Voici le contenu de votre liste :\n')
        with open(liste_courses_path, 'r') as f:
            content = json.load(f)
            print(content)

    elif choice == '4':
        with open(liste_courses_path, 'w') as f:
            json.dump(list(), f)
        print(f'Confirmation: liste vidée !\n')

    elif choice == '5':
        sys.exit()

    else:
        print('Choix invalide, recommencez.')

    print('------------------------------------')