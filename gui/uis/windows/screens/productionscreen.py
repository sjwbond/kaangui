# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productionscreen.ui'
#
# Created: Fri Jul 22 14:13:15 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

production_default_input = {
    "group_generators_by_power_station": True,
    "rounding_up_threshold": 0,
    "self_tune": False,
    "rounding_up_start": 0.0,
    "rounding_up_end": 0.0,
    "rounding_up_increment": 0.0,
    "capacity_factor_threshold": 0,
    "capacity_factor_error_threshold": 0,
    "precision": 0,
    "max_tranches": 10,
    "formulate_additional_unit_commitment_constraints_upfront": True,
    "formulate_ramp_constrains_upfront": True,
    "unit_commitment_optimality": "Linear",
    "heat_rates_nonconvexities": "Warn Adjust Report Adjusted",
    "start_cost_method": "Optimize",
    "capacity_factor_refers_to": "Installed Capacity",
    "integers_in_lookahead": "Auto"
}

class Ui_ProductionScreen(QObject):
    input = production_default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1070, 830)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.start_cost_method_groupBox = QGroupBox(self.groupBox)
        self.start_cost_method_groupBox.setObjectName("start_cost_method_groupBox")
        self.gridLayout_8 = QGridLayout(self.start_cost_method_groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.optimize_radioButton = QRadioButton(self.start_cost_method_groupBox)
        self.optimize_radioButton.setChecked(True)
        self.optimize_radioButton.setObjectName("optimize_radioButton")
        self.gridLayout_8.addWidget(self.optimize_radioButton, 0, 0, 1, 1)
        self.calculate_radioButton = QRadioButton(self.start_cost_method_groupBox)
        self.calculate_radioButton.setObjectName("calculate_radioButton")
        self.gridLayout_8.addWidget(self.calculate_radioButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.start_cost_method_groupBox, 6, 0, 1, 1)
        self.rounding_up_threshold_groupBox = QGroupBox(self.groupBox)
        self.rounding_up_threshold_groupBox.setEnabled(True)
        self.rounding_up_threshold_groupBox.setObjectName("rounding_up_threshold_groupBox")
        self.gridLayout_4 = QGridLayout(self.rounding_up_threshold_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.increment_label = QLabel(self.rounding_up_threshold_groupBox)
        self.increment_label.setEnabled(False)
        self.increment_label.setObjectName("increment_label")
        self.gridLayout_4.addWidget(self.increment_label, 5, 0, 2, 1)
        self.rounding_up_threshold_horizontalSlider = QSlider(self.rounding_up_threshold_groupBox)
        self.rounding_up_threshold_horizontalSlider.setEnabled(False)
        self.rounding_up_threshold_horizontalSlider.setMaximum(100)
        self.rounding_up_threshold_horizontalSlider.setOrientation(Qt.Horizontal)
        self.rounding_up_threshold_horizontalSlider.setObjectName("rounding_up_threshold_horizontalSlider")
        self.gridLayout_4.addWidget(self.rounding_up_threshold_horizontalSlider, 0, 0, 1, 2)
        self.self_tune_checkBox = QCheckBox(self.rounding_up_threshold_groupBox)
        self.self_tune_checkBox.setEnabled(False)
        self.self_tune_checkBox.setObjectName("self_tune_checkBox")
        self.gridLayout_4.addWidget(self.self_tune_checkBox, 1, 0, 1, 1)
        self.end_label = QLabel(self.rounding_up_threshold_groupBox)
        self.end_label.setEnabled(False)
        self.end_label.setObjectName("end_label")
        self.gridLayout_4.addWidget(self.end_label, 4, 0, 1, 1)
        self.zero_label = QLabel(self.rounding_up_threshold_groupBox)
        self.zero_label.setObjectName("zero_label")
        self.gridLayout_4.addWidget(self.zero_label, 0, 2, 1, 1)
        self.start_label = QLabel(self.rounding_up_threshold_groupBox)
        self.start_label.setEnabled(False)
        self.start_label.setObjectName("start_label")
        self.gridLayout_4.addWidget(self.start_label, 3, 0, 1, 1)
        self.rounding_up_start_doubleSpinbox = QDoubleSpinBox(self.rounding_up_threshold_groupBox)
        self.rounding_up_start_doubleSpinbox.setEnabled(False)
        self.rounding_up_start_doubleSpinbox.setSingleStep(0.01)
        self.rounding_up_start_doubleSpinbox.setObjectName("rounding_up_start_doubleSpinbox")
        self.gridLayout_4.addWidget(self.rounding_up_start_doubleSpinbox, 3, 1, 1, 1)
        self.rounding_up_end_doubleSpinbox = QDoubleSpinBox(self.rounding_up_threshold_groupBox)
        self.rounding_up_end_doubleSpinbox.setEnabled(False)
        self.rounding_up_end_doubleSpinbox.setSingleStep(0.01)
        self.rounding_up_end_doubleSpinbox.setObjectName("rounding_up_end_doubleSpinbox")
        self.gridLayout_4.addWidget(self.rounding_up_end_doubleSpinbox, 4, 1, 1, 1)
        self.rounding_up_increment_doubleSpinbox = QDoubleSpinBox(self.rounding_up_threshold_groupBox)
        self.rounding_up_increment_doubleSpinbox.setEnabled(False)
        self.rounding_up_increment_doubleSpinbox.setSingleStep(0.01)
        self.rounding_up_increment_doubleSpinbox.setObjectName("rounding_up_increment_doubleSpinbox")
        self.gridLayout_4.addWidget(self.rounding_up_increment_doubleSpinbox, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.rounding_up_threshold_groupBox, 1, 0, 1, 1)
        self.capacity_factor_groupBox = QGroupBox(self.groupBox)
        self.capacity_factor_groupBox.setObjectName("capacity_factor_groupBox")
        self.gridLayout_7 = QGridLayout(self.capacity_factor_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.installed_capacity_radioButton = QRadioButton(self.capacity_factor_groupBox)
        self.installed_capacity_radioButton.setChecked(True)
        self.installed_capacity_radioButton.setObjectName("installed_capacity_radioButton")
        self.gridLayout_7.addWidget(self.installed_capacity_radioButton, 0, 0, 1, 1)
        self.rated_capacity_radioButton = QRadioButton(self.capacity_factor_groupBox)
        self.rated_capacity_radioButton.setObjectName("rated_capacity_radioButton")
        self.gridLayout_7.addWidget(self.rated_capacity_radioButton, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.capacity_factor_groupBox, 5, 0, 1, 1)
        self.integers_in_lookahead_groupBox = QGroupBox(self.groupBox)
        self.integers_in_lookahead_groupBox.setObjectName("integers_in_lookahead_groupBox")
        self.gridLayout_6 = QGridLayout(self.integers_in_lookahead_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.never_radioButton = QRadioButton(self.integers_in_lookahead_groupBox)
        self.never_radioButton.setObjectName("never_radioButton")
        self.gridLayout_6.addWidget(self.never_radioButton, 0, 0, 1, 1)
        self.auto_radioButton = QRadioButton(self.integers_in_lookahead_groupBox)
        self.auto_radioButton.setChecked(True)
        self.auto_radioButton.setObjectName("auto_radioButton")
        self.gridLayout_6.addWidget(self.auto_radioButton, 0, 1, 1, 1)
        self.always_radioButton = QRadioButton(self.integers_in_lookahead_groupBox)
        self.always_radioButton.setObjectName("always_radioButton")
        self.gridLayout_6.addWidget(self.always_radioButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.integers_in_lookahead_groupBox, 3, 0, 1, 1)
        self.dynamic_program_radioButton = QGroupBox(self.groupBox)
        self.dynamic_program_radioButton.setObjectName("dynamic_program_radioButton")
        self.gridLayout_5 = QGridLayout(self.dynamic_program_radioButton)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.capacity_factor_threshold_label = QLabel(self.dynamic_program_radioButton)
        self.capacity_factor_threshold_label.setObjectName("capacity_factor_threshold_label")
        self.gridLayout_5.addWidget(self.capacity_factor_threshold_label, 0, 0, 1, 1)
        self.capacity_factor_threshold_spinBox = QSpinBox(self.dynamic_program_radioButton)
        self.capacity_factor_threshold_spinBox.setObjectName("capacity_factor_threshold_spinBox")
        self.gridLayout_5.addWidget(self.capacity_factor_threshold_spinBox, 0, 1, 1, 1)
        self.capacity_factor_error_threshold_label = QLabel(self.dynamic_program_radioButton)
        self.capacity_factor_error_threshold_label.setObjectName("capacity_factor_error_threshold_label")
        self.gridLayout_5.addWidget(self.capacity_factor_error_threshold_label, 1, 0, 1, 1)
        self.capacity_factor_error_threshold_spinBox = QSpinBox(self.dynamic_program_radioButton)
        self.capacity_factor_error_threshold_spinBox.setObjectName("capacity_factor_error_threshold_spinBox")
        self.gridLayout_5.addWidget(self.capacity_factor_error_threshold_spinBox, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.dynamic_program_radioButton, 2, 0, 1, 1)
        self.group_generators_by_power_station_checkBox = QCheckBox(self.groupBox)
        self.group_generators_by_power_station_checkBox.setChecked(True)
        self.group_generators_by_power_station_checkBox.setObjectName("group_generators_by_power_station_checkBox")
        self.gridLayout_2.addWidget(self.group_generators_by_power_station_checkBox, 4, 0, 1, 1)
        self.formulate_additional_unit_commitment_constraints_upfront_checkBox = QCheckBox(self.groupBox)
        self.formulate_additional_unit_commitment_constraints_upfront_checkBox.setChecked(True)
        self.formulate_additional_unit_commitment_constraints_upfront_checkBox.setObjectName("formulate_additional_unit_commitment_constraints_upfront_checkBox")
        self.gridLayout_2.addWidget(self.formulate_additional_unit_commitment_constraints_upfront_checkBox, 7, 0, 1, 1)
        self.formulate_ramp_constrains_upfront_checkBox = QCheckBox(self.groupBox)
        self.formulate_ramp_constrains_upfront_checkBox.setChecked(True)
        self.formulate_ramp_constrains_upfront_checkBox.setObjectName("formulate_ramp_constrains_upfront_checkBox")
        self.gridLayout_2.addWidget(self.formulate_ramp_constrains_upfront_checkBox, 8, 0, 1, 1)
        self.unit_commitment_optimally_groupBox = QGroupBox(self.groupBox)
        self.unit_commitment_optimally_groupBox.setObjectName("unit_commitment_optimally_groupBox")
        self.gridLayout_3 = QGridLayout(self.unit_commitment_optimally_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.linear_radioButton = QRadioButton(self.unit_commitment_optimally_groupBox)
        self.linear_radioButton.setChecked(True)
        self.linear_radioButton.setObjectName("linear_radioButton")
        self.gridLayout_3.addWidget(self.linear_radioButton, 0, 0, 1, 1)
        self.rounded_relaxation_radioButton = QRadioButton(self.unit_commitment_optimally_groupBox)
        self.rounded_relaxation_radioButton.setObjectName("rounded_relaxation_radioButton")
        self.gridLayout_3.addWidget(self.rounded_relaxation_radioButton, 1, 0, 1, 1)
        self.integer_radioButton = QRadioButton(self.unit_commitment_optimally_groupBox)
        self.integer_radioButton.setObjectName("integer_radioButton")
        self.gridLayout_3.addWidget(self.integer_radioButton, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.unit_commitment_optimally_groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_9 = QGridLayout(self.groupBox_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.piecewise_linear_approximation_groupBox = QGroupBox(self.groupBox_2)
        self.piecewise_linear_approximation_groupBox.setObjectName("piecewise_linear_approximation_groupBox")
        self.gridLayout_10 = QGridLayout(self.piecewise_linear_approximation_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.precision_label = QLabel(self.piecewise_linear_approximation_groupBox)
        self.precision_label.setObjectName("precision_label")
        self.gridLayout_10.addWidget(self.precision_label, 0, 0, 1, 1)
        self.precision_spinBox = QSpinBox(self.piecewise_linear_approximation_groupBox)
        self.precision_spinBox.setObjectName("precision_spinBox")
        self.gridLayout_10.addWidget(self.precision_spinBox, 0, 1, 1, 1)
        self.max_tranches_label = QLabel(self.piecewise_linear_approximation_groupBox)
        self.max_tranches_label.setObjectName("max_tranches_label")
        self.gridLayout_10.addWidget(self.max_tranches_label, 1, 0, 1, 1)
        self.max_tranches_spinBox = QSpinBox(self.piecewise_linear_approximation_groupBox)
        self.max_tranches_spinBox.setMaximum(1000)
        self.max_tranches_spinBox.setProperty("value", 10)
        self.max_tranches_spinBox.setObjectName("max_tranches_spinBox")
        self.gridLayout_10.addWidget(self.max_tranches_spinBox, 1, 1, 1, 1)
        self.gridLayout_9.addWidget(self.piecewise_linear_approximation_groupBox, 0, 0, 1, 1)
        self.heat_rates_nonconvexities_groupBox = QGroupBox(self.groupBox_2)
        self.heat_rates_nonconvexities_groupBox.setObjectName("heat_rates_nonconvexities_groupBox")
        self.gridLayout_11 = QGridLayout(self.heat_rates_nonconvexities_groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.throw_error_radioButton = QRadioButton(self.heat_rates_nonconvexities_groupBox)
        self.throw_error_radioButton.setObjectName("throw_error_radioButton")
        self.gridLayout_11.addWidget(self.throw_error_radioButton, 0, 0, 1, 1)
        self.warn_adjust_report_raw_radioButton = QRadioButton(self.heat_rates_nonconvexities_groupBox)
        self.warn_adjust_report_raw_radioButton.setObjectName("warn_adjust_report_raw_radioButton")
        self.gridLayout_11.addWidget(self.warn_adjust_report_raw_radioButton, 1, 0, 1, 1)
        self.warn_adjust_report_adjusted_radioButton = QRadioButton(self.heat_rates_nonconvexities_groupBox)
        self.warn_adjust_report_adjusted_radioButton.setChecked(True)
        self.warn_adjust_report_adjusted_radioButton.setObjectName("warn_adjust_report_adjusted_radioButton")
        self.gridLayout_11.addWidget(self.warn_adjust_report_adjusted_radioButton, 2, 0, 1, 1)
        self.no_warn_adjust_radioButton = QRadioButton(self.heat_rates_nonconvexities_groupBox)
        self.no_warn_adjust_radioButton.setObjectName("no_warn_adjust_radioButton")
        self.gridLayout_11.addWidget(self.no_warn_adjust_radioButton, 3, 0, 1, 1)
        self.allow_non_convex_radioButton = QRadioButton(self.heat_rates_nonconvexities_groupBox)
        self.allow_non_convex_radioButton.setObjectName("allow_non_convex_radioButton")
        self.gridLayout_11.addWidget(self.allow_non_convex_radioButton, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.heat_rates_nonconvexities_groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)


        self.retranslateUi(Form)
        QObject.connect(self.rounding_up_threshold_horizontalSlider, SIGNAL("valueChanged(int)"), self.zero_label.setNum)
        QMetaObject.connectSlotsByName(Form)


        self.linear_radioButton.clicked.connect(self.roundingUpThresholdHide)
        self.rounded_relaxation_radioButton.clicked.connect(self.roundingUpThresholdHide)
        self.integer_radioButton.clicked.connect(self.roundingUpThresholdHide)
        self.self_tune_checkBox.clicked.connect(self.selfTuneHide)
    
    def setInput(self, input):
        self.input = input
        self.loadproductionscreen()
        self.roundingUpThresholdHide()
    
    def getOutput(self):
        self.saveproductionscreen()
        return self.output

    def loadproductionscreen(self):
        self.group_generators_by_power_station_checkBox.setChecked(self.input["group_generators_by_power_station"])
        self.rounding_up_threshold_horizontalSlider.setValue(self.input["rounding_up_threshold"]*100)
        self.self_tune_checkBox.setChecked(self.input["self_tune"])
        self.rounding_up_start_doubleSpinbox.setValue(self.input["rounding_up_start"])
        self.rounding_up_end_doubleSpinbox.setValue(self.input["rounding_up_end"])
        self.rounding_up_increment_doubleSpinbox.setValue(self.input["rounding_up_increment"])
        self.capacity_factor_threshold_spinBox.setValue(self.input["capacity_factor_threshold"])
        self.capacity_factor_error_threshold_spinBox.setValue(self.input["capacity_factor_error_threshold"])
        self.precision_spinBox.setValue(self.input["precision"])
        self.max_tranches_spinBox.setValue(self.input["max_tranches"])
        self.formulate_additional_unit_commitment_constraints_upfront_checkBox.setChecked(self.input["formulate_additional_unit_commitment_constraints_upfront"])
        self.formulate_ramp_constrains_upfront_checkBox.setChecked(self.input["formulate_ramp_constrains_upfront"])

        self.linear_radioButton.setChecked(self.input["unit_commitment_optimality"] == "Linear")
        self.rounded_relaxation_radioButton.setChecked(self.input["unit_commitment_optimality"] == "Rounded Relaxation")
        self.integer_radioButton.setChecked(self.input["unit_commitment_optimality"] == "Integer")
        
        self.throw_error_radioButton.setChecked(self.input["heat_rates_nonconvexities"] == "Throw Error")
        self.warn_adjust_report_raw_radioButton.setChecked(self.input["heat_rates_nonconvexities"] == "Warn Adjust Report Raw")
        self.warn_adjust_report_adjusted_radioButton.setChecked(self.input["heat_rates_nonconvexities"] == "Warn Adjust Report Adjusted")
        self.no_warn_adjust_radioButton.setChecked(self.input["heat_rates_nonconvexities"] == "No Warn Adjust")
        self.allow_non_convex_radioButton.setChecked(self.input["heat_rates_nonconvexities"] == "Allow Non-convex")

        self.optimize_radioButton.setChecked(self.input["start_cost_method"] == "Optimize")
        self.optimize_radioButton.setChecked(self.input["start_cost_method"] == "Calculate")

        self.installed_capacity_radioButton.setChecked(self.input["capacity_factor_refers_to"] == "Installed Capacity")
        self.rated_capacity_radioButton.setChecked(self.input["capacity_factor_refers_to"] == "Rated Capacity")

        self.never_radioButton.setChecked(self.input["integers_in_lookahead"] == "Never")
        self.auto_radioButton.setChecked(self.input["integers_in_lookahead"] == "Auto")
        self.always_radioButton.setChecked(self.input["integers_in_lookahead"] == "Always")

    def saveproductionscreen(self):
        self.output = production_default_input | {
            "group_generators_by_power_station": self.group_generators_by_power_station_checkBox.isChecked(),
            "rounding_up_threshold": self.rounding_up_threshold_horizontalSlider.value()/100,
            "self_tune": self.self_tune_checkBox.isChecked(),
            "rounding_up_start": self.rounding_up_start_doubleSpinbox.value(),
            "rounding_up_end": self.rounding_up_end_doubleSpinbox.value(),
            "rounding_up_increment": self.rounding_up_increment_doubleSpinbox.value(),
            "capacity_factor_threshold": self.capacity_factor_threshold_spinBox.value(),
            "capacity_factor_error_threshold": self.capacity_factor_error_threshold_spinBox.value(),
            "precision": self.precision_spinBox.value(),
            "max_tranches": self.max_tranches_spinBox.value(),
            "formulate_additional_unit_commitment_constraints_upfront": self.formulate_additional_unit_commitment_constraints_upfront_checkBox.isChecked(),
            "formulate_ramp_constrains_upfront": self.formulate_ramp_constrains_upfront_checkBox.isChecked(),
        }

        if self.linear_radioButton.isChecked():
            self.output["unit_commitment_optimality"] = "Linear"
        if self.rounded_relaxation_radioButton.isChecked():
            self.output["unit_commitment_optimality"] = "Rounded Relaxation"
        if self.integer_radioButton.isChecked():
            self.output["unit_commitment_optimality"] = "Integer"

        if self.throw_error_radioButton.isChecked():
            self.output["heat_rates_nonconvexities"] = "Throw Error"
        if self.warn_adjust_report_raw_radioButton.isChecked():
            self.output["heat_rates_nonconvexities"] = "Warn Adjust Report Raw"
        if self.warn_adjust_report_adjusted_radioButton.isChecked():
            self.output["heat_rates_nonconvexities"] = "Warn Adjust Report Adjusted"
        if self.no_warn_adjust_radioButton.isChecked():
            self.output["heat_rates_nonconvexities"] = "No Warn Adjust"
        if self.allow_non_convex_radioButton.isChecked():
            self.output["heat_rates_nonconvexities"] = "Allow Non-convex"

        if self.optimize_radioButton.isChecked():
            self.output["start_cost_method"] = "Optimize"
        if self.calculate_radioButton.isChecked():
            self.output["start_cost_method"] = "Calculate"
    
        if self.installed_capacity_radioButton.isChecked():
            self.output["capacity_factor_refers_to"] = "Installed Capacity"
        if self.rated_capacity_radioButton.isChecked():
            self.output["capacity_factor_refers_to"] = "Rated Capacity"

        if self.never_radioButton.isChecked():
            self.output["integers_in_lookahead"] = "Never"
        if self.auto_radioButton.isChecked():
            self.output["integers_in_lookahead"] = "Auto"
        if self.always_radioButton.isChecked():
            self.output["integers_in_lookahead"] = "Always"

    def roundingUpThresholdHide(self):
        if self.rounded_relaxation_radioButton.isChecked() == True:
            self.rounding_up_threshold_horizontalSlider.setEnabled(True)
            self.self_tune_checkBox.setEnabled(True)
            self.selfTuneHide()
        else:
            self.rounding_up_threshold_horizontalSlider.setEnabled(False)
            self.self_tune_checkBox.setEnabled(False)
            self.start_label.setEnabled(False)
            self.end_label.setEnabled(False)
            self.increment_label.setEnabled(False)
            self.rounding_up_start_doubleSpinbox.setEnabled(False)
            self.rounding_up_end_doubleSpinbox.setEnabled(False)
            self.rounding_up_increment_doubleSpinbox.setEnabled(False)

    def selfTuneHide(self):
        if self.self_tune_checkBox.isChecked() == True:
            self.start_label.setEnabled(True)
            self.end_label.setEnabled(True)
            self.increment_label.setEnabled(True)
            self.rounding_up_start_doubleSpinbox.setEnabled(True)
            self.rounding_up_end_doubleSpinbox.setEnabled(True)
            self.rounding_up_increment_doubleSpinbox.setEnabled(True)
        if self.self_tune_checkBox.isChecked() == False:
            self.start_label.setEnabled(False)
            self.end_label.setEnabled(False)
            self.increment_label.setEnabled(False)
            self.rounding_up_start_doubleSpinbox.setEnabled(False)
            self.rounding_up_end_doubleSpinbox.setEnabled(False)
            self.rounding_up_increment_doubleSpinbox.setEnabled(False)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.start_cost_method_groupBox.setTitle(QApplication.translate("Form", "Start Cost Method"))
        self.optimize_radioButton.setText(QApplication.translate("Form", "Optimize"))
        self.calculate_radioButton.setText(QApplication.translate("Form", "Calculate"))
        self.rounding_up_threshold_groupBox.setTitle(QApplication.translate("Form", "Rounding Up Threshold"))
        self.increment_label.setText(QApplication.translate("Form", "Increment:"))
        self.self_tune_checkBox.setText(QApplication.translate("Form", "Self Tune"))
        self.end_label.setText(QApplication.translate("Form", "End:"))
        self.zero_label.setText(QApplication.translate("Form", "0"))
        self.start_label.setText(QApplication.translate("Form", "Start:"))
        self.capacity_factor_groupBox.setTitle(QApplication.translate("Form", "Capacity Factor Refers to"))
        self.installed_capacity_radioButton.setText(QApplication.translate("Form", "Installed Capcity"))
        self.rated_capacity_radioButton.setText(QApplication.translate("Form", "Rated Capacity"))
        self.integers_in_lookahead_groupBox.setTitle(QApplication.translate("Form", "Integers in Look-ahead"))
        self.never_radioButton.setText(QApplication.translate("Form", "Never"))
        self.auto_radioButton.setText(QApplication.translate("Form", "Auto"))
        self.always_radioButton.setText(QApplication.translate("Form", "Always"))
        self.dynamic_program_radioButton.setTitle(QApplication.translate("Form", "Dynamic Program"))
        self.capacity_factor_threshold_label.setText(QApplication.translate("Form", "Capacity Factor Threshold (%):"))
        self.capacity_factor_error_threshold_label.setText(QApplication.translate("Form", "Capacity Factor Error Threshold (%):"))
        self.group_generators_by_power_station_checkBox.setText(QApplication.translate("Form", "Group Generators by Power Station"))
        self.formulate_additional_unit_commitment_constraints_upfront_checkBox.setText(QApplication.translate("Form", "Formulate additional unit commitment constraints upfront"))
        self.formulate_ramp_constrains_upfront_checkBox.setText(QApplication.translate("Form", "Formulate ramp constraints upfront"))
        self.unit_commitment_optimally_groupBox.setTitle(QApplication.translate("Form", "Unit Commitment Optimality"))
        self.linear_radioButton.setText(QApplication.translate("Form", "Linear"))
        self.rounded_relaxation_radioButton.setText(QApplication.translate("Form", "Rounded Relaxation"))
        self.integer_radioButton.setText(QApplication.translate("Form", "Integer"))
        self.piecewise_linear_approximation_groupBox.setTitle(QApplication.translate("Form", "Piecewise Linear Approximation"))
        self.precision_label.setText(QApplication.translate("Form", "Precision (%)"))
        self.max_tranches_label.setText(QApplication.translate("Form", "Max Tranches"))
        self.heat_rates_nonconvexities_groupBox.setTitle(QApplication.translate("Form", "Heat Rates Non-convexities"))
        self.throw_error_radioButton.setText(QApplication.translate("Form", "Throw Error"))
        self.warn_adjust_report_raw_radioButton.setText(QApplication.translate("Form", "Warn Adjust Report Raw"))
        self.warn_adjust_report_adjusted_radioButton.setText(QApplication.translate("Form", "Warn Adjust Report Adjusted"))
        self.no_warn_adjust_radioButton.setText(QApplication.translate("Form", "No Warn Adjust"))
        self.allow_non_convex_radioButton.setText(QApplication.translate("Form", "Allow Non-convex"))
