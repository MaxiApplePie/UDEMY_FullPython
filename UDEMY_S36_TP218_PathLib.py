from pathlib import Path
import shutil

p = Path.home()

for f in p.iterdir():
    print(f.name)
