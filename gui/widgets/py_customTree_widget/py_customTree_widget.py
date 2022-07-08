
from qt_core import *
import pandas as pd

class CustomTreeItem(QTreeWidgetItem):
    """
    Custom QTreeWidgetItem with Widgets
    """

    def __init__(self, parent, name, col=False, table=""):
        """
        parent (QTreeWidget) : Item's QTreeWidget parent.
        name   (str)         : Item's name. just an example.
        """

        ## Init super class ( QtGui.QTreeWidgetItem )
        super(CustomTreeItem, self).__init__(parent)

        ## Column 0 - Text:
        self.setText(0, name)

        if col and isinstance(table, pd.DataFrame):

            self.table = QTableWidget()

            self.table.setRowCount(len(table))
            self.table.setColumnCount(len(table.columns))
            self.table.setHorizontalHeaderLabels(table.columns)

            for row in range(len(table)):
                for col in range(len(table.columns)):
                    self.table.setItem(
                        row, col, QTableWidgetItem(table.iloc[row, col])
                    )

            self.treeWidget().setItemWidget(self, 1, self.table)

        ## Column 2 - Button:
        self.button = QPushButton()
        self.button.setText("button %s" % name)
        self.treeWidget().setItemWidget(self, 2, self.button)

        ## Signals
        # self.treeWidget().connect(
        #     self.button, QtCore.SIGNAL("clicked()"), self.buttonPressed
        # )

    @property
    def name(self):
        """
        Return name ( 1st column text )
        """
        return self.text(0)

    @property
    def value(self):
        """
        Return value ( 2nd column int)
        """
        return self.spinBox.value()

    def buttonPressed(self):
        """
        Triggered when Item's button pressed.
        an example of using the Item's own values.
        """
        print(f"This Item name:{self.name} value:{self.value}")
