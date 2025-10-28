import json

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QListView, QDockWidget
from PyQt6.uic import loadUi
from modele_liste_fonctions import ModeleListeFonctions


class VueFonction(QDockWidget):

    def __init__(self):
        super().__init__()


    def update_model(self):
        list_model = ModeleListeFonctions('fonctions.json')
        return list_model

    def on_ajouter_clicked(self, fonction):
        ModeleListeFonctions('fonctions.json').add_item(fonction)
        return self.update_model()

    def on_supprimer_clicked(self, index):
        ModeleListeFonctions('fonctions.json').remove_item(index)
        return self.update_model()