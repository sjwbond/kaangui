# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lrmc_models.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from qt_core import *


lrmc_models_default_input = {
    "Locational Granularity": "Region",
    "Optimisation Granularity": "Year",
    "Feature Binning Periodicity": "Month",
    "Feature Bins Per Period": 6
}

settings = {
    "Location Granularities": ["Region", "Country", "Continent"],
    "Types": ["Year", "Month", "Week", "Day"]
}


class Ui_LRMCModels(QObject):
    def setupUi(self, Dialog):
        Dialog.setObjectName("LRMCModels")
        Dialog.resize(900, 600)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.locationalGranularityLabel = QLabel(Dialog)
        self.locationalGranularityLabel.setObjectName("locationalGranularityLabel")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.locationalGranularityLabel)
        self.locationalGranularityComboBox = QComboBox(Dialog)
        self.locationalGranularityComboBox.setObjectName("locationalGranularityComboBox")
        self.locationalGranularityComboBox.addItems(settings["Location Granularities"])
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.locationalGranularityComboBox)
        self.optimisationGranularityLabel = QLabel(Dialog)
        self.optimisationGranularityLabel.setObjectName("optimisationGranularityLabel")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.optimisationGranularityLabel)
        self.optimisationGranularityComboBox = QComboBox(Dialog)
        self.optimisationGranularityComboBox.setObjectName("optimisationGranularityComboBox")
        self.optimisationGranularityComboBox.addItems(settings["Types"])
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.optimisationGranularityComboBox)
        self.featureBinningPeriodicityLabel = QLabel(Dialog)
        self.featureBinningPeriodicityLabel.setObjectName("featureBinningPeriodicityLabel")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.featureBinningPeriodicityLabel)
        self.featureBinningPeriodicityComboBox = QComboBox(Dialog)
        self.featureBinningPeriodicityComboBox.setObjectName("featureBinningPeriodicityComboBox")
        self.featureBinningPeriodicityComboBox.addItems(settings["Types"])
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.featureBinningPeriodicityComboBox)
        self.featureBinsPerPeriodLabel = QLabel(Dialog)
        self.featureBinsPerPeriodLabel.setObjectName("featureBinsPerPeriodLabel")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.featureBinsPerPeriodLabel)
        self.featureBinsPerPeriodSpinBox = QSpinBox(Dialog)
        self.featureBinsPerPeriodSpinBox.setMaximum(10000)
        self.featureBinsPerPeriodSpinBox.setObjectName("featureBinsPerPeriodSpinBox")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.featureBinsPerPeriodSpinBox)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LRMC Model"))
        self.locationalGranularityLabel.setText(_translate("Dialog", "Locational Granularity"))
        self.optimisationGranularityLabel.setText(_translate("Dialog", "Optimisation Granularity"))
        self.featureBinningPeriodicityLabel.setText(_translate("Dialog", "Feature Binning Periodicity"))
        self.featureBinsPerPeriodLabel.setText(_translate("Dialog", "Feature Bins Per Period"))

    def setInput(self, input):
        self.input = input
        self.locationalGranularityComboBox.setCurrentText(self.input["Locational Granularity"])
        self.optimisationGranularityComboBox.setCurrentText(self.input["Optimisation Granularity"])
        self.featureBinningPeriodicityComboBox.setCurrentText(self.input["Feature Binning Periodicity"])
        self.featureBinsPerPeriodSpinBox.setValue(self.input["Feature Bins Per Period"])
    
    def getOutput(self):
        output = {
            "Locational Granularity": self.locationalGranularityComboBox.currentText(),
            "Optimisation Granularity": self.optimisationGranularityComboBox.currentText(),
            "Feature Binning Periodicity": self.featureBinningPeriodicityComboBox.currentText(),
            "Feature Bins Per Period": self.featureBinsPerPeriodSpinBox.value()
        }
        return output