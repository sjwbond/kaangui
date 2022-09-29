# ///////////////////////////////////////////////////////////////
from gui.uis.custom.api import create_model, delete_model, get_model, list_models, update_model
from gui.uis.custom.model_controller import ModelController
from gui.uis.custom.model_helpers import model_to_dict
from gui.uis.custom.node_tree_view import NodeTreeView
from gui.uis.custom.parents_table_view import ParentsTableView
from gui.uis.custom.properties_table_widget import PropertiesTableWidget
from gui.uis.custom.styled_button import StyledButton
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

from main import OpenModelDialog


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

        # LEFT COLUMN
        # ///////////////////////////////////////////////////////////////

        # ICON BUTTON 1
        self.delete_table_row_button = StyledButton(text="Delete Selected Rows", themes=self.themes)
        self.add_table_row_button = StyledButton(text="Add New Row", themes=self.themes)
        self.copy_table_row_button = StyledButton(text="Copy Selected Rows", themes=self.themes)
        self.paste_table_row_button = StyledButton(text="Paste Copied Rows", themes=self.themes)
        self.add_table_2_row_button = StyledButton(text="Add Parentship", themes=self.themes)
        self.delete_table_2_row_button = StyledButton(text="Delete Selected Parentships", themes=self.themes)
        self.create_new_model_button = StyledButton(text="Create New Model", icon_name="icon_file.svg", themes=self.themes)
        self.create_json_database_from_txt_files_button = StyledButton(text="Create Model Json file From Txt Folder", icon_name="icon_attachment.svg", themes=self.themes)
        self.open_api_model_button = StyledButton(text="Open Model", icon_name="icon_restore.svg", themes=self.themes)
        self.save_api_model_button = StyledButton(text="Save Model", icon_name="icon_save.svg", themes=self.themes)

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
        self.table_widget = PropertiesTableWidget(self.themes["app_color"])

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

        self.controller = ModelController(tree=self.tree, properties_table=self.table_widget, parents_table=self.table_widget_2)

        @Slot(str)
        def onTextChanged(text: str):
            self.controller.set_filter_text(text)
        self.filterEdit.textChanged.connect(onTextChanged)

        self.table_widget.itemChanged.connect(self.controller.save_properties_table)
        self.tree.clicked.connect(self.controller.update_properties_table)
        self.delete_table_2_row_button.clicked.connect(self.controller.delete_seleted_rows_parent)
        self.add_table_2_row_button.clicked.connect(self.controller.add_new_rows_parent)
        self.delete_table_row_button.clicked.connect(self.controller.delete_seleted_rows)
        self.add_table_row_button.clicked.connect(self.controller.add_new_rows)
        self.copy_table_row_button.clicked.connect(self.controller.copy_seleted_rows)
        self.paste_table_row_button.clicked.connect(self.controller.paste_copied_rows)

        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.controller.openMenu)

        # Model Functions
        def create_new_model():
            qm=QMessageBox()
            ret = qm.question(self.tree, '', "Are you sure to create a new model? It will reset the unsaved changes", qm.Yes | qm.No)
            if ret == qm.Yes:
                self.data = {}
                self.system_inputs = {}
                self.tree.rootModel.clear()
                self.tree.rootNode = self.tree.rootModel.invisibleRootItem()
                
                modelNode = QStandardItem("New Model")
                modelNode.setEditable(False)
                modelNode.setIcon(QIcon(Functions.set_svg_icon("icon_restore.svg")))
                modelNode.setData("model", Qt.UserRole)
                modelNode.setFlags(Qt.ItemIsDropEnabled | modelNode.flags())
                self.tree.rootNode.appendRow(modelNode)
                
                self.controller.add_node_to_tree(self.system_inputs, modelNode)
                self.controller.create_all_base_folders()
                self.controller.clear_tables()

        self.create_new_model_button.clicked.connect(create_new_model)

        # API
        def save_model_to_api():
            modelNode = self.tree.rootModel.index(0, 0)
            data = self.data | {"name": modelNode.data(Qt.DisplayRole), "SystemInputs": model_to_dict(self.tree.rootModel)}
            modelId = modelNode.data(Qt.UserRole+1)
            if modelId == None:
                modelId = create_model(data)
                self.tree.rootModel.invisibleRootItem().child(0, 0).setData(modelId, Qt.UserRole+1)
            else:
                update_model(modelId, data)

        self.save_api_model_button.clicked.connect(save_model_to_api)

        def open_model_from_api():
            dialog = OpenModelDialog()
            models = list_models()
            itemModel = QStandardItemModel()
            dialog.modelList.setModel(itemModel)
            dialog.modelList.setEditTriggers(QAbstractItemView.NoEditTriggers)
            for model in models:
                item = QStandardItem(model["name"])
                item.setData(model["id"], Qt.UserRole)
                itemModel.appendRow(item)

            def delete_model_clicked():
                selection = dialog.modelList.selectedIndexes()
                if len(selection) < 1:
                    return
                modelId = selection[0].data(Qt.UserRole)
                delete_model(modelId)
                itemModel.removeRow(selection[0].row())

            dialog.deleteModel.clicked.connect(delete_model_clicked)
            dialog.show()
            if dialog.exec_():
                selection = dialog.modelList.selectedIndexes()
                if len(selection) < 1:
                    return
                modelId = selection[0].data(Qt.UserRole)
                model = get_model(modelId)
                self.data = model
                self.system_inputs = model["SystemInputs"]
                self.tree.rootModel.clear()
                self.tree.rootNode = self.tree.rootModel.invisibleRootItem()
                
                modelNode = QStandardItem(model["name"])
                modelNode.setEditable(False)
                modelNode.setIcon(QIcon(Functions.set_svg_icon("icon_restore.svg")))
                modelNode.setData("model", Qt.UserRole) 
                modelNode.setData(modelId, Qt.UserRole+1)
                modelNode.setFlags(Qt.ItemIsDropEnabled | modelNode.flags())
                self.tree.rootNode.appendRow(modelNode)
                    
                self.controller.add_node_to_tree(self.system_inputs, modelNode)
                self.controller.clear_tables()
        
        self.open_api_model_button.clicked.connect(open_model_from_api)

        def create_json_from_txt():
            name = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.working_directory, QFileDialog.ShowDirsOnly)
            text, okPressed = QInputDialog.getText(self, "Json File Name", "Json File Name:", text="")
            if okPressed and text != '':
                data = readTxt(name, text)
                with open("data/"+ text +'.mdl', 'w') as fp:
                    json.dump(data, fp, sort_keys=True, indent=4)
        self.create_json_database_from_txt_files_button.clicked.connect(create_json_from_txt)

        self.tree.viewport().installEventFilter(self)

        # ADD WIDGETS
        self.ui.load_pages.table_button_layout.addWidget(self.add_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.delete_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.copy_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.paste_table_row_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_new_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.open_api_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.save_api_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_json_database_from_txt_files_button)
        self.ui.load_pages.tree_layout.addWidget(self.filterEdit)
        self.ui.load_pages.tree_layout.addWidget(self.tree)
        self.ui.load_pages.table_layout.addWidget(self.table_widget)
        self.ui.load_pages.parentship_table_layout.addWidget(self.table_widget_2)
        self.ui.load_pages.parentship_button_layout.addWidget(self.add_table_2_row_button)
        self.ui.load_pages.parentship_button_layout.addWidget(self.delete_table_2_row_button)
