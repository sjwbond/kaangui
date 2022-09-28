from qt_core import *

style = '''
QLineEdit {
	background-color: #333;
	border: 0px solid transparent;
	padding-left: 1px;
    padding-right: 1px;
	selection-color: #FFF;
	selection-background-color: #00ABE8;
    color: #FFF;
}
QLineEdit:focus {
	border: 0px solid transparent;
    background-color: #4D5066;
}
'''

class TextDelegate(QItemDelegate):
    def __init__(self):
        super().__init__()

    def createEditor(self, parent, option, index: QModelIndex):
        self.edit = QLineEdit(parent)
        self.connect(self.edit, SIGNAL("currentIndexChanged(int)"), self, SLOT("currentIndexChanged()"))
        self.edit.setStyleSheet(style)
        return self.edit

    def setEditorData(self, edit, index):
        text = index.data(Qt.DisplayRole)
        edit.setText(text)

    def setModelData(self, edit, model, index):
        model.setData(index, edit.text(), Qt.DisplayRole)

    @Slot()
    def currentIndexChanged(self): 
        self.commitData.emit(self.sender())
