employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

print(employes)
age_paul = employes["id01"].get("age")
print(age_paul)
 
# Au revoir Paul
del(employes["id01"])
print(employes)

# Julie, tu veillis
employes["id02"]["age"] = 26
print(employes)


