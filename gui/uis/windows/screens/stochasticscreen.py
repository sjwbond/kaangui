# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stochasticscreen.ui'
#
# Created: Mon Jun 20 12:03:52 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

class Ui_StochasticsScreen(QObject):
    dataSaved = Signal(dict)

    default_input = {
            "outage_patterns": 1,
            "weibull_shape_parameter": 3,
            "samples_per_pattern": 5,
            "stochastic_samples": 1,
            "reduced_samples": 0,
            "reduction_relative_accuracy": 99,
            "forced_outages_in_lookahead": False,
            "efor_maintenance_adjust": False,
            "outage_method": "Normal",
            "automatically_schedule": "All",
            "convergence_period_type": ""
    }
    input = default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1091, 828)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stochastic_samples_label = QLabel(self.groupBox_4)
        self.stochastic_samples_label.setObjectName("stochastic_samples_label")
        self.gridLayout_2.addWidget(self.stochastic_samples_label, 0, 0, 1, 1)
        self.stochastic_samples_spinBox = QSpinBox(self.groupBox_4)
        self.stochastic_samples_spinBox.setMaximum(10000)
        self.stochastic_samples_spinBox.setProperty("value", 1)
        self.stochastic_samples_spinBox.setObjectName("stochastic_samples_spinBox")
        self.gridLayout_2.addWidget(self.stochastic_samples_spinBox, 0, 1, 1, 1)
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 2)
        self.reduced_samples_spinBox = QSpinBox(self.groupBox_4)
        self.reduced_samples_spinBox.setObjectName("reduced_samples_spinBox")
        self.gridLayout_2.addWidget(self.reduced_samples_spinBox, 3, 1, 1, 1)
        self.reduction_relative_accuracy_spinBox = QSpinBox(self.groupBox_4)
        self.reduction_relative_accuracy_spinBox.setProperty("value", 100)
        self.reduction_relative_accuracy_spinBox.setObjectName("reduction_relative_accuracy_spinBox")
        self.gridLayout_2.addWidget(self.reduction_relative_accuracy_spinBox, 4, 1, 1, 1)
        self.reduction_relative_accuracy_label = QLabel(self.groupBox_4)
        self.reduction_relative_accuracy_label.setObjectName("reduction_relative_accuracy_label")
        self.gridLayout_2.addWidget(self.reduction_relative_accuracy_label, 4, 0, 1, 1)
        self.reduced_samples_label = QLabel(self.groupBox_4)
        self.reduced_samples_label.setObjectName("reduced_samples_label")
        self.gridLayout_2.addWidget(self.reduced_samples_label, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_7 = QGridLayout(self.groupBox_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.outage_patterns_label = QLabel(self.groupBox_5)
        self.outage_patterns_label.setObjectName("outage_patterns_label")
        self.gridLayout_7.addWidget(self.outage_patterns_label, 0, 0, 1, 1)
        self.outage_patterns_spinBox = QSpinBox(self.groupBox_5)
        self.outage_patterns_spinBox.setProperty("value", 1)
        self.outage_patterns_spinBox.setObjectName("outage_patterns_spinBox")
        self.gridLayout_7.addWidget(self.outage_patterns_spinBox, 0, 1, 1, 2)
        self.label_6 = QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 1, 0, 1, 3)
        self.total_samples_simulated_label = QLabel(self.groupBox_5)
        font = QFont()
        font.setBold(True)
        self.total_samples_simulated_label.setFont(font)
        self.total_samples_simulated_label.setObjectName("total_samples_simulated_label")
        self.gridLayout_7.addWidget(self.total_samples_simulated_label, 2, 0, 1, 1)
        self.one_label = QLabel(self.groupBox_5)
        font = QFont()
        font.setBold(True)
        self.one_label.setFont(font)
        self.one_label.setObjectName("one_label")
        self.gridLayout_7.addWidget(self.one_label, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 0, 0, 1, 1)
        self.automatically_schedule_groupBox = QGroupBox(self.groupBox_2)
        self.automatically_schedule_groupBox.setObjectName("automatically_schedule_groupBox")
        self.verticalLayout = QVBoxLayout(self.automatically_schedule_groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.all_radioButton = QRadioButton(self.automatically_schedule_groupBox)
        self.all_radioButton.setChecked(True)
        self.all_radioButton.setObjectName("all_radioButton")
        self.verticalLayout.addWidget(self.all_radioButton)
        self.forced_only_radioButton = QRadioButton(self.automatically_schedule_groupBox)
        self.forced_only_radioButton.setObjectName("forced_only_radioButton")
        self.verticalLayout.addWidget(self.forced_only_radioButton)
        self.maintenance_only_radioButton = QRadioButton(self.automatically_schedule_groupBox)
        self.maintenance_only_radioButton.setObjectName("maintenance_only_radioButton")
        self.verticalLayout.addWidget(self.maintenance_only_radioButton)
        self.planned_only_radioButton = QRadioButton(self.automatically_schedule_groupBox)
        self.planned_only_radioButton.setObjectName("planned_only_radioButton")
        self.verticalLayout.addWidget(self.planned_only_radioButton)
        self.gridLayout_4.addWidget(self.automatically_schedule_groupBox, 1, 0, 1, 1)
        self.outage_method_groupBox = QGroupBox(self.groupBox_2)
        self.outage_method_groupBox.setObjectName("outage_method_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.outage_method_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.normal_radioButton = QRadioButton(self.outage_method_groupBox)
        self.normal_radioButton.setChecked(True)
        self.normal_radioButton.setObjectName("normal_radioButton")
        self.verticalLayout_2.addWidget(self.normal_radioButton)
        self.convergent_radioButton = QRadioButton(self.outage_method_groupBox)
        self.convergent_radioButton.setObjectName("convergent_radioButton")
        self.verticalLayout_2.addWidget(self.convergent_radioButton)
        self.gridLayout_4.addWidget(self.outage_method_groupBox, 2, 0, 1, 1)
        self.groupBox_8 = QGroupBox(self.groupBox_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.samples_per_pattern_label = QLabel(self.groupBox_8)
        self.samples_per_pattern_label.setEnabled(False)
        self.samples_per_pattern_label.setObjectName("samples_per_pattern_label")
        self.gridLayout_5.addWidget(self.samples_per_pattern_label, 0, 0, 1, 2)
        self.samples_per_pattern_spinBox = QSpinBox(self.groupBox_8)
        self.samples_per_pattern_spinBox.setEnabled(False)
        self.samples_per_pattern_spinBox.setMaximum(1000)
        self.samples_per_pattern_spinBox.setProperty("value", 5)
        self.samples_per_pattern_spinBox.setObjectName("samples_per_pattern_spinBox")
        self.gridLayout_5.addWidget(self.samples_per_pattern_spinBox, 0, 2, 1, 2)
        self.convergence_period_type_label = QLabel(self.groupBox_8)
        self.convergence_period_type_label.setEnabled(False)
        self.convergence_period_type_label.setObjectName("convergence_period_type_label")
        self.gridLayout_5.addWidget(self.convergence_period_type_label, 1, 0, 1, 1)
        self.day_radioButton = QRadioButton(self.groupBox_8)
        self.day_radioButton.setEnabled(False)
        self.day_radioButton.setObjectName("day_radioButton")
        self.gridLayout_5.addWidget(self.day_radioButton, 1, 1, 1, 1)
        self.week_radioButton = QRadioButton(self.groupBox_8)
        self.week_radioButton.setEnabled(False)
        self.week_radioButton.setObjectName("week_radioButton")
        self.gridLayout_5.addWidget(self.week_radioButton, 1, 2, 1, 2)
        self.month_radioButton = QRadioButton(self.groupBox_8)
        self.month_radioButton.setEnabled(False)
        self.month_radioButton.setObjectName("month_radioButton")
        self.gridLayout_5.addWidget(self.month_radioButton, 1, 4, 1, 1)
        self.year_radioButton = QRadioButton(self.groupBox_8)
        self.year_radioButton.setEnabled(False)
        self.year_radioButton.setObjectName("year_radioButton")
        self.gridLayout_5.addWidget(self.year_radioButton, 1, 5, 1, 1)
        self.weibull_shape_parameter_label = QLabel(self.groupBox_8)
        self.weibull_shape_parameter_label.setObjectName("weibull_shape_parameter_label")
        self.gridLayout_5.addWidget(self.weibull_shape_parameter_label, 2, 0, 1, 3)
        self.weibull_shape_parameter_spinBox = QSpinBox(self.groupBox_8)
        self.weibull_shape_parameter_spinBox.setProperty("value", 3)
        self.weibull_shape_parameter_spinBox.setObjectName("weibull_shape_parameter_spinBox")
        self.gridLayout_5.addWidget(self.weibull_shape_parameter_spinBox, 2, 3, 1, 2)
        self.forced_outages_in_lookahead_checkBox = QCheckBox(self.groupBox_8)
        self.forced_outages_in_lookahead_checkBox.setObjectName("forced_outages_in_lookahead_checkBox")
        self.gridLayout_5.addWidget(self.forced_outages_in_lookahead_checkBox, 3, 0, 1, 5)
        self.efor_maintenance_adjust_checkBox = QCheckBox(self.groupBox_8)
        self.efor_maintenance_adjust_checkBox.setObjectName("efor_maintenance_adjust_checkBox")
        self.gridLayout_5.addWidget(self.efor_maintenance_adjust_checkBox, 4, 0, 1, 4)
        self.gridLayout_4.addWidget(self.groupBox_8, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.buttonBox = QDialogButtonBox(self.groupBox_3)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_6.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)

        self.stochastic_samples_spinBox.valueChanged.connect(self.maxOfSamples)
        self.reduced_samples_spinBox.valueChanged.connect(self.maxOfSamples)
        self.outage_patterns_spinBox.valueChanged.connect(self.maxOfSamples)

        self.normal_radioButton.clicked.connect(self.outageMethodHide)
        self.convergent_radioButton.clicked.connect(self.outageMethodHide)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)



        btn = self.buttonBox.button(QDialogButtonBox.Ok)
        btn.clicked.connect(self.saveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.Cancel)
        btn.clicked.connect(self.dontsaveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.RestoreDefaults)
        btn.clicked.connect(self.restoredefaults)

    def saveandclose(self):
        self.savestochasticsscreen()

    def dontsaveandclose(self):
        pass

    def restoredefaults(self):
        self.input = self.default_input
        self.loadstochasticsscreen()
        self.outageMethodHide()
    
    def setInput(self, input):
        self.input = self.default_input | input
        self.loadstochasticsscreen()
        self.outageMethodHide()
    
    def getOutput(self):
        return self.output

    def loadstochasticsscreen(self):
        self.outage_patterns_spinBox.setValue(self.input["outage_patterns"])
        self.weibull_shape_parameter_spinBox.setValue(self.input["weibull_shape_parameter"])
        self.samples_per_pattern_spinBox.setValue(self.input["samples_per_pattern"])
        self.stochastic_samples_spinBox.setValue(self.input["stochastic_samples"])
        self.reduced_samples_spinBox.setValue(self.input["reduced_samples"])
        self.reduction_relative_accuracy_spinBox.setValue(self.input["reduction_relative_accuracy"])
        self.forced_outages_in_lookahead_checkBox.setChecked(self.input["forced_outages_in_lookahead"])
        self.efor_maintenance_adjust_checkBox.setChecked(self.input["efor_maintenance_adjust"])
        
        self.normal_radioButton.setChecked(self.input["outage_method"] == "Normal")
        self.convergent_radioButton.setChecked(self.input["outage_method"] == "Convergent")

        self.all_radioButton.setChecked(self.input["automatically_schedule"] == "All")
        self.forced_only_radioButton.setChecked(self.input["automatically_schedule"] == "Forced Only")
        self.maintenance_only_radioButton.setChecked(self.input["automatically_schedule"] == "Maintenance Only")
        self.planned_only_radioButton.setChecked(self.input["automatically_schedule"] == "Planned Only")

        self.day_radioButton.setChecked(self.input["convergence_period_type"] == "Day")
        self.week_radioButton.setChecked(self.input["convergence_period_type"] == "Week")
        self.month_radioButton.setChecked(self.input["convergence_period_type"] == "Month")
        self.year_radioButton.setChecked(self.input["convergence_period_type"] == "Year")

    def savestochasticsscreen(self):
        self.output = {
            "outage_patterns": self.outage_patterns_spinBox.value(),
            "weibull_shape_parameter": self.weibull_shape_parameter_spinBox.value(),
            "samples_per_pattern": self.samples_per_pattern_spinBox.value(),
            "stochastic_samples": self.stochastic_samples_spinBox.value(),
            "reduced_samples": self.reduced_samples_spinBox.value(),
            "reduction_relative_accuracy": self.reduction_relative_accuracy_spinBox.value(),
            "forced_outages_in_lookahead": self.forced_outages_in_lookahead_checkBox.isChecked(),
            "efor_maintenance_adjust": self.efor_maintenance_adjust_checkBox.isChecked()
        }

        if self.normal_radioButton.isChecked():
            self.output["outage_method"] = "Normal"
        if self.convergent_radioButton.isChecked():
            self.output["outage_method"] = "Convergent"

        if self.all_radioButton.isChecked():
            self.output["automatically_schedule"] = "All"
        if self.forced_only_radioButton.isChecked():
            self.output["automatically_schedule"] = "Forced Only"
        if self.maintenance_only_radioButton.isChecked():
            self.output["automatically_schedule"] = "Maintenance Only"
        if self.planned_only_radioButton.isChecked():
            self.output["automatically_schedule"] = "Planned Only"

        if self.day_radioButton.isChecked():
            self.output["convergence_period_type"] = "Day"
        if self.week_radioButton.isChecked():
            self.output["convergence_period_type"] = "Week"
        if self.month_radioButton.isChecked():
            self.output["convergence_period_type"] = "Month"
        if self.year_radioButton.isChecked():
            self.output["convergence_period_type"] = "Year"

        self.dataSaved.emit(self.output)

    def maxOfSamples(self):
        if self.reduced_samples_spinBox.value() == 0:
            self.one_label.setText(str(max(self.stochastic_samples_spinBox.value(),self.outage_patterns_spinBox.value())))
        else:
            self.one_label.setText(str(max(self.reduced_samples_spinBox.value(),self.outage_patterns_spinBox.value())))

    def outageMethodHide(self):
        if self.normal_radioButton.isChecked() == True:
            self.samples_per_pattern_label.setEnabled(False)
            self.samples_per_pattern_spinBox.setEnabled(False)
            self.convergence_period_type_label.setEnabled(False)
            self.day_radioButton.setEnabled(False)
            self.week_radioButton.setEnabled(False)
            self.month_radioButton.setEnabled(False)
            self.year_radioButton.setEnabled(False)
            self.weibull_shape_parameter_spinBox.setEnabled(True)
            self.weibull_shape_parameter_label.setEnabled(True)

        if self.convergent_radioButton.isChecked() == True:
            self.samples_per_pattern_label.setEnabled(True)
            self.samples_per_pattern_spinBox.setEnabled(True)
            self.convergence_period_type_label.setEnabled(True)
            self.day_radioButton.setEnabled(True)
            self.week_radioButton.setEnabled(True)
            self.month_radioButton.setEnabled(True)
            self.year_radioButton.setEnabled(True)
            self.weibull_shape_parameter_spinBox.setEnabled(False)
            self.weibull_shape_parameter_label.setEnabled(False)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.stochastic_samples_label.setText(QApplication.translate("Form", "Stochastic Samples:"))
        self.label_2.setText(QApplication.translate("Form", "This is the number of samples drawn for each Vabiable object\n"
" in the simulation"))
        self.reduction_relative_accuracy_label.setText(QApplication.translate("Form", "Reduction Relative Accuracy"))
        self.reduced_samples_label.setText(QApplication.translate("Form", "Reduced Samples:"))
        self.outage_patterns_label.setText(QApplication.translate("Form", "Outage Patterns:"))
        self.label_6.setText(QApplication.translate("Form", "This is the number of patterns of forced outages and maintenance\n"
" outages drawn for the simulation"))
        self.total_samples_simulated_label.setText(QApplication.translate("Form", "Total Samples Simulated:"))
        self.one_label.setText(QApplication.translate("Form", "1"))
        self.automatically_schedule_groupBox.setTitle(QApplication.translate("Form", "Automatically Schedule"))
        self.all_radioButton.setText(QApplication.translate("Form", "All"))
        self.forced_only_radioButton.setText(QApplication.translate("Form", "Forced Only"))
        self.maintenance_only_radioButton.setText(QApplication.translate("Form", "Maintenance Only"))
        self.planned_only_radioButton.setText(QApplication.translate("Form", "Planned Only"))
        self.outage_method_groupBox.setTitle(QApplication.translate("Form", "Outage Method"))
        self.normal_radioButton.setText(QApplication.translate("Form", "Normal"))
        self.convergent_radioButton.setText(QApplication.translate("Form", "Convergent"))
        self.groupBox_8.setTitle(QApplication.translate("Form", "GroupBox"))
        self.samples_per_pattern_label.setText(QApplication.translate("Form", "Sample per Pattern:"))
        self.convergence_period_type_label.setText(QApplication.translate("Form", "Convergence Period Type:"))
        self.day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.month_radioButton.setText(QApplication.translate("Form", "Month"))
        self.year_radioButton.setText(QApplication.translate("Form", "Year"))
        self.weibull_shape_parameter_label.setText(QApplication.translate("Form", "Weibull Shape Parameter:"))
        self.forced_outages_in_lookahead_checkBox.setText(QApplication.translate("Form", "Forced Outages in Lookahead"))
        self.efor_maintenance_adjust_checkBox.setText(QApplication.translate("Form", "EFOR Maintenance Adjust"))
