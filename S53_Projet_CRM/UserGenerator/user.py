"""module to generate users"""
from faker import Faker
from pprint import pprint
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename= BASE_DIR / 'user.log', level=logging.INFO)


faking = Faker(locale='fr_FR')


def get_user():
    """generate single user
 
    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f'{faking.first_name()} {faking.last_name()}'


def get_users(nb_users : int):
    """Generate a liste of user

    Args:
        nb_users (int): Number of users to generate

    Returns:
        list: users
    """
    logging.info(f"Generating a list of {nb_users} users.")
    users_list = list()
    return [get_user() for _ in range(nb_users)]


if __name__ == "__main__":
   print(get_users(4))
