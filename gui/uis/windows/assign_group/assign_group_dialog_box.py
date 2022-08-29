# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerIWlzyq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_Dialog_Assign_Group(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(744, 486)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")

        self.horizontalLayout_2.addWidget(self.label_1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.horizontalLayout.addWidget(self.listWidget_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_1.setText(QCoreApplication.translate("Dialog", u"Parent Object", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Parent Property", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Add Parent Object", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Delete Row", None))
    # retranslateUi

