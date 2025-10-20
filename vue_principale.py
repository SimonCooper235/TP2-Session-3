from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QMessageBox
from PyQt6.uic import loadUi

from modele_integration import ModeleInetgration
from modele_liste_fonctions import ModeleListeFonctions
from vue_canvas import MPLCanvas


class VuePrincipal(QMainWindow):
    fonctionLineEdit : QLineEdit()
    borneInfLineEdit : QLineEdit()
    borneSupLineEdit : QLineEdit()
    matplotlibVLayout : QVBoxLayout()

    __model = ModeleInetgration()
    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', self)

        self.model = ModeleListeFonctions()
        canvas = MPLCanvas(self.model)

        self.matplotlibVLayout.insertWidget(0, canvas)

        self.fonctionLineEdit.editingFinished.connect(self.on_fonction_edited)




    def on_fonction_edited(self):
        #Attention la validation n'est pas implémentée dans ce corrigé, c'est voulu...
        fonct_str = self.fonctionLineEdit.text()
        if self.model.validate_fonction(fonct_str) :
            self.model.fonction = fonct_str
        else :
            QMessageBox.critical(self, "Erreur", "La fonction est invalide")
            self.fonctionLineEdit.clear()
            self.fonctionLineEdit.setStyleSheet("background-color: white;")