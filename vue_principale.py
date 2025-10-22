from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QMessageBox, QSlider, QCheckBox, QPushButton, \
    QButtonGroup
from PyQt6.uic import loadUi

from modele_integration import ModeleIntegration
from modele_liste_fonctions import ModeleListeFonctions
from vue_canvas import MPLCanvas


class VuePrincipal(QMainWindow):
    fonctionLineEdit : QLineEdit
    borneInfLineEdit : QLineEdit
    borneSupLineEdit : QLineEdit
    sommeLineEdit : QLineEdit
    integraleLineEdit : QLineEdit
    matplotlibVLayout : QVBoxLayout
    nombreHorizontalSlider : QSlider
    gaucheCheckBox : QCheckBox
    droiteCheckBox : QCheckBox
    calculerPushButton : QPushButton
    exporterPushButton : QPushButton


    __model = ModeleIntegration

    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', self)


        self.model = ModeleIntegration()
        canvas = MPLCanvas(self.model)

        self.matplotlibVLayout.addWidget(canvas)

        self.fonctionLineEdit.editingFinished.connect(self.on_fonction_edited)
        self.borneInfLineEdit.textChanged.connect(self.on_borne_inf_edited)
        self.borneInfLineEdit.setText("-1")
        self.borneSupLineEdit.textChanged.connect(self.on_borne_sup_edited)
        self.borneSupLineEdit.setText("2")

        button_group = QButtonGroup(self)
        button_group.addButton(self.gaucheCheckBox)
        button_group.addButton(self.droiteCheckBox)
        button_group.setExclusive(True)

        self.calculerPushButton.clicked.connect(self.on_calculer_button_push)
        self.nombreHorizontalSlider.valueChanged.connect(self.on_slider_moved)




    def on_fonction_edited(self):
        fonct_str = self.fonctionLineEdit.text()
        if self.model.validate_fonction(fonct_str) :
            self.model.fonction = fonct_str
        else :
            QMessageBox.critical(self, "Erreur", "la fonction est invalide")
            self.fonctionLineEdit.clear()
            self.fonctionLineEdit.setStyleSheet("background-color: red;")

    def on_borne_inf_edited(self, borne):
        try:
            borne_int = int(borne)
            if self.model.validate_bornes(borne_int):
                self.model.borneInf = borne_int
            else:
                self.borneInfLineEdit.setStyleSheet("background-color : red;")
        except ValueError as e :
            pass

    def on_borne_sup_edited(self, borne):
        try:
            borne_int = int(borne)
            if self.model.validate_bornes(borne_int):
                self.model.borneSup = borne_int
            else:
                self.borneSupLineEdit.setStyleSheet("background-color : red;")
        except ValueError as e :
            pass

    def on_slider_moved(self, value):
        self.model.nombreHorizontalSlider = value

    def on_calculer_button_push(self):
        self.model.calculer_somme_riemann()
        somme_str = f"{self.model.sommeLineEdit}"
        self.sommeLineEdit.setText(somme_str)