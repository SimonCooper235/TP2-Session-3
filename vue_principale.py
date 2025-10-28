
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QMessageBox, QSlider, QCheckBox, QPushButton, \
    QButtonGroup, QDockWidget, QListView, QComboBox
from PyQt6.uic import loadUi

from modele_integration import ModeleIntegration
from modele_liste_fonctions import Signal
from vue_canvas import MPLCanvas
from vue_fonctions import VueFonction

class VuePrincipal(QMainWindow):
    fonctionCombobox : QComboBox
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

    actionFonctions : QAction

    fonctionDockWidget : QDockWidget
    ajouterPushButton: QPushButton
    fonctionListView: QListView
    fonctionLineEdit: QLineEdit
    enregistrerPushButton: QPushButton
    supprimerPushButton: QPushButton

    def __init__(self):
        super().__init__()
        loadUi('ui/fenêtre_principale.ui', self)

        self.model = ModeleIntegration()
        self.signal = Signal()
        self.signal.fonction_changer.connect(self.update_model)

        canvas = MPLCanvas(self.model)
        self.dockWidget = VueFonction()
        self.update_model()

        self.fonctionDockWidget.setHidden(True)
        self.matplotlibVLayout.addWidget(canvas)

        self.fonctionCombobox.currentTextChanged.connect(self.on_comboBox_changed)
        self.borneInfLineEdit.textChanged.connect(self.on_borne_inf_edited)
        self.borneInfLineEdit.setText("-1")
        self.borneSupLineEdit.textChanged.connect(self.on_borne_sup_edited)
        self.borneSupLineEdit.setText("2")

        button_group = QButtonGroup(self)
        button_group.addButton(self.gaucheCheckBox)
        button_group.addButton(self.droiteCheckBox)
        button_group.setExclusive(True)
        self.gaucheCheckBox.setChecked(True)
        self.gaucheCheckBox.checkStateChanged.connect(self.on_check_changed)

        self.calculerPushButton.clicked.connect(canvas.dessiner_integration)
        self.calculerPushButton.clicked.connect(self.on_calculer_button_push)
        self.nombreHorizontalSlider.valueChanged.connect(self.on_slider_moved)

        self.fonctionLineEdit.editingFinished.connect(self.on_fonction_edited)
        self.actionFonctions.triggered.connect(self.on_fonctions_triggered)
        self.ajouterPushButton.clicked.connect(self.on_ajouter_pushed)
        self.supprimerPushButton.clicked.connect(self.on_supprimer_pushed)



    def on_fonction_edited(self):
        fonct_str = self.fonctionLineEdit.text()
        if self.model.validate_fonction(fonct_str) :
            self.model.fonction = fonct_str
        else :
            QMessageBox.critical(self, "Erreur", "la fonction est invalide")
            self.fonctionLineEdit.clear()
            self.fonctionLineEdit.setStyleSheet("background-color: red;")

    def on_borne_inf_edited(self, borne):
        if self.model.validate_bornes(borne) and int(borne) < int(self.borneSupLineEdit.text()):
            self.model.borneInf = int(borne)
            self.borneInfLineEdit.setStyleSheet("background-color : white;")
        else:
            self.borneInfLineEdit.setStyleSheet("background-color : red;")

    def on_borne_sup_edited(self, borne):
        if self.model.validate_bornes(borne) and int(borne) > int(self.borneInfLineEdit.text()):
            self.model.borneSup = int(borne)
            self.borneInfLineEdit.setStyleSheet("background-color : white;")
        else:
            self.borneSupLineEdit.setStyleSheet("background-color : red;")

    def on_slider_moved(self, value):
        self.model.nombreHorizontalSlider = value

    def on_calculer_button_push(self):
        self.model.calculer_somme_riemann()
        self.model.calculer_intégrale()

        somme_str = f"{self.model.sommeLineEdit}"
        self.sommeLineEdit.setText(somme_str)

        integrale_float = float(self.model.integraleLineEdit)
        integrale_str = f"{integrale_float}"
        self.integraleLineEdit.setText(integrale_str)

    def on_check_changed(self):
        if self.gaucheCheckBox.isChecked():
            self.model.gaucheCheckBox = True
            self.model.droiteCheckBox = False
        else:
            self.model.gaucheCheckBox = False
            self.model.droiteCheckBox = True

    def on_fonctions_triggered(self):
        self.fonctionDockWidget.setHidden(False)
        self.update_model()

    def on_ajouter_pushed(self):
        model = self.dockWidget.on_ajouter_clicked(self.fonctionLineEdit.text())
        self.fonctionListView.setModel(model)

    def on_supprimer_pushed(self):
        model = self.dockWidget.on_supprimer_clicked(self.fonctionListView.currentIndex())
        self.fonctionListView.setModel(model)

    def update_model(self):
        model = self.dockWidget.update_model()
        self.fonctionCombobox.setModel(model)
        self.fonctionListView.setModel(model)

    def on_comboBox_changed(self):
        self.model.fonction = self.fonctionCombobox.currentText()