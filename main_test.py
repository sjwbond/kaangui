from main import MainWindow
from qt_core import *

test_model = {
    "name": "Test Model",
    "Simulation": {
        "Competition": {},
        "Diagnostics": {},
        "Execution Plans": {},
        "Horizons": {},
        "LRMC Models": {},
        "MT Schedule": {},
        "PASA": {},
        "Performance": {},
        "Production": {},
        "Reports": {},
        "ST Schedule": {},
        "Settings": {},
        "Stochastics": {},
        "Transmission": {}
    },
    "SystemInputs": {
        "Currency": {
            "EUR": {
                "Object_Name": "EUR",
                "Object_Type": "Currency",
                "Parent Objects": [],
                "Properties": [
                    {
                        "Date_From": "2000-01-01",
                        "Date_To": "2100-01-01",
                        "Group_id": "",
                        "Parent Object": "",
                        "Priority": "",
                        "Property": "",
                        "Scenario": "",
                        "Target Object": "",
                        "Timeslice": "",
                        "Timeslice_Index": "",
                        "Value": "",
                        "Variable": "",
                        "Variable_Effect": ""
                    }
                ]
            },
            "USD": {
                "Object_Name": "USD",
                "Object_Type": "Currency",
                "Parent Objects": [],
                "Properties": []
            },
            "Subfolder": {
                "TRY": {
                    "Object_Name": "TRY",
                    "Object_Type": "Currency",
                    "Parent Objects": [],
                    "Properties": []
                }
            }
        },
        "DBDataSource": {},
        "DBTimeSeries": {},
        "DataSource": {},
        "Demand": {},
        "Emissions": {},
        "Fuel": {},
        "Generator": {},
        "Group": {},
        "Hydro_Generator": {},
        "Line": {},
        "Node": {},
        "Reservoir": {},
        "Storage": {},
        "Variable": {}
    }
}

