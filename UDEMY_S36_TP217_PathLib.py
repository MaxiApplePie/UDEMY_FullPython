from pathlib import Path
import shutil

print(Path.home())
print(Path.cwd())

p = Path.cwd() / "Dossiertest"
print(p)
p.mkdir(exist_ok=True)

p = Path.cwd() / "Dossiertest" / "1" / "2" / "3"
# p.mkdir(exist_ok=True, parents=True)

p = p / "readme.rtf"
# p.unlink()

p = p.parent
print(p)
# p.rmdir()
p = p.parent.parent.parent
print(p)
shutil.rmtree(p)
