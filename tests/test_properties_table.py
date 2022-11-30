from qt_core import *
from . fixtures import create_test_widget

def test_add_new_row(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Make sure properties table contains 1 row
    assert widget.controller.properties_table.model().rowCount() == 1

    # Press Add New Row button
    qtbot.mouseClick(widget.add_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 2 rows
    assert widget.controller.properties_table.model().rowCount() == 2

def test_delete_selected_rows(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 3 times
    for i in range(3):
        qtbot.mouseClick(widget.add_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 4 rows
    assert widget.controller.properties_table.model().rowCount() == 4
    
    # Mark rows by index
    for i in range(widget.controller.properties_model.rowCount(QModelIndex())):
        item = widget.controller.properties_model.setDataAt(i, 0, f"{i}", Qt.DisplayRole)
    
    # Select and delete second row
    selection_model = QItemSelectionModel(widget.controller.properties_proxy_model)
    idx = widget.controller.properties_proxy_model.index(1, 0)
    selection_model.select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    selected = selection_model.selectedRows()
    widget.controller.properties_table.setSelectionModel(selection_model)
    qtbot.mouseClick(widget.delete_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 3 rows
    assert widget.controller.properties_table.model().rowCount() == 3

    # Make sure remaining items are marked with ids 0, 2, 3
    row_data = [widget.controller.properties_model.dataAt(i, 0, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "2", "3"]

def test_copy_paste_selected_rows(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 3 times
    for i in range(3):
        qtbot.mouseClick(widget.add_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 4 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 4
    
    # Mark rows by index
    for i in range(widget.controller.properties_model.rowCount(QModelIndex())):
        item = widget.controller.properties_model.setDataAt(i, 0, f"{i}", Qt.DisplayRole)
    
    # Select, copy, and paste second row twice
    widget.controller.properties_table.selectRow(1)
    qtbot.mouseClick(widget.copy_table_row_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.paste_table_row_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.paste_table_row_button, Qt.MouseButton.LeftButton)

    # Select, copy, and paste fourth row
    widget.controller.properties_table.selectRow(3)
    qtbot.mouseClick(widget.copy_table_row_button, Qt.MouseButton.LeftButton)
    qtbot.mouseClick(widget.paste_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 7 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 7

    # Make sure remaining items are marked with ids 0, 1, 2, 3, 1, 1, 3
    row_data = [widget.controller.properties_model.dataAt(i, 0, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "1", "2", "3", "1", "1", "3"]

def test_save_table(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 3 times
    for i in range(3):
        qtbot.mouseClick(widget.add_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 4 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 4
    
    # Mark rows by index
    for i in range(widget.controller.properties_model.rowCount(QModelIndex())):
        item = widget.controller.properties_model.setDataAt(i, 0, f"{i}", Qt.DisplayRole)

    # Change selected object and back
    widget.controller.select_path(["Currency", "USD"])
    widget.controller.select_path(["Currency", "EUR"])

    # Make sure properties table contains 3 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 4

    # Make sure remaining items are marked with ids 0, 1, 2, 3
    row_data = [widget.controller.properties_model.dataAt(i, 0, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "1", "2", "3"]
