from typing import List, Union
from qt_core import *
from gui.uis.custom.constants import plot_colors

class TimeSeriesTableModel(QAbstractTableModel):
    itemChanged = Signal()

    def __init__(self, data: List[List[str]]):
        super(TimeSeriesTableModel, self).__init__()
        self._data = data

    def getData(self):
        return self._data

    def data(self, index: Union[QModelIndex, QPersistentModelIndex], role: Qt.ItemDataRole):
        return self.dataAt(index.row(), index.column(), role)

    def dataAt(self, row: int, column: int, role: Qt.ItemDataRole):
        if column == 0:
            if role == Qt.ForegroundRole:
                r, g, b = plot_colors[row % len(plot_colors)]
                return QColor(r, g, b)
            if role == Qt.DisplayRole:
                return "▇▇"

        if role == Qt.DisplayRole:
            return self._data[row][column-1]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            if section == 0:
                return "Color"
            if section == 1:
                return "Result"
            if section == 2:
                return "Time Series Name"
            elif section == 3:
                return "Sample From"
            elif section == 4:
                return "Sample To"
            else:
                return section
        return super().headerData(section, orientation, role)
    
    def setData(self, index: Union[QModelIndex, QPersistentModelIndex], text: str, role: Qt.ItemDataRole):
        return self.setDataAt(index.row(), index.column(), text, role)
    
    def setDataAt(self, row: int, column: int, text: str, role: Qt.ItemDataRole):
        if role == Qt.DisplayRole:
            self._data[row][column-1] = text
            self.itemChanged.emit()
            return True
        return False

    def rowCount(self, index: Union[QModelIndex, QPersistentModelIndex]):
        return len(self._data)

    def columnCount(self, index: Union[QModelIndex, QPersistentModelIndex]):
        return 5

    def flags(self, index: Union[QModelIndex, QPersistentModelIndex]):
        if index.column() in [3, 4]:
            return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled
    
    def appendRow(self, row: list[str]):
        self.beginInsertRows(QModelIndex(), len(self._data), len(self._data))
        self._data.append(row)
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
