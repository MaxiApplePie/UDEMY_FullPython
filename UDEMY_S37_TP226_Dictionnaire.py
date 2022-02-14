
d = {
    0: {
        "prenom": "Pierre",
        "ville": "Marseille"
    },
    1: {
        "prenom": "Alain",
        "ville": "Lyon"
    }
}
print(d[0]["ville"])

d[0]["ville"] = "Bordeaux"

print(d[0]["ville"])
print(d[0].get("toto", 'Pas de bol'))

films = {
    0: {
        "nom": "Le seigneur des anneaux",
        "prix": "12€"
    },
    1: {
        "nom": "Harry Potter",
        "prix": "9€"
    },
    2: {
        "nom": "Balde runner",
        "prix": "7.5€"
    }
}

print(films[0].keys())

for cle, valeur in films.items():
    print(cle)
    print(valeur)