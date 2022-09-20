from qt_core import *

from gui.widgets.py_table_widget import PyTableWidget


class PropertiesTableWidget(PyTableWidget):
  def __init__(self, theme):
    super().__init__(
        radius = 8,
        color = theme["text_foreground"],
        selection_color = theme["context_color"],
        bg_color = theme["bg_two"],
        header_horizontal_color = theme["dark_two"],
        header_vertical_color = theme["bg_three"],
        bottom_line_color = theme["bg_three"],
        grid_line_color = theme["bg_one"],
        scroll_bar_bg_color = theme["bg_one"],
        scroll_bar_btn_color = theme["dark_four"],
        context_color = theme["context_color"]
    )

    self.setColumnCount(13)
    self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.setSelectionMode(QAbstractItemView.ExtendedSelection)
    self.setSelectionBehavior(QAbstractItemView.SelectRows)

    # Columns / Header
    self.column_1 = QTableWidgetItem()
    self.column_1.setTextAlignment(Qt.AlignCenter)
    self.column_1.setText("Parent Object")

    self.column_2 = QTableWidgetItem()
    self.column_2.setTextAlignment(Qt.AlignCenter)
    self.column_2.setText("Target Object")

    self.column_3 = QTableWidgetItem()
    self.column_3.setTextAlignment(Qt.AlignCenter)
    self.column_3.setText("Property")

    self.column_4 = QTableWidgetItem()
    self.column_4.setTextAlignment(Qt.AlignCenter)
    self.column_4.setText("Date_From")

    self.column_5 = QTableWidgetItem()
    self.column_5.setTextAlignment(Qt.AlignCenter)
    self.column_5.setText("Date_To")

    self.column_6 = QTableWidgetItem()
    self.column_6.setTextAlignment(Qt.AlignCenter)
    self.column_6.setText("Value")

    self.column_7 = QTableWidgetItem()
    self.column_7.setTextAlignment(Qt.AlignCenter)
    self.column_7.setText("Variable")

    self.column_8 = QTableWidgetItem()
    self.column_8.setTextAlignment(Qt.AlignCenter)
    self.column_8.setText("Variable_Effect")

    self.column_9 = QTableWidgetItem()
    self.column_9.setTextAlignment(Qt.AlignCenter)
    self.column_9.setText("Timeslice")

    self.column_10 = QTableWidgetItem()
    self.column_10.setTextAlignment(Qt.AlignCenter)
    self.column_10.setText("Timeslice_Index")

    self.column_11 = QTableWidgetItem()
    self.column_11.setTextAlignment(Qt.AlignCenter)
    self.column_11.setText("Group_id")

    self.column_12 = QTableWidgetItem()
    self.column_12.setTextAlignment(Qt.AlignCenter)
    self.column_12.setText("Priority")

    self.column_13 = QTableWidgetItem()
    self.column_13.setTextAlignment(Qt.AlignCenter)
    self.column_13.setText("Scenario")

    # Set columns
    self.setHorizontalHeaderItem(0, self.column_1)
    self.setHorizontalHeaderItem(1, self.column_2)
    self.setHorizontalHeaderItem(2, self.column_3)
    self.setHorizontalHeaderItem(3, self.column_4)
    self.setHorizontalHeaderItem(4, self.column_5)
    self.setHorizontalHeaderItem(5, self.column_6)
    self.setHorizontalHeaderItem(6, self.column_7)
    self.setHorizontalHeaderItem(7, self.column_8)
    self.setHorizontalHeaderItem(8, self.column_9)
    self.setHorizontalHeaderItem(9, self.column_10)
    self.setHorizontalHeaderItem(10, self.column_11)
    self.setHorizontalHeaderItem(11, self.column_12)
    self.setHorizontalHeaderItem(12, self.column_13)