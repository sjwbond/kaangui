# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openexistingmodel2.ui'
#
# Created: Thu May  5 15:14:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

class Ui_Dialog_Open_Existing_Model(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(846, 460)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QRect(420, 410, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setGeometry(QRect(20, 20, 241, 361))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QListWidget(Dialog)
        self.listWidget_2.setGeometry(QRect(280, 20, 256, 361))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(570, 20, 161, 31))
        font = QFont()
        font.setPointSize(11)
        #font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(570, 60, 241, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QObject.connect(self.buttonBox, SIGNAL("accepted()"), Dialog.accept)
        QObject.connect(self.buttonBox, SIGNAL("rejected()"), Dialog.reject)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QApplication.translate("Dialog", "Model Derived From:", None))
        self.label_2.setText(QApplication.translate("Dialog", "", None))

