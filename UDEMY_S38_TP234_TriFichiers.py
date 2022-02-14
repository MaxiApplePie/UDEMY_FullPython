"""
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, xls, csv, odp, pages : Documents
autres : Divers
"""

from importlib.resources import path
from pathlib import Path
import random
import string

# Parametrage
extensions_liste = ['mp3', 'wav', 'flac', 'avi', 'mp4', 'gif', 'bmp', 'png', 'jpg', 'txt', 'pptx', 'xls', 'csv', 'odp', 'pages', 'bobby']

dirs = {
    '.mp3': 'Musique',
    '.wav': 'Musique',
    '.flac': 'Musique',
    '.avi': 'Videos',
    '.mp4': 'Videos',
    '.gif': 'Videos',
    '.bmp': 'Images', 
    '.png': 'Images', 
    '.jpg' : 'Images', 
    '.txt': 'Documents',
    '.pptx': 'Documents',
    '.xls': 'Documents',
    '.csv': 'Documents',
    '.odp': 'Documents',
    '.pages': 'Documents'
    }

letters = "azertyuiopmlkjhgfdsqwxcvbn"
letters_list = list()
for l in letters:
    letters_list.append(l)
print(letters_list)

# Generation des fichiers
""" for i in range(50):
    file_middle = ''.join(random.choice(letters_list) for i in range(random.randint(7, 22)))
    file_extension = random.choice(extensions_liste)
    file = file_middle + '.' + file_extension
    print(file)

    p = Path.cwd() / 'source' / file
    print(p)
    p.touch()
 """

# Tri des fichiers
tri_dir = Path.cwd() / 'source'
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = Path.cwd() / 'target' / dirs.get(f.suffix, 'Autres')
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)