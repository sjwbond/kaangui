from functools import partial
from gui.uis.windows.screens.diagnosticscreen import Ui_DiagnosticsScreen, diagnostics_default_input
from gui.uis.windows.screens.horizonscreen import Ui_HorizonScreen, horizons_default_input
from gui.uis.windows.screens.ltplanscreen import Ui_LTPlanScreen, ltplan_default_input
from gui.uis.windows.screens.mtschedulescreen import Ui_MTScheaduleScreen, mtschedule_default_input
from gui.uis.windows.screens.pasascreen import Ui_PASAScreen, pasa_default_input
from gui.uis.windows.screens.productionscreen import Ui_ProductionScreen, production_default_input
from gui.uis.windows.screens.stochasticscreen import Ui_StochasticScreen, stochastic_default_input
from gui.uis.windows.screens.stschedulescreen import Ui_STScheduleScreen, stschedule_default_input
from qt_core import *


tree_structure = {
    "Execute": {
        "Models": ("Model", "models"),
        "Projects": ("Project", "projects")
    },
    "Settings": {
        "Competition": ("Competition", "competitions"),
        "Diagnostics": ("Diagnostic", "diagnostics"),
        "Performance": ("Performance", "performance"),
        "Production": ("Production", "production"),
        "Stochastics": ("Stochastic", "stochastics"),
        "Transmission": ("Transmission", "transmission")
    },
    "Simulation": {
        "ST Schedule": ("Short Term Schedule", "stschedule"),
        "MT Schedule": ("Medium Term Schedule", "mtschedule"),
        "LT Plan": ("Long Term Plan", "ltplan"),
        "Horizons": ("Horizaon", "horizons"),
        "PASA": ("PASA", "pasa"),
        "Reports": ("Report", "reports")
    }
}


style = '''
QPushButton {
	border: none;
    padding-left: 10px;
    padding-right: 10px;
    color: #f8f8f2;
	border-radius: 8px;	
	background-color: #282a36;
    min-height: 30px;
}
QPushButton:hover {
	background-color: #333645;
}
QPushButton:pressed {
	background-color: #3C4052;
}

QGroupBox {
    border: 1px solid #4D5066;
    border-radius: 8px;
    margin-top: 8px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 7px;
    padding: 0px 5px 0px 5px;
}

QSpinBox,
QDoubleSpinBox {
	background-color: #282a36;
	border-radius: 8px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: #f5f6f9;
	selection-background-color: #555555;
    color: #f8f8f2;
    min-height: 25px;
}
QSpinBox:focus,
QDoubleSpinBox:focus {
	border: 2px solid #ffffff;
    background-color: #333645;
}

QComboBox {
	background-color: #282a36;
	border-radius: 8px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: #f5f6f9;
	selection-background-color: #555555;
    color: #f8f8f2;
    min-height: 25px;
}
QComboBox:focus {
	border: 2px solid #ffffff;
    background-color: #333645;
}

QDateEdit {
	background-color: #282a36;
	border-radius: 8px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: #f5f6f9;
	selection-background-color: #555555;
    color: #f8f8f2;
    min-height: 25px;
}
QDateEdit:focus {
	border: 2px solid #ffffff;
    background-color: #333645;
}
'''


