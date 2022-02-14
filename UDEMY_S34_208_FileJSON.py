import json
from textwrap import indent

file_path = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\S34_204_File.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

data.append(4)

with open(file_path, 'w', encoding='utf-8') as f:
    data = json.dump(data, f, indent=4)

print(data)
    


