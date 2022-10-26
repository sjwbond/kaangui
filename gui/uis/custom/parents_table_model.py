from typing import List, Union
from qt_core import *

class ParentsTableModel(QAbstractTableModel):
    itemChanged = Signal()

    def __init__(self, data: List[List[str]]):
        super(ParentsTableModel, self).__init__()
        self._data = data

    def getData(self):
        return self._data

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Parent Object"
            elif section == 1:
                return "Parent Property"
            else:
                return section
        return super().headerData(section, orientation, role)
    
    def setData(self, index: Union[QModelIndex, QPersistentModelIndex], text: str, role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            self._data[index.row()][index.column()] = text
            self.itemChanged.emit()
            return True
        return False

    def rowCount(self, index: Union[QModelIndex, QPersistentModelIndex]):
        return len(self._data)

    def columnCount(self, index: Union[QModelIndex, QPersistentModelIndex]):
        return 2

    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    
    def appendNewRow(self):
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.append(["", ""])
        self.endInsertRows()
        self.itemChanged.emit()
    
    def removeRows(self, indexes: List[Union[QModelIndex, QPersistentModelIndex]]):
        if len(indexes) == 0:
            return
        sr: List[QModelIndex] = sorted(indexes)
        sr.reverse()
        for index in sr:
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            self._data.pop(index.row())
            self.endRemoveRows()
        self.itemChanged.emit()
