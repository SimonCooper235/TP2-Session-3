from dataclasses import dataclass

from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex

class Bibliotheque:
    @classmethod
    def bibli_fonctions(cls):
        fonction1=Fonction("x**2")
        fonction2=Fonction("tan(x)")
        fonction3=Fonction("cos(x)")
        fonction4=Fonction("sin(x)")
        fonctions = [fonction1, fonction2, fonction3, fonction4]
        return fonctions

@dataclass
class Fonction:
    __fonction : str

    @property
    def fonction(self):
        return self.__fonction

    @fonction.setter
    def fonction(self, fonction):
        self.__fonction = fonction

    def __str__(self):
        return f'{self.__fonction}'


class ModeleListeFonctions(QAbstractListModel):
    pass