import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex

class Bibliotheque:
    def bibliotheque(self):
        fonctions = Fonction.fonction
        with open("fonctions.json", "w", encoding="utf-8") as f:
            json_str = json.dump(fonctions.to_json, f)

        with open("fonctions.json", "r", encoding="utf-8") as f:
            json_str = json.load(f)
            fonction = Fonction.from_json(json_str)
        return


@dataclass_json
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
    def __init__(self, data):
        super().__init__(data)

        self.__fonction = data

    def data(self, index, role):
        if not index.isValid():
            return None
        livre = self.__fonction[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return livre.__str__()
        elif role == Qt.ItemDataRole.UserRole:
            return livre
        elif role == Qt.ItemDataRole.ToolTipRole:
            return livre.titre
        return None

    def rowCount(self, parent = QModelIndex):
        return len(self.__fonction)

    def add_fonction(self, fonction):
        fonc_fonction = Fonction(fonction)
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.__fonction.append(fonc_fonction)
        self.endInsertRows()
