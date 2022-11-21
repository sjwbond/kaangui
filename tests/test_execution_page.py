from main import MainWindow
from qt_core import *
from . fixtures import create_test_widget, test_simulation_1

def create_object(widget: MainWindow, row1: int, row2: int, name: str, type: str):
    item = get_node_item(widget, row1, row2)
    widget.execution_controller.create_new(item, name, type)

def get_node_index(widget: MainWindow, row1: int, row2: int) -> QStandardItem:
    parent_idx = widget.execution_controller.model.index(row1, 0)
    target_idx = widget.execution_controller.model.index(row2, 0, parent_idx)
    return target_idx

def get_node_item(widget: MainWindow, row1: int, row2: int) -> QStandardItem:
    target_idx = get_node_index(widget, row1, row2)
    target_item = widget.execution_controller.model.itemFromIndex(target_idx)
    return target_item

def get_object_index(widget: MainWindow, row1: int, row2: int, row3: int) -> QStandardItem:
    parent_idx = widget.execution_controller.model.index(row1, 0)
    parent2_idx = widget.execution_controller.model.index(row2, 0, parent_idx)
    target_idx = widget.execution_controller.model.index(row3, 0, parent2_idx)
    return target_idx

def get_object_item(widget: MainWindow, row1: int, row2: int, row3: int) -> QStandardItem:
    target_idx = get_object_index(widget, row1, row2, row3)
    target_item = widget.execution_controller.model.itemFromIndex(target_idx)
    return target_item

def test_create_new(qtbot):
    widget = create_test_widget(qtbot)

    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # Create new Settings object
    item = get_node_item(widget, 0, 1)
    widget.execution_controller.create_new(item, "Settings", "settings")

    # Check that New Settings now exists
    item = get_object_item(widget, 0, 1, 0)
    assert item.data(Qt.DisplayRole) == "New Settings"

def test_save_prompt_if_changed(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    global messages_shown
    messages_shown = 0
    def increment_messages(*args):
        global messages_shown
        messages_shown += 1
        return QMessageBox.Yes
    monkeypatch.setattr(QMessageBox, "question", increment_messages)

    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # Create new Horizon object
    item = get_node_item(widget, 2, 3)
    widget.execution_controller.create_new(item, "Horizon", "horizons")

    # Select newly created object
    idx = get_object_index(widget, 2, 3, 0)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()
    old_data = idx.data(Qt.UserRole + 1)

    # Select different node
    idx = get_node_index(widget, 1, 3)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()

    # Make sure no prompt was displayed
    assert messages_shown == 0

    # Select newly created object again
    idx = get_object_index(widget, 2, 3, 0)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()

    # Modify object
    widget.execution_controller.right_side_screen.onSpinBox.setValue(654)

    # Select different node
    idx = get_node_index(widget, 1, 3)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()

    # Make sure no prompt was displayed
    assert messages_shown == 1
    
    # Make sure data was saved
    idx = get_object_index(widget, 2, 3, 0)
    new_data = idx.data(Qt.UserRole + 1)
    assert old_data != new_data

def test_rename(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    
    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # Create new Horizon object
    item = get_node_item(widget, 2, 3)
    widget.execution_controller.create_new(item, "Horizon", "horizons")

    # Rename object
    item = get_object_item(widget, 2, 3, 0)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("My Horizon", True))
    widget.execution_controller.rename(item)

    # Make sure object name has changed
    assert item.data(Qt.DisplayRole) == "My Horizon"

def test_delete(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    
    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # Create new Horizon object
    item = get_node_item(widget, 2, 3)
    widget.execution_controller.create_new(item, "Horizon", "horizons")

    # Delete object
    idx = get_object_index(widget, 2, 3, 0)
    monkeypatch.setattr(QMessageBox, "question", lambda *args, **args2: QMessageBox.Yes)
    widget.execution_controller.delete(idx)

    # Make sure object no longer exists
    idx = get_object_index(widget, 2, 3, 0)
    assert idx.data(Qt.DisplayRole) is None

def test_save_prompt_if_changed(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    
    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # 1. Create new Horizon object
    item = get_node_item(widget, 2, 3)
    widget.execution_controller.create_new(item, "Horizon", "horizons")

    # Select newly created object
    idx = get_object_index(widget, 2, 3, 0)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()

    # Store object state
    old_data = idx.data(Qt.UserRole + 1)

    # 2. Modify object
    widget.execution_controller.right_side_screen.onSpinBox.setValue(654)

    # Select different node and save
    monkeypatch.setattr(QMessageBox, "question", lambda *args, **args2: QMessageBox.Yes)
    idx = get_node_index(widget, 1, 3)
    widget.execution_tree.selectionModel().clear()
    widget.execution_tree.selectionModel().select(idx, QItemSelectionModel.Select | QItemSelectionModel.Rows)
    widget.execution_controller.selection_changed()

    # Make sure object has changed
    new_data = idx.data(Qt.UserRole + 1)
    assert old_data != new_data

    # 3. Rename object
    item = get_object_item(widget, 2, 3, 0)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("My Horizon", True))
    widget.execution_controller.rename(item)

    # Make sure object name has changed
    assert item.data(Qt.DisplayRole) == "My Horizon"

    # Undo 3 (Rename object)
    widget.execution_controller.undo()
    assert item.data(Qt.DisplayRole) == "New Horizon"
    
    # Redo 3 (Rename object)
    widget.execution_controller.redo()
    assert item.data(Qt.DisplayRole) == "My Horizon"

    # Undo 3 again (Rename object)
    widget.execution_controller.undo()
    assert item.data(Qt.DisplayRole) == "New Horizon"

    # Undo 2 (Modify object)
    widget.execution_controller.undo()
    idx = get_object_index(widget, 2, 3, 0)
    undone_state = idx.data(Qt.UserRole + 1)
    assert undone_state == old_data

    # Undo 1 (Create new Horizon object)
    widget.execution_controller.undo()
    idx = get_object_index(widget, 2, 3, 0)
    assert idx.data(Qt.UserRole + 1) is None

    # Redo 1 (Create new Horizon object)
    widget.execution_controller.redo()
    idx = get_object_index(widget, 2, 3, 0)
    assert idx.data(Qt.UserRole + 1) == old_data

def test_set_get_simulation(qtbot):
    widget = create_test_widget(qtbot)
    
    # Switch to execution page
    qtbot.mouseClick(widget.ui.left_menu.top_layout.itemAt(3).widget(), Qt.MouseButton.LeftButton)

    # Load a simulation
    widget.execution_controller.set_simulation(test_simulation_1)

    # Make sure objects exist
    idx = get_object_index(widget, 0, 0, 0)
    assert idx.data(Qt.DisplayRole) == "New Execution Plans"
    idx = get_object_index(widget, 1, 1, 0)
    assert idx.data(Qt.DisplayRole) == "New Diagnostic"
    idx = get_object_index(widget, 2, 3, 0)
    assert idx.data(Qt.DisplayRole) == "New Horizon"

    # Get simulation
    simulation = widget.execution_controller.get_simulation()

    # Make sure simulation is equal to loaded simulation
    assert simulation == test_simulation_1