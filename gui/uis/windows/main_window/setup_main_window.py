# ///////////////////////////////////////////////////////////////
###
#TO DO LIST
# Alphabetical & Typewise Sorting of tree view
# deleteObject Function => If the last object in a folder is deleted, the folder is deleted as well. The folder should remain
# add_node_to_tree Function => When a new folder is created, it is an empty dict. It is detected in an if statement. Maybe not the best practice?
###

from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
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
from functools import reduce 
import operator
from main import AnotherWindow
from main import ListViewOpenExistingModel
from functools import partial
import copy
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
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_widgets.svg",
            "btn_id" : "btn_widgets",
            "btn_text" : "Show Custom Widgets",
            "btn_tooltip" : "Show custom widgets",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_add_user.svg",
            "btn_id" : "btn_add_user",
            "btn_text" : "Add Users",
            "btn_tooltip" : "Add users",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_file.svg",
            "btn_id" : "btn_new_file",
            "btn_text" : "New File",
            "btn_tooltip" : "Create new file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_folder_open.svg",
            "btn_id" : "btn_open_file",
            "btn_text" : "Open File",
            "btn_tooltip" : "Open file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_save.svg",
            "btn_id" : "btn_save",
            "btn_text" : "Save File",
            "btn_tooltip" : "Save file",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_info",
            "btn_text" : "Information",
            "btn_tooltip" : "Open informations",
            "show_top" : False,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Settings",
            "btn_tooltip" : "Open settings",
            "show_top" : False,
            "is_active" : False
        }
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_search.svg",
            "btn_id" : "btn_search",
            "btn_tooltip" : "Search",
            "is_active" : False
        },
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Top settings",
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
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

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

        # BTN 1
        self.left_btn_1 = PyPushButton(
            text="Btn 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_btn_1.setMaximumHeight(40)
        self.ui.left_column.menus.btn_1_layout.addWidget(self.left_btn_1)

        # BTN 2
        self.left_btn_2 = PyPushButton(
            text="Btn With Icon",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        self.left_btn_2.setIcon(self.icon)
        self.left_btn_2.setMaximumHeight(40)
        self.ui.left_column.menus.btn_2_layout.addWidget(self.left_btn_2)

        # BTN 3 - Default QPushButton
        self.left_btn_3 = QPushButton("Default QPushButton")
        self.left_btn_3.setMaximumHeight(40)
        self.ui.left_column.menus.btn_3_layout.addWidget(self.left_btn_3)

        # PAGES
        # ///////////////////////////////////////////////////////////////

        # PAGE 1 - ADD LOGO TO MAIN PAGE
        #self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        # self.label_Kaan = QLabel() 
        #self.logo_Kaan = QPixmap(r"C:\Users\ui921788\Documents\Gui\gui\images\svg_imageslogo-removebg-preview.png")
        # self.label_Kaan.setPixmap(self.logo_Kaan)  
        # self.ui.load_pages.label_logo.setPixmap(self.logo_Kaan)
        
        # # PAGE 2
        # # CIRCULAR PROGRESS 1
        # self.circular_progress_1 = PyCircularProgress(
        #     value = 80,
        #     progress_color = self.themes["app_color"]["context_color"],
        #     text_color = self.themes["app_color"]["text_title"],
        #     font_size = 14,
        #     bg_color = self.themes["app_color"]["dark_four"]
        # )
        # self.circular_progress_1.setFixedSize(200,200)

        # # CIRCULAR PROGRESS 2
        # self.circular_progress_2 = PyCircularProgress(
        #     value = 45,
        #     progress_width = 4,
        #     progress_color = self.themes["app_color"]["context_color"],
        #     text_color = self.themes["app_color"]["context_color"],
        #     font_size = 14,
        #     bg_color = self.themes["app_color"]["bg_three"]
        # )
        # self.circular_progress_2.setFixedSize(160,160)

        # # CIRCULAR PROGRESS 3
        # self.circular_progress_3 = PyCircularProgress(
        #     value = 75,
        #     progress_width = 2,
        #     progress_color = self.themes["app_color"]["pink"],
        #     text_color = self.themes["app_color"]["white"],
        #     font_size = 14,
        #     bg_color = self.themes["app_color"]["bg_three"]
        # )
        # self.circular_progress_3.setFixedSize(140,140)

        # # PY SLIDER 1
        # self.vertical_slider_1 = PySlider(
        #     margin=8,
        #     bg_size=10,
        #     bg_radius=5,
        #     handle_margin=-3,
        #     handle_size=16,
        #     handle_radius=8,
        #     bg_color = self.themes["app_color"]["dark_three"],
        #     bg_color_hover = self.themes["app_color"]["dark_four"],
        #     handle_color = self.themes["app_color"]["context_color"],
        #     handle_color_hover = self.themes["app_color"]["context_hover"],
        #     handle_color_pressed = self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_1.setMinimumHeight(100)

        # # PY SLIDER 2
        # self.vertical_slider_2 = PySlider(
        #     bg_color = self.themes["app_color"]["dark_three"],
        #     bg_color_hover = self.themes["app_color"]["dark_three"],
        #     handle_color = self.themes["app_color"]["context_color"],
        #     handle_color_hover = self.themes["app_color"]["context_hover"],
        #     handle_color_pressed = self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_2.setMinimumHeight(100)

        # # PY SLIDER 3
        # self.vertical_slider_3 = PySlider(
        #     margin=8,
        #     bg_size=10,
        #     bg_radius=5,
        #     handle_margin=-3,
        #     handle_size=16,
        #     handle_radius=8,
        #     bg_color = self.themes["app_color"]["dark_three"],
        #     bg_color_hover = self.themes["app_color"]["dark_four"],
        #     handle_color = self.themes["app_color"]["context_color"],
        #     handle_color_hover = self.themes["app_color"]["context_hover"],
        #     handle_color_pressed = self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_3.setOrientation(Qt.Horizontal)
        # self.vertical_slider_3.setMaximumWidth(200)

        # # PY SLIDER 4
        # self.vertical_slider_4 = PySlider(
        #     bg_color = self.themes["app_color"]["dark_three"],
        #     bg_color_hover = self.themes["app_color"]["dark_three"],
        #     handle_color = self.themes["app_color"]["context_color"],
        #     handle_color_hover = self.themes["app_color"]["context_hover"],
        #     handle_color_pressed = self.themes["app_color"]["context_pressed"]
        # )
        # self.vertical_slider_4.setOrientation(Qt.Horizontal)
        # self.vertical_slider_4.setMaximumWidth(200)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_heart.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "Icon button - Heart",
            width = 40,
            height = 40,
            radius = 20,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )


        self.save_table_button = PyPushButton(
            
            text="Save Table",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("table-row-remove-svgrepo-com.svg"))
        self.save_table_button.setIcon(self.icon)
        self.save_table_button.setMaximumHeight(40)

        self.delete_table_row_button = PyPushButton(
            
            text="Delete Selected Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_save.svg"))
        self.delete_table_row_button.setIcon(self.icon)
        self.delete_table_row_button.setMaximumHeight(40)

        self.add_table_row_button = PyPushButton(
            
            text="Add New Row",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        self.add_table_row_button.setIcon(self.icon)
        self.add_table_row_button.setMaximumHeight(40)

        self.copy_table_row_button = PyPushButton(
            
            text="Copy Selected Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        self.add_table_row_button.setIcon(self.icon)
        self.add_table_row_button.setMaximumHeight(40)

        self.paste_table_row_button = PyPushButton(
            
            text="Paste Copied Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        self.add_table_row_button.setIcon(self.icon)
        self.add_table_row_button.setMaximumHeight(40)


        self.create_new_model_button = PyPushButton(
            
            text="Create New Model",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_file.svg"))
        self.create_new_model_button.setIcon(self.icon)
        self.create_new_model_button.setMaximumHeight(40)

        self.open_existing_model_button = PyPushButton(
            
            text="Open Existing Model",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_restore.svg"))
        self.open_existing_model_button.setIcon(self.icon)
        self.open_existing_model_button.setMaximumHeight(40)



        # # PUSH BUTTON 1
        # self.push_button_1 = PyPushButton(
        #     text = "Button Without Icon",
        #     radius  =8,
        #     color = self.themes["app_color"]["text_foreground"],
        #     bg_color = self.themes["app_color"]["dark_one"],
        #     bg_color_hover = self.themes["app_color"]["dark_three"],
        #     bg_color_pressed = self.themes["app_color"]["dark_four"]
        # )
        # self.push_button_1.setMinimumHeight(40)

        # # PUSH BUTTON 2
        # self.push_button_2 = PyPushButton(
        #     text = "Button With Icon",
        #     radius = 8,
        #     color = self.themes["app_color"]["text_foreground"],
        #     bg_color = self.themes["app_color"]["dark_one"],
        #     bg_color_hover = self.themes["app_color"]["dark_three"],
        #     bg_color_pressed = self.themes["app_color"]["dark_four"]
        #)
        # self.icon_2 = QIcon(Functions.set_svg_icon("icon_settings.svg"))
        # self.push_button_2.setMinimumHeight(40)
        # self.push_button_2.setIcon(self.icon_2)

        # PY LINE EDIT
        self.line_edit = PyLineEdit(
            text = "",
            place_holder_text = "Place holder text",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.line_edit.setMinimumHeight(30)

        # TOGGLE BUTTON
        self.toggle_button = PyToggle(
            width = 50,
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        # TABLE WIDGETS
        self.table_widget = PyTableWidget(
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
        self.table_widget.setColumnCount(13)
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("Parent Object")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignCenter)
        self.column_2.setText("Target Object")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignCenter)
        self.column_3.setText("Property")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignCenter)
        self.column_4.setText("Date_From")

        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignCenter)
        self.column_5.setText("Date_To")

        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignCenter)
        self.column_6.setText("Value")

        self.column_7 = QTableWidgetItem()
        self.column_7.setTextAlignment(Qt.AlignCenter)
        self.column_7.setText("Variable")

        self.column_8 = QTableWidgetItem()
        self.column_8.setTextAlignment(Qt.AlignCenter)
        self.column_8.setText("Variable_Effect")

        self.column_9 = QTableWidgetItem()
        self.column_9.setTextAlignment(Qt.AlignCenter)
        self.column_9.setText("Timeslice")

        self.column_10 = QTableWidgetItem()
        self.column_10.setTextAlignment(Qt.AlignCenter)
        self.column_10.setText("Timeslice_Index")

        self.column_11 = QTableWidgetItem()
        self.column_11.setTextAlignment(Qt.AlignCenter)
        self.column_11.setText("Group_id")

        self.column_12 = QTableWidgetItem()
        self.column_12.setTextAlignment(Qt.AlignCenter)
        self.column_12.setText("Priority")

        self.column_13 = QTableWidgetItem()
        self.column_13.setTextAlignment(Qt.AlignCenter)
        self.column_13.setText("Scenario")

        self.table_header_hash = {'Parent Object':0, "Target Object":1, "Property":2, "Date_From":3,	"Date_To":4,	"Value":5,	"Variable":6,	"Variable_Effect":7,	"Timeslice":8,	"Timeslice_Index":9,	"Group_id":10,	"Priority":11,	"Scenario":12}


        # Set column
        self.table_widget.setHorizontalHeaderItem(0, self.column_1)
        self.table_widget.setHorizontalHeaderItem(1, self.column_2)
        self.table_widget.setHorizontalHeaderItem(2, self.column_3)
        self.table_widget.setHorizontalHeaderItem(3, self.column_4)
        self.table_widget.setHorizontalHeaderItem(4, self.column_5)
        self.table_widget.setHorizontalHeaderItem(5, self.column_6)
        self.table_widget.setHorizontalHeaderItem(6, self.column_7)
        self.table_widget.setHorizontalHeaderItem(7, self.column_8)
        self.table_widget.setHorizontalHeaderItem(8, self.column_9)
        self.table_widget.setHorizontalHeaderItem(9, self.column_10)
        self.table_widget.setHorizontalHeaderItem(10, self.column_11)
        self.table_widget.setHorizontalHeaderItem(11, self.column_12)
        self.table_widget.setHorizontalHeaderItem(12, self.column_13)





        
        def add_node_to_tree(self, model_node, tree_node):
        
            for node_key in model_node:
                node = QStandardItem(node_key)
                node.setEditable(False)

                if not "Properties" in model_node[node_key]:
                    add_node_to_tree(self, model_node[node_key], node)
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


        @Slot(str)
        def onTextChanged(self, text):
            self.proxyModel.setFilterRegularExpression(text)
        

        
        model = {}


        self.tree = QTreeView()
        self.tree.setSortingEnabled(True)
        self.tree.sortByColumn(0, Qt.AscendingOrder)
        self.filterEdit = QLineEdit(self)
        self.filterEdit.textChanged.connect(lambda text: onTextChanged(self,self.filterEdit.text()))
        self.root_model = QStandardItemModel()
        self.proxyModel = QSortFilterProxyModel(
            self, recursiveFilteringEnabled=True
        )
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setSourceModel(self.root_model)
        self.tree.setModel(self.proxyModel)
        root_node = self.root_model.invisibleRootItem()

        with open("C:/Users/ui921788/Desktop/New Gui on Simon Repo/datasmall.json", 'r') as f:
            self.data = json.load(f)
            
        if "SystemInputs" in self.data:
            self.system_inputs = self.data["SystemInputs"]

            add_node_to_tree(self, self.system_inputs, root_node)


        self.currentlySelectedModelObject =[] #To keep curretly selected object branch




        def update_properties_table():
            # First determine all parent names for the selected object
            # ///////////////////////////////////////////////////////////////   
            
            tabledata = self.tree.selectedIndexes()[0].data(Qt.UserRole)
            
            if tabledata is not None:
                self.table_widget.setRowCount(len(tabledata["Properties"]))
                for i, item in enumerate(tabledata["Properties"]):
                    for key, value in self.table_header_hash.items():
                        self.table_widget.setItem(i, value, QTableWidgetItem(item[key]))

            else:
                self.table_widget.setRowCount(0)
            

        def getFromDict(dataDict, mapList):
            try:
                return reduce(operator.getitem, mapList, dataDict)
            except KeyError:
                return None

        def setInDict(dataDict, mapList, value):
            getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

        def addInDict(dataDict, mapList, key, value):
            getFromDict(dataDict, mapList)[key] = value

        def save_properties_table():
            
            getSelected = self.tree.selectedIndexes()
            keysList = getNodeNameAndParentList(getSelected)

            self.currentlySelectedModelObject = copy.deepcopy(keysList)

            setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],[])

            listofPropertiesToAppend = []
            for row in range(self.table_widget.rowCount()):
                tempDict = {}
                for column in range(self.table_widget.columnCount()):
                    try:
                        tempDict[self.table_widget.horizontalHeaderItem(column).text()]=self.table_widget.item(row, column).text()
                    except AttributeError:
                        tempDict[self.table_widget.horizontalHeaderItem(column).text()]=""
                listofPropertiesToAppend.append(tempDict)
              
            setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],listofPropertiesToAppend)
            reset_tree()

        def reset_tree():
            self.root_model.clear()
            root_node = self.root_model.invisibleRootItem()
            add_node_to_tree(self, self.system_inputs, root_node)

        self.tree.clicked.connect(update_properties_table)
        self.save_table_button.clicked.connect(save_properties_table)
        
        def delete_seleted_rows():
            indexes = self.table_widget.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.table_widget.removeRow(index.row()) 

        self.delete_table_row_button.clicked.connect(delete_seleted_rows)

        def add_new_rows():
            rowPosition = self.table_widget.rowCount()
            self.table_widget.insertRow(rowPosition)
            for column in range(self.table_widget.columnCount()):        
                self.table_widget.setItem(rowPosition, column, QTableWidgetItem(""))  

        self.add_table_row_button.clicked.connect(add_new_rows)

        self.rowsToCopy = []
        def copy_seleted_rows():
            self.rowsToCopy = []
            indexes = self.table_widget.selectionModel().selectedRows()
            for index in sorted(indexes):
                rowToCopyDict = {}
                for column in range(self.table_widget.columnCount()):
                    rowToCopyDict[self.table_widget.horizontalHeaderItem(column).text()] = self.table_widget.item(index.row(), column).text()
                self.rowsToCopy.append(copy.deepcopy(rowToCopyDict))
            

        self.copy_table_row_button.clicked.connect(copy_seleted_rows)


        def paste_copied_rows():
            rowPosition = self.table_widget.rowCount()
            for i in range(len(self.rowsToCopy)):
                self.table_widget.insertRow(rowPosition)
                
                rowToPasteDict = self.rowsToCopy[i]
                for column in range(self.table_widget.columnCount()):
                    self.table_widget.setItem(rowPosition, column, QTableWidgetItem(rowToPasteDict[self.table_widget.horizontalHeaderItem(column).text()]))  
                rowPosition = self.table_widget.rowCount()
            

        self.paste_table_row_button.clicked.connect(paste_copied_rows)

