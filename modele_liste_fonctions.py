from PyQt6.QtCore import QObject, pyqtSignal
import sympy as sp


class ModeleListeFonctions(QObject):
    __x = sp.symbols("x")
    __fonction : None=None
    __borneInf : int = -1
    __borneSup : int = 2
    def __init__(self):
        super().__init__()

