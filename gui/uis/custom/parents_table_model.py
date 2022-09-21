from typing import List
from qt_core import *

class ParentsTableModel(QAbstractTableModel):
    itemChanged = Signal()

    def __init__(self, data: List[List[str]]):
        super(ParentsTableModel, self).__init__()
        self._data = data

    def getData(self):
        return self._data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
    
    def setData(self, index, text, role):
        if role == Qt.DisplayRole:
            self._data[index.row()][index.column()] = text
            self.itemChanged.emit()
            return True
        return False

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if len(self._data) == 0:
            return 0
        return len(self._data[0])

    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    
    def appendNewRow(self):
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.append(["", ""])
        self.endInsertRows()
        self.itemChanged.emit()
    
    def removeRows(self, indexes: List[QModelIndex]):
        if len(indexes) == 0:
            return
        sr: List[QModelIndex] = sorted(indexes)
        sr.reverse()
        for index in sr:
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            self._data.pop(index.row())
            self.endRemoveRows()
        self.itemChanged.emit()
