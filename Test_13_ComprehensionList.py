mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if not mdp:
    print(mdp_trop_court.upper())
elif mdp.isdigit():
    print('Votre mot de passe ne contient que des nombres.')
elif len(mdp) < 8:
    print(mdp_trop_court.capitalize())
else:
    print('Inscription terminée.')