# Right click menu for Tree Widget
# ///////////////////////////////////////////////////////////////


        def openMenu(position):
            treewidgetatfocus = QApplication.focusWidget()
            selectedType = ""
            selectedItem = self.tree.selectedIndexes()[0].data(Qt.UserRole)
            
            if selectedItem == "folder":
                selectedType = "Folder"
            else:
                selectedType = "Model Object"

            menu = QMenu()

            if selectedType == "Model Object":

                qmenurenameobject = QAction("Rename Object", self)
                menu.addAction(qmenurenameobject)
                qmenucopyobject = QAction("Copy Object and its content", self)
                menu.addAction(qmenucopyobject)
                qmenupasteobject = QAction("Paste Object and its content", self)
                menu.addAction(qmenupasteobject)
                qmenudeleteobject = QAction("Delete Object and its content", self)
                menu.addAction(qmenudeleteobject)               

               
                if qmenurenameobject:
                    qmenurenameobject.triggered.connect(partial(renameObject))
                if qmenucopyobject:
                    qmenucopyobject.triggered.connect(partial(copyObject))
                if qmenupasteobject:
                    qmenupasteobject.triggered.connect(partial(pasteObject))
                if qmenudeleteobject:
                    qmenudeleteobject.triggered.connect(partial(deleteObject)) 


            elif selectedType == "Folder":

                qmenunewobject = QAction("Create a New Object under " + self.tree.selectedIndexes()[0].data(0))
                menu.addAction(qmenunewobject)
                qmenunewfolder = QAction("Create a New Folder under " + self.tree.selectedIndexes()[0].data(0))
                menu.addAction(qmenunewfolder)
                qmenurenamefolder = QAction("Rename Folder", self)
                menu.addAction(qmenurenamefolder)
                qmenucopyfolder = QAction("Copy Folder and its content", self)
                menu.addAction(qmenucopyfolder)
                
                qmenupastefolder = QAction("Paste Folder and its content", self)
                if not self.dictFolderToCopy:
                    qmenupastefolder.setEnabled(False)
                menu.addAction(qmenupastefolder)

                qmenupasteobject = QAction("Paste Folder and its content", self)
                if not self.dictObjectToCopy:
                    qmenupasteobject.setEnabled(False)
                menu.addAction(qmenupasteobject)

                qmenudeletefolder = QAction("Delete Folder and its content", self)
                menu.addAction(qmenudeletefolder)

                if qmenunewobject:
                    qmenunewobject.triggered.connect(partial(createNewObject,"from folder"))
                if qmenunewfolder:
                    qmenunewfolder.triggered.connect(partial(createNewFolder))
                if qmenudeletefolder:
                    qmenurenamefolder.triggered.connect(partial(renameFolder))
                if qmenucopyfolder:
                    qmenucopyfolder.triggered.connect(partial(copyFolder))
                if qmenupastefolder:
                    qmenupastefolder.triggered.connect(partial(pasteFolder))
                if qmenupasteobject:
                    qmenupasteobject.triggered.connect(partial(pasteObject))               
                if qmenurenamefolder:
                    qmenudeletefolder.triggered.connect(partial(deleteFolder))

            menu.exec_(treewidgetatfocus.viewport().mapToGlobal(position))

