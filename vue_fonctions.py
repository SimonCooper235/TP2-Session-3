import json

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QListView, QDockWidget

import modele_liste_fonctions
import vue_principale
from modele_liste_fonctions import Fonction, ModeleListeFonctions, Bibliotheque


class VueFonction(QDockWidget):


    def __init__(self):
        super().__init__()


    def on_fonction_clicked(self):
        list_model = ModeleListeFonctions(Bibliotheque.bibliotheque)
        return list_model

    def on_ajouter_clicked(self, fonction):
        Fonction.fonction = fonction
        ModeleListeFonctions(Bibliotheque.bibliotheque).add_fonction(fonction)
        return self.on_fonction_clicked()
