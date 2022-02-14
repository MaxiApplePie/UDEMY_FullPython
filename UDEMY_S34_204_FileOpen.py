file_path = r"D:\DEV\UDEMY_Tuto_45h_PYTHON\UDEMY_FullPython\Resources\S34_204_File.txt"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read().splitlines()
    print(content)


