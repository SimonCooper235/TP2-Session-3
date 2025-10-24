from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.uic import loadUi
import sympy as sp


class ModeleListeFonctions(QObject):
    __x = sp.Symbol('x')
    __fonction : None = None

    def __init__(self):
        super().__init__()


