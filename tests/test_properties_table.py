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
        item = widget.controller.properties_model.setDataAt(i, 1, f"{i}", Qt.DisplayRole)
    
    # Select and delete second row
    selection_model = QItemSelectionModel(widget.controller.properties_proxy_model)
    idx = widget.controller.properties_proxy_model.index(1, 1)
    selection_model.select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.controller.properties_table.setSelectionModel(selection_model)
    qtbot.mouseClick(widget.delete_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 3 rows
    assert widget.controller.properties_table.model().rowCount() == 3

    # Make sure remaining items are marked with ids 0, 2, 3
    row_data = [widget.controller.properties_model.dataAt(i, 1, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
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
        widget.controller.properties_model.setDataAt(i, 1, f"{i}", Qt.DisplayRole)
    
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
    row_data = [widget.controller.properties_model.dataAt(i, 1, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
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
        widget.controller.properties_model.setDataAt(i, 1, f"{i}", Qt.DisplayRole)

    # Change selected object and back
    widget.controller.select_path(["Currency", "USD"])
    widget.controller.select_path(["Currency", "EUR"])

    # Make sure properties table still contains 4 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 4

    # Make sure remaining items are marked with ids 0, 1, 2, 3
    row_data = [widget.controller.properties_model.dataAt(i, 1, Qt.DisplayRole) for i in range(widget.controller.properties_model.rowCount(QModelIndex()))]
    assert row_data == ["0", "1", "2", "3"]

def test_copy_paste_selected_cells(qtbot):
    widget = create_test_widget(qtbot)

    # Select EUR object
    widget.controller.select_path(["Currency", "EUR"])

    # Press Add New Row button 3 times
    for i in range(3):
        qtbot.mouseClick(widget.add_table_row_button, Qt.MouseButton.LeftButton)

    # Make sure properties table contains 4 rows
    assert widget.controller.properties_model.rowCount(QModelIndex()) == 4
    
    # Mark cells by row and column
    for i in range(widget.controller.properties_model.rowCount(QModelIndex())):
        widget.controller.properties_model.setDataAt(i, 1, f"{i},1", Qt.DisplayRole)
        widget.controller.properties_model.setDataAt(i, 2, f"{i},2", Qt.DisplayRole)
        widget.controller.properties_model.setDataAt(i, 3, f"{i},3", Qt.DisplayRole)
        widget.controller.properties_model.setDataAt(i, 4, f"{i},4", Qt.DisplayRole)
    
    # Select cells (0,1) through (1,2) and press Ctrl+C
    widget.controller.properties_table.selectionModel().clear()
    for i in range(0, 2):
        for j in range(1, 3):
            idx = widget.controller.properties_proxy_model.index(i, j, QModelIndex())
            widget.controller.properties_table.selectionModel().select(idx, QItemSelectionModel.Select)
    widget.controller.copyPropertiesShortcut()
    # qtbot.keyPress(widget.controller.properties_table, "C", Qt.ControlModifier)

    # Select cells (2,3) through (3,4) and press Ctrl+V
    widget.controller.properties_table.selectionModel().clear()
    for i in range(2, 4):
        for j in range(3, 5):
            idx = widget.controller.properties_proxy_model.index(i, j, QModelIndex())
            widget.controller.properties_table.selectionModel().select(idx, QItemSelectionModel.Select)
    widget.controller.pastePropertiesShortcut()
    # qtbot.keyPress(widget.controller.properties_table, "V", Qt.ControlModifier)

    # Make sure items were copied correctly
    assert widget.controller.properties_model.dataAt(0, 1, Qt.DisplayRole) == f"0,1"
    assert widget.controller.properties_model.dataAt(0, 2, Qt.DisplayRole) == f"0,2"
    assert widget.controller.properties_model.dataAt(0, 3, Qt.DisplayRole) == f"0,3"
    assert widget.controller.properties_model.dataAt(0, 4, Qt.DisplayRole) == f"0,4"

    assert widget.controller.properties_model.dataAt(1, 1, Qt.DisplayRole) == f"1,1"
    assert widget.controller.properties_model.dataAt(1, 2, Qt.DisplayRole) == f"1,2"
    assert widget.controller.properties_model.dataAt(1, 3, Qt.DisplayRole) == f"1,3"
    assert widget.controller.properties_model.dataAt(1, 4, Qt.DisplayRole) == f"1,4"

    assert widget.controller.properties_model.dataAt(2, 1, Qt.DisplayRole) == f"2,1"
    assert widget.controller.properties_model.dataAt(2, 2, Qt.DisplayRole) == f"2,2"
    assert widget.controller.properties_model.dataAt(2, 3, Qt.DisplayRole) == f"0,1"
    assert widget.controller.properties_model.dataAt(2, 4, Qt.DisplayRole) == f"0,2"

    assert widget.controller.properties_model.dataAt(3, 1, Qt.DisplayRole) == f"3,1"
    assert widget.controller.properties_model.dataAt(3, 2, Qt.DisplayRole) == f"3,2"
    assert widget.controller.properties_model.dataAt(3, 3, Qt.DisplayRole) == f"1,1"
    assert widget.controller.properties_model.dataAt(3, 4, Qt.DisplayRole) == f"1,2"