def create_test_widget(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    # Load test model
    widget.load_model(test_model)
    widget.controller.tree.expandAll()

    return widget

def test_create_new_model(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.Yes)

    # Create new model
    widget.create_new_model()

    # Make sure model name is now New Model
    idx_model = widget.controller.tree.rootModel.index(0, 0)
    assert idx_model.data(Qt.DisplayRole) == "New Model"

    # Make sure some folders exist
    idx_currency = widget.controller.get_item_by_path(["Currency"])
    idx_fuel = widget.controller.get_item_by_path(["Fuel"])
    idx_node = widget.controller.get_item_by_path(["Node"])

    assert idx_currency.data(Qt.UserRole) == "folder"
    assert idx_fuel.data(Qt.UserRole) == "folder"
    assert idx_node.data(Qt.UserRole) == "folder"

    # Make sure EUR no longer exists
    idx_eur_gone = widget.controller.get_item_by_path(["Currency", "EUR"])
    assert idx_eur_gone is None

def test_rename_model(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("My Model", True))

    # Rename model
    widget.controller.select_model()
    widget.controller.renameModel()

    # Make sure model name has changed
    idx_model = widget.controller.tree.rootModel.index(0, 0)
    assert idx_model.data(Qt.DisplayRole) == "My Model"

def test_rename_folder(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("My Folder", True))

    # Rename folder
    widget.controller.select_path(["Currency", "Subfolder"])
    widget.controller.renameByModel()

    # Make sure folder name has changed
    idx_subfolder = widget.controller.get_item_by_path(["Currency", "My Folder"])
    assert idx_subfolder.data(Qt.DisplayRole) == "My Folder"

    idx_subfolder_gone = widget.controller.get_item_by_path(["Currency", "Subfolder"])
    assert idx_subfolder_gone is None

def test_rename_object(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("JPY", True))

    # Rename object
    widget.controller.select_path(["Currency", "Subfolder", "TRY"])
    widget.controller.renameByModel()

    # Make sure object name has changed
    idx_jpy = widget.controller.get_item_by_path(["Currency", "Subfolder", "JPY"])
    assert idx_jpy.data(Qt.DisplayRole) == "JPY"

    idx_try_gone = widget.controller.get_item_by_path(["Currency", "Subfolder", "TRY"])
    assert idx_try_gone is None

def test_rename_no_conflict(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QInputDialog, "getText", lambda *args, **args2: ("USD", True))

    global errors_shown
    errors_shown = 0
    def increment_errors(*args):
        global errors_shown
        errors_shown += 1
    monkeypatch.setattr(QMessageBox, "exec", increment_errors)

    # Rename object
    widget.controller.select_path(["Currency", "EUR"])
    widget.controller.renameByModel()

    # Make sure object name has not changed
    idx_jpy = widget.controller.get_item_by_path(["Currency", "EUR"])
    assert idx_jpy.data(Qt.DisplayRole) == "EUR"

    # Make sure error dialog was displayed once
    assert errors_shown == 1

def test_copy_paste(qtbot):
    widget = create_test_widget(qtbot)

    # Copy EUR object
    widget.controller.select_path(["Currency", "EUR"])
    widget.controller.copyByModel()

    # Paste under Currency
    widget.controller.select_path(["Currency"])
    widget.controller.pasteByModel()

    # Make sure Copy of EUR now exists
    idx_copy_of_eur = widget.controller.get_item_by_path(["Currency", "Copy of EUR"])
    assert idx_copy_of_eur.data(Qt.DisplayRole) == "Copy of EUR"
    assert idx_copy_of_eur.data(Qt.UserRole) == test_model["SystemInputs"]["Currency"]["EUR"]

def test_cut_paste(qtbot):
    widget = create_test_widget(qtbot)

    # Cut EUR object
    widget.controller.select_path(["Currency", "EUR"])
    widget.controller.cutByModel()

    # Make sure that EUR object is gone
    idx_eur_gone = widget.controller.get_item_by_path(["Currency", "EUR"])
    assert idx_eur_gone is None

    # Paste under Currency
    widget.controller.select_path(["Currency"])
    widget.controller.pasteByModel()

    # Make sure EUR now exists
    idx_eur_pasted = widget.controller.get_item_by_path(["Currency", "EUR"])
    assert idx_eur_pasted.data(Qt.DisplayRole) == "EUR"
    assert idx_eur_pasted.data(Qt.UserRole) == test_model["SystemInputs"]["Currency"]["EUR"]

    # Paste again under currency
    widget.controller.pasteByModel()

    # Make sure that Copy of EUR now exists
    idx_copy_of_eur = widget.controller.get_item_by_path(["Currency", "Copy of EUR"])
    assert idx_copy_of_eur.data(Qt.DisplayRole) == "Copy of EUR"
    assert idx_copy_of_eur.data(Qt.UserRole) == test_model["SystemInputs"]["Currency"]["EUR"]

def test_delete(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    monkeypatch.setattr(QMessageBox, "question", lambda *args: QMessageBox.Yes)

    # Delete EUR object
    widget.controller.select_path(["Currency", "EUR"])
    widget.controller.deleteByModel()

    # Make sure that EUR object is gone
    idx_eur_gone = widget.controller.get_item_by_path(["Currency", "EUR"])
    assert idx_eur_gone is None

    # Delete USD object
    widget.controller.select_path(["Currency", "USD"])
    widget.controller.deleteByModel()

    # Make sure that USD object is gone
    idx_eur_gone = widget.controller.get_item_by_path(["Currency", "USD"])
    assert idx_eur_gone is None

def test_cannot_paste_under_different_folder(qtbot, monkeypatch):
    widget = create_test_widget(qtbot)
    global errors_shown
    errors_shown = 0
    def increment_errors(*args):
        global errors_shown
        errors_shown += 1
    monkeypatch.setattr(QMessageBox, "exec", increment_errors)

    # Copy EUR object
    widget.controller.select_path(["Currency", "EUR"])
    widget.controller.copyByModel()

    # Paste under Demand
    widget.controller.select_path(["Demand"])
    widget.controller.pasteByModel()

    # Make sure error dialog was displayed once
    assert errors_shown == 1

    # Make sure EUR does not exist under Demand
    idx_copy_of_eur = widget.controller.get_item_by_path(["Demand", "EUR"])
    assert idx_copy_of_eur is None

# qtbot.mouseClick(widget.ui.left_column.title_label.text(), qt_api.QtCore.Qt.MouseButton.LeftButton)
