from dataclasses import dataclass

@dataclass
class User:
    first_name: str
    last_name:str

u1 = User(first_name='a', last_name='b')
print(u1)
print(u1.last_name)