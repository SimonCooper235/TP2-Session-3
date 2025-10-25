from PyQt6.QtWidgets import QListView, QLineEdit, QPushButton, QWidget
from PyQt6.uic import loadUi

from modele_integration import ModeleIntegration
from modele_liste_fonctions import Bibliotheque, ModeleListeFonctions


class VueFonction(QWidget):
    fonctionListView : QListView
    fonctionLineEdit : QLineEdit
    enregistrerPushButton : QPushButton
    ajouterPushButton : QPushButton
    supprimerPushButton : QPushButton

    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', self)

        self.list_model = ModeleListeFonctions(Bibliotheque.bibliotheque())

        self.fonctionListView.setModel(self.list_model)