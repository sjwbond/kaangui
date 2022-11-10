from functools import partial
from gui.uis.custom.node_tree_view import NodeTreeView
from gui.uis.windows.screens.diagnosticscreen import Ui_DiagnosticsScreen, diagnostics_default_input
from gui.uis.windows.screens2.horizons import Ui_Horizons, horizons_default_input
from gui.uis.windows.screens2.lrmc_models import Ui_LRMCModels, lrmc_models_default_input
from gui.uis.windows.screens2.execution_plans import Ui_ExecutionPlans, execution_plans_default_input
from gui.uis.windows.screens.mtschedulescreen import Ui_MTScheaduleScreen, mtschedule_default_input
from gui.uis.windows.screens.pasascreen import Ui_PASAScreen, pasa_default_input
from gui.uis.windows.screens.productionscreen import Ui_ProductionScreen, production_default_input
from gui.uis.windows.screens.stochasticscreen import Ui_StochasticScreen, stochastic_default_input
from gui.uis.windows.screens.stschedulescreen import Ui_STScheduleScreen, stschedule_default_input
from gui.uis.custom.constants import tree_structure, execution_priorities
from gui.uis.windows.screens2.settings import Ui_Settings, settings_default_input
from qt_core import *


container_style = '''
QFrame {{
    background-color: {background_color};
    border: none;
}}
'''

style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 10px;
    color: {foreground_color};
	border-radius: {border_radius}px;	
	background-color: {background_color};
    min-height: 30px;
}}
QPushButton:hover {{
	background-color: {focus_color};
}}
QPushButton:pressed {{
	background-color: {pressed_color};
}}

QGroupBox {{
    border: 1px solid {background_color_2};
    border-radius: {border_radius}px;
    margin-top: 8px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 7px;
    padding: 0px 5px 0px 5px;
}}

QSpinBox,
QDoubleSpinBox {{
	background-color: {background_color};
	border-radius: {border_radius}px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {foreground_color};
	selection-background-color: #555555;
    color: {foreground_color};
    min-height: 25px;
}}
QSpinBox:focus,
QDoubleSpinBox:focus {{
	border: 2px solid #ffffff;
    background-color: {focus_color};
}}

QComboBox {{
	background-color: {background_color};
	border-radius: {border_radius}px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {foreground_color};
	selection-background-color: #555555;
    color: {foreground_color};
    min-height: 25px;
}}
QComboBox:focus {{
	border: 2px solid #ffffff;
    background-color: {focus_color};
}}

QDateEdit {{
	background-color: {background_color};
	border-radius: {border_radius}px;
	border: 2px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {foreground_color};
	selection-background-color: #555555;
    color: {foreground_color};
    min-height: 25px;
}}
QDateEdit:focus {{
	border: 2px solid #ffffff;
    background-color: {focus_color};
}}

QLineEdit {{
	background-color: #333;
	border: 0px solid transparent;
	padding-left: 1px;
    padding-right: 1px;
	selection-color: #FFF;
	selection-background-color: #00ABE8;
    color: #FFF;
}}
QLineEdit:focus {{
	border: 0px solid transparent;
    background-color: {background_color_2};
}}

