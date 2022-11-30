# ///////////////////////////////////////////////////////////////
from datetime import datetime
import re

from gui.uis.windows.open_model.open_model import Ui_OpenModelDialog
from gui.uis.custom.api import WebAPI
from gui.uis.custom.execution_controller import ExecutionController
from gui.uis.custom.model_controller import ModelController
from gui.uis.custom.model_helpers import model_to_dict, sanitize_json
from gui.uis.custom.node_tree_view import NodeTreeView
from gui.uis.custom.parents_table_view import ParentsTableView
from gui.uis.custom.properties_table_view import PropertiesTableView
from gui.uis.custom.styled_button import StyledButton
from gui.widgets.py_tree_view.py_tree_view import PyTreeView
from . functions_main_window import *
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

## KAAN FUNCTIONS
# ///////////////////////////////////////////////////////////////
from gui.core.functions import *
import json
from gui.widgets.py_customTree_widget import *
from gui.core.create_json import readTxt


class OpenModelDialog(QDialog, Ui_OpenModelDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
    
    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_model",
            "btn_text" : "Model",
            "btn_tooltip" : "Model",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_execution",
            "btn_text" : "Execution",
            "btn_tooltip" : "Execution",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_results",
            "btn_text" : "Results",
            "btn_tooltip" : "Results",
            "show_top" : True,
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_2)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # CREATE WebAPI INSTANCE
        # ///////////////////////////////////////////////////////////////
        self.api = WebAPI(settings.items["api_path"], settings.items["user_id"])

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # ICON BUTTON 1
        self.delete_table_row_button = StyledButton(text="Delete Selected Row", themes=self.themes)
        self.add_table_row_button = StyledButton(text="Add New Row", themes=self.themes)
        self.copy_table_row_button = StyledButton(text="Copy Selected Rows", themes=self.themes)
        self.paste_table_row_button = StyledButton(text="Paste Copied Rows", themes=self.themes)
        self.add_table_2_row_button = StyledButton(text="Add Parentship", themes=self.themes)
        self.delete_table_2_row_button = StyledButton(text="Delete Selected Parentships", themes=self.themes)
        self.undo_button = StyledButton(text="Undo", themes=self.themes, icon_name="icon_undo.svg")
        self.redo_button = StyledButton(text="Redo", themes=self.themes, icon_name="icon_redo.svg")
        self.create_new_model_button = StyledButton(text="Create New Model", icon_name="icon_file.svg", themes=self.themes)
        self.create_json_database_from_txt_files_button = StyledButton(text="Create Model Json file From Txt Folder", icon_name="icon_attachment.svg", themes=self.themes)
        self.open_api_model_button = StyledButton(text="Open Model", icon_name="icon_restore.svg", themes=self.themes)
        self.save_api_model_button = StyledButton(text="Save Model", icon_name="icon_save.svg", themes=self.themes)
        self.open_json_model_button = StyledButton(text="Open JSON", icon_name="icon_restore.svg", themes=self.themes)
        self.save_json_model_button = StyledButton(text="Save JSON", icon_name="icon_save.svg", themes=self.themes)

        self.execution_undo_button = StyledButton(text="Undo", themes=self.themes, icon_name="icon_undo.svg")
        self.execution_redo_button = StyledButton(text="Redo", themes=self.themes, icon_name="icon_redo.svg")
        self.execution_save_button = StyledButton(text="Save", themes=self.themes, icon_name="icon_save.svg")

        # PY LINE EDIT
        self.filterEdit = PyLineEdit(
            text = "",
            place_holder_text = "Type to search",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PropertiesTableView(self.themes["app_color"])

        self.table_widget_2 = ParentsTableView(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.working_directory = os.getcwd()
        self.tree = NodeTreeView(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.controller = ModelController(tree=self.tree, properties_table=self.table_widget, parents_table=self.table_widget_2, object_properties=self.settings["object_properties"], parent_properties=self.settings["parent_properties"])

        @Slot(str)
        def onTextChanged(text: str):
            self.controller.set_filter_text(text)
        self.filterEdit.textChanged.connect(onTextChanged)

        self.tree.clicked.connect(self.controller.update_properties_table)
        self.delete_table_2_row_button.clicked.connect(self.controller.delete_seleted_rows_parent)
        self.add_table_2_row_button.clicked.connect(self.controller.add_new_rows_parent)
        self.delete_table_row_button.clicked.connect(self.controller.delete_seleted_rows)
        self.add_table_row_button.clicked.connect(self.controller.add_new_rows)
        self.copy_table_row_button.clicked.connect(self.controller.copy_seleted_rows)
        self.paste_table_row_button.clicked.connect(self.controller.paste_copied_rows)

        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.controller.openMenu)
        
        self.redo_button.clicked.connect(self.controller.redo)
        self.undo_button.clicked.connect(self.controller.undo)

        self.create_new_model_button.clicked.connect(self.create_new_model)
        self.save_api_model_button.clicked.connect(self.save_model_to_api)
        self.open_api_model_button.clicked.connect(self.open_model_from_api)
        self.save_json_model_button.clicked.connect(self.save_model_to_json)
        self.open_json_model_button.clicked.connect(self.open_model_from_json)
        self.create_json_database_from_txt_files_button.clicked.connect(self.create_json_from_txt)

        self.tree.viewport().installEventFilter(self)

        # EXECUTION

        self.execution_tree = PyTreeView(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["bg_one"],
            bg_color = self.themes["app_color"]["bg_two"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )

        self.execution_screen_scroll_area = QHBoxLayout()
        self.execution_screen_scroll_area.addWidget(QWidget())

        self.execution_controller = ExecutionController(
            node_tree=self.tree,
            execution_tree=self.execution_tree,
            container=self.execution_screen_scroll_area,
            theme=self.themes["app_color"],
            options=settings.items["options"],
            object_properties=settings.items["object_properties"]
        )
        self.execution_controller.executed.connect(self.send_model_to_queue)

        self.execution_undo_button.clicked.connect(self.execution_controller.undo)
        self.execution_redo_button.clicked.connect(self.execution_controller.redo)
        self.execution_save_button.clicked.connect(self.save_execution)

        # ADD WIDGETS
        self.ui.load_pages.table_button_layout.addWidget(self.add_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.delete_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.copy_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.paste_table_row_button)
        self.ui.load_pages.row_3_layout.addWidget(self.undo_button)
        self.ui.load_pages.row_3_layout.addWidget(self.redo_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_new_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.open_api_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.save_api_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.open_json_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.save_json_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_json_database_from_txt_files_button)
        self.ui.load_pages.tree_layout.addWidget(self.filterEdit)
        self.ui.load_pages.tree_layout.addWidget(self.tree)
        self.ui.load_pages.table_layout.addWidget(self.table_widget)
        self.ui.load_pages.parentship_table_layout.addWidget(self.table_widget_2)
        self.ui.load_pages.parentship_button_layout.addWidget(self.add_table_2_row_button)
        self.ui.load_pages.parentship_button_layout.addWidget(self.delete_table_2_row_button)

        self.ui.load_pages.row_8_layout.addWidget(self.execution_tree, 1)
        self.ui.load_pages.row_8_layout.addLayout(self.execution_screen_scroll_area, 3)
        self.ui.load_pages.row_9_layout.addWidget(self.execution_undo_button)
        self.ui.load_pages.row_9_layout.addWidget(self.execution_redo_button)
        self.ui.load_pages.row_9_layout.addWidget(self.execution_save_button)

    # Model Functions
    def create_new_model(self):
        qm=QMessageBox()
        ret = qm.question(self.tree, '', "Are you sure to create a new model? It will reset the unsaved changes", qm.Yes | qm.No)
        if ret == qm.Yes:
            self.load_model({
                "name": "New Model",
                "SystemInputs": {}
            })
            self.controller.create_all_base_folders()
            self.controller.save_base_snapshot()

    # API
    def dump_model(self):
        return self.data | {"name": self.tree.rootModel.index(0, 0).data(Qt.DisplayRole), "Simulation": self.execution_controller.get_simulation(), "SystemInputs": model_to_dict(self.tree.rootModel)}

    def save_model_to_api(self):
        data = self.dump_model()
        modelId = self.tree.rootModel.index(0, 0).data(Qt.UserRole+1)
        if modelId == None:
            (modelId, hash) = self.api.create_model(data)
            self.tree.rootModel.invisibleRootItem().child(0, 0).setData(modelId, Qt.UserRole+1)
            self.data["name"] = self.tree.rootModel.invisibleRootItem().child(0, 0).data(Qt.DisplayRole)
            self.data["hash"] = hash
        else:
            new_hash = self.api.update_model(modelId, data)
            self.data["name"] = self.tree.rootModel.invisibleRootItem().child(0, 0).data(Qt.DisplayRole)
            self.data["hash"] = new_hash

                
    def load_model(self, model):
        self.data = model
        self.system_inputs = model["SystemInputs"]
        self.tree.rootModel.clear()
        self.tree.rootNode = self.tree.rootModel.invisibleRootItem()

        if "Simulation" in self.data:
            self.execution_controller.set_simulation(self.data["Simulation"])
        else:
            self.execution_controller.set_simulation({})

        modelNode = QStandardItem(model["name"])
        modelNode.setEditable(False)
        modelNode.setIcon(QIcon(Functions.set_svg_icon("icon_restore.svg")))
        modelNode.setData("model", Qt.UserRole)
        if "modelId" in model:
            modelNode.setData(model["modelId"], Qt.UserRole+1)
        modelNode.setFlags(Qt.ItemIsDropEnabled | modelNode.flags())
        self.tree.rootNode.appendRow(modelNode)
        self.tree.setExpanded(self.tree.proxyModel.mapFromSource(self.tree.rootModel.indexFromItem(modelNode)), True)
            
        self.controller.add_node_to_tree(self.system_inputs, modelNode)
        self.controller.clear_tables()
        self.controller.save_base_snapshot()

    def open_model_from_api(self):
        dialog = OpenModelDialog()
        models = self.api.list_models()
        itemModel = QStandardItemModel()
        dialog.modelList.setModel(itemModel)
        dialog.modelList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for model in models:
            item = QStandardItem(model["name"])
            item.setData(model, Qt.UserRole)
            itemModel.appendRow(item)

        dialog.versionList.setColumnCount(4)
        dialog.versionList.setHorizontalHeaderLabels(["Name", "Saved At", "Saved By", "Current?"])
        dialog.versionList.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        dialog.versionList.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        dialog.versionList.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        dialog.versionList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        def selection_changed(selected: QItemSelection, deselected: QItemSelection):
            if selected.length() < 1:
                dialog.versionList.setRowCount(0)
            modelS = selected.indexes()[0].data(Qt.UserRole)
            versions = self.api.get_model_history(modelS["modelId"])
            dialog.versionList.setRowCount(len(versions))
            for ix in range(len(versions)):
                version = versions[ix]
                date = datetime.fromisoformat(version['savedAt'][0:-1])
                formatted_date = date.strftime("%d-%m-%Y %H:%M:%S")
                is_current = modelS["hash"] == version['hash']

                name_item = QTableWidgetItem(version['name'])
                name_item.setData(Qt.UserRole, version["versionId"])

                dialog.versionList.setItem(ix, 0, name_item)
                dialog.versionList.setItem(ix, 1, QTableWidgetItem(formatted_date))
                dialog.versionList.setItem(ix, 2, QTableWidgetItem(version['savedByName']))
                dialog.versionList.setItem(ix, 3, QTableWidgetItem("Yes" if is_current else ""))

        dialog.modelList.selectionModel().selectionChanged.connect(selection_changed)

        dialog.show()
        if dialog.exec_():
            selection = dialog.modelList.selectedIndexes()
            versionSelection = dialog.versionList.selectedIndexes()
            if len(selection) < 1:
                return
                
            modelId = selection[0].data(Qt.UserRole)["modelId"]
            model = None

            if len(versionSelection) == 0:
                model = self.api.get_model(modelId)
            else:
                model = self.api.get_model_version(versionSelection[0].data(Qt.UserRole))
            
            self.load_model(model)

    def save_model_to_json(self):
        data = self.dump_model()
        (name, _) = QFileDialog.getSaveFileName(None, "Select JSON File", dir=f"{data['name']}.json")
        data = sanitize_json(data)
        if name != '':
            with open(name, "w", encoding="utf8") as file:
                json.dump(data, file, sort_keys=True, indent=4)

    def open_model_from_json(self):
        (name, _) = QFileDialog.getOpenFileName(None, "Select JSON File")
        if name != '':
            with open(name, "r", encoding="utf8") as file:
                model = json.load(file)
                model = sanitize_json(model)
                # Extract file name from path without extension
                m = re.match(r"^(?:.*[\/\\])?([^\/\\]+?|)(?=(?:\.[^\/\\.]*)?$)", name)
                model["name"] = m.group(1)
                self.load_model(model)

    def create_json_from_txt(self):
        name = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.working_directory, QFileDialog.ShowDirsOnly)
        if name != '':
            (outname, _) = QFileDialog.getSaveFileName(None, "Select JSON File", dir=f".json")
            if outname != '':
                data = readTxt(name)
                with open(outname, "w", encoding="utf8") as file:
                    json.dump(data, file, sort_keys=True, indent=4)

    def send_model_to_queue(self, name, priority):
        self.save_model_to_api()
        self.api.send_model_to_processing(name, self.data["hash"], priority)

    def save_execution(self):
        self.execution_controller.save()
        self.save_model_to_api()