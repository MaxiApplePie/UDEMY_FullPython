import random

print('*** Le jeu du nombre mystère ***')
nb_essais = 5
attempts = 0

soluce = random.randint(0, 100)

while attempts < 5:
    print(f'Il te reste {nb_essais} essais')
    number_input = input('Devine le nombre : ')
    if not number_input.isdigit():
        print('Veuillez entrer un nombre valide.')
    else:
        if int(number_input) > soluce:
            print('Le nombre mystere est plus petit')
        elif int(number_input) < soluce:
            print('Le nombre mystere est plus grand')
        else:
            print('Bravo, vous avez gagné')
            break
        attempts += 1
    if attempts == 5:
        print(f'Le nombre mystere etait {soluce}')
        print('Dommage vous avez perdu')

print('Fin du jeu')