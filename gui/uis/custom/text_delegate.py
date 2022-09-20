from qt_core import *

class TextDelegate(QItemDelegate):
    def __init__(self):
        super().__init__()

    def createEditor(self, parent, option, proxyModelIndex):
        edit = QLineEdit(parent)
        a = proxyModelIndex.model()
        b = a.data(proxyModelIndex, Qt.DisplayRole)
        edit.setText(b)
        self.connect(edit, SIGNAL("currentIndexChanged(int)"), self, SLOT("currentIndexChanged()"))
        return edit

    def setModelData(self, edit, model, index):
        model.setData(index, edit.text(), Qt.DisplayRole)

    @Slot()
    def currentIndexChanged(self): 
        self.commitData.emit(self.sender())
