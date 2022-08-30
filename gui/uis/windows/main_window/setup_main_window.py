# ///////////////////////////////////////////////////////////////
###
#TO DO LIST
# Alphabetical & Typewise Sorting of tree view
# add_node_to_tree Function => When a new folder is created, it is an empty dict. It is detected in an if statement. Maybe not the best practice?
# cutObject Function => Make object text less bold
# Pasting of cut objects => Naming should be fixed (when moved it should not be "copy of xxx") and if the same object name exist in the new folder, it should be asked to replace or skip or renamed etc..
# assignGroupByModel function => read comments
# self.ui.load_pages.parentship_button_layout.addStretch() does not work properly
# stylesheets

###

from sqlite3 import connect
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.widgets.py_tree_view.py_tree_view import PyTreeView
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
from main import AssignGroup
from functools import partial
import copy
from gui.core.create_json import readTxt
import csv

from gui.uis.windows.main_window import ui_main

from pymongo import MongoClient
import gridfs


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
            "btn_text" : "Setup Model Objects",
            "btn_tooltip" : "Setup Model Objects",
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
            self.ui.title_bar.set_title("Welcome to Fundamental Model")

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
        #self.icon = QIcon(Functions.set_svg_icon("table-row-remove-svgrepo-com.svg"))
        #self.save_table_button.setIcon(self.icon)
        self.save_table_button.setMaximumHeight(40)

        self.delete_table_row_button = PyPushButton(
            
            text="Delete Selected Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        #self.icon = QIcon(Functions.set_svg_icon("icon_save.svg"))
        #self.delete_table_row_button.setIcon(self.icon)
        self.delete_table_row_button.setMaximumHeight(40)

        self.add_table_row_button = PyPushButton(
            
            text="Add New Row",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        #self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        #self.add_table_row_button.setIcon(self.icon)
        self.add_table_row_button.setMaximumHeight(40)

        self.copy_table_row_button = PyPushButton(
            
            text="Copy Selected Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        #self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        #self.copy_table_row_button.setIcon(self.icon)
        self.copy_table_row_button.setMaximumHeight(40)

        self.paste_table_row_button = PyPushButton(
            
            text="Paste Copied Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        #self.icon = QIcon(Functions.set_svg_icon("new-line-svgrepo-com.svg"))
        #self.paste_table_row_button.setIcon(self.icon)
        self.paste_table_row_button.setMaximumHeight(40)


        self.add_table_2_row_button = PyPushButton(
            
            text="Add New Row",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )

        self.add_table_2_row_button.setMaximumHeight(40)



        self.delete_table_2_row_button = PyPushButton(
            
            text="Delete Selected Rows",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        #self.icon = QIcon(Functions.set_svg_icon("icon_save.svg"))
        #self.delete_table_row_button.setIcon(self.icon)
        self.delete_table_2_row_button.setMaximumHeight(40)



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

        self.save_model_button = PyPushButton(
            
            text="Save Model",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_save.svg"))
        self.save_model_button.setIcon(self.icon)
        self.save_model_button.setMaximumHeight(40)

        self.create_json_database_from_txt_files_button = PyPushButton(
            
            text="Create Model Json file From Txt Folder",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_attachment.svg"))
        self.create_json_database_from_txt_files_button.setIcon(self.icon)
        self.create_json_database_from_txt_files_button.setMaximumHeight(40)

        self.to_MongoBD_button = PyPushButton(
            
            text="Save Moden in Mongo",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_attachment.svg"))
        self.to_MongoBD_button.setIcon(self.icon)
        self.to_MongoBD_button.setMaximumHeight(40)


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
        self.filterEdit.setMinimumHeight(30)

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




        
        self.table_widget_2 = PyTableWidget(
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            #bg_color = self.themes["app_color"]["bg_two"],
            bg_color = "#eee",
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]

        )
        self.table_widget.setStyleSheet("background-color: #eee;")
        self.table_widget_2.setStyleSheet("background-color: #eee;")
        self.table_widget_2.setColumnCount(2)
        self.table_widget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget_2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table_widget_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.column_1_2 = QTableWidgetItem()
        self.column_1_2.setTextAlignment(Qt.AlignCenter)
        self.column_1_2.setText("Parent Object")

        self.column_2_2 = QTableWidgetItem()
        self.column_2_2.setTextAlignment(Qt.AlignCenter)
        self.column_2_2.setText("Parent Property")

       
        self.table_header_hash_2 = {'Parent Object':0, "Parent Property":1}


        # Set column
        self.table_widget_2.setHorizontalHeaderItem(0, self.column_1_2)
        self.table_widget_2.setHorizontalHeaderItem(1, self.column_2_2)







        self.expandedSet = set()
        

        
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
                
        def remove_node_from_tree(self, tree_node):
            self.root_model.removeRow(tree_node.row(), tree_node.parent())


        @Slot(str)
        def onTextChanged(self, text):
            self.proxyModel.setFilterRegularExpression(text)
        

        
        model = {}

        self.working_directory = os.getcwd() 
        self.tree = QTreeView()

        self.tree.setSortingEnabled(True)
        self.tree.sortByColumn(0, Qt.AscendingOrder)
        #self.filterEdit = QLineEdit(self)
        self.filterEdit.textChanged.connect(lambda text: onTextChanged(self,self.filterEdit.text()))
        self.root_model = QStandardItemModel()
        self.proxyModel = QSortFilterProxyModel(
            self, recursiveFilteringEnabled=True
        )
        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setSourceModel(self.root_model)
        self.tree.setModel(self.proxyModel)
        self.tree.setDragDropMode(QAbstractItemView.InternalMove)
        root_node = self.root_model.invisibleRootItem()

        with open(self.working_directory+"\\datasmall.json", 'r') as f:
            self.data = json.load(f)
            
        if "SystemInputs" in self.data:
            self.system_inputs = self.data["SystemInputs"]

            add_node_to_tree(self, self.system_inputs, root_node)
                

        self.currentlySelectedModelObject =[] #To keep curretly selected object branch



        self.properties_table_object_properties_dict= {}
        with open(self.working_directory+"\\Properties of Object Types.csv", mode='r') as infile:
            reader = csv.reader(infile)
            for rows in reader:
                self.properties_table_object_properties_dict[rows[0]] = []
            infile.seek(0)
            for rows in reader:
                self.properties_table_object_properties_dict[rows[0]].append(rows[1])             

        def deneme(row, column):
            
            def removeComboBox():
                temp = combo.currentText()
                
                self.table_widget.setItem(row, column, QTableWidgetItem(temp))
                combo.hide()

            if column == 2:
                combo = QComboBox()
                props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                combo.addItem("")
                for t in props:
                    combo.addItem(t)
                
                self.table_widget.setCellWidget(row,column,combo)
                combo.showPopup()
                combo.currentIndexChanged.connect(removeComboBox)
            else:
                pass
            




        self.table_widget.cellDoubleClicked.connect(deneme)
        


        def update_properties_table():
            # First determine all parent names for the selected object
            # ///////////////////////////////////////////////////////////////

            try:
                self.table_widget.itemChanged.disconnect()
            except (TypeError, RuntimeError):
                # was never connected;
                # PyQt raises TypeError, PySide raises RuntimeError
                print ("RuntimeError 1")
                pass
            try:
                self.table_widget_2.itemChanged.disconnect()
            except (TypeError, RuntimeError):
                # was never connected
                # PyQt raises TypeError, PySide raises RuntimeError
                print ("RuntimeError 2")
                pass

            tabledata = self.tree.selectedIndexes()[0].data(Qt.UserRole)
            
            if tabledata is not None:
                try:
                    self.table_widget.setRowCount(len(tabledata["Properties"]))
                    for i, item in enumerate(tabledata["Properties"]):
                        for key, value in self.table_header_hash.items():
                            if key == "Property":
                                combo = QComboBox()
                                props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                                for t in props:
                                    combo.addItem(t)
                                ### would the connect work for all comboboxes???
                                
                                self.table_widget.setCellWidget(i,value,combo)
                                combo.setCurrentIndex(props.index(item[key]))
                                combo.currentIndexChanged.connect(save_properties_table)
                            else:
                                self.table_widget.setItem(i, value, QTableWidgetItem(item[key]))
                                #self.table_widget.setCellWidget(i, value, QLineEdit(item[key]))
                except TypeError as e:
                    if str(e) == 'string indices must be integers':
                        pass
                    else:
                        raise


            if tabledata is not None:
                try:
                    self.table_widget_2.setRowCount(len(tabledata["Parent Objects"]))
                    for i, item in enumerate(tabledata["Parent Objects"]):
                        for key, value in self.table_header_hash_2.items():
                            if key == "Parent Object":
                                combo_2 = QComboBox()
                                props = get_all_object_names(self.root_model)
                                for t in props:
                                    combo_2.addItem(t)
                                self.table_widget_2.setCellWidget(i,value,combo_2)
                                combo_2.setCurrentIndex(props.index(item[key]))
                                combo_2.currentIndexChanged.connect(save_parent_table)
                            else:
                                it = QTableWidgetItem(item[key])
                                
                                self.table_widget_2.setItem(i, value, it)
                                #self.table_widget_2.openPersistentEditor(it)

                                #self.table_widget_2.setCellWidget(i, value, QLineEdit(item[key]))
                except TypeError as e:
                    if str(e) == 'string indices must be integers':
                        pass
                    else:
                        raise


                except Exception as e:
                    raise

            else:
                self.table_widget.setRowCount(0)
            self.table_widget.itemChanged.connect(save_properties_table)
            self.table_widget_2.itemChanged.connect(save_parent_table)

        def getFromDict(dataDict, mapList):
            try:
                return reduce(operator.getitem, mapList, dataDict)
            except KeyError:
                return None

        def setInDict(dataDict, mapList, value):
            getFromDict(dataDict, mapList[:-1])[mapList[-1]] = copy.deepcopy(value)

        def addInDict(dataDict, mapList, key, value):
            getFromDict(dataDict, mapList)[key] = copy.deepcopy(value)

        def save_properties_table():
            
            getSelected = self.tree.selectedIndexes()
            keysList = getNodeNameAndParentList(getSelected)

            self.currentlySelectedModelObject = copy.deepcopy(keysList)


            #### Following 1 line is directly changing data dict file, became obsolete with model view approach
            #setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],[])

            listofPropertiesToAppend = []
            for row in range(self.table_widget.rowCount()):
                tempDict = {}
                for column in range(self.table_widget.columnCount()):
                    try:
                        if isinstance(self.table_widget.cellWidget(row, column) , QComboBox):
                            tempDict[self.table_widget.horizontalHeaderItem(column).text()]= self.table_widget.cellWidget(row, column).currentText()
                        else:
                            #tempDict[self.table_widget.horizontalHeaderItem(column).text()]=self.table_widget.cellWidget(row, column).text()
                            tempDict[self.table_widget.horizontalHeaderItem(column).text()]= self.table_widget.item(row, column).text()
                    except AttributeError:
                        tempDict[self.table_widget.horizontalHeaderItem(column).text()]=""
                listofPropertiesToAppend.append(tempDict)
            
            #### Following 4 lines are directly changing data dict file, became obsolete with model view approach  
            #setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],listofPropertiesToAppend)
            #reset_tree()
            #add_node_to_tree(self, listofPropertiesToAppend, self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))
            #self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole)["Properties"].clear()
            ####
            
            temp = copy.deepcopy(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
            temp["Properties"].clear()
            temp["Properties"] = listofPropertiesToAppend.copy()
            self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)


        #self.table_widget.selectionModel().selectionChanged.connect(save_properties_table)
        self.table_widget.itemChanged.connect(save_properties_table)
        self.tree.clicked.connect(update_properties_table)
        self.save_table_button.clicked.connect(save_properties_table)


        def save_parent_table():
            
            getSelected = self.tree.selectedIndexes()
            keysList = getNodeNameAndParentList(getSelected)

            self.currentlySelectedModelObject = copy.deepcopy(keysList)


            #### Following 1 line is directly changing data dict file, became obsolete with model view approach
            #setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],[])

            listofParentsToAppend = []
            for row in range(self.table_widget_2.rowCount()):
                tempDict = {}
                for column in range(self.table_widget_2.columnCount()):
                    try:
                        if isinstance(self.table_widget_2.cellWidget(row, column) , QComboBox):
                            tempDict[self.table_widget_2.horizontalHeaderItem(column).text()]= self.table_widget_2.cellWidget(row, column).currentText()
                        else:
                            tempDict[self.table_widget_2.horizontalHeaderItem(column).text()]=self.table_widget_2.item(row, column).text()
                    except AttributeError:
                        tempDict[self.table_widget_2.horizontalHeaderItem(column).text()]=""
                listofParentsToAppend.append(tempDict)
            
            #### Following 4 lines are directly changing data dict file, became obsolete with model view approach  
            #setInDict(self.system_inputs,self.currentlySelectedModelObject+["Properties"],listofPropertiesToAppend)
            #reset_tree()
            #add_node_to_tree(self, listofPropertiesToAppend, self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))
            #self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole)["Properties"].clear()
            ####
            
            temp = copy.deepcopy(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
            temp["Parent Objects"].clear()
            temp["Parent Objects"] = listofParentsToAppend.copy()
            self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)

        self.table_widget_2.itemChanged.connect(save_parent_table)
        #self.table_widget_2.selectionModel().selectionChanged.connect(save_parent_table)


        def delete_seleted_rows_parent():
            indexes = self.table_widget_2.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.table_widget_2.removeRow(index.row()) 

        self.delete_table_2_row_button.clicked.connect(delete_seleted_rows_parent)

        def add_new_rows_parent():
            try:
                self.table_widget_2.itemChanged.disconnect()
            except (TypeError, RuntimeError):
                # was never connected;
                # PyQt raises TypeError, PySide raises RuntimeError
                print ("RuntimeError 1")
                pass
            rowPosition = self.table_widget_2.rowCount()
            self.table_widget_2.insertRow(rowPosition)
            for column in range(self.table_widget_2.columnCount()):
                if column == 0:
                    combo = QComboBox()
                    props = get_all_object_names(self.root_model)
                    combo.addItem("")
                    for t in props:
                        combo.addItem(t)          
                    self.table_widget_2.setCellWidget(rowPosition,column,combo)
                    combo.currentIndexChanged.connect(save_parent_table)
                else:
                    self.table_widget_2.setItem(rowPosition, column, QTableWidgetItem(""))  
            self.table_widget_2.itemChanged.connect(save_parent_table)        
        self.add_table_2_row_button.clicked.connect(add_new_rows_parent)


        # def reset_tree():
        #     iterate_tree_items_via_model_depth_first(self.tree)    
        #     self.root_model.clear()
        #     root_node = self.root_model.invisibleRootItem()
        #     add_node_to_tree(self, self.system_inputs, root_node)
        #     expand_iterate_tree_items_via_model_depth_first(self.tree)
        

        
        def delete_seleted_rows():
            indexes = self.table_widget.selectionModel().selectedRows()
            for index in sorted(indexes):
                self.table_widget.removeRow(index.row()) 

        self.delete_table_row_button.clicked.connect(delete_seleted_rows)

        def add_new_rows():
            try:
                self.table_widget.itemChanged.disconnect()
            except (TypeError, RuntimeError):
                # was never connected;
                # PyQt raises TypeError, PySide raises RuntimeError
                print ("RuntimeError 1")
                pass
            rowPosition = self.table_widget.rowCount()
            self.table_widget.insertRow(rowPosition)
            for column in range(self.table_widget.columnCount()):
                if column == 2:
                    combo = QComboBox()
                    props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                    combo.addItem("")
                    for t in props:
                        combo.addItem(t)          
                    self.table_widget.setCellWidget(rowPosition,column,combo)
                    combo.currentIndexChanged.connect(save_properties_table)
                
                elif column == 3:
                    self.table_widget.setItem(rowPosition, column, QTableWidgetItem("2000-01-01"))  
                elif column == 4:
                    self.table_widget.setItem(rowPosition, column, QTableWidgetItem("2100-01-01"))  

                else:
                    self.table_widget.setItem(rowPosition, column, QTableWidgetItem(""))  
                #self.table_widget.setCellWidget(rowPosition, column, QLineEdit(""))
            self.table_widget.itemChanged.connect(save_properties_table)
        self.add_table_row_button.clicked.connect(add_new_rows)

        self.rowsToCopy = []
        def copy_seleted_rows():
            self.rowsToCopy = []
            indexes = self.table_widget.selectionModel().selectedRows()
            for index in sorted(indexes):
                rowToCopyDict = {}
                for column in range(self.table_widget.columnCount()):
                    if column == 2:
                        rowToCopyDict[self.table_widget.horizontalHeaderItem(column).text()] = self.table_widget.cellWidget(index.row(), column).currentText()
                    else:
                        rowToCopyDict[self.table_widget.horizontalHeaderItem(column).text()] = self.table_widget.item(index.row(), column).text()
                self.rowsToCopy.append(copy.deepcopy(rowToCopyDict))
            

        self.copy_table_row_button.clicked.connect(copy_seleted_rows)


        def paste_copied_rows():
            rowPosition = self.table_widget.rowCount()
            for i in range(len(self.rowsToCopy)):
                self.table_widget.insertRow(rowPosition)
                rowToPasteDict = self.rowsToCopy[i]
                for column in range(self.table_widget.columnCount()):
                    if column == 2:
                        combo = QComboBox()
                        props = self.properties_table_object_properties_dict[self.tree.selectedIndexes()[0].data(Qt.UserRole)["Object_Type"]]
                        for t in props:
                            combo.addItem(t)
                        
                        self.table_widget.setCellWidget(rowPosition,column,combo)
                        combo.setCurrentIndex(props.index(rowToPasteDict[self.table_widget.horizontalHeaderItem(column).text()]))
                        combo.currentIndexChanged.connect(save_properties_table)

                    else:
                        self.table_widget.setItem(rowPosition, column, QTableWidgetItem(rowToPasteDict[self.table_widget.horizontalHeaderItem(column).text()]))                                            



  
                rowPosition = self.table_widget.rowCount()
            

        self.paste_table_row_button.clicked.connect(paste_copied_rows)

# Right click menu for Tree Widget
# ///////////////////////////////////////////////////////////////


        def openMenu(position):

            try:
                treewidgetatfocus = QApplication.focusWidget()
                selectedType = ""
                if self.tree.selectedIndexes():
                    selectedItem = self.tree.selectedIndexes()[0].data(Qt.UserRole)

                    if selectedItem == "folder":
                        selectedType = "Folder"
                    else:
                        selectedType = "Model Object"

                    menu = QMenu()

                    if selectedType == "Model Object":

                        qmenurenameobject = QAction("Rename Object", self)
                        menu.addAction(qmenurenameobject)
                        qmenucopyobject = QAction("Copy Object", self)
                        menu.addAction(qmenucopyobject)
                        qmenucutobject = QAction("Cut Object", self)
                        menu.addAction(qmenucutobject)
                        qmenupasteobject = QAction("Paste Object", self)
                        menu.addAction(qmenupasteobject)
                        qmenudeleteobject = QAction("Delete Object", self)
                        menu.addAction(qmenudeleteobject)
                        qmenuassigngroupbject = QAction("Assign a Group to the Object", self)
                        menu.addAction(qmenuassigngroupbject)

                        if qmenurenameobject:
                            qmenurenameobject.triggered.connect(partial(renameObjectByModel))
                        if qmenucopyobject:
                            qmenucopyobject.triggered.connect(partial(copyObjectByModel))
                        if qmenucutobject:
                            qmenucutobject.triggered.connect(partial(cutObjectByModel))
                        if qmenupasteobject:
                            qmenupasteobject.triggered.connect(partial(pasteObjectByModel))
                        if qmenudeleteobject:
                            qmenudeleteobject.triggered.connect(partial(deleteObjectByModel))
                        if qmenuassigngroupbject:
                            qmenuassigngroupbject.triggered.connect(partial(assignGroupByModel))

                    elif selectedType == "Folder":

                        qmenunewobject = QAction("Create a New Object under " + self.tree.selectedIndexes()[0].data(0))
                        menu.addAction(qmenunewobject)
                        qmenunewfolder = QAction("Create a New Folder under " + self.tree.selectedIndexes()[0].data(0))
                        menu.addAction(qmenunewfolder)
                        qmenurenamefolder = QAction("Rename Folder", self)
                        menu.addAction(qmenurenamefolder)
                        qmenucopyfolder = QAction("Copy Folder and its content", self)
                        menu.addAction(qmenucopyfolder)

                        qmenupastefolder = QAction("Paste " + self.copiedFolderName + " under " + self.tree.selectedIndexes()[0].data(0), self)
                        if not self.dictFolderToCopy:
                            qmenupastefolder.setEnabled(False)
                        menu.addAction(qmenupastefolder)

                        qmenupasteobject = QAction("Paste " + self.copiedObjectName + " under " + self.tree.selectedIndexes()[0].data(0), self)
                        if not self.dictObjectToCopy:
                            qmenupasteobject.setEnabled(False)
                        menu.addAction(qmenupasteobject)

                        qmenudeletefolder = QAction("Delete Folder and its content", self)
                        menu.addAction(qmenudeletefolder)

                        if qmenunewobject:
                            qmenunewobject.triggered.connect(partial(createNewObjectByModel))
                        if qmenunewfolder:
                            qmenunewfolder.triggered.connect(partial(createNewFolderByModel))
                        if qmenudeletefolder:
                            qmenurenamefolder.triggered.connect(partial(renameFolderByModel))
                        if qmenucopyfolder:
                            qmenucopyfolder.triggered.connect(partial(copyFolderByModel))
                        if qmenupastefolder:
                            qmenupastefolder.triggered.connect(partial(pasteFolderByModel))
                        if qmenupasteobject:
                            qmenupasteobject.triggered.connect(partial(pasteObjectByModel))
                        if qmenurenamefolder:
                            qmenudeletefolder.triggered.connect(partial(deleteFolderByModel))

                    menu.exec_(treewidgetatfocus.viewport().mapToGlobal(position))

            except IndexError as e:
                raise
            except Exception as e:
                raise


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


        self.dictFolderToCopy = {}
        self.copiedFolderName = ""
        self.isFolderCopied = False
        self.isFolderCut = False
        self.dictObjectToCopy = {}
        self.copiedObjectName = ""
        self.isObjectCopied = False
        self.isObjectCut = False

        def resetClipboard(copiedType):
            if copiedType == "Folder":
                self.isFolderCopied = True
                self.dictObjectToCopy = {}
                self.copiedObjectName = ""
                self.isObjectCopied = False
            if copiedType == "Object":
                self.isObjectCopied = True
                self.dictFolderToCopy = {}
                self.copiedFolderName = ""
                self.isFolderCopied = False

        def createNewObjectByModel():
            try:
                text, okPressed = QInputDialog.getText(self, "New object name","New object name:", text="New Object")
                if okPressed and text != '':
                    getSelected = self.tree.selectedIndexes()
                    keysList = getNodeNameAndParentList(getSelected)
                    newObjectDict = {text : {"Model Id": "yarrak",
                    "Object_Name": text,
                    "Object_Type": keysList[0],
                    "Parent Objects": [],
                    "Properties": []
                    }}

                add_node_to_tree(self, newObjectDict, self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))

            except Exception as e:
                raise



        # def createNewObject(newObjectType):     #This works 28.07.2022 22:52
    
        #     text, okPressed = QInputDialog.getText(self, "New object name","New object name:", text="New Object")
        #     if okPressed and text != '':
                
        #         getSelected = self.tree.selectedIndexes()
        #         keysList = getNodeNameAndParentList(getSelected)

        #         newObjectDict = {"Model Id": "yarrak",
		# 			"Object_Name": text,
		# 			"Object_Type": keysList[0],
		# 			"Parent Object": [],
		# 			"Properties": []
        #             }

        #         addInDict(self.system_inputs, keysList , text, newObjectDict)

        #         reset_tree()

        # def deleteObject():     #This works 28.07.2022 22:52
            
        #     ### TODO !!! If the last object in a folder is deleted, the folder is deleted as well. The folder should remain

        #     qm = QMessageBox
        #     ret = qm.question(self,'', "Are you sure to delete object?", qm.Yes | qm.No)
            
        #     if ret ==  qm.Yes:
                
        #         getSelected = self.tree.selectedIndexes()
        #         deletedObjectName = getSelected[0].data(0)
        #         keysList=getNodeParentList(getSelected)

        #         getFromDict(self.system_inputs,keysList).pop(deletedObjectName, None)
                
        #         if not getFromDict(self.system_inputs,keysList):
        #             setInDict(self.system_inputs,keysList , "")

        #         reset_tree()
        #     else:
        #         pass


        def assignGroupByModel():
            print(self.tree.selectedIndexes()[0].data(Qt.UserRole)["Parent Object"])
            getSelected = self.tree.selectedIndexes()
            self.dialogBox = AssignGroup()
            self.dialogBox.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
            
            items_obj=get_all_object_names(self.root_model)
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
                temp = copy.deepcopy(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).data(Qt.UserRole))
                temp["Parent Object"].clear()
                for selected in self.dialogBox.listWidget.selectedItems():
                    temp["Parent Object"].append(selected.text())
                self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).setData(temp, Qt.UserRole)
                

        def deleteObjectByModel():
            qm = QMessageBox
            ret = qm.question(self,'', "Are you sure to delete object?", qm.Yes | qm.No)

            if ret ==  qm.Yes:
                getSelected = self.tree.selectedIndexes()

                remove_node_from_tree(self, self.proxyModel.mapToSource(getSelected[0]))




        def renameObjectByModel():
            getSelected = self.tree.selectedIndexes()
            text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
            if okPressed and text != '':
                self.proxyModel.setData(self.tree.currentIndex(), text)

        # def renameObject():     #This works 28.07.2022 23:52
        #     getSelected = self.tree.selectedIndexes()
        #     keysList=getNodeParentList(getSelected)
        #     renamedObjectName = getSelected[0].data(0)

        #     text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
        #     if okPressed and text != '':
        #         getFromDict(self.system_inputs,keysList)[text] = getFromDict(self.system_inputs,keysList).pop(renamedObjectName)

        #     reset_tree()

        global dragStart
        def dragStart():
            getSelected = self.tree.selectedIndexes()
            if getSelected[0].data(Qt.UserRole) == "folder":
                pass  #cut folder function is to be coded
            else:
                cutObjectByModel()

        global dragEnd
        self.dragTarget = "" 
        def dragEnd(dragTarget):
            self.dragTarget = dragTarget
            pasteObjectByModel()
        
        # def copyObject():        #This works 28.07.2022 23:52
        #     getSelected = self.tree.selectedIndexes()
        #     self.copiedObjectName = getSelected[0].data(0)
        #     keysList=getNodeParentList(getSelected) + [self.copiedObjectName]
        #     a = getFromDict(self.system_inputs,keysList)
        #     self.dictObjectToCopy = copy.deepcopy(a)
        #     resetClipboard("Object")

        def copyObjectByModel():        #This works 28.07.2022 23:52
            getSelected = self.tree.selectedIndexes()
            self.copiedObjectName = getSelected[0].data(0)
            #keysList=getNodeParentList(getSelected) + [self.copiedObjectName]
            a = getSelected[0].data(Qt.UserRole)
            self.dictObjectToCopy =  copy.deepcopy(a)
            resetClipboard("Object")

        # def cutObject():
        #     getSelected = self.tree.selectedIndexes()
        #     self.copiedObjectName = getSelected[0].data(0)
        #     keysList=getNodeParentList(getSelected) + [self.copiedObjectName]
        #     a = getFromDict(self.system_inputs,keysList)
        #     self.dictObjectToCopy = copy.deepcopy(a)
        #     keysList=getNodeParentList(getSelected)
        #     getFromDict(self.system_inputs,keysList).pop(self.copiedObjectName, None)

        #     resetClipboard("Object")


        def cutObjectByModel():
            getSelected = self.tree.selectedIndexes()
            self.copiedObjectName = getSelected[0].data(0)
            #keysList=getNodeParentList(getSelected) + [self.copiedObjectName]
            a = getSelected[0].data(Qt.UserRole)
            self.dictObjectToCopy = copy.deepcopy(a)
            remove_node_from_tree(self, self.proxyModel.mapToSource(getSelected[0]))




        def copyShortcut():
            getSelected = self.tree.selectedIndexes()
            if getSelected[0].data(Qt.UserRole) == "folder":
                copyFolderByModel()
            else:
                copyObjectByModel()
        
        self.tree.short_copy_object = QShortcut(QKeySequence("Ctrl+C"),self)
        self.tree.short_copy_object.activated.connect(copyShortcut)


        # def pasteObject():
        #     if self.dragTarget == "":
        #         print("drag yok")
        #         getSelected = self.tree.selectedIndexes()

        #         if getSelected[0].data(Qt.UserRole) == "folder":
        #             pasteUnderFolderName = getSelected[0].data(0)
        #             keysList=getNodeNameAndParentList(getSelected) + [self.copiedObjectName]
        #         else:
        #             pasteUnderFolderName = getNodeParentList(getSelected)[-1]
        #             keysList=getNodeParentList(getSelected) + [self.copiedObjectName]


        #     else:
        #         print("drag bu abicim")
        #         getSelected = self.dragTarget

        #         if getSelected[0].data(Qt.UserRole) == "folder":
        #             pasteUnderFolderName = getSelected[0].data(0)
        #             keysList=getNodeNameAndParentList(getSelected) + [self.copiedObjectName]
        #         else:
        #             pasteUnderFolderName = getNodeParentList(getSelected)[-1]
        #             keysList=getNodeParentList(getSelected) + [self.copiedObjectName]



        #     copiedObjectName = "copy of " + self.copiedObjectName
            


                

        #     counter = 0
        #     keysListCopy = keysList.copy()
        #     while getFromDict(self.system_inputs,keysList) is not None:
        #         counter+=1
                
        #         keysList[-1] = keysListCopy[-1] + " (" + str(counter) + ")"

        #     addInDict(self.system_inputs, keysList[:-1], keysList[-1], copy.deepcopy(self.dictObjectToCopy))
            
            #reset_tree()


        def pasteObjectByModel():
            if self.dragTarget == "":
                print("drag yok")
                getSelected = self.tree.selectedIndexes()

                if getSelected[0].data(Qt.UserRole) == "folder":
                    pasteUnderFolderName = getSelected[0].data(0)
                    keysList=getNodeNameAndParentList(getSelected) + [self.copiedObjectName]
                else:
                    pasteUnderFolderName = getNodeParentList(getSelected)[-1]
                    keysList=getNodeParentList(getSelected) + [self.copiedObjectName]


            else:
                print("drag bu abicim")
                getSelected = self.dragTarget


            
                         

            counter = 0

            names=[]
            if getSelected[0].data(Qt.UserRole) == "folder":
                for i in range (self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).rowCount()):
                    names.append(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).child(i).data(0))
            else:
                for i in range (self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0].parent())).rowCount()):
                    names.append(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0].parent())).child(i).data(0))                

            copiedObjectName = "copy of " + self.copiedObjectName
            while copiedObjectName in names:
                
                counter+=1                
                copiedObjectName = "copy of " + self.copiedObjectName + " (" + str(counter) + ")"
                
            self.dictObjectToPaste = {copiedObjectName : self.dictObjectToCopy}

            if getSelected[0].data(Qt.UserRole) == "folder":
                add_node_to_tree(self, copy.deepcopy(self.dictObjectToPaste), self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))
            else:
                add_node_to_tree(self, copy.deepcopy(self.dictObjectToPaste), self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0].parent())))



        def pasteShortcut():
            if self.isFolderCopied == True:
                pasteFolderByModel()
            elif self.isObjectCopied == True:
                pasteObjectByModel()
            else:
                pass

        self.tree.short_copy_object = QShortcut(QKeySequence("Ctrl+V"),self)
        self.tree.short_copy_object.activated.connect(pasteShortcut)




