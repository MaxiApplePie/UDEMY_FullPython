from PySide2 import QtWidgets
import currency_converter


class App(QtWidgets.QWidget):
    """Fenetre

    Args:
        QtWidgets (_type_): _description_
    """ 
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle('Convertisseur de devises by LMC')
        self.setup_UI()
        self.set_default_values()
        self.setup_connections()
        self.setup_css()

    def setup_css(self):
        self.setStyleSheet("""
        background-color: rgb(30,30,30);
        color: rgb(240,240,240);
        border: none;
        """)
        self.btn_inverse.setStyleSheet("""
        background-color: red;
        
        """)

    def setup_UI(self):
        # Interface graphique .. self = Il faut apparenter le layout à l'interface
        self.layout = QtWidgets.QHBoxLayout(self)
        
        # Combo Box : cbb_
        self.cbb_devisesFrom = QtWidgets.QComboBox()
        self.spn_montant = QtWidgets.QSpinBox()
        self.cbb_devisesTo = QtWidgets.QComboBox()
        self.spn_montantConverti = QtWidgets.QSpinBox()
        self.btn_inverse = QtWidgets.QPushButton('Inversion devises')
        
        self.layout.addWidget(self.cbb_devisesFrom)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devisesTo)
        self.layout.addWidget(self.spn_montantConverti)
        self.layout.addWidget(self.btn_inverse)

    def set_default_values(self):
        self.cbb_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.cbb_devisesFrom.setCurrentText('EUR')
        self.cbb_devisesTo.setCurrentText('USD')

        self.spn_montant.setRange(1, 1000000)
        self.spn_montantConverti.setRange(1, 1000000)
        self.spn_montant.setValue(100)
        self.spn_montantConverti.setValue(100)

    def setup_connections(self):
        # Attention ... focntions depreciées
        self.cbb_devisesFrom.activated.connect(self.compute)
        self.cbb_devisesTo.activated.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.btn_inverse.clicked.connect(self.inverser_devises)

    def compute(self):
        montant = self.spn_montant.value()
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        try:
            resultat = self.c.convert(montant, devise_from, devise_to)
        except currency_converter.currency_converter.RateNotFoundError:
            print('Echec de conversion')
        else:
            self.spn_montantConverti.setValue(resultat)

    def inverser_devises(self):
        devise_from = self.cbb_devisesFrom.currentText()
        devise_to = self.cbb_devisesTo.currentText()
        self.cbb_devisesFrom.setCurrentText(devise_to)
        self.cbb_devisesTo.setCurrentText(devise_from)        
        self.compute()


# >>> Application 
app = QtWidgets.QApplication([])
# >>> Fenetre 
win = App()
win.show()
app.exec_()