class ExecutionController:
    def __init__(self, tree: QTreeView, container: QScrollArea) -> None:
        self.tree = tree
        self.container = container
        self.model = QStandardItemModel()
        self.simulation = {}
        self.right_side_screen = None
        self.last_index = None
        
        self.tree.setHeaderHidden(True)
        self.tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tree.setDragEnabled(False)
        self.tree.setAcceptDrops(False)
        self.tree.setDropIndicatorShown(False)
        self.tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)

        self.tree.clicked.connect(self.selection_changed)
        self.tree.customContextMenuRequested.connect(self.open_menu)

        self.set_simulation({})

    def set_simulation(self, simulation: dict):
        self.simulation = simulation
        self.model = QStandardItemModel()

        for (key_a, value_a) in tree_structure.items():
            item = QStandardItem(key_a)
            item.setData(("category", key_a, key_a), Qt.UserRole)
            self.model.invisibleRootItem().appendRow(item)
            
            for (key_b, value_b) in value_a.items():
                (name, type) = value_b
                subitem = QStandardItem(key_b)
                subitem.setData(("node", name, type), Qt.UserRole)
                item.appendRow(subitem)

                if key_a in simulation:
                    if key_b in simulation[key_a]:
                        for (key_c, value_c) in simulation[key_a][key_b].items():
                            subsubitem = QStandardItem(key_c)
                            subsubitem.setData(("leaf", key_c, type), Qt.UserRole)
                            subsubitem.setData(value_c, Qt.UserRole + 1)
                            subitem.appendRow(subsubitem)
        
        self.tree.setModel(self.model)
        self.tree.expandAll()
    
    def get_simulation(self) -> dict:
        simulation = {}

        for i in range(self.model.rowCount()):
            ix_a = self.model.index(i, 0, self.model.invisibleRootItem().index())
            simulation[ix_a.data(Qt.DisplayRole)] = {}

            for i in range(self.model.rowCount(ix_a)):
                ix_b = self.model.index(i, 0, ix_a)
                simulation[ix_a.data(Qt.DisplayRole)][ix_b.data(Qt.DisplayRole)] = {}

                for i in range(self.model.rowCount(ix_b)):
                    ix_c = self.model.index(i, 0, ix_b)
                    simulation[ix_a.data(Qt.DisplayRole)][ix_b.data(Qt.DisplayRole)][ix_c.data(Qt.DisplayRole)] = ix_c.data(Qt.UserRole + 1)

        return simulation

    def open_menu(self, position):
        if len(self.tree.selectedIndexes()) > 0:
            index = self.tree.selectedIndexes()[0]
            item = self.model.itemFromIndex(index)
            user_data = index.data(Qt.UserRole)

            if user_data is not None:
                (level, name, type) = user_data
                menu = QMenu()

                if level == "node":
                    qmenu_create_new = QAction(f"Create New {name}")
                    qmenu_create_new.triggered.connect(partial(self.create_new, item, name, type))
                    menu.addAction(qmenu_create_new)
                elif level == "leaf":
                    qmenu_rename = QAction(f"Rename")
                    qmenu_rename.triggered.connect(partial(self.rename, item))
                    menu.addAction(qmenu_rename)

                    qmenu_delete = QAction(f"Delete")
                    qmenu_delete.triggered.connect(partial(self.delete, index))
                    menu.addAction(qmenu_delete)

                menu.exec_(QApplication.focusWidget().viewport().mapToGlobal(position))

    def create_new(self, item: QStandardItem, name, type):
        subitems = [self.model.index(i, 0, item.index()).data(Qt.DisplayRole) for i in range(item.rowCount())]
        new_name = f"New {name}"
        counter = 1
        while new_name in subitems:
            counter += 1
            new_name = f"New {name} ({counter})"

        subitem = QStandardItem(new_name)
        subitem.setData(("leaf", name, type), Qt.UserRole)
        if type == "diagnostics":
            subitem.setData(diagnostics_default_input, Qt.UserRole + 1)
        elif type == "horizons":
            subitem.setData(horizons_default_input, Qt.UserRole + 1)
        elif type == "ltplan":
            subitem.setData(ltplan_default_input, Qt.UserRole + 1)
        elif type == "mtschedule":
            subitem.setData(mtschedule_default_input, Qt.UserRole + 1)
        elif type == "pasa":
            subitem.setData(pasa_default_input, Qt.UserRole + 1)
        elif type == "production":
            subitem.setData(production_default_input, Qt.UserRole + 1)
        elif type == "stochastics":
            subitem.setData(stochastic_default_input, Qt.UserRole + 1)
        elif type == "stschedule":
            subitem.setData(stschedule_default_input, Qt.UserRole + 1)
        item.appendRow(subitem)

    def rename(self, item: QStandardItem):
        new_name, okPressed = QInputDialog.getText(None, "Rename", "New name:", text=item.data(Qt.DisplayRole))
        if not okPressed or new_name == '':
            return

        subitems = [self.model.index(i, 0, item.parent().index()).data(Qt.DisplayRole) for i in range(item.parent().rowCount())]
        while new_name in subitems:
            new_name, okPressed = QInputDialog.getText(None, "Rename", "An object with the same name exists. Please choose a different name.\nNew name:", text=item.data(Qt.DisplayRole))
            if not okPressed or new_name == '':
                return

        item.setData(new_name, Qt.DisplayRole)

    def delete(self, index: QModelIndex):
        ret = QMessageBox.question(None, "Delete", "Are you sure you wish to delete this object?", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.model.removeRow(index.row(), index.parent())

    def selection_changed(self):
        if len(self.tree.selectedIndexes()) == 0:
            return

        index = self.tree.selectedIndexes()[0]
        item = self.model.itemFromIndex(index)
        user_data = index.data(Qt.UserRole)

        if user_data is None:
            return

        (level, name, type) = user_data

        if self.last_index is not None:
            self.check_save_data(self.model.itemFromIndex(self.last_index))

        self.last_index = index

        self.clear_right_widget()
        
        if level == "leaf":
            if type == "diagnostics":
                self.set_right_data_screen(Ui_DiagnosticsScreen(), item)
            elif type == "production":
                self.set_right_data_screen(Ui_ProductionScreen(), item)
            elif type == "stochastics":
                self.set_right_data_screen(Ui_StochasticScreen(), item)
            elif type == "stschedule":
                self.set_right_data_screen(Ui_STScheduleScreen(), item)
            elif type == "mtschedule":
                self.set_right_data_screen(Ui_MTScheaduleScreen(), item)
            elif type == "ltplan":
                self.set_right_data_screen(Ui_LTPlanScreen(), item)
            elif type == "horizons":
                self.set_right_data_screen(Ui_HorizonScreen(), item)
            elif type == "pasa":
                self.set_right_data_screen(Ui_PASAScreen(), item)
    
    def set_right_data_screen(self, screen: QObject, item: QStandardItem):
        self.right_side_frame = QFrame()
        self.right_side_screen = screen
        self.right_side_screen.setupUi(self.right_side_frame)
        self.right_side_screen.setInput(item.data(Qt.UserRole + 1))
        self.right_side_frame.setStyleSheet(style)
        self.container.setWidget(self.right_side_frame)
    
    def clear_right_widget(self):
        self.right_side_frame = None
        self.right_side_screen = None
        self.container.setWidget(QWidget())

    def check_save_data(self, item: QStandardItem):
        if self.right_side_screen is None:
            return

        old_data = item.data(Qt.UserRole + 1)
        new_data = self.right_side_screen.getOutput()
        for (key, value) in old_data.items():
            if key not in new_data:
                print(f"{key}: {value} > ?")
            elif new_data[key] != value:
                print(f"{key}: {value} > {new_data[key]}")

        if old_data == new_data:
            return

        ret = QMessageBox.question(None, "Object Changed", "Would you like to save changes made to this object?", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            item.setData(new_data, Qt.UserRole + 1)

    def save_data(self, item: QStandardItem):
        data = self.right_side_screen.getOutput()
        item.setData(data, Qt.UserRole + 1)
