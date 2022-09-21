import copy
import csv
from functools import partial
import json
import sys
from gui.uis.custom.api import list_models
from gui.uis.custom.model_helpers import get_all_object_names, model_to_dict_1
from qt_core import *
from gui.core.functions import *
from gui.uis.custom.node_tree_view import NodeTreeView
from gui.uis.custom.parents_table_model import ParentsTableModel
from gui.uis.custom.parents_table_view import ParentsTableView
from gui.widgets.comboBoxSearchable.comboBoxSearchable import ExtendedComboBox
from gui.uis.custom.properties_table_widget import PropertiesTableWidget
from main import AssignGroup


CLIPBOARD_FOLDER = "folder"
CLIPBOARD_OBJECT = "object"

table_header_hash = {'Parent Object':0, "Target Object":1, "Property":2, "Date_From":3,	"Date_To":4,	"Value":5,	"Variable":6,	"Variable_Effect":7,	"Timeslice":8,	"Timeslice_Index":9,	"Group_id":10,	"Priority":11,	"Scenario":12}
table_header_hash_2 = {'Parent Object':0, "Parent Property":1}

class ModelController:
    def __init__(self, tree: NodeTreeView, properties_table: PropertiesTableWidget, parents_table: ParentsTableView):
        self.tree = tree
        self.properties_table = properties_table
        self.parents_model = None
        self.parents_table = parents_table
        self.clipboard: list[dict] = []
        self.currentlySelectedModelObject =[] #To keep curretly selected object branch

        self.clipboardType = None
        self.clipboardContents = None
        self.clipboardName = None

        self.tree.setHeaderHidden(True)

        self.tree.short_copy_object = QShortcut(QKeySequence("Ctrl+C"), self.tree)
        self.tree.short_copy_object.activated.connect(self.copyShortcut)

        self.tree.short_copy_object = QShortcut(QKeySequence("Ctrl+V"), self.tree)
        self.tree.short_copy_object.activated.connect(self.pasteShortcut)

        self.properties_table_object_properties_dict= {}
        with open(os.getcwd()+"\\Properties of Object Types.csv", mode='r') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                self.properties_table_object_properties_dict[rows[0]] = []
            infile.seek(0)
            for rows in reader:
                self.properties_table_object_properties_dict[rows[0]].append(rows[1])
        
    def set_filter_text(self, text: str):
        self.tree.proxyModel.setFilterRegularExpression(text)
        
    def add_node_to_tree(self, model_node: dict, tree_node: QStandardItem):
        for node_key in model_node:
            node = QStandardItem(node_key)
            node.setEditable(False)

            if not "Properties" in model_node[node_key]:
                self.add_node_to_tree(model_node[node_key], node)
                if node.hasChildren():
                    node.setIcon(QIcon(Functions.set_svg_icon("icon_folder.svg")))
                    node.setData("folder", Qt.UserRole)                     
                    tree_node.appendRow(node)

                if not model_node[node_key]: #this is to check if the folder is newly created and hence empty
                    node.setIcon(QIcon(Functions.set_svg_icon("icon_folder.svg")))
                    node.setData("folder", Qt.UserRole)              
                    tree_node.appendRow(node)
            else:
                node.setIcon(QIcon(Functions.set_svg_icon("icon_file.svg")))
                node.setData(model_node[node_key], Qt.UserRole) 
                tree_node.appendRow(node)

    def remove_node_from_tree(self, tree_node):
        self.tree.rootModel.removeRow(tree_node.row(), tree_node.parent())

    def update_properties_table(self):
        tabledata = self.tree.selectedIndexes()[0].data(Qt.UserRole)
        
        if tabledata == "folder" or tabledata == "model":
            self.properties_table.setRowCount(0)
            self.parents_table.setModel(ParentsTableModel([]))
        elif tabledata is not None:
            self.properties_table.setRowCount(len(tabledata["Properties"]))
            props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
            for i, item in enumerate(tabledata["Properties"]):
                for key, value in table_header_hash.items():
                    if key == "Property":
                        combo = ExtendedComboBox()
                        
                        for t in props:
                            combo.addItem(t)

                        self.properties_table.setCellWidget(i,value,combo)
                        combo.setCurrentIndex(props.index(item[key]))
                        combo.currentIndexChanged.connect(self.save_properties_table)
                    else:
                        self.properties_table.setItem(i, value, QTableWidgetItem(item[key]))

            data = []
            for item in tabledata["Parent Objects"]:
                data.append([
                    item["Parent Object"],
                    item["Parent Property"]
                ])

            self.parents_model = ParentsTableModel(data)
            self.parents_model.itemChanged.connect(self.save_parent_table)
            self.parents_table.setModel(self.parents_model)

            # TODO update props when model has changed
            props = get_all_object_names(self.tree.rootModel)
            self.parents_table.setComboProps(props)

    def save_properties_table(self):
        getSelected = self.tree.selectedIndexes()
        keysList = self.getNodeNameAndParentList(getSelected)

        self.currentlySelectedModelObject = copy.deepcopy(keysList)

        listofPropertiesToAppend = []
        for row in range(self.properties_table.rowCount()):
            tempDict = {}
            for column in range(self.properties_table.columnCount()):
                try:
                    if isinstance(self.properties_table.cellWidget(row, column) , QComboBox):
                        tempDict[self.properties_table.horizontalHeaderItem(column).text()]= self.properties_table.cellWidget(row, column).currentText()
                    else:
                        tempDict[self.properties_table.horizontalHeaderItem(column).text()]= self.properties_table.item(row, column).text()
                except AttributeError:
                    tempDict[self.properties_table.horizontalHeaderItem(column).text()]=""
            listofPropertiesToAppend.append(tempDict)
        
        temp = copy.deepcopy(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
        temp["Properties"].clear()
        temp["Properties"] = listofPropertiesToAppend.copy()
        self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)

    def save_parent_table(self):
        getSelected = self.tree.selectedIndexes()
        keysList = self.getNodeNameAndParentList(getSelected)

        self.currentlySelectedModelObject = copy.deepcopy(keysList)

        listofParentsToAppend = []
        data = self.parents_model.getData()
        for row in data:
            tempDict = {
                "Parent Object": row[0],
                "Parent Property": row[1]
            }
            listofParentsToAppend.append(tempDict)
        
        # TODO clean up this bit
        temp = copy.deepcopy(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
        temp["Parent Objects"].clear()
        temp["Parent Objects"] = listofParentsToAppend.copy()
        self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)

    def delete_seleted_rows_parent(self):
        if self.parents_model is not None:
            indexes = self.parents_table.selectionModel().selectedRows()
            self.parents_model.removeRows(indexes)

    def add_new_rows_parent(self):
        if self.parents_model is not None:
            self.parents_model.appendNewRow()

    def delete_seleted_rows(self):
        indexes = self.properties_table.selectionModel().selectedRows()
        for index in sorted(indexes):
            self.properties_table.removeRow(index.row())

    def add_new_rows(self):
        rowPosition = self.properties_table.rowCount()
        self.properties_table.insertRow(rowPosition)
        for column in range(self.properties_table.columnCount()):
            if column == 2:
                combo = ExtendedComboBox()

                props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                combo.addItem("")
                for t in props:
                    combo.addItem(t)          
                self.properties_table.setCellWidget(rowPosition,column,combo)

                combo.currentIndexChanged.connect(self.save_properties_table)
            
            elif column == 3:
                self.properties_table.setItem(rowPosition, column, QTableWidgetItem("2000-01-01"))  
            elif column == 4:
                self.properties_table.setItem(rowPosition, column, QTableWidgetItem("2100-01-01"))  

            else:
                self.properties_table.setItem(rowPosition, column, QTableWidgetItem(""))

    def copy_seleted_rows(self):
        self.clipboard = []
        indexes = self.properties_table.selectionModel().selectedRows()
        for index in sorted(indexes):
            rowToCopyDict = {}
            for column in range(self.properties_table.columnCount()):
                if column == 2:
                    rowToCopyDict[self.properties_table.horizontalHeaderItem(column).text()] = self.properties_table.cellWidget(index.row(), column).currentText()
                else:
                    rowToCopyDict[self.properties_table.horizontalHeaderItem(column).text()] = self.properties_table.item(index.row(), column).text()
            self.clipboard.append(copy.deepcopy(rowToCopyDict))

    def paste_copied_rows(self):
        rowPosition = self.properties_table.rowCount()
        for i in range(len(self.clipboard)):
            self.properties_table.insertRow(rowPosition)
            rowToPasteDict = self.clipboard[i]
            for column in range(self.properties_table.columnCount()):
                if column == 2:
                    combo = ExtendedComboBox()

                    props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                    for t in props:
                        combo.addItem(t)
                    
                    self.properties_table.setCellWidget(rowPosition,column,combo)
                    combo.setCurrentIndex(props.index(rowToPasteDict[self.properties_table.horizontalHeaderItem(column).text()]))
                    combo.currentIndexChanged.connect(self.save_properties_table)

                else:
                    self.properties_table.setItem(rowPosition, column, QTableWidgetItem(rowToPasteDict[self.properties_table.horizontalHeaderItem(column).text()]))                                            

            rowPosition = self.properties_table.rowCount()

    # Helping function for gettin selected nodes parents
    # ///////////////////////////////////////////////////////////////

    def getNodeNameAndParentList(self, getSelected: list[QModelIndex]):
        parents: list[QModelIndex] = []
        for index in getSelected:
            while index.parent().isValid():
                index = index.parent()
                parents.append(index.sibling(index.row(), 0))
        parentObjects = [index.data() for index in parents]
        parentObjects.reverse()
        return parentObjects + [getSelected[0].data(0)]

    # Right click menu for Tree Widget
    # ///////////////////////////////////////////////////////////////

    def openMenu(self, position):
        if len(self.tree.selectedIndexes()) > 0:
            selectedItem = self.tree.selectedIndexes()[0].data(Qt.UserRole)
            menu = QMenu()

            children = []
            for i in range (self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(self.tree.selectedIndexes()[0])).rowCount()):
                children.append(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(self.tree.selectedIndexes()[0])).child(i).data(0))

            if selectedItem == "model":
                menuitems = []
                for type in self.properties_table_object_properties_dict.keys():
                    if type not in children:
                        menuitem = QAction(type)
                        menuitem.triggered.connect(partial(self.createNewFolderByModelWithName, type))
                        menuitems.append(menuitem)
                newfoldermenu = QMenu("Create Folder")
                newfoldermenu.addActions(menuitems)
                menu.addMenu(newfoldermenu)

                qmenurenamemodel = QAction("Rename Model")
                qmenurenamemodel.triggered.connect(self.renameModel)
                menu.addAction(qmenurenamemodel)
            elif selectedItem == "folder":
                qmenunewobject = QAction("Create a New Object under " + self.tree.selectedIndexes()[0].data(0))
                qmenunewobject.triggered.connect(self.createNewObjectByModel)
                menu.addAction(qmenunewobject)

                qmenunewfolder = QAction("Create a New Folder under " + self.tree.selectedIndexes()[0].data(0))
                qmenunewfolder.triggered.connect(self.createNewFolderByModel)
                menu.addAction(qmenunewfolder)

                qmenurenamefolder = QAction("Rename Folder")
                qmenurenamefolder.triggered.connect(self.renameFolderByModel)
                menu.addAction(qmenurenamefolder)

                qmenucopyfolder = QAction("Copy Folder and its content")
                qmenucopyfolder.triggered.connect(self.copyFolderByModel)
                menu.addAction(qmenucopyfolder)

                if self.clipboardType != None:
                    qmenupaste = QAction("Paste " + self.clipboardName + " under " + self.tree.selectedIndexes()[0].data(0))
                    if self.clipboardType == CLIPBOARD_FOLDER:
                        qmenupaste.triggered.connect(self.pasteFolderByModel)
                    elif self.clipboardType == CLIPBOARD_OBJECT:
                        qmenupaste.triggered.connect(self.pasteObjectByModel)
                    menu.addAction(qmenupaste)

                qmenudeletefolder = QAction("Delete Folder and its content")
                qmenudeletefolder.triggered.connect(self.deleteFolderByModel)
                menu.addAction(qmenudeletefolder)
            else:
                qmenurenameobject = QAction("Rename Object")
                qmenurenameobject.triggered.connect(self.renameObjectByModel)
                menu.addAction(qmenurenameobject)

                qmenucopyobject = QAction("Copy Object")
                qmenucopyobject.triggered.connect(self.copyObjectByModel)
                menu.addAction(qmenucopyobject)

                qmenucutobject = QAction("Cut Object")
                qmenucutobject.triggered.connect(self.cutObjectByModel)
                menu.addAction(qmenucutobject)
                
                qmenupasteobject = QAction("Paste Object")
                qmenupasteobject.triggered.connect(self.pasteObjectByModel)
                menu.addAction(qmenupasteobject)

                qmenudeleteobject = QAction("Delete Object")
                qmenudeleteobject.triggered.connect(self.deleteObjectByModel)
                menu.addAction(qmenudeleteobject)

            menu.exec_(QApplication.focusWidget().viewport().mapToGlobal(position))

    # Functions for model object manipulation
    # ///////////////////////////////////////////////////////////////

    def createNewObjectByModel(self):
        try:
            text, okPressed = QInputDialog.getText(self.tree, "New object name","New object name:", text="New Object")
            if okPressed and text != '':
                getSelected = self.tree.selectedIndexes()
                keysList = self.getNodeNameAndParentList(getSelected)
                newObjectDict = {text : {"Model Id": "yarrak",
                "Object_Name": text,
                "Object_Type": keysList[1],
                "Parent Objects": [],
                "Properties": []
                }}

            self.add_node_to_tree(newObjectDict, self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])))

        except Exception as e:
            raise

    def assignGroupByModel(self):
        getSelected = self.tree.selectedIndexes()
        self.dialogBox = AssignGroup()
        self.dialogBox.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        
        items_obj = self.get_all_object_names(self.tree.rootModel)
        for item in items_obj:
            item = QListWidgetItem(item)
            item.setCheckState(Qt.Unchecked)
            self.dialogBox.listWidget.addItem(item)

        items_obj_prop = ["a","b","c"]
        for item in items_obj_prop: 
            item = QListWidgetItem(item)
            item.setCheckState(Qt.Unchecked)
            self.dialogBox.listWidget_2.addItem(item)     

        def click_add_button():
            print("botuno bastin")

        self.dialogBox.pushButton.clicked.connect(click_add_button)

        self.dialogBox.show()
        
        if self.dialogBox.exec_():
            ###### Is there are way to set data only for a certain sub dict of the Qt.UserRole????? I just want to edit
            ###### "Parent Object", so the entire data doesn't have to be copied - edited - pasted ????
            temp = copy.deepcopy(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
            temp["Parent Object"].clear()
            for selected in self.dialogBox.listWidget.selectedItems():
                temp["Parent Object"].append(selected.text())
            self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)
            
    def deleteObjectByModel(self):
        qm = QMessageBox
        ret = qm.question(self.tree, '', "Are you sure to delete object?", qm.Yes | qm.No)

        if ret ==  qm.Yes:
            getSelected = self.tree.selectedIndexes()

            self.remove_node_from_tree(self.tree.proxyModel.mapToSource(getSelected[0]))

    def renameObjectByModel(self):
        getSelected = self.tree.selectedIndexes()
        text, okPressed = QInputDialog.getText(self.tree, "New name", "New name:", text=getSelected[0].data(0))
        if okPressed and text != '':
            self.tree.proxyModel.setData(self.tree.currentIndex(), text)

    def copyObjectByModel(self):
        getSelected = self.tree.selectedIndexes()
        self.clipboardName = getSelected[0].data(0)
        #keysList=getNodeParentList(getSelected) + [self.clipboardName]
        a = getSelected[0].data(Qt.UserRole)
        self.clipboardContents =  copy.deepcopy(a)
        self.clipboardType = CLIPBOARD_OBJECT

    def cutObjectByModel(self):
        getSelected = self.tree.selectedIndexes()
        self.clipboardName = getSelected[0].data(0)
        a = getSelected[0].data(Qt.UserRole)
        self.clipboardContents = copy.deepcopy(a)
        self.remove_node_from_tree(self.tree.proxyModel.mapToSource(getSelected[0]))

    def copyShortcut(self):
        getSelected = self.tree.selectedIndexes()
        if getSelected[0].data(Qt.UserRole) == "folder":
            self.copyFolderByModel()
        else:
            self.copyObjectByModel()

    def pasteObjectByModel(self):
        getSelected = self.tree.selectedIndexes()

        names=[]
        if getSelected[0].data(Qt.UserRole) == "folder":
            for i in range (self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).rowCount()):
                names.append(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).child(i).data(0))
        else:
            for i in range (self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0].parent())).rowCount()):
                names.append(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0].parent())).child(i).data(0))                

        counter = 0
        clipboardName = self.clipboardName
        if clipboardName in names:
            clipboardName = "copy of " + self.clipboardName
        while clipboardName in names:
            counter+=1                
            clipboardName = "copy of " + self.clipboardName + " (" + str(counter) + ")"
            
        self.dictObjectToPaste = {clipboardName : self.clipboardContents}

        if getSelected[0].data(Qt.UserRole) == "folder":
            self.add_node_to_tree(copy.deepcopy(self.dictObjectToPaste), self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])))
        else:
            self.add_node_to_tree(copy.deepcopy(self.dictObjectToPaste), self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0].parent())))

    def pasteShortcut(self):
        if self.clipboardTypee == CLIPBOARD_FOLDER:
            self.pasteFolderByModel()
        elif self.clipboardTypee == CLIPBOARD_OBJECT:
            self.pasteObjectByModel()
        else:
            pass

    # Functions for folder manipulation
    # ///////////////////////////////////////////////////////////////

    def createNewFolderByModel(self):  
        text, okPressed = QInputDialog.getText(self.tree, "New folder name","New folder name:", text="New Folder")
        if okPressed and text != '':
            getSelected = self.tree.selectedIndexes()
            newObjectDict = {text : {}}

        self.add_node_to_tree(newObjectDict, self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])))

    def createNewFolderByModelWithName(self, name):
        getSelected = self.tree.selectedIndexes()
        newObjectDict = {name : {}}
        self.add_node_to_tree(newObjectDict, self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])))

    def deleteFolderByModel(self):     
        qm = QMessageBox
        ret = qm.question(self.tree, '', "Are you sure to delete folder and its content?", qm.Yes | qm.No)
        if ret ==  qm.Yes:
            getSelected = self.tree.selectedIndexes()
            self.remove_node_from_tree(self.tree.proxyModel.mapToSource(getSelected[0]))
        else:
            pass

    def renameFolderByModel(self):
        getSelected = self.tree.selectedIndexes()
        text, okPressed = QInputDialog.getText(self.tree, "New name","New name:", text=getSelected[0].data(0))
        if okPressed and text != '':
            self.tree.proxyModel.setData(self.tree.currentIndex(), text)

    def renameModel(self):
        getSelected = self.tree.selectedIndexes()
        text, okPressed = QInputDialog.getText(self.tree, "New name","New name:", text=getSelected[0].data(0))
        if okPressed and text != '':
            self.tree.proxyModel.setData(self.tree.currentIndex(), text)

    def copyFolderByModel(self):       
        getSelected = self.tree.selectedIndexes()
        self.clipboardName = getSelected[0].data(0)
        #### The folder node is identified and send to a modification model_to_dict function
        a = model_to_dict_1(self.tree.rootModel.indexFromItem(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0]))), self.tree.rootModel)
        self.clipboardContents = copy.deepcopy(a)
        self.clipboardType = CLIPBOARD_FOLDER

    def pasteFolderByModel(self):
        getSelected = self.tree.selectedIndexes()

        names=[]
        for i in range (self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).rowCount()):
            names.append(self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])).child(i).data(0))

        counter = 0
        clipboardName = self.clipboardName
        if clipboardName in names:
            clipboardName = "copy of " + self.clipboardName
        while clipboardName in names:
            counter+=1                
            clipboardName = "copy of " + self.clipboardName + " (" + str(counter) + ")"
            
        self.dictFolderToPaste = {clipboardName : self.clipboardContents}
        self.add_node_to_tree(copy.deepcopy(self.dictFolderToPaste), self.tree.rootModel.itemFromIndex(self.tree.proxyModel.mapToSource(getSelected[0])))

    # Drag and drop
    # ///////////////////////////////////////////////////////////////
        
    global dragStart
    def dragStart(self):
        getSelected = self.tree.selectedIndexes()
        if getSelected[0].data(Qt.UserRole) == "folder":
            pass  #cut folder function is to be coded
        else:
            self.copyObjectByModel()

    global dragEnd
    def dragEnd(self, dragTarget):
        self.pasteObjectByModel(dragTarget)
