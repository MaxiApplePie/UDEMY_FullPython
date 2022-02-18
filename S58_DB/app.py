import json

fichier = "settings.json"

with open(fichier, 'r') as f:
    content = json.load(f)

#print(content.get("font-size"))

content["font-size"] = 15

with open(fichier, 'w') as f:
    json.dump(content, f, indent=4)
