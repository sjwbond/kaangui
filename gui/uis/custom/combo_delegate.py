from qt_core import *

from gui.widgets.comboBoxSearchable.comboBoxSearchable import ExtendedComboBox

class ComboDelegate(QItemDelegate):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.selectedIndex = 0
    
    def setItems(self, items):
        self.items = items

    def createEditor(self, parent, option, proxyModelIndex):
        combo = ExtendedComboBox(parent)
        combo.addItems(self.items)
        combo.setEditable(True)
        self.connect(combo, SIGNAL("currentIndexChanged(int)"), self, SLOT("currentIndexChanged()"))
        return combo

    def setModelData(self, combo, model, index):
        comboIndex = combo.currentIndex()
        text = self.items[comboIndex]        
        model.setData(index, text, Qt.DisplayRole)

    @Slot()
    def currentIndexChanged(self): 
        self.commitData.emit(self.sender())