# Helping function for gettin selected nodes parents
# ///////////////////////////////////////////////////////////////

        def getNodeParentList(getSelected):
            parents = []
            for index in getSelected:
                while index.parent().isValid():
                    index = index.parent()
                    parents.append(index.sibling(index.row(), 0))
            parentObjects = [index.data() for index in parents]
            parentObjects.reverse()
            return parentObjects 

        def getNodeNameAndParentList(getSelected):
            parents = []
            for index in getSelected:
                while index.parent().isValid():
                    index = index.parent()
                    parents.append(index.sibling(index.row(), 0))
            parentObjects = [index.data() for index in parents]
            parentObjects.reverse()
            return parentObjects + [getSelected[0].data(0)]

# Functions for model object manipulation
# ///////////////////////////////////////////////////////////////

        def createNewObject(newObjectType):     #This works 28.07.2022 22:52
    
            text, okPressed = QInputDialog.getText(self, "New object name","New object name:", text="New Object")
            if okPressed and text != '':
                
                getSelected = self.tree.selectedIndexes()
                keysList = getNodeNameAndParentList(getSelected)

                newObjectDict = {"Model Id": "yarrak",
					"Object_Name": text,
					"Object_Type": keysList[0],
					"Parent Object": [],
					"Properties": []
                    }

                addInDict(self.system_inputs, keysList , text, newObjectDict)

                reset_tree()

        def deleteObject():     #This works 28.07.2022 22:52
            
            ### TODO !!! If the last object in a folder is deleted, the folder is deleted as well. The folder should remain

            qm = QMessageBox
            ret = qm.question(self,'', "Are you sure to delete object?", qm.Yes | qm.No)
            
            if ret ==  qm.Yes:
                
                getSelected = self.tree.selectedIndexes()
                deletedObjectName = getSelected[0].data(0)
                keysList=getNodeParentList(getSelected)

                getFromDict(self.system_inputs,keysList).pop(deletedObjectName, None)
                
                if not getFromDict(self.system_inputs,keysList):
                    setInDict(self.system_inputs,keysList , "")

                reset_tree()
            else:
                pass
        
        def renameObject():     #This works 28.07.2022 23:52
            getSelected = self.tree.selectedIndexes()
            keysList=getNodeParentList(getSelected)
            renamedObjectName = getSelected[0].data(0)

            text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
            if okPressed and text != '':
                getFromDict(self.system_inputs,keysList)[text] = getFromDict(self.system_inputs,keysList).pop(renamedObjectName)

            reset_tree()


        self.dictObjectToCopy = {}
        def copyObject():        #This works 28.07.2022 23:52
            getSelected = self.tree.selectedIndexes()
            self.copiedObjectName = getSelected[0].data(0)
            keysList=getNodeParentList(getSelected) + [self.copiedObjectName]
            a = getFromDict(self.system_inputs,keysList)
            self.dictObjectToCopy = copy.deepcopy(a)
            print(self.dictObjectToCopy)

        def pasteObject():
            copiedObjectName = "copy of " + self.copiedObjectName
            getSelected = self.tree.selectedIndexes()
            if getSelected[0].data(Qt.UserRole) == "folder":
                pasteUnderFolderName = getSelected[0].data(0)
                keysList=getNodeNameAndParentList(getSelected) + [copiedObjectName]
            else:
                pasteUnderFolderName = getNodeParentList(getSelected)[-1]
                keysList=getNodeParentList(getSelected) + [copiedObjectName]
                
            
            #keysList=getNodeParentList(getSelected) + [pasteUnderFolderName] + [copiedObjectName]
            
            counter = 0
            keysListCopy = keysList.copy()
            while getFromDict(self.system_inputs,keysList) is not None:
                counter+=1
                
                keysList[-1] = keysListCopy[-1] + " (" + str(counter) + ")"

            addInDict(self.system_inputs, keysList[:-1], keysList[-1], copy.deepcopy(self.dictObjectToCopy))
            print(self.system_inputs)
            reset_tree()

