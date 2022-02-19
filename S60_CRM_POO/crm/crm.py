import re
import string
from tinydb import TinyDB, where
from pathlib import Path
from pprint import pprint

class User:

    DB = TinyDB(Path(__file__).resolve().parent / 'db.json', indent=4)

    def __init__(self, first_name: str, last_name: str, phone_number: str='', address: str=''):
        self.first_name = first_name
        self.last_name = last_name 
        self.phone_number = phone_number
        self.address = address 

    def __repr__(self):
        return f"User({self.first_name}, {self.last_name})"

    def __str__(self):
        return f"{self.full_name} habite {self.address}, numero {self.phone_number}.\n"

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    
    @property
    def db_instance(self):
        return User.DB.get((where('first_name') == self.first_name) & (where('last_name') == self.last_name))

    def _checks(self):
        self._check_phone_number()
        self._check_names()

    def _check_phone_number(self):
        phone_number = re.sub(r'[+()\s]*', '', self.phone_number)
        if len(phone_number) < 10 or not phone_number.isdigit():
            raise ValueError(f"Numéro de téléphone {self.phone_number} invalide.")

    def _check_names(self):
        if not(self.first_name and self.last_name):
            raise ValueError("Le prénom et le nom ne peuvent pas être vides.")

        specials_char = string.punctuation + string.digits

        for char in self.first_name + self.last_name:
            if char in specials_char:
                raise ValueError(f"Nom invalide: {self.full_name}")

    def save(self, validate_data=False) -> int():
        if validate_data:
            self._checks()
        return User.DB.insert(self.__dict__)

    def delete(self) -> list[int]:
        if self.exists():
            return User.DB.remove(doc_ids=[self.db_instance.doc_id])
        return []

    def exists(self):
        if self.exists():
            return -1
        else:
            return bool(self.db_instance)

def get_all_users():
    return [User(**user) for user in User.DB.all()]
    # for user in User.DB.all():
    #     each_user = User(**user)
    #     print(each_user.last_name)


if __name__ ==  '__main__':
    
    martin = User('Sophie', 'Daniel')
    print(martin.db_instance)
    print(martin.delete())
    # >> Enregistremetn des données dans DB
    # from faker import Faker
    # fake = Faker(locale='fr_FR')
    # for _ in range(10):
    #     user = User(fake.first_name(), fake.last_name(), fake.phone_number(), fake.address())
    #     print(user.save(validate_data=True))
    #     print('-' * 10)

    # >> Test get all users    
    # pprint(get_all_users())