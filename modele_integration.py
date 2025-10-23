import numpy as np
from PyQt6.QtCore import QObject, pyqtSignal
import sympy as sp

class ModeleIntegration(QObject):
    __x = sp.Symbol('x')
    __fonction : None = None
    __sommeLineEdit : float = 0
    __integraleLineEdit : float = 0
    __borneInf : int = 0
    __borneSup : int = 0
    __nombreHorizontalSlider : int = 100
    __gaucheCheckBox : bool = True
    __droiteCheckBox : bool = False

    modelChanged = pyqtSignal()

    def __init__(self):
        super().__init__()

    @property
    def fonction(self):
        try:
            f = sp.lambdify(self.__x, self.__fonction, 'numpy')
        except   Exception as e:
            print(e)
            f = None
        return f

    @fonction.setter
    def fonction(self, value):
        self.__fonction = sp.sympify(value)
        self.modelChanged.emit()

    @property
    def borneInf(self):
        return self.__borneInf

    @borneInf.setter
    def borneInf(self, borne):
        self.__borneInf = borne
        self.modelChanged.emit()

    @property
    def borneSup(self):
        return self.__borneSup

    @borneSup.setter
    def borneSup(self, borne):
        self.__borneSup = borne
        self.modelChanged.emit()

    @property
    def nombreHorizontalSlider(self):
        return self.__nombreHorizontalSlider

    @nombreHorizontalSlider.setter
    def nombreHorizontalSlider(self, nombreHorizontalSlider):
        self.__nombreHorizontalSlider = nombreHorizontalSlider
        self.modelChanged.emit()

    @property
    def gaucheCheckBox(self):
        return self.__gaucheCheckBox

    @gaucheCheckBox.setter
    def gaucheCheckBox(self, checkBox):
        self.__gaucheCheckBox = checkBox
        self.modelChanged.emit()

    @property
    def droiteCheckBox(self):
        return self.__droiteCheckBox

    @droiteCheckBox.setter
    def droiteCheckBox(self, checkBox):
        self.__droiteCheckBox = checkBox
        self.modelChanged.emit()

    @property
    def sommeLineEdit(self):
        return self.__sommeLineEdit

    @sommeLineEdit.setter
    def sommeLineEdit(self, somme):
        self.__sommeLineEdit = somme
        self.modelChanged.emit()

    @property
    def integraleLineEdit(self):
        return self.__integraleLineEdit

    @integraleLineEdit.setter
    def integraleLineEdit(self, integrale):
        self.__integraleLineEdit = integrale
        self.modelChanged.emit()

    def calculer_somme_riemann(self):
        x = np.linspace(self.__borneInf, self.__borneSup, self.__nombreHorizontalSlider + 1)
        dx = (self.__borneSup - self.__borneInf)/self.__nombreHorizontalSlider
        if self.__gaucheCheckBox:
            f = sp.lambdify(self.__x, self.__fonction, 'numpy')
            gauche_somme = np.sum(f(x[:-1]) * dx)
            self.__sommeLineEdit = gauche_somme
        elif self.__droiteCheckBox:
            f = sp.lambdify(self.__x, self.__fonction, 'numpy')
            droite_somme = np.sum(f(x[1:]) * dx)
            self.__sommeLineEdit = droite_somme
        else:
            pass

    def calculer_intégrale(self):
        self.__integraleLineEdit = sp.integrate(self.__fonction, (self.__x, self.__borneInf, self.__borneSup))

    def validate_fonction(self, fonction_str):
        return True

    def validate_bornes(self, bornes_str):
        return True
