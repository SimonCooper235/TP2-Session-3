from PyQt6.QtCore import QObject, pyqtSignal
import sympy as sp


class ModeleListeFonctions(QObject):
    __x = sp.symbols("x")
    __fonction : None=None
    __borneInf : int = -1
    __borneSup : int = 2

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


    def validate_fonction(self, fonction_str):
        return True


    def validate_bornes(self, bornes_str):
        return True

