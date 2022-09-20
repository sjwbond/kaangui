from qt_core import *

class ParentsTableModel(QAbstractTableModel):
    itemChanged = Signal()

    def __init__(self, data):
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
