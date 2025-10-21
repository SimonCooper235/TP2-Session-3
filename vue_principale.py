from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QMessageBox
from PyQt6.uic import loadUi


from modele_liste_fonctions import ModeleListeFonctions
from vue_canvas import MPLCanvas


class VuePrincipal(QMainWindow):
    fonctionLineEdit: QLineEdit
    borneInfLineEdit: QLineEdit
    borneSupLineEdit: QLineEdit
    matplotlibVLayout: QVBoxLayout

    __model = ModeleListeFonctions

    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', self)

        self.model = ModeleListeFonctions()
        canvas = MPLCanvas(self.model)

        self.matplotlibVLayout.addWidget(canvas)

        self.fonctionLineEdit.editingFinished.connect(self.on_fonction_edited)
        self.borneInfLineEdit.textChanged.connect(self.on_borne_inf_edited)
        self.borneInfLineEdit.setText("-1")
        self.borneSupLineEdit.textChanged.connect(self.on_borne_sup_edited)
        self.borneSupLineEdit.setText("2")

    def on_fonction_edited(self):
        fonct_str = self.fonctionLineEdit.text()
        if self.model.validate_fonction(fonct_str) :
            self.model.fonction = fonct_str
        else :
            self.fonctionLineEdit.clear()
            self.fonctionLineEdit.setStyleSheet("background-color: red;")

    def on_borne_inf_edited(self):
        borne_int = int(self.borneInfLineEdit.text())
        if self.model.validate_bornes(borne_int):
            self.model.borneInf = borne_int
        else:
            self.borneInfLineEdit.setStyleSheet("background-color : red;")

    def on_borne_sup_edited(self):
        borne_int = int(self.borneSupLineEdit.text())
        if self.model.validate_bornes(borne_int):
            self.model.borneSup = borne_int
        else:
            self.borneSupLineEdit.setStyleSheet("background-color : red;")