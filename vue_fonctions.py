from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QListView, QLineEdit, QPushButton, QDockWidget
from PyQt6.uic import loadUi

import modele_liste_fonctions
import vue_principale
from modele_liste_fonctions import Bibliotheque, ModeleListeFonctions


class VueFonction(QDockWidget):
    fonctionListView: QListView
    fonctionLineEdit : QLineEdit
    enregistrerPushButton : QPushButton
    ajouterPushButton : QPushButton
    supprimerPushButton : QPushButton

    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', vue_principale.VuePrincipal)

        self.ajouterPushButton.clicked.connect(lambda : print("Hello"))


    def on_ajouter_clicked(self):
        list_view = QListView(self)
        model = QStandardItemModel()
        items = modele_liste_fonctions.Bibliotheque.bibli_fonctions()
        for item_fonction in items :
            fonc_str = item_fonction.__str__()
            item = QStandardItem(fonc_str)
            model.appendRow(item)
        list_view.setModel(model)
        return list_view