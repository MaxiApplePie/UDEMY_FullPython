import os
import json
import logging
-
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, 'data', 'movies.json')

# logging.basicConfig(level=logging.WARNING,
#         filename='app.log',
#         filemode='a',
#         format='%(asctime)s - %(levelname)s - %(message)s')


def get_movies():

    with open(DATA_FILE, 'r') as f:
        movies_title = json.load(f)
    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:

    def __init__(self, title):
        self.title = title.title()


    def __repr__(self):
        return f"{self.title}"


    def _get_movies(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)


    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)


    def add_to_movies(self):
        movies = self._get_movies()
        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà dans la liste.")
            return False

    def remove_from_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas dans la liste.")
            return False

# CLI 
# from movie import Movie
# r = Movie('le seigneur des anneaux')
if __name__ == '__main__':
    movies = get_movies()
    print(movies)