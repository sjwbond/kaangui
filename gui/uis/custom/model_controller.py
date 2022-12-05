import copy
from functools import partial
from gui.uis.custom.model_helpers import findFreeName, get_all_object_names, model_to_dict, model_to_dict_1
from gui.uis.custom.properties_table_model import PropertiesTableModel
from gui.uis.windows.assign_group.assign_group_dialog_box import Ui_Dialog_Assign_Group
from qt_core import *
from gui.core.functions import *
from gui.uis.custom.node_tree_view import NodeTreeView
from gui.uis.custom.parents_table_model import ParentsTableModel
from gui.uis.custom.parents_table_view import ParentsTableView
from gui.uis.custom.properties_table_view import PropertiesTableView


CLIPBOARD_FOLDER = "folder"
CLIPBOARD_OBJECT = "object"

table_header_hash = {'Parent Object':0, "Target Object":1, "Property":2, "Date_From":3,	"Date_To":4,	"Value":5,	"Variable":6,	"Variable_Effect":7,	"Timeslice":8,	"Timeslice_Index":9,	"Group_id":10,	"Priority":11,	"Scenario":12}
table_header_hash_2 = {'Parent Object':0, "Parent Property":1}


class AssignGroup(QDialog, Ui_Dialog_Assign_Group):
    def __init__(self, parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)


