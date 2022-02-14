import json
from textwrap import indent

file_path = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\S34_204_File.json"

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(list(range(1, 4)), f, indent=4)

