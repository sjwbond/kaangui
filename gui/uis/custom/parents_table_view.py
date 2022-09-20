from gui.uis.custom.combo_delegate import ComboDelegate
from gui.uis.custom.text_delegate import TextDelegate
from qt_core import *

class ParentsTableView(QTableView):
    def __init__(self):
        super().__init__()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        # self.column_1 = QTableWidgetItem()
        # self.column_1.setTextAlignment(Qt.AlignCenter)
        # self.column_1.setText("Parent Object")

        # self.column_2 = QTableWidgetItem()
        # self.column_2.setTextAlignment(Qt.AlignCenter)
        # self.column_2.setText("Parent Property")
        
        # self.setHorizontalHeaderItem(0, self.column_1)
        # self.setHorizontalHeaderItem(1, self.column_2)

        self.comboDelegate = ComboDelegate([])
        self.setItemDelegateForColumn(0, self.comboDelegate)
        
        self.textDelegate = TextDelegate()
        self.setItemDelegateForColumn(1, self.textDelegate)
    
    def setComboProps(self, props):
        self.comboDelegate.setItems(props)
