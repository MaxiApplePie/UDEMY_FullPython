import random

player_1 = 'Lolo'
player_2 = 'Ennemi'

points_de_vie_player1 = 50
points_de_vie_player2 = 50
nombre_de_potions_player1 = 3

1
while True:
    choice = '0'
    while choice not in ['1', '2']:
        choice = input("Souhaitez vous attaquer(1) ou utiliser une potion(2) ? ")

    # Gestion du choix
    if choice == '1':
        attak = random.randint(5, 15)
        points_de_vie_player2 -= attak
        print(f'Vous avez infligé {attak} \U0001F52B points de dommage')
    elif choice == '2':
        potion_bonus = random.randint(15, 50)
        points_de_vie_player1 += potion_bonus
        print(f'Vous avez récupéré {potion_bonus} \U0001FA79 points de vie')
        nombre_de_potions_player1 -= 1

    if points_de_vie_player2 <= 0:
        print('Tu as gagné !')
        break

    # L'ennemi vous attaque
    attak = random.randint(5, 15)
    print(f'L\'ennemi vous a infligé {attak} \U0001F52B points de dommage')
    points_de_vie_player1 -= attak

    # Bilan vie
    if points_de_vie_player1 <= 0:
        print('Tu as perdu !')
        break
    
    print(f'Il vous reste {points_de_vie_player1} points de vie.')
    print(f'Il reste {points_de_vie_player2} points de vie à votre ennemi .')

    print('------------------------------------------------------')