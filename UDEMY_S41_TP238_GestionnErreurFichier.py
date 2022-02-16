from pathlib import Path

nom_fichier = r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\fichier_invalide'
# nom_fichier = 'yyyy'
# nom_fichier = r'D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\fichier_valide.txt'

try:
    with open(nom_fichier, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('Fichier non trouvé.')