# Functions for folder manipulation
# ///////////////////////////////////////////////////////////////

        def createNewFolder():  #This works 28.07.2022 22:52

            text, okPressed = QInputDialog.getText(self, "New folder name","New folder name:", text="New Folder")
            if okPressed and text != '':
                getSelected = self.tree.selectedIndexes()
                keysList=getNodeNameAndParentList(getSelected)
                addInDict(self.system_inputs, keysList , text , {"":""})
                reset_tree()

        def deleteFolder():     #This works 28.07.2022 22:52
            qm = QMessageBox
            ret = qm.question(self,'', "Are you sure to delete folder and its content?", qm.Yes | qm.No)
            if ret ==  qm.Yes:
                getSelected = self.tree.selectedIndexes()
                deletedFolderName = getSelected[0].data(0)
                keysList=getNodeParentList(getSelected)

                getFromDict(self.system_inputs,keysList).pop(deletedFolderName, None)

                reset_tree()
            else:
                pass

        def renameFolder():     #This works 28.07.2022 22:52
            getSelected = self.tree.selectedIndexes()
            keysList=getNodeParentList(getSelected)
            renamedFolderName = getSelected[0].data(0)

            text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
            if okPressed and text != '':
                getFromDict(self.system_inputs,keysList)[text] = getFromDict(self.system_inputs,keysList).pop(renamedFolderName)

            reset_tree()


        self.dictFolderToCopy = {}
        self.copiedFolderName = ""

        def copyFolder():       #This works 28.07.2022 22:52
            getSelected = self.tree.selectedIndexes()
            self.copiedFolderName = getSelected[0].data(0)
            keysList=getNodeParentList(getSelected) + [self.copiedFolderName]
            a = getFromDict(self.system_inputs,keysList)
            self.dictFolderToCopy = copy.deepcopy(a)
            


        def pasteFolder():      #This works 28.07.2022 22:52
            getSelected = self.tree.selectedIndexes()
            pasteUnderFolderName = getSelected[0].data(0)
            copiedFolderName = "copy of " + self.copiedFolderName
            keysList=getNodeParentList(getSelected) + [pasteUnderFolderName] + [copiedFolderName]
            counter = 0
            keysListCopy = keysList.copy()
            while getFromDict(self.system_inputs,keysList) is not None:
                counter+=1
                
                keysList[-1] = keysListCopy[-1] + " (" + str(counter) + ")"

            setInDict(self.system_inputs, keysList, copy.deepcopy(self.dictFolderToCopy))
            
            reset_tree()


        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(openMenu)








        def pop():
            self.bok.show()
            
          
        self.bok = ListViewOpenExistingModel()
        self.create_new_model_button.clicked.connect(pop)

        def openexistingmodel(self):
    
            self.ListViewOpenExistingModelobject = ListViewOpenExistingModel()

            db = globalvars.client['deneme']
            items=[]
            for collections in db[self.collectionname].find({},{"_id":0,"Model Name":1}):
                item = collections["Model Name"]
                if item not in items:
                    items.append(item)
                    item = QListWidgetItem(item)
                    self.ListViewOpenExistingModelobject.listWidget.addItem(item)

            self.ListViewOpenExistingModelobject.show()
            self.ListViewOpenExistingModelobject.listWidget.itemClicked.connect(lambda: self.modeltimestamplistupdate(self.ListViewOpenExistingModelobject.listWidget.selectedItems()[0].text()))
            self.ListViewOpenExistingModelobject.listWidget_2.itemClicked.connect(lambda: self.modelderivedfromlabelupdate(self.ListViewOpenExistingModelobject.listWidget.selectedItems()[0].text(),self.ListViewOpenExistingModelobject.listWidget_2.selectedItems()[0].text()))

            if self.ListViewOpenExistingModelobject.exec_():
                self.treeWidget_system.clear()
                self.treeWidget_simulation.clear()
                globalvars.currentModelName = self.ListViewOpenExistingModelobject.listWidget.selectedItems()[0].text()
                globalvars.currentModelTimeStamp = self.ListViewOpenExistingModelobject.listWidget_2.selectedItems()[0].text()
                self.derivedmodelname = self.ListViewOpenExistingModelobject.listWidget.selectedItems()[0].text()
                self.derivedmodelTimeStamp = self.ListViewOpenExistingModelobject.listWidget_2.selectedItems()[0].text()
                self.readfromDB(globalvars.currentModelName, globalvars.currentModelTimeStamp)
                self.addItems2(self.treeWidget_system.invisibleRootItem())
                self.addItems1(self.treeWidget_simulation.invisibleRootItem())
            globalvars.client.close()

        # ADD WIDGETS
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_1)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_2)
        # self.ui.load_pages.row_1_layout.addWidget(self.circular_progress_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_1)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_2)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_3)
        # self.ui.load_pages.row_2_layout.addWidget(self.vertical_slider_4)
        self.ui.load_pages.row_3_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.table_button_layout.addWidget(self.add_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.delete_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.save_table_button)
        self.ui.load_pages.table_button_layout.addWidget(self.copy_table_row_button)
        self.ui.load_pages.table_button_layout.addWidget(self.paste_table_row_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_new_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.open_existing_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.row_5_layout.addWidget(self.filterEdit)
        self.ui.load_pages.row_5_layout.addWidget(self.tree)

        self.ui.load_pages.table_layout.addWidget(self.table_widget)
 
        # RIGHT COLUMN
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(Functions.set_svg_icon("icon_arrow_right.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(Functions.set_svg_icon("icon_arrow_left.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

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