# Functions for folder manipulation
# ///////////////////////////////////////////////////////////////

        # def createNewFolder():  #This works 28.07.2022 22:52

        #     text, okPressed = QInputDialog.getText(self, "New folder name","New folder name:", text="New Folder")
        #     if okPressed and text != '':
        #         getSelected = self.tree.selectedIndexes()
        #         keysList=getNodeNameAndParentList(getSelected)
        #         addInDict(self.system_inputs, keysList , text , {"":""})
        #         reset_tree()

        def createNewFolderByModel():  

            text, okPressed = QInputDialog.getText(self, "New folder name","New folder name:", text="New Folder")
            if okPressed and text != '':
                getSelected = self.tree.selectedIndexes()
                newObjectDict = {text : {}}       

            add_node_to_tree(self, newObjectDict, self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))



        # def deleteFolder():     #This works 28.07.2022 22:52
        #     qm = QMessageBox
        #     ret = qm.question(self,'', "Are you sure to delete folder and its content?", qm.Yes | qm.No)
        #     if ret ==  qm.Yes:
        #         getSelected = self.tree.selectedIndexes()
        #         deletedFolderName = getSelected[0].data(0)
        #         keysList=getNodeParentList(getSelected)

        #         getFromDict(self.system_inputs,keysList).pop(deletedFolderName, None)

        #         reset_tree()
        #     else:
        #         pass

        def deleteFolderByModel():     #This works 28.07.2022 22:52
            qm = QMessageBox
            ret = qm.question(self,'', "Are you sure to delete folder and its content?", qm.Yes | qm.No)
            if ret ==  qm.Yes:
                getSelected = self.tree.selectedIndexes()
                remove_node_from_tree(self, self.proxyModel.mapToSource(getSelected[0]))
            else:
                pass


        # def renameFolder():     #This works 28.07.2022 22:52
        #     getSelected = self.tree.selectedIndexes()
        #     keysList=getNodeParentList(getSelected)
        #     renamedFolderName = getSelected[0].data(0)

        #     text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
        #     if okPressed and text != '':
        #         getFromDict(self.system_inputs,keysList)[text] = getFromDict(self.system_inputs,keysList).pop(renamedFolderName)

        #     reset_tree()

        def renameFolderByModel():
            getSelected = self.tree.selectedIndexes()
            text, okPressed = QInputDialog.getText(self, "New name","New name:", text=getSelected[0].data(0))
            if okPressed and text != '':
                self.proxyModel.setData(self.tree.currentIndex(), text)


        # def copyFolder():       #This works 28.07.2022 22:52
        #     getSelected = self.tree.selectedIndexes()
        #     self.copiedFolderName = getSelected[0].data(0)
        #     keysList=getNodeParentList(getSelected) + [self.copiedFolderName]
        #     a = getFromDict(self.system_inputs,keysList)
        #     self.dictFolderToCopy = copy.deepcopy(a)
        #     resetClipboard("Folder")

        def copyFolderByModel():       #This works 28.07.2022 22:52
            getSelected = self.tree.selectedIndexes()
            self.copiedFolderName = getSelected[0].data(0)
            #### The folder node is identified and send to a modification model_to_dict function
            a = model_to_dict_1(self.root_model.indexFromItem(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0]))), self.root_model)
            self.dictFolderToCopy = copy.deepcopy(a[self.copiedFolderName])
            resetClipboard("Folder")



        # def pasteFolder():      #This works 28.07.2022 22:52

        #     copiedFolderName = "copy of " + self.copiedFolderName
        #     getSelected = self.tree.selectedIndexes()
        #     if getSelected[0].data(Qt.UserRole) == "folder":
        #         pasteUnderFolderName = getSelected[0].data(0)
        #         keysList=getNodeNameAndParentList(getSelected) + [copiedFolderName]
        #     else:
        #         pasteUnderFolderName = getNodeParentList(getSelected)[-1]
        #         keysList=getNodeParentList(getSelected) + [copiedFolderName]

        #     counter = 0
        #     keysListCopy = keysList.copy()
        #     while getFromDict(self.system_inputs,keysList) is not None:
        #         counter+=1
                
        #         keysList[-1] = keysListCopy[-1] + " (" + str(counter) + ")"

        #     setInDict(self.system_inputs, keysList, copy.deepcopy(self.dictFolderToCopy))
            
        #     reset_tree()


        def pasteFolderByModel():      #This works 28.07.2022 22:52

            copiedFolderName = "copy of " + self.copiedFolderName
            getSelected = self.tree.selectedIndexes()
            # if getSelected[0].data(Qt.UserRole) == "folder":
            #     pasteUnderFolderName = getSelected[0].data(0)
            #     keysList=getNodeNameAndParentList(getSelected) + [copiedFolderName]
            # else:
            #     pasteUnderFolderName = getNodeParentList(getSelected)[-1]
            #     keysList=getNodeParentList(getSelected) + [copiedFolderName]

            counter = 0
            #keysListCopy = keysList.copy()
            names=[]
            for i in range (self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).rowCount()):
                names.append(self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])).child(i).data(0))

            while copiedFolderName in names:
                counter+=1
                
                copiedFolderName = "copy of " + self.copiedFolderName + " (" + str(counter) + ")"
                
            self.dictFolderToPaste = {copiedFolderName : self.dictFolderToCopy}
            add_node_to_tree(self, copy.deepcopy(self.dictFolderToPaste), self.root_model.itemFromIndex(self.proxyModel.mapToSource(getSelected[0])))




        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(openMenu)


        #//////////////////
        # Following first 2 functions are keeping track of and the second 2 are re-establishing the current expansion status of the treeview
        

        # def iterate_tree_items_via_model_depth_first(tree_obj):
        #     model = tree_obj.model()
        #     absolute_row = [-1]
        #     for row in range(model.rowCount()):
        #         for column in range(model.columnCount()):
        #             item = model.index(row, column)
        #             if column == 0:
        #                 absolute_row[0] += 1
        #         if self.tree.isExpanded(item):
        #             self.expandedSet.add(item.data(0))    
                    
        #         _iterate_items_via_model_depth_first(model.index(row, 0), model, absolute_row)


        # def _iterate_items_via_model_depth_first(parent_item, model, absolute_row):
        #     for row in range(model.rowCount(parent_item)):
        #         for column in range(model.columnCount(parent_item)):
        #             item = model.index(row, column, parent_item)
        #             if column == 0:
        #                 absolute_row[0] += 1
        #         if self.tree.isExpanded(item):
        #             self.expandedSet.add(item.data(0))  

        #         item_0 = model.index(row, column, parent_item)
        #         if model.hasChildren(item_0):
        #             _iterate_items_via_model_depth_first(item_0, model, absolute_row)



        # def expand_iterate_tree_items_via_model_depth_first(tree_obj):
        #     model = tree_obj.model()
        #     absolute_row = [-1]
        #     for row in range(model.rowCount()):
        #         for column in range(model.columnCount()):
        #             item = model.index(row, column)
        #             if column == 0:
        #                 absolute_row[0] += 1
        #         if item.data(0) in self.expandedSet:
        #             self.tree.expand(item)    
                    
        #         _expand_iterate_items_via_model_depth_first(model.index(row, 0), model, absolute_row)


        # def _expand_iterate_items_via_model_depth_first(parent_item, model, absolute_row):
        #     for row in range(model.rowCount(parent_item)):
        #         for column in range(model.columnCount(parent_item)):
        #             item = model.index(row, column, parent_item)
        #             if column == 0:
        #                 absolute_row[0] += 1
        #         if item.data(0) in self.expandedSet:
        #             self.tree.expand(item)  

        #         item_0 = model.index(row, column, parent_item)
        #         if model.hasChildren(item_0):
        #             _expand_iterate_items_via_model_depth_first(item_0, model, absolute_row)




        def save_model_to_MongoBD():
    
            try:
                self.data["SystemInputs"] = model_to_dict(self.root_model)
                client = MongoClient("127.0.0.1", 27017)
                db = client['DB_Fundamental']
                fs = gridfs.GridFS(db)
                a = fs.put(self.data["SystemInputs"])
            except Exception as e:
                raise

        self.to_MongoBD_button.clicked.connect(save_model_to_MongoBD)



        def file_save():

            try:
                name = QFileDialog.getSaveFileName(self, 'Save File')

                self.data["SystemInputs"] = model_to_dict(self.root_model)

                with open(name[0]+'.mdl', 'w') as fp:
                    json.dump(self.data, fp, sort_keys=True, indent=4)

            except Exception as e:
                raise

        self.save_model_button.clicked.connect(file_save)


        def fill_dict_from_model(parent_index, d, model):

            ################ Kaan: I dont like the following quick fix for the main folders, but this might change in future anyways

            if model.rowCount(parent_index) == 0:
                if parent_index.data(Qt.UserRole) == "folder":
                    if parent_index.data() in d: 
                        d[parent_index.data()][model.index(0, 0).data(0)] = {}
                    else:
                        d[parent_index.data()] = {} 
            else:
            ################
            
                for i in range(model.rowCount(parent_index)):
                    ix = model.index(i, 0, parent_index)

                    
                    if model.index(i, 0, parent_index).data(Qt.UserRole) == "folder":
                        if parent_index.data() in d: 
                            d[parent_index.data()][model.index(i, 0, parent_index).data(0)] = {}
                        else:
                            d[parent_index.data()] = {} 
                    else:
                        if parent_index.data() in d:
                            d[parent_index.data()][model.index(i, 0, parent_index).data(0)] =  model.index(i, 0, parent_index).data(Qt.UserRole)
                        else:
                            d[parent_index.data()] = {model.index(i, 0, parent_index).data(0) :  model.index(i, 0, parent_index).data(Qt.UserRole)}


                    fill_dict_from_model(ix, d[parent_index.data()], model)
            
            

        def model_to_dict(model):

            d = dict()
            for i in range(model.rowCount()):
                ix = model.index(i, 0)
                fill_dict_from_model(ix, d, model)

            return d


        def model_to_dict_1(ix, model):
            d = dict()
            fill_dict_from_model(ix, d, model)    
            return d


        def _get_all_object_names(parent_index, d, model):
    
            
                for i in range(model.rowCount(parent_index)):
                    ix = model.index(i, 0, parent_index)

                    
                    if model.index(i, 0, parent_index).data(Qt.UserRole) == "folder":
                        pass
                    else:

                        d.append(model.index(i, 0, parent_index).data(0))


                    _get_all_object_names(ix, d, model)

        def get_all_object_names(model):
    
            d = list()
            for i in range(model.rowCount()):
                ix = model.index(i, 0)
                _get_all_object_names(ix, d, model)

            return d

        def file_open():
            name = QFileDialog.getOpenFileName(self, 'Open File')
            if name != ('',''):
                with open(name[0], 'r') as f:
                    self.data = json.load(f)
                    if "SystemInputs" in self.data:
                        self.system_inputs = self.data["SystemInputs"]
                        self.root_model.clear()
                        root_node = self.root_model.invisibleRootItem()
                        add_node_to_tree(self, self.system_inputs, root_node)
            else:
                pass    
        self.open_existing_model_button.clicked.connect(file_open)


        def create_json_from_txt():
            name = QFileDialog.getExistingDirectory(None, 'Select a folder:', self.working_directory, QFileDialog.ShowDirsOnly)


            text, okPressed = QInputDialog.getText(self, "Json File Name","Json File Name:", text="")
            if okPressed and text != '':
                aaa=readTxt(name, text)
                with open("data/"+ text +'.mdl', 'w') as fp:
                    json.dump(aaa, fp, sort_keys=True, indent=4)

        self.create_json_database_from_txt_files_button.clicked.connect(create_json_from_txt)        



        def create_new_model():
            qm=QMessageBox()
            ret = qm.question(self,'', "Are you sure to create a new model? It will reset the unsaved changes", qm.Yes | qm.No)
            if ret == qm.Yes:

                with open(os.path.dirname(sys.argv[0]) + "/objecttypes.json", 'r') as f:
                    self.data = json.load(f)
                    if "SystemInputs" in self.data:
                        self.system_inputs = self.data["SystemInputs"]
                        self.root_model.clear()
                        root_node = self.root_model.invisibleRootItem()
                        add_node_to_tree(self, self.system_inputs, root_node)
            else:
                pass

        self.tree.viewport().installEventFilter(self)




        def pop():
            self.bok.show()
            
          
        self.bok = ListViewOpenExistingModel()
        self.create_new_model_button.clicked.connect(create_new_model)

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
        self.ui.load_pages.row_3_layout.addWidget(self.save_model_button)
        self.ui.load_pages.row_3_layout.addWidget(self.create_json_database_from_txt_files_button)
        self.ui.load_pages.row_3_layout.addWidget(self.to_MongoBD_button)
        #self.ui.load_pages.row_3_layout.addWidget(self.toggle_button)
        #self.ui.load_pages.row_4_layout.addWidget(self.line_edit)
        self.ui.load_pages.tree_layout.addWidget(self.filterEdit)
        self.ui.load_pages.tree_layout.addWidget(self.tree)

        self.ui.load_pages.table_layout.addWidget(self.table_widget)
        self.ui.load_pages.parentship_table_layout.addWidget(self.table_widget_2)

        self.ui.load_pages.parentship_button_layout.addWidget(self.add_table_2_row_button)

        self.ui.load_pages.parentship_button_layout.addWidget(self.delete_table_2_row_button)
        
        self.ui.load_pages.parentship_button_layout.addStretch()

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

