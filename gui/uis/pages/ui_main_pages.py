# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pagesuBSlRl.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1_layout = QHBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        
        self.results_list_layout = QVBoxLayout()
        self.results_list_layout.setObjectName(u"results_list_layout")
        self.page_1_layout.addLayout(self.results_list_layout)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        # self.row_5_layout = QVBoxLayout()
        # self.row_5_layout.setObjectName(u"row_5_layout")

        # self.verticalLayout.addLayout(self.row_5_layout)

        self.row_5_layout = QHBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")
        
        self.tree_layout = QVBoxLayout()
        self.tree_layout.setObjectName(u"tree_layout")

        self.row_5_layout.addLayout(self.tree_layout)



        self.parentship_layout = QVBoxLayout()
        self.parentship_layout.setObjectName(u"parentship_layout")

        self.parentship_button_layout = QHBoxLayout()
        self.parentship_button_layout.setObjectName(u"parentship_button_layout")
        

        
        self.parentship_layout.addLayout(self.parentship_button_layout)


        self.parentship_table_layout = QVBoxLayout()
        self.parentship_table_layout.setObjectName(u"parentship_table_layout")

        self.parentship_layout.addLayout(self.parentship_table_layout)


        self.row_5_layout.addLayout(self.parentship_layout)




        self.verticalLayout.addLayout(self.row_5_layout)


        self.row_6_layout = QHBoxLayout()
        self.row_6_layout.setObjectName(u"row_6_layout")
        self.table_button_layout = QVBoxLayout()
        self.table_button_layout.setObjectName(u"table_button_layout")

        self.row_6_layout.addLayout(self.table_button_layout)

        self.table_layout = QVBoxLayout()
        self.table_layout.setObjectName(u"table_layout")

        self.row_6_layout.addLayout(self.table_layout)


        self.verticalLayout.addLayout(self.row_6_layout)



        self.row_7_layout = QHBoxLayout()
        self.row_7_layout.setObjectName(u"row_7_layout")
        self.table_button_layout_2 = QVBoxLayout()
        self.table_button_layout_2.setObjectName(u"table_button_layout_2")

        self.row_7_layout.addLayout(self.table_button_layout_2)

        self.table_layout_2 = QVBoxLayout()
        self.table_layout_2.setObjectName(u"table_layout_2")

        self.row_7_layout.addLayout(self.table_layout_2)


        self.verticalLayout.addLayout(self.row_7_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")

        self.row_9_layout = QHBoxLayout()
        self.row_9_layout.setObjectName(u"row_9_layout")

        self.page_3_layout.addLayout(self.row_9_layout)

        self.row_8_layout = QHBoxLayout()
        self.row_8_layout.setObjectName(u"row_8_layout")

        self.page_3_layout.addLayout(self.row_8_layout)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Model Objects", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here a new  or a previously saved model can be loaded and modified\n"
"The top tree view displays all the objects of the model. The below table object displays selected object properties in detail", None))
    # retranslateUi

