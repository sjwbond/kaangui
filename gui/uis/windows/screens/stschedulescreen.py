# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stschedulescreen.ui'
#
# Created: Thu Jun 23 10:10:38 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

class Ui_STScheduleScreen(QObject):
    dataSaved = Signal(dict)

    default_input = {
        "discount_rate": 0,
        "discount_period": "Week",
        "end_effects_method": "Perpetuity",
        "heat_rate": "Detailed",
        "transmission_detail": "Nodal",
        "stochastic_method": "Independent Samples (Sequential)"
    }
    input = default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1117, 740)
        self.gridLayout_5 = QGridLayout(Form)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.transmission_detail_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transmission_detail_groupBox.sizePolicy().hasHeightForWidth())
        self.transmission_detail_groupBox.setSizePolicy(sizePolicy)
        self.transmission_detail_groupBox.setObjectName("transmission_detail_groupBox")
        self.gridLayout_4 = QGridLayout(self.transmission_detail_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.regional_radioButton = QRadioButton(self.transmission_detail_groupBox)
        self.regional_radioButton.setObjectName("radioButton")
        self.gridLayout_4.addWidget(self.regional_radioButton, 0, 0, 1, 1)
        self.zonal_radioButton = QRadioButton(self.transmission_detail_groupBox)
        self.zonal_radioButton.setObjectName("zonal_radioButton")
        self.gridLayout_4.addWidget(self.zonal_radioButton, 0, 1, 1, 1)
        self.nodal_radioButton = QRadioButton(self.transmission_detail_groupBox)
        self.nodal_radioButton.setChecked(True)
        self.nodal_radioButton.setObjectName("nodal_radioButton")
        self.gridLayout_4.addWidget(self.nodal_radioButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.transmission_detail_groupBox)
        self.heat_rate_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heat_rate_groupBox.sizePolicy().hasHeightForWidth())
        self.heat_rate_groupBox.setSizePolicy(sizePolicy)
        self.heat_rate_groupBox.setObjectName("heat_rate_groupBox")
        self.gridLayout_3 = QGridLayout(self.heat_rate_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.detailed_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.detailed_radioButton.setChecked(True)
        self.detailed_radioButton.setObjectName("detailed_radioButton")
        self.gridLayout_3.addWidget(self.detailed_radioButton, 0, 0, 1, 1)
        self.simple_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simple_radioButton.setObjectName("simple_radioButton")
        self.gridLayout_3.addWidget(self.simple_radioButton, 0, 1, 1, 1)
        self.simplest_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simplest_radioButton.setObjectName("simplest_radioButton")
        self.gridLayout_3.addWidget(self.simplest_radioButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.heat_rate_groupBox)
        self.stochastic_method_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stochastic_method_groupBox.sizePolicy().hasHeightForWidth())
        self.stochastic_method_groupBox.setSizePolicy(sizePolicy)
        self.stochastic_method_groupBox.setObjectName("stochastic_method_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.stochastic_method_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.deterministic_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.deterministic_radioButton.setObjectName("deterministic_radioButton")
        self.verticalLayout_2.addWidget(self.deterministic_radioButton)
        self.independant_samples_sequential_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_sequential_radioButton.setChecked(True)
        self.independant_samples_sequential_radioButton.setObjectName("independant_samples_sequential_radioButton")
        self.verticalLayout_2.addWidget(self.independant_samples_sequential_radioButton)
        self.independant_samples_parallel_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_parallel_radioButton.setObjectName("independant")
        self.verticalLayout_2.addWidget(self.independant_samples_parallel_radioButton)
        self.scenariowise_decomposition_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.scenariowise_decomposition_radioButton.setObjectName("scenariowise_decomposition_radioButton")
        self.verticalLayout_2.addWidget(self.scenariowise_decomposition_radioButton)
        self.verticalLayout.addWidget(self.stochastic_method_groupBox)
        self.discounting_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discounting_groupBox.sizePolicy().hasHeightForWidth())
        self.discounting_groupBox.setSizePolicy(sizePolicy)
        self.discounting_groupBox.setObjectName("discounting_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.discounting_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QGroupBox(self.discounting_groupBox)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.discount_rate_spinBox = QSpinBox(self.groupBox_6)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discount_rate_spinBox.sizePolicy().hasHeightForWidth())
        self.discount_rate_spinBox.setSizePolicy(sizePolicy)
        self.discount_rate_spinBox.setObjectName("discount_rate_spinBox")
        self.gridLayout.addWidget(self.discount_rate_spinBox, 0, 2, 1, 1)
        self.discount_rate_label = QLabel(self.groupBox_6)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discount_rate_label.sizePolicy().hasHeightForWidth())
        self.discount_rate_label.setSizePolicy(sizePolicy)
        self.discount_rate_label.setObjectName("label")
        self.gridLayout.addWidget(self.discount_rate_label, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.end_effects_method_label = QLabel(self.discounting_groupBox)
        self.end_effects_method_label.setObjectName("end_effects_method_label")
        self.verticalLayout_3.addWidget(self.end_effects_method_label)
        self.groupBox_7 = QGroupBox(self.discounting_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.none_radioButton = QRadioButton(self.groupBox_7)
        self.none_radioButton.setObjectName("none_radioButton")
        self.horizontalLayout_5.addWidget(self.none_radioButton)
        self.perpetuity_radioButton = QRadioButton(self.groupBox_7)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.perpetuity_radioButton.sizePolicy().hasHeightForWidth())
        self.perpetuity_radioButton.setSizePolicy(sizePolicy)
        self.perpetuity_radioButton.setChecked(True)
        self.perpetuity_radioButton.setObjectName("perpetuity_radioButton")
        self.horizontalLayout_5.addWidget(self.perpetuity_radioButton)
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.discount_period_label = QLabel(self.discounting_groupBox)
        self.discount_period_label.setObjectName("discount_period_label")
        self.verticalLayout_3.addWidget(self.discount_period_label)
        self.groupBox_8 = QGroupBox(self.discounting_groupBox)
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_2 = QGridLayout(self.groupBox_8)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.hour_radioButton = QRadioButton(self.groupBox_8)
        self.hour_radioButton.setObjectName("hour_radioButton")
        self.gridLayout_2.addWidget(self.hour_radioButton, 0, 0, 1, 1)
        self.day_radioButton = QRadioButton(self.groupBox_8)
        self.day_radioButton.setObjectName("day_radioButton")
        self.gridLayout_2.addWidget(self.day_radioButton, 0, 1, 1, 1)
        self.week_radioButton = QRadioButton(self.groupBox_8)
        self.week_radioButton.setChecked(True)
        self.week_radioButton.setObjectName("week_radioButton")
        self.gridLayout_2.addWidget(self.week_radioButton, 0, 2, 1, 1)
        self.month_radioButton = QRadioButton(self.groupBox_8)
        self.month_radioButton.setObjectName("month_radioButton")
        self.gridLayout_2.addWidget(self.month_radioButton, 0, 3, 1, 1)
        self.year_radioButton = QRadioButton(self.groupBox_8)
        self.year_radioButton.setObjectName("year_radioButton")
        self.gridLayout_2.addWidget(self.year_radioButton, 0, 4, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_8)
        self.verticalLayout.addWidget(self.discounting_groupBox)
        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_9 = QGroupBox(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy)
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_6 = QGridLayout(self.groupBox_9)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.buttonBox = QDialogButtonBox(self.groupBox_9)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_6.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_9, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)



        QMetaObject.connectSlotsByName(Form)
        btn = self.buttonBox.button(QDialogButtonBox.Ok)
        btn.clicked.connect(self.saveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.Cancel)
        btn.clicked.connect(self.dontsaveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.RestoreDefaults)
        btn.clicked.connect(self.restoredefaults)

    def saveandclose(self):
        self.savestschedulescreen()

    def dontsaveandclose(self):
        pass

    def restoredefaults(self):
        self.input = self.default_input
        self.loadstschedulescreen()
    
    def setInput(self, input):
        self.input = self.default_input | input
        self.loadstschedulescreen()
    
    def getOutput(self):
        return self.output


    def loadstschedulescreen(self):
        self.discount_rate_spinBox.setValue(self.input["discount_rate"])

        self.hour_radioButton.setChecked(self.input["discount_period"] == "Hour")
        self.day_radioButton.setChecked(self.input["discount_period"] == "Day")
        self.week_radioButton.setChecked(self.input["discount_period"] == "Week")
        self.month_radioButton.setChecked(self.input["discount_period"] == "Month")
        self.year_radioButton.setChecked(self.input["discount_period"] == "Year")

        self.none_radioButton.setChecked(self.input["end_effects_method"] == "None")
        self.perpetuity_radioButton.setChecked(self.input["end_effects_method"] == "Perpetuity")

        self.detailed_radioButton.setChecked(self.input["heat_rate"] == "Detailed")
        self.simple_radioButton.setChecked(self.input["heat_rate"] == "Simple")
        self.simplest_radioButton.setChecked(self.input["heat_rate"] == "Simplest")

        self.regional_radioButton.setChecked(self.input["transmission_detail"] == "Regional")
        self.zonal_radioButton.setChecked(self.input["transmission_detail"] == "Zonal")
        self.nodal_radioButton.setChecked(self.input["transmission_detail"] == "Nodal")

        self.deterministic_radioButton.setChecked(self.input["stochastic_method"] == "Deterministic")
        self.independant_samples_sequential_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Sequential)")
        self.independant_samples_parallel_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Parallel)")
        self.scenariowise_decomposition_radioButton.setChecked(self.input["stochastic_method"] == "Scenario-wise Decomposition")

    def savestschedulescreen(self):
        self.output = {
            "discount_rate": self.discount_rate_spinBox.value()
        }

        if self.hour_radioButton.isChecked():
            self.output["discount_period"] = "Hour"
        if self.day_radioButton.isChecked():
            self.output["discount_period"] = "Day"
        if self.week_radioButton.isChecked():
            self.output["discount_period"] = "Week"
        if self.month_radioButton.isChecked():
            self.output["discount_period"] = "Month"
        if self.year_radioButton.isChecked():
            self.output["discount_period"] = "Year"

        if self.none_radioButton.isChecked():
            self.output["end_effects_method"] = "None"
        if self.perpetuity_radioButton.isChecked():
            self.output["end_effects_method"] = "Perpetuity"

        if self.detailed_radioButton.isChecked():
            self.output["heat_rate"] = "Detailed"
        if self.simple_radioButton.isChecked():
            self.output["heat_rate"] = "Simple"
        if self.simplest_radioButton.isChecked():
            self.output["heat_rate"] = "Simplest"

        if self.regional_radioButton.isChecked():
            self.output["transmission_detail"] = "Regional"
        if self.zonal_radioButton.isChecked():
            self.output["transmission_detail"] = "Zonal"
        if self.nodal_radioButton.isChecked():
            self.output["transmission_detail"] = "Nodal"

        if self.deterministic_radioButton.isChecked():
            self.output["stochastic_method"] = "Deterministic"
        if self.independant_samples_sequential_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Sequential)"
        if self.independant_samples_parallel_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Parallel)"
        if self.scenariowise_decomposition_radioButton.isChecked():
            self.output["stochastic_method"] = "Scenario-wise Decomposition"

        self.dataSaved.emit(self.output)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.transmission_detail_groupBox.setTitle(QApplication.translate("Form", "Transmission Detail"))
        self.regional_radioButton.setText(QApplication.translate("Form", "Regional"))
        self.zonal_radioButton.setText(QApplication.translate("Form", "Zonal"))
        self.nodal_radioButton.setText(QApplication.translate("Form", "Nodal"))
        self.heat_rate_groupBox.setTitle(QApplication.translate("Form", "Heat Rate"))
        self.detailed_radioButton.setText(QApplication.translate("Form", "Detailed"))
        self.simple_radioButton.setText(QApplication.translate("Form", "Simple"))
        self.simplest_radioButton.setText(QApplication.translate("Form", "Simplest"))
        self.stochastic_method_groupBox.setTitle(QApplication.translate("Form", "Stochastic Method"))
        self.deterministic_radioButton.setText(QApplication.translate("Form", "Deterministic"))
        self.independant_samples_sequential_radioButton.setText(QApplication.translate("Form", "Independent Samples (Sequential)"))
        self.independant_samples_parallel_radioButton.setText(QApplication.translate("Form", "Independent Samples (Parallel)"))
        self.scenariowise_decomposition_radioButton.setText(QApplication.translate("Form", "Scenario-wise Decomposition"))
        self.discounting_groupBox.setTitle(QApplication.translate("Form", "Discounting"))
        self.discount_rate_label.setText(QApplication.translate("Form", "Discount Rate (%)"))
        self.end_effects_method_label.setText(QApplication.translate("Form", "End Effects Method"))
        self.none_radioButton.setText(QApplication.translate("Form", "None"))
        self.perpetuity_radioButton.setText(QApplication.translate("Form", "Perpetuity"))
        self.discount_period_label.setText(QApplication.translate("Form", "Discount Period"))
        self.hour_radioButton.setText(QApplication.translate("Form", "Hour"))
        self.day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.month_radioButton.setText(QApplication.translate("Form", "Month"))
        self.year_radioButton.setText(QApplication.translate("Form", "Year"))

