from PySide2 import QtWidgets, QtCore
import movie as mv
from movie import Movie

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('CineClub')
        self.setupUI()
        self.populate_movies()
        self.setup_connections()

    def setupUI(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.line_movie_name = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton('Ajouter un film')
        self.txt_movie_list = QtWidgets.QListWidget()
        self.txt_movie_list.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete_movies = QtWidgets.QPushButton('Supprimer le(s) film(s)')

        self.layout.addWidget(self.line_movie_name)
        self.layout.addWidget(self.btn_add_movie)
        self.layout.addWidget(self.txt_movie_list)
        self.layout.addWidget(self.btn_delete_movies)

    def setup_connections(self):
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_delete_movies.clicked.connect(self.remove_movie)
        self.line_movie_name.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        movies = mv.get_movies() 
        for movie in movies:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.txt_movie_list.addItem(lw_item)

    def add_movie(self):
        movie_title = self.line_movie_name.text()
        if not movie_title:
            return False

        movie = Movie(movie_title)
        resultat = movie.add_to_movies()
        if resultat:
            lw_item = QtWidgets.QListWidgetItem(movie.title)
            lw_item.setData(QtCore.Qt.UserRole, movie)
            self.txt_movie_list.addItem(lw_item)

        self.line_movie_name.clear()

    def remove_movie(self):
        for selected_item in self.txt_movie_list.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.txt_movie_list.takeItem(self.txt_movie_list.row(selected_item))




# >>> Application 
app = QtWidgets.QApplication([])
# >>> Fenetre 
win = App()
win.show()
app.exec_()