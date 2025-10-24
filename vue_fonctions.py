from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QListView, QLineEdit, QPushButton, QMessageBox, QWidget
from PyQt6.uic import loadUi
from modele_integration import ModeleIntegration


class VueFonction(QWidget):
    fonctionListView : QListView
    fonctionLineEdit : QLineEdit
    enregistrerPushButton : QPushButton
    ajouterPushButton : QPushButton
    supprimerPushButton : QPushButton

    __model = ModeleIntegration

    def __init__(self):
        super().__init__()
        loadUi("ui/fonctions.ui", self)
        self.model = ModeleIntegration()

        self.fonctionLineEdit.editingFinished.connect(self.on_fonction_edited)
        self.ajouterPushButton.clicked.connect(self.on_ajouter_clicked)

    def on_fonction_edited(self):
        fonct_str = self.fonctionLineEdit.text()
        if self.model.validate_fonction(fonct_str) :
            self.model.fonction = fonct_str
        else :
            QMessageBox.critical(self, "Erreur", "la fonction est invalide")
            self.fonctionLineEdit.clear()
            self.fonctionLineEdit.setStyleSheet("background-color: red;")

    def on_ajouter_clicked(self):
        self.fonctionListView.addAction(self.fonctionLineEdit.text())
