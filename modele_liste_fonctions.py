import json
from dataclasses import dataclass
from dataclasses_json import dataclass_json

from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex

@dataclass_json
@dataclass
class Fonction:
    __fonction : str

    def __str__(self):
        return self.__fonction



class ModeleListeFonctions(QAbstractListModel):
    def __init__(self, json = None, parent=None):
        super().__init__(parent)

        self.__data = []
        self.__json = json
        if json:
            self.load_json(json)

    @property
    def fonction(self):
        return self.__data

    def data(self, index, role = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or not (0 <= index.row() < len(self.__data)):
            return None
        fonction = self.__data[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return fonction.__str__()
        return None

    def set_data(self, index, value, role = Qt.ItemDataRole.DisplayRole):
        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            self.__data[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole])
            self.save_json()
            return True
        return False

    def rowCount(self, parent = QModelIndex):
        return len(self.__data)

    def load_json(self, json_file):
        try :
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.__data = data
        except Exception as e:
            print(e)
            return

        self.layoutChanged.emit()

    def save_json(self):
        with open(self.__json, 'w', encoding="utf-8") as f:
            json.dump(self.__data, f)

    def add_item(self, item):
        self.beginInsertRows(QModelIndex(), len(self.__data), len(self.__data))
        self.__data.append(item)
        self.endInsertRows()
        self.save_json()

    def remove_item(self, index):
        row = index.row()
        if 0 <= row < len(self.__data):
            self.beginRemoveRows(QModelIndex(), row, row)
            del self.__data[row]
            self.endRemoveRows()
            self.save_json()
