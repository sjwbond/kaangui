# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_model.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenModelDialog(object):
    def setupUi(self, OpenModelDialog):
        OpenModelDialog.setObjectName("OpenModelDialog")
        OpenModelDialog.resize(736, 482)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(OpenModelDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(OpenModelDialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.modelList = QtWidgets.QListView(OpenModelDialog)
        self.modelList.setObjectName("modelList")
        self.verticalLayout.addWidget(self.modelList)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(OpenModelDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.versionList = QtWidgets.QListView(OpenModelDialog)
        self.versionList.setObjectName("versionList")
        self.verticalLayout_3.addWidget(self.versionList)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenModelDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(OpenModelDialog)
        self.buttonBox.accepted.connect(OpenModelDialog.accept)
        self.buttonBox.rejected.connect(OpenModelDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenModelDialog)

    def retranslateUi(self, OpenModelDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenModelDialog.setWindowTitle(_translate("OpenModelDialog", "Open Model"))
        self.label.setText(_translate("OpenModelDialog", "Models"))
        self.label_2.setText(_translate("OpenModelDialog", "History"))