QTableWidget {{
	background-color: {background_color_2};
	padding: 5px;
	border-radius: {border_radius}px;
	gridline-color: #44475a;
    color: {foreground_color};
}}
QTableWidget::item{{
	border-color: none;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: rgb(44, 49, 60);
    border-bottom: 1px solid #595D75;
}}
QTableWidget::item:selected{{
	background-color: {background_color_2};
}}
QHeaderView::section{{
	background-color: {background_color_2};
	max-width: 30px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
QTableWidget::horizontalHeader {{	
	background-color: {background_color_2};
}}
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {background_color_2};
	padding: 3px;
    border-top-left-radius: {border_radius}px;
}}
QTableView {{
	background-color: {background_color_2};
	padding: 5px;
	border-radius: {border_radius}px;
	gridline-color: #44475a;
    color: {foreground_color};
}}
QTableView::item{{
	border-color: none;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: rgb(44, 49, 60);
    border-bottom: 1px solid #595D75;
}}
QTableView::item:selected{{
	background-color: {background_color_2};
}}
QHeaderView::section{{
	background-color: {background_color_2};
	max-width: 30px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
QTableView::horizontalHeader {{
	background-color: {background_color_2};
}}
QTableView QTableCornerButton::section {{
    border: none;
	background-color: {background_color_2};
	padding: 3px;
    border-top-left-radius: {border_radius}px;
}}
QHeaderView::section:horizontal
{{
    border: none;
	background-color: {background_color_2};
	padding: 3px;
}}
QHeaderView::section:vertical
{{
    border: none;
	background-color: {background_color_2};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid #595D75;
    margin-bottom: 1px;
}}
'''


class ExecutionController(QObject):
    executed = Signal(str, int)

    def __init__(self, node_tree: NodeTreeView, execution_tree: QTreeView, container: QScrollArea, theme: dict, options: dict) -> None:
        self.node_tree = node_tree
        self.execution_tree = execution_tree
        self.container = container
        self.theme = theme
        self.options = options
        self.model = QStandardItemModel()
        self.simulation = {}
        self.right_side_screen = None
        self.last_index = None

        container.setStyleSheet(container_style.format(background_color=theme["bg_one"]))

        self.undo_history: list[dict] = []
        self.redo_history: list[dict] = []

        self.execution_tree.setHeaderHidden(True)
        self.execution_tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.execution_tree.setDragEnabled(False)
        self.execution_tree.setAcceptDrops(False)
        self.execution_tree.setDropIndicatorShown(False)
        self.execution_tree.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.execution_tree.setContextMenuPolicy(Qt.CustomContextMenu)

        self.execution_tree.clicked.connect(self.selection_changed)
        self.execution_tree.customContextMenuRequested.connect(self.open_menu)

        self.short_paste_object = QShortcut(QKeySequence("F2"), self.execution_tree)
        self.short_paste_object.activated.connect(self.renameShortcut)

        self.short_paste_object = QShortcut(QKeySequence("Delete"), self.execution_tree)
        self.short_paste_object.activated.connect(self.deleteShortcut)

        self.short_undo_object = QShortcut(QKeySequence("Ctrl+Z"), self.execution_tree)
        self.short_undo_object.activated.connect(self.undo)

        self.short_redo_object = QShortcut(QKeySequence("Ctrl+Y"), self.execution_tree)
        self.short_redo_object.activated.connect(self.redo)

        super().__init__()

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

                if key_b in simulation:
                    for (key_c, value_c) in simulation[key_b].items():
                        subsubitem = QStandardItem(key_c)
                        subsubitem.setData(("leaf", key_c, type), Qt.UserRole)
                        subsubitem.setData(value_c, Qt.UserRole + 1)
                        subitem.appendRow(subsubitem)
        
        self.execution_tree.setModel(self.model)
        self.execution_tree.expandAll()
        self.selection_changed()
        self.clear_history()
    
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
        if len(self.execution_tree.selectedIndexes()) > 0:
            index = self.execution_tree.selectedIndexes()[0]
            item = self.model.itemFromIndex(index)
            user_data = index.data(Qt.UserRole)

            if user_data is not None:
                (level, name, type) = user_data

                if level == "node":
                    menu = QMenu()

                    qmenu_create_new = QAction(f"Create New {name}")
                    qmenu_create_new.triggered.connect(partial(self.create_new, item, name, type))
                    menu.addAction(qmenu_create_new)

                    menu.exec_(QApplication.focusWidget().viewport().mapToGlobal(position))
                elif level == "leaf":
                    menu = QMenu()

                    if type == "models":
                        menuitems = []
                        for (label, priority) in execution_priorities:
                            menuitem = QAction(f"{label} Priority")
                            menuitem.triggered.connect(partial(self.execute_model, item, priority))
                            menuitems.append(menuitem)

                        qmenu_execute_model = QMenu("Execute Model")
                        qmenu_execute_model.addActions(menuitems)
                        menu.addMenu(qmenu_execute_model)

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
        if type == "executionplan":
            subitem.setData(execution_plans_default_input, Qt.UserRole + 1)
        if type == "settings":
            subitem.setData(settings_default_input, Qt.UserRole + 1)
        if type == "diagnostics":
            subitem.setData(diagnostics_default_input, Qt.UserRole + 1)
        elif type == "horizons":
            subitem.setData(horizons_default_input, Qt.UserRole + 1)
        elif type == "lrmcmodels":
            subitem.setData(lrmc_models_default_input, Qt.UserRole + 1)
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

        self.create_undo_snapshot_added(self.get_item_path(subitem), (subitem.data(Qt.UserRole), subitem.data(Qt.UserRole + 1)))

    def execute_model(self, item: QStandardItem, priority: int):
        self.check_save_data(item)
        self.executed.emit(item.data(Qt.DisplayRole), priority)

    def execute_selected_model(self, priority: int):
        if len(self.execution_tree.selectedIndexes()) > 0:
            index = self.execution_tree.selectedIndexes()[0]
            item = self.model.itemFromIndex(index)
            self.check_save_data(item)
            self.executed.emit(item.data(Qt.DisplayRole), priority)

    def replace_item_in_models_settings(self, type: str, old: str, new: str):
        items = self.get_objects_of_type("leaf", "models")

        for item in items:
            data = item.data(Qt.UserRole + 1)

            if type not in data:
                return

            if data[type] == old:
                data[type] = new

            item.setData(data, Qt.UserRole + 1)

    def rename(self, item: QStandardItem):
        old_name = item.data(Qt.DisplayRole)
        _, _, type = item.data(Qt.UserRole)

        new_name, okPressed = QInputDialog.getText(None, "Rename", "New name:", text=old_name)
        if not okPressed or new_name == '' or new_name == old_name:
            return

        subitems = [self.model.index(i, 0, item.parent().index()).data(Qt.DisplayRole) for i in range(item.parent().rowCount())]
        while new_name in subitems:
            new_name, okPressed = QInputDialog.getText(None, "Rename", "An object with the same name exists. Please choose a different name.\nNew name:", text=old_name)
            if not okPressed or new_name == '' or new_name == old_name:
                return

        old_path = self.get_item_path(item)

        item.setData(new_name, Qt.DisplayRole)

        self.replace_item_in_models_settings(type, old_name, new_name)

        self.create_undo_snapshot_renamed(old_path, self.get_item_path(item))
    
    def renameShortcut(self):
        current = self.execution_tree.currentIndex()
        if current is not None:
            self.rename(self.model.itemFromIndex(current))

    def delete(self, index: QModelIndex):
        ret = QMessageBox.question(None, "Delete", "Are you sure you wish to delete this object?", QMessageBox.Yes | QMessageBox.No)
        if ret != QMessageBox.Yes:
            return

        item = self.model.itemFromIndex(index)
        self.create_undo_snapshot_removed(self.get_item_path(item), (item.data(Qt.UserRole), item.data(Qt.UserRole + 1)))

        self.model.removeRow(index.row(), index.parent())
    
    def deleteShortcut(self):
        current = self.execution_tree.currentIndex()
        if current is not None:
            self.delete(current)

    def get_simulations(self, index: QModelIndex = None):
        res = []
        item = None
        model = self.node_tree.rootModel

        if index is None:
            item = model.invisibleRootItem()
        else:
            item = model.itemFromIndex(index)

        for i in range(item.rowCount()):
            ix = model.index(i, 0, item.index())
            it = model.itemFromIndex(ix)
            idata = it.data(Qt.UserRole)

            if "Properties" in idata:
                for iproperty in idata["Properties"]:
                    if "Scenario" in iproperty and iproperty["Scenario"] != "":
                        res.append(iproperty["Scenario"])
            
            res = res + self.get_simulations(ix)

        return res

    def get_objects_of_type(self, level: str, type: str, index: QModelIndex = None) -> list[QStandardItem]:
        res = []
        item = None

        if index is None:
            item = self.model.invisibleRootItem()
        else:
            item = self.model.itemFromIndex(index)

        for i in range(item.rowCount()):
            ix = self.model.index(i, 0, item.index())
            it = self.model.itemFromIndex(ix)
            ilevel, _, itype = it.data(Qt.UserRole)

            if ilevel == level and itype == type:
                res.append(it)
            
            res = res + self.get_objects_of_type(level, type, ix)

        return res
    
    def get_objects_of_level_by_type(self, level: str, res: dict = None, index: QModelIndex = None):
        if res is None:
            res = {}
        item = None

        if index is None:
            item = self.model.invisibleRootItem()
        else:
            item = self.model.itemFromIndex(index)

        for i in range(item.rowCount()):
            ix = self.model.index(i, 0, item.index())
            it = self.model.itemFromIndex(ix)
            iname = it.data(Qt.DisplayRole)
            ilevel, _, itype = it.data(Qt.UserRole)

            if ilevel == level:
                if itype not in res:
                    res[itype] = []
                res[itype].append(iname)
            
            res = self.get_objects_of_level_by_type(level, res, ix)

        return res

    def selection_changed(self):
        if len(self.execution_tree.selectedIndexes()) == 0:
            self.clear_right_widget()
            return

        index = self.execution_tree.selectedIndexes()[0]
        item = self.model.itemFromIndex(index)
        user_data = index.data(Qt.UserRole)

        if user_data is None:
            self.clear_right_widget()
            return

        (level, name, type) = user_data

        if self.last_index is not None:
            self.check_save_data(self.model.itemFromIndex(self.last_index))

        self.last_index = index

        self.clear_right_widget()
        
        if level == "leaf":
            if type == "executionplans":
                self.set_right_data_screen(Ui_ExecutionPlans(), item)
            if type == "settings":
                self.set_right_data_screen(Ui_Settings(), item)
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
            elif type == "lrmcmodels":
                self.set_right_data_screen(Ui_LRMCModels(), item)
            elif type == "horizons":
                self.set_right_data_screen(Ui_Horizons(), item)
            elif type == "pasa":
                self.set_right_data_screen(Ui_PASAScreen(), item)
    
    def set_right_data_screen(self, screen: QObject, item: QStandardItem):
        self.right_side_frame = QFrame()
        self.right_side_screen = screen
        self.right_side_screen.setupUi(self.right_side_frame)
        
        if hasattr(self.right_side_screen, "executed"):
            self.right_side_screen.executed.connect(self.execute_selected_model)
        if hasattr(self.right_side_screen, "setChoices"):
            self.right_side_screen.setChoices(self.options)
        if hasattr(self.right_side_screen, "setOptions"):
            self.right_side_screen.setOptions(self.get_objects_of_level_by_type("leaf"))
        if hasattr(self.right_side_screen, "setScenarios"):
            self.right_side_screen.setScenarios(self.get_simulations())

        self.right_side_screen.setInput(item.data(Qt.UserRole + 1))
        self.right_side_frame.setStyleSheet(style.format(
            border_radius=8,
            background_color=self.theme["dark_one"],
            foreground_color=self.theme["text_foreground"],
            focus_color=self.theme["dark_three"],
            pressed_color=self.theme["dark_four"],
            background_color_2=self.theme["bg_two"],
        ))
        self.container.setWidget(self.right_side_frame)
    
    def clear_right_widget(self):
        self.right_side_frame = None
        self.right_side_screen = None
        self.container.setWidget(QWidget())

    def check_save_data(self, item: QStandardItem = None):
        if item is None:
            if self.last_index is None:
                return
            item = self.model.itemFromIndex(self.last_index)

        if self.right_side_screen is None or item is None:
            return

        old_data = item.data(Qt.UserRole + 1)
        new_data = self.right_side_screen.getOutput()

        if old_data == new_data:
            return

        ret = QMessageBox.question(None, "Object Changed", "Would you like to save changes made to this object?", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            old_data = item.data(Qt.UserRole + 1)

            item.setData(new_data, Qt.UserRole + 1)

            self.create_undo_snapshot_changed(self.get_item_path(item), old_data, new_data)

    def save(self):
        if self.last_index is None:
            return

        item = self.model.itemFromIndex(self.last_index)
        old_data = item.data(Qt.UserRole + 1)

        new_data = self.right_side_screen.getOutput()
        item.setData(new_data, Qt.UserRole + 1)

        self.create_undo_snapshot_changed(self.get_item_path(item), old_data, new_data)

    def clear_history(self):
        self.undo_history = []
        self.redo_history = []

    def get_item_by_path(self, path: list[str], index: QModelIndex = None) -> QModelIndex:
        if len(path) == 0:
            return index

        if index is None:
            index = self.model.invisibleRootItem().index()

        for i in range(self.model.rowCount(index)):
            ix = self.model.index(i, 0, index)
            name = ix.data(Qt.DisplayRole)
            if name == path[0]:
                return self.get_item_by_path(path[1:], ix)

        return index

    def undo_snapshot_diff(self, diff: dict):
        for path, _ in diff["added"]:
            index = self.get_item_by_path(path)
            self.model.removeRow(index.row(), index.parent())

        for path, old in diff["removed"]:
            name = path[-1]
            index = self.get_item_by_path(path[:-1])
            item = self.model.itemFromIndex(index)
            subitem = QStandardItem(name)
            data1, data2 = old
            subitem.setData(data1, Qt.UserRole)
            subitem.setData(data2, Qt.UserRole + 1)
            item.appendRow(subitem)

        for old_path, new_path in diff["renamed"]:
            old_name = old_path[-1]
            index = self.get_item_by_path(new_path)
            item = self.model.itemFromIndex(index)
            new_name = item.data(Qt.DisplayRole)
            _, _, type = item.data(Qt.UserRole)
            self.replace_item_in_models_settings(type, new_name, old_name)
            item.setData(old_name, Qt.DisplayRole)

        for path, old, _ in diff["changed"]:
            index = self.get_item_by_path(path)
            self.model.itemFromIndex(index).setData(old, Qt.UserRole + 1)
                
        self.selection_changed()

    def redo_snapshot_diff(self, diff: dict):
        for path, _ in diff["removed"]:
            index = self.get_item_by_path(path)
            self.model.removeRow(index.row(), index.parent())

        for path, new in diff["added"]:
            name = path[-1]
            index = self.get_item_by_path(path[:-1])
            item = self.model.itemFromIndex(index)
            subitem = QStandardItem(name)
            data1, data2 = new
            subitem.setData(data1, Qt.UserRole)
            subitem.setData(data2, Qt.UserRole + 1)
            item.appendRow(subitem)

        for old_path, new_path in diff["renamed"]:
            new_name = new_path[-1]
            index = self.get_item_by_path(old_path)
            item = self.model.itemFromIndex(index)
            old_name = item.data(Qt.DisplayRole)
            _, _, type = item.data(Qt.UserRole)
            self.replace_item_in_models_settings(type, old_name, new_name)
            self.model.itemFromIndex(index).setData(new_name, Qt.DisplayRole)

        for path, _, new in diff["changed"]:
            index = self.get_item_by_path(path)
            self.model.itemFromIndex(index).setData(new, Qt.UserRole + 1)
        
        self.selection_changed()

    def get_item_path(self, item: QStandardItem):
        res = [item.data(Qt.DisplayRole)]
        parent = item.parent()
        while parent is not None:
            res = [parent.data(Qt.DisplayRole)] + res
            parent = parent.parent()
        return res

    def create_undo_snapshot(self, diff: dict):
        self.redo_history.clear()
        self.undo_history.append(diff)

    def create_undo_snapshot_added(self, path, new):
        self.create_undo_snapshot({
            "added": [(path, new)],
            "removed": [],
            "renamed": [],
            "changed": []
        })

    def create_undo_snapshot_removed(self, path, old):
        self.create_undo_snapshot({
            "added": [],
            "removed": [(path, old)],
            "renamed": [],
            "changed": []
        })

    def create_undo_snapshot_renamed(self, old_path, new_path):
        self.create_undo_snapshot({
            "added": [],
            "removed": [],
            "renamed": [(old_path, new_path)],
            "changed": []
        })

    def create_undo_snapshot_changed(self, path, old, new):
        self.create_undo_snapshot({
            "added": [],
            "removed": [],
            "renamed": [],
            "changed": [(path, old, new)]
        })
    
    def pop_undo_item(self) -> dict:
        if len(self.undo_history) > 0:
            item = self.undo_history.pop()
            self.redo_history.append(item)
            return item
        return None
    
    def pop_redo_item(self) -> dict:
        if len(self.redo_history) > 0:
            item = self.redo_history.pop()
            self.undo_history.append(item)
            return item
        return None

    def undo(self):
        self.check_save_data()
        self.last_index = None
        item = self.pop_undo_item()
        if item is not None:
            self.undo_snapshot_diff(item)
            self.selection_changed()

    def redo(self):
        self.check_save_data()
        self.last_index = None
        item = self.pop_redo_item()
        if item is not None:
            self.redo_snapshot_diff(item)
            self.selection_changed()