class ModelController:
    def __init__(self, tree: NodeTreeView, properties_table: PropertiesTableView, parents_table: ParentsTableView, object_properties: dict, parent_properties: list[str]):
        self.tree = tree
        self.properties_table = properties_table
        self.parents_model = None
        self.parents_table = parents_table
        self.clipboard: list[dict] = []
        self.object_names = set()

        self.base_snapshot = {}
        self.last_snapshot = {}
        self.undo_history: list[dict] = []
        self.redo_history: list[dict] = []
        self.pause_history = False

        self.tree.itemDropped.connect(self.create_undo_snapshot)

        self.clipboardType = None
        self.clipboardContents = None
        self.clipboardName = None
        self.clipboardAncestors = None

        self.tree.setHeaderHidden(True)

        self.tree.short_paste_object = QShortcut(QKeySequence("F2"), self.tree)
        self.tree.short_paste_object.activated.connect(self.renameShortcut)

        self.tree.short_paste_object = QShortcut(QKeySequence("Delete"), self.tree)
        self.tree.short_paste_object.activated.connect(self.deleteShortcut)

        self.tree.short_cut_object = QShortcut(QKeySequence("Ctrl+X"), self.tree)
        self.tree.short_cut_object.activated.connect(self.cutShortcut)

        # self.tree.short_copy_object = QShortcut(QKeySequence("Ctrl+C"), self.tree)
        # self.tree.short_copy_object.activated.connect(self.copyShortcut)

        # self.tree.short_paste_object = QShortcut(QKeySequence("Ctrl+V"), self.tree)
        # self.tree.short_paste_object.activated.connect(self.pasteShortcut)

        self.tree.short_undo_object = QShortcut(QKeySequence("Ctrl+Z"), self.tree)
        self.tree.short_undo_object.activated.connect(self.undoShortcut)

        self.tree.short_redo_object = QShortcut(QKeySequence("Ctrl+Y"), self.tree)
        self.tree.short_redo_object.activated.connect(self.redoShortcut)

        self.properties_table.short_copy_properties = QShortcut(QKeySequence("Ctrl+C"), self.properties_table)
        self.properties_table.short_copy_properties.activated.connect(self.copyPropertiesShortcut)

        self.properties_table.short_paste_properties = QShortcut(QKeySequence("Ctrl+V"), self.properties_table)
        self.properties_table.short_paste_properties.activated.connect(self.pastePropertiesShortcut)

        self.properties_table_object_properties_dict = object_properties
        self.parent_properties = parent_properties
    
    def create_snapshot(self) -> dict:
        modelNode = self.tree.rootModel.index(0, 0)
        return {
            "name": modelNode.data(Qt.DisplayRole),
            "SystemInputs": model_to_dict(self.tree.rootModel)
        }

    def save_base_snapshot(self):
        self.base_snapshot = self.create_snapshot()
        self.last_snapshot = self.base_snapshot
        self.undo_history = []
        self.redo_history = []

    def get_diff(self, old: dict, new: dict, path: list[str], added: list, removed: list, changed: list):
        for key in new.keys():
            if key not in old or type(old[key]) != type(new[key]):
                added.append((path + [key], None, new[key]))

        for key in old.keys():
            if key not in new or type(old[key]) != type(new[key]):
                removed.append((path + [key], old[key], None))

        for key in old.keys():
            if key in new:
                if ((type(old[key]) is not dict and type(new[key]) is not dict) or "Properties" in new[key]) and old[key] != new[key]:
                    changed.append((path + [key], old[key], new[key]))
                elif type(old[key]) is dict and type(new[key]) is dict and "Properties" not in new[key]:
                    self.get_diff(old[key], new[key], path + [key], added, removed, changed)
                
    def create_snapshot_diff(self, snapshot: dict) -> dict:
        added = []
        removed = []
        changed = []
        self.get_diff(self.last_snapshot, snapshot, [], added, removed, changed)
        return {
            "added": added,
            "removed": removed,
            "changed": changed
        }

    def get_item_by_path(self, path: list[str]) -> QModelIndex:
        return self.get_item_by_path_(self.tree.rootModel.index(0, 0), path)

    def get_item_by_path_(self, index: QModelIndex, path: list[str]) -> QModelIndex:
        if len(path) == 0:
            return index

        for i in range(self.tree.rootModel.rowCount(index)):
            ix = self.tree.rootModel.index(i, 0, index)
            name = ix.data(Qt.DisplayRole)
            if name == path[0]:
                return self.get_item_by_path_(ix, path[1:])

        return None

    def undo_snapshot_diff(self, diff: dict):
        for item in diff["added"]:
            (path, _, _) = item
            index = self.get_item_by_path(path[1:])
            self.remove_node_from_tree(index)

        for item in diff["removed"]:
            (path, old, _) = item
            name = path[-1]
            index = self.get_item_by_path(path[1:-1])
            self.add_node_to_tree({name: old}, self.tree.rootModel.itemFromIndex(index))

        for item in diff["changed"]:
            (path, old, new) = item
            index = self.get_item_by_path(path[1:])
            if path == ["name"]:
                self.tree.rootModel.itemFromIndex(index).setData(old, Qt.DisplayRole)
                self.object_names.remove(new)
                self.object_names.add(old)
            else:
                self.tree.rootModel.itemFromIndex(index).setData(old, Qt.UserRole)
                
        self.update_properties_table()

    def redo_snapshot_diff(self, diff: dict):
        for item in diff["removed"]:
            (path, _, _) = item
            index = self.get_item_by_path(path[1:])
            self.remove_node_from_tree(index)

        for item in diff["added"]:
            (path, _, new) = item
            name = path[-1]
            index = self.get_item_by_path(path[1:-1])
            self.add_node_to_tree({name: new}, self.tree.rootModel.itemFromIndex(index))

        for item in diff["changed"]:
            (path, old, new) = item
            index = self.get_item_by_path(path[1:])
            if path == ["name"]:
                self.tree.rootModel.itemFromIndex(index).setData(new, Qt.DisplayRole)
                self.object_names.remove(old)
                self.object_names.add(new)
            else:
                self.tree.rootModel.itemFromIndex(index).setData(new, Qt.UserRole)
        
        self.update_properties_table()

    def create_undo_snapshot(self):
        if self.pause_history:
            return

        snapshot = self.create_snapshot()
        diff = self.create_snapshot_diff(snapshot)
        if len(diff["added"]) == 0 and len(diff["removed"]) == 0 and len(diff["changed"]) == 0:
            return

        self.redo_history.clear()
        self.last_snapshot = snapshot
        self.undo_history.append(diff)

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
        self.create_undo_snapshot()
        self.pause_history = True
        item = self.pop_undo_item()
        if item is not None:
            self.undo_snapshot_diff(item)
            self.last_snapshot = self.create_snapshot()
        self.pause_history = False

    def redo(self):
        self.pause_history = True
        item = self.pop_redo_item()
        if item is not None:
            self.redo_snapshot_diff(item)
            self.last_snapshot = self.create_snapshot()
        self.pause_history = False

    def set_filter_text(self, text: str):
        self.tree.proxyModel.setFilterRegularExpression(text)

    def add_node_to_tree(self, model_node: dict, tree_node: QStandardItem):
        for node_key in model_node:
            node = QStandardItem(node_key)
            node.setEditable(False)
            if not "Properties" in model_node[node_key]:
                self.add_node_to_tree(model_node[node_key], node)

                node.setIcon(QIcon(Functions.set_svg_icon("icon_folder.svg")))
                node.setData("folder", Qt.UserRole)
                node.setFlags(Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | node.flags())
            else:
                self.object_names.add(node_key)
                node.setIcon(QIcon(Functions.set_svg_icon("icon_file.svg")))
                node.setData(model_node[node_key], Qt.UserRole) 
                node.setFlags(Qt.ItemIsDragEnabled | node.flags() & (~Qt.ItemIsDropEnabled))

            tree_node.appendRow(node)

    def remove_node_from_tree(self, tree_node: QModelIndex):
        self.object_names.remove(tree_node.data(Qt.DisplayRole))
        self.tree.rootModel.removeRow(tree_node.row(), tree_node.parent())

    def update_properties_table(self):
        selected = self.tree.selectedIndexes()
        self.pause_history = True

        properties = []
        props = set()

        for i in range(len(selected)):
            name = selected[i].data(Qt.DisplayRole)
            tabledata = selected[i].data(Qt.UserRole)
            if tabledata not in ["folder", "model", None]:
                props.update(self.properties_table_object_properties_dict[tabledata["Object_Type"]])
                for item in tabledata["Properties"]:
                    properties.append([
                        name,
                        item["Parent Object"],
                        item["Target Object"],
                        item["Property"],
                        item["Date_From"],
                        item["Date_To"],
                        item["Value"],
                        item["Variable"],
                        item["Variable_Effect"],
                        item["Timeslice"],
                        item["Timeslice_Index"],
                        item["Group_id"],
                        item["Priority"],
                        item["Scenario"]
                    ])

        self.properties_model = PropertiesTableModel(properties)
        self.properties_model.itemChanged.connect(self.save_properties_table)
        self.properties_proxy_model = QSortFilterProxyModel(self.properties_table)
        self.properties_proxy_model.setSourceModel(self.properties_model)
        self.properties_table.setComboProps(list(props))
        self.properties_table.setModel(self.properties_proxy_model)

        parentships = []
        current = self.tree.currentIndex()
        if current is not None:
            tabledata = current.data(Qt.UserRole)
            if tabledata not in ["folder", "model", None]:
                for item in tabledata["Parent Objects"]:
                    parentships.append([
                        item["Parent Object"],
                        item["Parent Property"] if "Parent Property" in item else ""
                    ])

        self.parents_model = ParentsTableModel(parentships)
        self.parents_model.itemChanged.connect(self.save_parent_table)
        props = get_all_object_names(self.tree.rootModel)
        self.parents_table.setComboProps(props)
        self.parents_table.setModel(self.parents_model)

        self.pause_history = False
    
    def clear_tables(self):
        self.properties_model = PropertiesTableModel([])
        self.properties_model.itemChanged.connect(self.save_properties_table)
        self.properties_table.setModel(self.properties_model)
        self.parents_model = ParentsTableModel([])
        self.parents_model.itemChanged.connect(self.save_parent_table)
        self.parents_table.setModel(self.parents_model)

    def save_properties_table(self):
        self.properties_table.viewport().update()
        self.create_undo_snapshot()
        selected = self.tree.selectedIndexes()

        objectProperties = {}
        for row in range(self.properties_model.rowCount(QModelIndex())):
            name = self.properties_model.dataAt(row, 0, Qt.DisplayRole)
            if name not in objectProperties:
                objectProperties[name] = []

            object = {
                "Parent Object": self.properties_model.dataAt(row, 1, Qt.DisplayRole),
                "Target Object": self.properties_model.dataAt(row, 2, Qt.DisplayRole),
                "Property": self.properties_model.dataAt(row, 3, Qt.DisplayRole),
                "Date_From": self.properties_model.dataAt(row, 4, Qt.DisplayRole),
                "Date_To": self.properties_model.dataAt(row, 5, Qt.DisplayRole),
                "Value": self.properties_model.dataAt(row, 6, Qt.DisplayRole),
                "Variable": self.properties_model.dataAt(row, 7, Qt.DisplayRole),
                "Variable_Effect": self.properties_model.dataAt(row, 8, Qt.DisplayRole),
                "Timeslice": self.properties_model.dataAt(row, 9, Qt.DisplayRole),
                "Timeslice_Index": self.properties_model.dataAt(row, 10, Qt.DisplayRole),
                "Group_id": self.properties_model.dataAt(row, 11, Qt.DisplayRole),
                "Priority": self.properties_model.dataAt(row, 12, Qt.DisplayRole),
                "Scenario": self.properties_model.dataAt(row, 13, Qt.DisplayRole)
            }
            objectProperties[name].append(object)
        
        for i in range(len(selected)):
            item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected[i]))
            name = item.data(Qt.DisplayRole)
            data = copy.deepcopy(item.data(Qt.UserRole))
            data["Properties"].clear()
            if name in objectProperties:
                data["Properties"] = objectProperties[name]
            item.setData(data, Qt.UserRole)

        self.create_undo_snapshot()

    def save_parent_table(self):
        self.create_undo_snapshot()
        selected = self.tree.currentIndex()
        item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected))
        data = item.data(Qt.UserRole)
        data["Parent Objects"] = [{"Parent Object": row[0], "Parent Property": row[1]} for row in self.parents_model.getData()]
        item.setData(data, Qt.UserRole)
        self.create_undo_snapshot()

    def delete_seleted_rows_parent(self):
        if self.parents_model is not None:
            indexes = self.parents_table.selectionModel().selectedRows()
            self.parents_model.removeRows(indexes)

    def add_new_rows_parent(self):
        if self.parents_model is not None:
            self.parents_model.appendNewRow()

    def delete_seleted_rows(self):
        if self.properties_model is not None:
            indexes = self.properties_table.selectionModel().selectedRows()
            self.properties_model.removeRows(indexes)

    def add_new_rows(self):
        if self.properties_model is not None:
            selected = self.tree.selectedIndexes()
            name = selected[0].data(Qt.DisplayRole) if len(selected) == 1 else ""
            self.properties_model.appendNewRow(name)

    def copy_seleted_rows(self):
        self.clipboard = []
        indexes = self.properties_table.selectionModel().selectedRows()
        data = self.properties_model.getData()
        for index in indexes:
            self.clipboard.append(copy.deepcopy(data[index.row()]))

    def paste_copied_rows(self):
        for object in self.clipboard:
            self.properties_model.appendRow(object)

    def copyPropertiesShortcut(self):
        indexes = self.properties_table.selectionModel().selectedIndexes()
        if len(indexes) == 0:
            return

        row0 = indexes[0].row()
        col0 = indexes[0].column()

        items_out = []
        for index in indexes:
            row = index.row() - row0
            col = index.column() - col0

            while len(items_out) <= row:
                items_out.append([])
            while len(items_out[row]) <= col:
                items_out[row].append([])

            items_out[row][col] = index.data(Qt.DisplayRole)
        
        QApplication.clipboard().setText("\n".join(["\t".join(row) for row in items_out]))

    def pastePropertiesShortcut(self):
        indexes = self.properties_table.selectionModel().selectedIndexes()
        if len(indexes) == 0:
            return

        cb = QApplication.clipboard().text()
        items = [line.split() for line in cb.split("\n")]

        row0 = indexes[0].row()
        col0 = indexes[0].column()

        indexes_out = []
        items_out = []
        for index in indexes:
            row = index.row() - row0
            col = index.column() - col0

            if row >= len(items):
                continue
            if col >= len(items[row]):
                continue

            indexes_out.append(self.properties_proxy_model.mapToSource(index))
            items_out.append(items[row][col])
            
        self.properties_model.setDataMulti(indexes_out, items_out, Qt.DisplayRole)

    # Helping function for gettin selected nodes parents
    # ///////////////////////////////////////////////////////////////

    def getAncestry(self, index: QModelIndex):
        ancestry: list[str] = []
        while index.isValid():
            ancestry.append(index.data(Qt.DisplayRole))
            index = index.parent()
        ancestry.reverse()
        return ancestry

    # Right click menu for Tree Widget
    # ///////////////////////////////////////////////////////////////

    def openMenu(self, position):
        current = self.tree.currentIndex()
        if current is not None:
            selectedItem = current.data(Qt.UserRole)
            menu = QMenu()

            item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(current))
            if item is not None:
                children = [item.child(i).data(0) for i in range(item.rowCount())]

                if selectedItem == "model":
                    menuitems = []
                    for type in self.properties_table_object_properties_dict.keys():
                        if type not in children:
                            menuitem = QAction(type)
                            menuitem.triggered.connect(partial(self.createNewFolderByModelWithName, type))
                            menuitems.append(menuitem)
                    
                    if len(menuitems) > 0:
                        newfoldermenu = QMenu("Create Folder")
                        newfoldermenu.addActions(menuitems)
                        menu.addMenu(newfoldermenu)

                    qmenurenamemodel = QAction("Rename Model")
                    qmenurenamemodel.triggered.connect(self.renameModel)
                    menu.addAction(qmenurenamemodel)
                elif selectedItem == "folder":
                    qmenunewobject = QAction("Create a New Object under " + current.data(0))
                    qmenunewobject.triggered.connect(self.createNewObjectByModel)
                    menu.addAction(qmenunewobject)

                    qmenunewfolder = QAction("Create a New Folder under " + current.data(0))
                    qmenunewfolder.triggered.connect(self.createNewFolderByModel)
                    menu.addAction(qmenunewfolder)

                    isTopLevel = item.parent() == self.tree.rootModel.item(0, 0)

                    if not isTopLevel:
                        qmenurenamefolder = QAction("Rename Folder")
                        qmenurenamefolder.triggered.connect(self.renameByModel)
                        menu.addAction(qmenurenamefolder)

                    qmenucopyfolder = QAction("Copy Folder and its content")
                    qmenucopyfolder.triggered.connect(self.copyByModel)
                    menu.addAction(qmenucopyfolder)

                    if not isTopLevel:
                        qmenucutfolder = QAction("Cut Folder and its content")
                        qmenucutfolder.triggered.connect(self.cutByModel)
                        menu.addAction(qmenucutfolder)

                    if self.clipboardType != None:
                        qmenupaste = QAction("Paste " + self.clipboardName + " under " + current.data(0))
                        qmenupaste.triggered.connect(self.pasteByModel)
                        menu.addAction(qmenupaste)

                    if not isTopLevel:
                        qmenudeletefolder = QAction("Delete Folder and its content")
                        qmenudeletefolder.triggered.connect(self.deleteByModel)
                        menu.addAction(qmenudeletefolder)
                else:
                    qmenurenameobject = QAction("Rename Object")
                    qmenurenameobject.triggered.connect(self.renameByModel)
                    menu.addAction(qmenurenameobject)

                    qmenucopyobject = QAction("Copy Object")
                    qmenucopyobject.triggered.connect(self.copyByModel)
                    menu.addAction(qmenucopyobject)

                    qmenucutobject = QAction("Cut Object")
                    qmenucutobject.triggered.connect(self.cutByModel)
                    menu.addAction(qmenucutobject)
                    
                    qmenupasteobject = QAction("Paste Object")
                    qmenupasteobject.triggered.connect(self.pasteByModel)
                    menu.addAction(qmenupasteobject)

                    qmenuassignobject = QAction("Assign Group to Object")
                    qmenuassignobject.triggered.connect(self.assignGroupByModel)
                    menu.addAction(qmenuassignobject)

                    qmenudeleteobject = QAction("Delete Object")
                    qmenudeleteobject.triggered.connect(self.deleteByModel)
                    menu.addAction(qmenudeleteobject)

                menu.exec_(QApplication.focusWidget().viewport().mapToGlobal(position))

    # Functions for object and model manipulation
    # ///////////////////////////////////////////////////////////////

    def assignGroupByModel(self):
        selected = self.tree.currentIndex()
        self.dialogBox = AssignGroup()
        self.dialogBox.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.dialogBox.tableWidget.setColumnCount(2)
        self.dialogBox.tableWidget.setHorizontalHeaderLabels(["Parent Object", "Parent Property"])
        self.dialogBox.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dialogBox.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
            
        @Slot(str)
        def onTextChanged(text: str):
            for index in range(self.dialogBox.listWidget.count()):
                item = self.dialogBox.listWidget.item(index)
                if text.lower() in item.data(Qt.DisplayRole).lower():
                    item.setHidden(False)
                else:
                    item.setHidden(True)
                    item.setCheckState(Qt.Unchecked)
        self.dialogBox.lineEdit.textChanged.connect(onTextChanged)

        temp = copy.deepcopy(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected)).data(Qt.UserRole))
        self.dialogBox.tableWidget.setRowCount(len(temp["Parent Objects"]))
        for row in range(len(temp["Parent Objects"])):
            self.dialogBox.tableWidget.setItem(row, 0, QTableWidgetItem(temp["Parent Objects"][row]["Parent Object"]))
            self.dialogBox.tableWidget.setItem(row, 1, QTableWidgetItem(temp["Parent Objects"][row]["Parent Property"]))
        
        items_obj = get_all_object_names(self.tree.rootModel)
        for item in items_obj:
            item = QListWidgetItem(item)
            item.setCheckState(Qt.Unchecked)
            self.dialogBox.listWidget.addItem(item)

        for item in self.parent_properties: 
            item = QListWidgetItem(item)
            item.setCheckState(Qt.Unchecked)
            self.dialogBox.listWidget_2.addItem(item)

        def click_add_button():
            listWidget = self.dialogBox.listWidget
            listWidget_2 = self.dialogBox.listWidget_2
            tableWidget = self.dialogBox.tableWidget

            objects = [listWidget.item(x).data(Qt.DisplayRole) for x in range(listWidget.count()) if listWidget.item(x).checkState() == Qt.Checked]
            properties = [listWidget_2.item(x).data(Qt.DisplayRole) for x in range(listWidget_2.count()) if listWidget_2.item(x).checkState() == Qt.Checked]

            if len(properties) == 0:
                properties = [""]

            for object in objects:
                for property in properties:
                    ix = tableWidget.rowCount()
                    tableWidget.setRowCount(ix + 1)
                    tableWidget.setItem(ix, 0, QTableWidgetItem(object))
                    tableWidget.setItem(ix, 1, QTableWidgetItem(property))

        self.dialogBox.pushButton.clicked.connect(click_add_button)

        def click_remove_button():
            indexes = [index.row() for index in self.dialogBox.tableWidget.selectedIndexes()]
            indexes = list(set(indexes))
            indexes.sort()
            indexes.reverse()
            for index in indexes:
                self.dialogBox.tableWidget.removeRow(index)
            
        self.dialogBox.pushButton_2.clicked.connect(click_remove_button)

        def finished(result):
            if result != 1:
                return
            self.create_undo_snapshot()
            temp = copy.deepcopy(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected)).data(Qt.UserRole))
            temp["Parent Objects"] = []
            for row in range(self.dialogBox.tableWidget.rowCount()):
                temp["Parent Objects"].append({
                        "Parent Object": self.dialogBox.tableWidget.item(row, 0).data(Qt.DisplayRole),
                        "Parent Property": self.dialogBox.tableWidget.item(row, 1).data(Qt.DisplayRole)
                    })
            self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected)).setData(temp, Qt.UserRole)
            self.update_properties_table()
            self.create_undo_snapshot()

        self.dialogBox.finished.connect(finished)

        self.dialogBox.show()
        self.dialogBox.open()

    def deleteByModel(self):     
        qm = QMessageBox
        isObject = self.tree.proxyModel.itemData(self.tree.currentIndex())[Qt.UserRole] != "folder"
        ret = qm.question(self.tree, '', "Are you sure to delete object?" if isObject else "Are you sure to delete folder and its content?", qm.Yes | qm.No)

        if ret ==  qm.Yes:
            self.create_undo_snapshot()
            self.remove_node_from_tree(self.tree.proxyModel.mapToSource(self.tree.currentIndex()))
            self.create_undo_snapshot()

    def renameByModel(self):
        selected = self.tree.currentIndex()
        oldName = selected.data(Qt.DisplayRole)
        text, okPressed = QInputDialog.getText(self.tree, "New name", "New name:", text=oldName)
        if okPressed and text != '' and text != oldName:
            self.create_undo_snapshot()
            ix = selected
            ix2 = self.tree.proxyModel.mapToSource(ix)
            it = self.tree.rootModel.itemFromIndex(ix2)

            if text in self.object_names:
                msg = QMessageBox()
                msg.setWindowTitle("Rename Failed")
                msg.setText("An object with the same name already exists.")
                msg.exec()
                return

            it.setData(text, Qt.DisplayRole)
            if it.data(Qt.UserRole) not in ["folder", "mode", None]:
                self.object_names.remove(oldName)
                self.object_names.add(text)
            self.create_undo_snapshot()

    def copyByModel(self):
        selected = self.tree.currentIndex()
        self.clipboardName = selected.data(Qt.DisplayRole)
        self.clipboardAncestors = self.tree.getAncestors(selected)
        type = selected.data(Qt.UserRole)
        if type == "folder":
            self.clipboardContents = copy.deepcopy(model_to_dict_1(self.tree.rootModel.indexFromItem(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected))), self.tree.rootModel))
            self.clipboardType = CLIPBOARD_FOLDER
        else:
            self.clipboardContents = copy.deepcopy(selected.data(Qt.UserRole))
            self.clipboardType = CLIPBOARD_OBJECT

    def cutByModel(self):
        self.create_undo_snapshot()
        selected = self.tree.currentIndex()
        self.copyByModel()
        self.remove_node_from_tree(self.tree.proxyModel.mapToSource(selected))
        self.create_undo_snapshot()

    def pasteByModel(self):
        self.create_undo_snapshot()
        selected = self.tree.currentIndex()
        item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected))

        if selected.data(Qt.UserRole) != "folder" and selected.data(Qt.UserRole) != "model":
            item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected.parent()))
        
        targetAncestors = self.tree.getAncestors(item)
        if self.clipboardAncestors[0:2] != targetAncestors[0:2]:
            msg = QMessageBox()
            msg.setWindowTitle("Paste Failed")
            msg.setText("Cannot copy objects/folders across different top-level folders.")
            msg.exec()
            return
        
        self.dictToPaste = {self.findFreeName(self.clipboardName, "Copy of ") : self.clipboardContents}
        self.add_node_to_tree(copy.deepcopy(self.dictToPaste), item)
        self.create_undo_snapshot()

    def renameShortcut(self):
        self.renameByModel()

    def deleteShortcut(self):
        self.deleteByModel()

    def cutShortcut(self):
        self.cutByModel()

    def copyShortcut(self):
        self.copyByModel()

    def pasteShortcut(self):
        if self.clipboardType is not None:
            self.pasteByModel()

    def undoShortcut(self):
        self.undo()

    def redoShortcut(self):
        self.redo()

    # Functions for object manipulation
    # ///////////////////////////////////////////////////////////////

    def findFreeName(self, name, prefix = ""):
        counter = 0
        freeName = name
        if freeName in self.object_names:
            freeName = prefix + name
        while freeName in self.object_names:
            counter += 1
            freeName = prefix + name + " (" + str(counter) + ")"
        
        return freeName

    def createNewObjectByModel(self):
        try:
            text, okPressed = QInputDialog.getText(self.tree, "New object name","New object name:", text="New Object")
            if okPressed and text != '':
                selected = self.tree.currentIndex()
                keysList = self.getAncestry(selected)
                item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected))
                name = self.findFreeName(text)
                newObjectDict = {name : {
                "Object_Name": name,
                "Object_Type": keysList[1],
                "Parent Objects": [],
                "Properties": []
                }}

                self.create_undo_snapshot()
                self.add_node_to_tree(newObjectDict, item)
                self.create_undo_snapshot()

        except Exception as e:
            raise

    # Functions for folder manipulation
    # ///////////////////////////////////////////////////////////////

    def createNewFolderByModelWithName(self, name):
        self.create_undo_snapshot()
        selected = self.tree.currentIndex()
        item = self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(selected))
        name = findFreeName(item, name)
        newObjectDict = {name : {}}
        self.add_node_to_tree(newObjectDict, item)
        self.create_undo_snapshot()

    def createNewFolderByModel(self):
        text, okPressed = QInputDialog.getText(self.tree, "New folder name","New folder name:", text="New Folder")
        if okPressed and text != '':
            self.createNewFolderByModelWithName(text)
            self.create_undo_snapshot()

    # Functions for model manipulation
    # ///////////////////////////////////////////////////////////////

    def renameModel(self):
        selected = self.tree.currentIndex()
        text, okPressed = QInputDialog.getText(self.tree, "New name","New name:", text=selected.data(0))
        if okPressed and text != '':
            self.create_undo_snapshot()
            self.tree.proxyModel.setData(selected, text)
            self.create_undo_snapshot()
    
    def create_all_base_folders(self):
        object = {}
        for type in self.properties_table_object_properties_dict.keys():
            object[type] = {}
        self.add_node_to_tree(object, self.tree.rootModel.item(0, 0))

    def select_path(self, path: list[str]):
        idx = self.get_item_by_path(path)
        idx_proxy = self.tree.proxyModel.mapFromSource(idx)
        self.tree.setCurrentIndex(idx_proxy)
        self.update_properties_table()

    def select_model(self):
        idx = self.tree.rootModel.index(0, 0)
        idx_proxy = self.tree.proxyModel.mapFromSource(idx)
        self.tree.setCurrentIndex(idx_proxy)
        self.update_properties_table()
