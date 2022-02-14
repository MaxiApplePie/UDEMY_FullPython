from pathlib import Path

print(Path.home())
print(Path.cwd())

p = Path.cwd()
print(p.parent.parent)

print(p / "Documents")


