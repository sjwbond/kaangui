from qt_core import *
from . fixtures import create_test_widget
import time

def test_add_parentship(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Make sure properties table contains 0 row
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 0

    # Press Add New Row button twice
    qtbot.mouseClick(widget.add_table_2_row_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.add_table_2_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 2 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 2

def test_delete_parentships(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 5 times and mark items
    for i in range(5):
        qtbot.mouseClick(widget.add_table_2_row_button, Qt.MouseButton.LeftButton)
        widget.controller.parents_model.setDataAt(i, 0, f"{i}", Qt.DisplayRole)

    # Make sure properties table contains 5 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 5

    # Select second and third rows
    selection_model = widget.controller.parents_table.selectionModel()
    selection_model.clear()
    selection = QItemSelection()
    selection.append(QItemSelectionRange(widget.controller.parents_model.index(1, 0), widget.controller.parents_model.index(2, 0)))
    selection_model.select(selection, QItemSelectionModel.Select | QItemSelectionModel.Rows)

    # Delete selected rows
    qtbot.mouseClick(widget.delete_table_2_row_button, Qt.MouseButton.LeftButton)

    # Make parents table has 3 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 3

    # Make sure remaining rows have data "0", "3", "4"
    row_data = [widget.controller.parents_model.dataAt(i, 0, Qt.DisplayRole) for i in range(widget.controller.parents_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "3", "4"]

def test_save_parentships(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 5 times and mark items
    for i in range(5):
        qtbot.mouseClick(widget.add_table_2_row_button, Qt.MouseButton.LeftButton)
        widget.controller.parents_model.setDataAt(i, 0, f"{i}", Qt.DisplayRole)

    # Make sure properties table contains 5 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 5

    # Select another object
    widget.controller.select_path(["Currency", "USD"])

    # Make parents table has 0 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 0
    
    # Select EUR object back
    widget.controller.select_path(["Currency", "EUR"])

    # Make parents table has 5 rows
    assert widget.controller.parents_table.model().rowCount(QModelIndex()) == 5

    # Make sure remaining rows have data "0", "1", "2", "3", "4"
    row_data = [widget.controller.parents_model.dataAt(i, 0, Qt.DisplayRole) for i in range(widget.controller.parents_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "1", "2", "3", "4"]

def test_assign_groups(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Open Assign Group to Object dialog
    widget.controller.assignGroupByModel()

    # Select USD and TRY
    widget.controller.dialogBox.listWidget.item(0).setCheckState(Qt.Checked)
    widget.controller.dialogBox.listWidget.item(1).setCheckState(Qt.Unchecked)
    widget.controller.dialogBox.listWidget.item(2).setCheckState(Qt.Checked)
    
    # Press Add Parent Object button
    qtbot.mouseClick(widget.controller.dialogBox.pushButton, Qt.MouseButton.LeftButton)

    # Select EUR and TRY
    widget.controller.dialogBox.listWidget.item(0).setCheckState(Qt.Unchecked)
    widget.controller.dialogBox.listWidget.item(1).setCheckState(Qt.Checked)
    widget.controller.dialogBox.listWidget.item(2).setCheckState(Qt.Checked)

    # Check upstream_reservoir
    widget.controller.dialogBox.listWidget_2.item(0).setCheckState(Qt.Checked)

    # Press Add Parent Object button
    qtbot.mouseClick(widget.controller.dialogBox.pushButton, Qt.MouseButton.LeftButton)

    # Make sure parents table has items ("EUR", ""), ("TRY", ""), ("USD", "upstream_reservoir"), ("TRY", "upstream_reservoir")
    items = [(widget.controller.dialogBox.tableWidget.item(i, 0).text(), widget.controller.dialogBox.tableWidget.item(i, 1).text())
             for i in range(widget.controller.dialogBox.tableWidget.rowCount())]
    assert items == [("EUR", ""), ("TRY", ""), ("USD", "upstream_reservoir"), ("TRY", "upstream_reservoir")]

    # Select second and third rows in table
    selection_model = widget.controller.dialogBox.tableWidget.selectionModel()
    selection_model.clear()
    selection = QItemSelection()
    selection.append(QItemSelectionRange(widget.controller.dialogBox.tableWidget.model().index(1, 0), widget.controller.dialogBox.tableWidget.model().index(2, 0)))
    selection_model.select(selection, QItemSelectionModel.Select | QItemSelectionModel.Rows)

    # Press Delete Rows
    qtbot.mouseClick(widget.controller.dialogBox.pushButton_2, Qt.MouseButton.LeftButton)

    # Make sure table has items ("EUR", ""), ("TRY", "upstream_reservoir")
    items = [(widget.controller.dialogBox.tableWidget.item(i, 0).text(), widget.controller.dialogBox.tableWidget.item(i, 1).text())
             for i in range(widget.controller.dialogBox.tableWidget.rowCount())]
    assert items == [("EUR", ""), ("TRY", "upstream_reservoir")]
    
    # Close dialog with OK
    widget.controller.dialogBox.accept()

    # Make sure parents table has items ("EUR", ""), ("TRY", "upstream_reservoir")
    items = [(widget.controller.parents_model.dataAt(i, 0, Qt.DisplayRole), widget.controller.parents_model.dataAt(i, 1, Qt.DisplayRole))
             for i in range(widget.controller.parents_model.rowCount(QModelIndex()))]
    assert items == [("EUR", ""), ("TRY", "upstream_reservoir")]

    # Switch to different object and back
    widget.controller.select_path(["Currency", "USD"])
    widget.controller.select_path(["Currency", "EUR"])

    # Make sure parents table has items ("EUR", ""), ("TRY", "upstream_reservoir")
    items = [(widget.controller.parents_model.dataAt(i, 0, Qt.DisplayRole), widget.controller.parents_model.dataAt(i, 1, Qt.DisplayRole))
             for i in range(widget.controller.parents_model.rowCount(QModelIndex()))]
    assert items == [("EUR", ""), ("TRY", "upstream_reservoir")]
