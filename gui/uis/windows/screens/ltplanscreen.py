# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ltplanscreen.ui'
#
# Created: Thu Jun 16 15:51:21 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

class Ui_LTPlanScreen(QObject):
    dataSaved = Signal(dict)

    default_input = {
        "step_size_years": "0",
        "overlap_years": "0",
        "blocks_in_each_duration_curve": "12",
        "blocks_in_last_curve_in_horizon": "0",
        "discounting_rate": "0",
        "inflation_rate": "0",
        "pin_top": "-1",
        "pin_bottom": "-1",
        "integration_horizon_years": "-1",
        "allow_capacity_sharing": False,
        "number_of_solutions": "1",
        "solution_quality": "0",
        "use_effective_load_approach": False,
        "compute_reliability_indices": False,
        "compute_multiarea_reliability_incides": False,
        "outage_increment": "10",
        "maintenance_sculpting": False,
        "start_cost_amortization_hrs": "11",
        "make_capacity_payments": False,
        "write_expansion_plan_to_text_files": False,
        "samples_per_year": "4",
        "tax_rate": "0",
        "chronology": "",
        "one_duration_curve": "Year",
        "slicing_method": "",
        "sample": "",
        "end_effects_method": "",
        "depreciation_method": "None",
        "expansions_decisions_integer_optimality": "",
        "stochastic_method": "Deterministic",
        "transmission": "Regional",
        "heat_rate": "Simplest",
        "generation_pricing_method": "Average"
    }
    input = default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1295, 837)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.outages_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outages_groupBox.sizePolicy().hasHeightForWidth())
        self.outages_groupBox.setSizePolicy(sizePolicy)
        self.outages_groupBox.setObjectName("outages_groupBox")
        self.gridLayout_8 = QGridLayout(self.outages_groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.use_effective_load_approach_checkBox = QCheckBox(self.outages_groupBox)
        self.use_effective_load_approach_checkBox.setObjectName("use_effective_load_approach_checkBox")
        self.gridLayout_8.addWidget(self.use_effective_load_approach_checkBox, 0, 0, 1, 1)
        self.compute_reliability_indices_checkBox = QCheckBox(self.outages_groupBox)
        self.compute_reliability_indices_checkBox.setObjectName("compute_reliability_indices_checkBox")
        self.gridLayout_8.addWidget(self.compute_reliability_indices_checkBox, 1, 0, 1, 2)
        self.compute_multiarea_reliability_incides_checkBox = QCheckBox(self.outages_groupBox)
        self.compute_multiarea_reliability_incides_checkBox.setObjectName("compute_multiarea_reliability_incides_checkBox")
        self.gridLayout_8.addWidget(self.compute_multiarea_reliability_incides_checkBox, 2, 0, 1, 2)
        self.outage_increment_spinBox = QSpinBox(self.outages_groupBox)
        self.outage_increment_spinBox.setMaximum(1000)
        self.outage_increment_spinBox.setProperty("value", 10)
        self.outage_increment_spinBox.setObjectName("outage_increment_spinBox")
        self.gridLayout_8.addWidget(self.outage_increment_spinBox, 3, 0, 1, 1)
        self.outage_increment_mw_label = QLabel(self.outages_groupBox)
        self.outage_increment_mw_label.setObjectName("outage_increment_mw_label")
        self.gridLayout_8.addWidget(self.outage_increment_mw_label, 3, 1, 1, 1)
        self.maintenance_sculpting_checkBox = QCheckBox(self.outages_groupBox)
        self.maintenance_sculpting_checkBox.setObjectName("maintenance_sculpting_checkBox")
        self.gridLayout_8.addWidget(self.maintenance_sculpting_checkBox, 4, 0, 1, 2)
        self.verticalLayout_5.addWidget(self.outages_groupBox)
        self.stochastic_method_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stochastic_method_groupBox.sizePolicy().hasHeightForWidth())
        self.stochastic_method_groupBox.setSizePolicy(sizePolicy)
        self.stochastic_method_groupBox.setObjectName("stochastic_method_groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.stochastic_method_groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.deterministic_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.deterministic_radioButton.setChecked(True)
        self.deterministic_radioButton.setObjectName("deterministic_radioButton")
        self.verticalLayout_6.addWidget(self.deterministic_radioButton)
        self.independant_samples_sequential_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_sequential_radioButton.setObjectName("independant_samples_sequential_radioButton")
        self.verticalLayout_6.addWidget(self.independant_samples_sequential_radioButton)
        self.independant_samples_partial_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_partial_radioButton.setObjectName("independant_samples_partial_radioButton")
        self.verticalLayout_6.addWidget(self.independant_samples_partial_radioButton)
        self.scenariowise_decomposition_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.scenariowise_decomposition_radioButton.setObjectName("scenariowise_decomposition_radioButton")
        self.verticalLayout_6.addWidget(self.scenariowise_decomposition_radioButton)
        self.verticalLayout_5.addWidget(self.stochastic_method_groupBox)
        self.transmission_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transmission_groupBox.sizePolicy().hasHeightForWidth())
        self.transmission_groupBox.setSizePolicy(sizePolicy)
        self.transmission_groupBox.setObjectName("transmission_groupBox")
        self.horizontalLayout = QHBoxLayout(self.transmission_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regional_radioButton = QRadioButton(self.transmission_groupBox)
        self.regional_radioButton.setChecked(True)
        self.regional_radioButton.setObjectName("regional_radioButton")
        self.horizontalLayout.addWidget(self.regional_radioButton)
        self.zonal_radioButton = QRadioButton(self.transmission_groupBox)
        self.zonal_radioButton.setObjectName("zonal_radioButton")
        self.horizontalLayout.addWidget(self.zonal_radioButton)
        self.nodal_radioButton = QRadioButton(self.transmission_groupBox)
        self.nodal_radioButton.setObjectName("nodal_radioButton")
        self.horizontalLayout.addWidget(self.nodal_radioButton)
        self.verticalLayout_5.addWidget(self.transmission_groupBox)
        self.heat_rate_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heat_rate_groupBox.sizePolicy().hasHeightForWidth())
        self.heat_rate_groupBox.setSizePolicy(sizePolicy)
        self.heat_rate_groupBox.setObjectName("heat_rate_groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.heat_rate_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.detailed_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.detailed_radioButton.setObjectName("detailed_radioButton")
        self.horizontalLayout_2.addWidget(self.detailed_radioButton)
        self.simple_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simple_radioButton.setObjectName("simple_radioButton")
        self.horizontalLayout_2.addWidget(self.simple_radioButton)
        self.simplest_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simplest_radioButton.setChecked(True)
        self.simplest_radioButton.setObjectName("simplest_radioButton")
        self.horizontalLayout_2.addWidget(self.simplest_radioButton)
        self.verticalLayout_5.addWidget(self.heat_rate_groupBox)
        self.pricing_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pricing_groupBox.sizePolicy().hasHeightForWidth())
        self.pricing_groupBox.setSizePolicy(sizePolicy)
        self.pricing_groupBox.setObjectName("pricing_groupBox")
        self.gridLayout_9 = QGridLayout(self.pricing_groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.average_radioButton = QRadioButton(self.pricing_groupBox)
        self.average_radioButton.setObjectName("average_radioButton")
        self.gridLayout_9.addWidget(self.average_radioButton, 1, 0, 1, 1)
        self.marginal_radioButton = QRadioButton(self.pricing_groupBox)
        self.marginal_radioButton.setObjectName("marginal_radioButton")
        self.gridLayout_9.addWidget(self.marginal_radioButton, 1, 1, 1, 2)
        self.generation_pricing_method_label = QLabel(self.pricing_groupBox)
        self.generation_pricing_method_label.setObjectName("generation_pricing_method_label")
        self.gridLayout_9.addWidget(self.generation_pricing_method_label, 0, 0, 1, 2)
        self.make_capacity_payments_checkBox = QCheckBox(self.pricing_groupBox)
        self.make_capacity_payments_checkBox.setObjectName("make_capacity_payments_checkBox")
        self.gridLayout_9.addWidget(self.make_capacity_payments_checkBox, 3, 0, 1, 1)
        self.start_cost_amortization_hrs_label = QLabel(self.pricing_groupBox)
        self.start_cost_amortization_hrs_label.setObjectName("start_cost_amortization_hrs_label")
        self.gridLayout_9.addWidget(self.start_cost_amortization_hrs_label, 2, 0, 1, 1)
        self.start_cost_amortization_hrs_spinBox = QSpinBox(self.pricing_groupBox)
        self.start_cost_amortization_hrs_spinBox.setObjectName("start_cost_amortization_hrs_spinBox")
        self.gridLayout_9.addWidget(self.start_cost_amortization_hrs_spinBox, 2, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.pricing_groupBox)
        self.output_groupBox = QGroupBox(self.groupBox)
        self.output_groupBox.setObjectName("output_groupBox")
        self.gridLayout_10 = QGridLayout(self.output_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.write_expansion_plan_to_text_files_checkBox = QCheckBox(self.output_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.write_expansion_plan_to_text_files_checkBox.sizePolicy().hasHeightForWidth())
        self.write_expansion_plan_to_text_files_checkBox.setSizePolicy(sizePolicy)
        self.write_expansion_plan_to_text_files_checkBox.setObjectName("write_expansion_plan_to_text_files_checkBox")
        self.gridLayout_10.addWidget(self.write_expansion_plan_to_text_files_checkBox, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.output_groupBox)
        self.gridLayout_3.addWidget(self.groupBox, 0, 3, 1, 1)
        self.groupBox_18 = QGroupBox(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_18.sizePolicy().hasHeightForWidth())
        self.groupBox_18.setSizePolicy(sizePolicy)
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_11 = QGridLayout(self.groupBox_18)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.buttonBox = QDialogButtonBox(self.groupBox_18)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok|QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_11.addWidget(self.buttonBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_18, 1, 3, 1, 1)
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.step_size_groupBox = QGroupBox(self.groupBox_3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.step_size_groupBox.sizePolicy().hasHeightForWidth())
        self.step_size_groupBox.setSizePolicy(sizePolicy)
        self.step_size_groupBox.setObjectName("step_size_groupBox")
        self.gridLayout = QGridLayout(self.step_size_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.step_size_years_label = QLabel(self.step_size_groupBox)
        self.step_size_years_label.setObjectName("step_size_years_label")
        self.gridLayout.addWidget(self.step_size_years_label, 0, 0, 1, 1)
        self.step_size_years_spinBox = QSpinBox(self.step_size_groupBox)
        self.step_size_years_spinBox.setObjectName("step_size_years_spinBox")
        self.gridLayout.addWidget(self.step_size_years_spinBox, 0, 1, 1, 1)
        self.overlap_years_label = QLabel(self.step_size_groupBox)
        self.overlap_years_label.setObjectName("overlap_years_label")
        self.gridLayout.addWidget(self.overlap_years_label, 1, 0, 1, 1)
        self.overlap_years_spinBox = QSpinBox(self.step_size_groupBox)
        self.overlap_years_spinBox.setObjectName("overlap_years_spinBox")
        self.gridLayout.addWidget(self.overlap_years_spinBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.step_size_groupBox)
        self.chronology_groupBox = QGroupBox(self.groupBox_3)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chronology_groupBox.sizePolicy().hasHeightForWidth())
        self.chronology_groupBox.setSizePolicy(sizePolicy)
        self.chronology_groupBox.setObjectName("chronology_groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.chronology_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.partial_radioButton = QRadioButton(self.chronology_groupBox)
        self.partial_radioButton.setObjectName("partial_radioButton")
        self.verticalLayout_2.addWidget(self.partial_radioButton)
        self.fitterd_radioButton = QRadioButton(self.chronology_groupBox)
        self.fitterd_radioButton.setObjectName("fitterd_radioButton")
        self.verticalLayout_2.addWidget(self.fitterd_radioButton)
        self.samples_radioButton = QRadioButton(self.chronology_groupBox)
        self.samples_radioButton.setObjectName("samples_radioButton")
        self.verticalLayout_2.addWidget(self.samples_radioButton)
        self.one_duration_curve_each_groupBox = QGroupBox(self.chronology_groupBox)
        self.one_duration_curve_each_groupBox.setObjectName("one_duration_curve_each_groupBox")
        self.gridLayout_2 = QGridLayout(self.one_duration_curve_each_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.day_radioButton = QRadioButton(self.one_duration_curve_each_groupBox)
        self.day_radioButton.setObjectName("day_radioButton")
        self.gridLayout_2.addWidget(self.day_radioButton, 0, 0, 1, 1)
        self.week_radioButton = QRadioButton(self.one_duration_curve_each_groupBox)
        self.week_radioButton.setObjectName("week_radioButton")
        self.gridLayout_2.addWidget(self.week_radioButton, 0, 1, 1, 1)
        self.month_radioButton = QRadioButton(self.one_duration_curve_each_groupBox)
        self.month_radioButton.setObjectName("month_radioButton")
        self.gridLayout_2.addWidget(self.month_radioButton, 0, 2, 1, 1)
        self.year_radioButton = QRadioButton(self.one_duration_curve_each_groupBox)
        self.year_radioButton.setObjectName("year_radioButton")
        self.gridLayout_2.addWidget(self.year_radioButton, 0, 3, 1, 1)
        self.blocks_in_each_duration_curve_label = QLabel(self.one_duration_curve_each_groupBox)
        self.blocks_in_each_duration_curve_label.setObjectName("blocks_in_each_duration_curve_label")
        self.gridLayout_2.addWidget(self.blocks_in_each_duration_curve_label, 1, 0, 1, 1)
        self.blocks_in_each_duration_curve_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.blocks_in_each_duration_curve_spinBox.setProperty("value", 12)
        self.blocks_in_each_duration_curve_spinBox.setObjectName("blocks_in_each_duration_curve_spinBox")
        self.gridLayout_2.addWidget(self.blocks_in_each_duration_curve_spinBox, 1, 1, 1, 1)
        self.blocks_in_last_curve_in_horizon_label = QLabel(self.one_duration_curve_each_groupBox)
        self.blocks_in_last_curve_in_horizon_label.setObjectName("blocks_in_last_curve_in_horizon_label")
        self.gridLayout_2.addWidget(self.blocks_in_last_curve_in_horizon_label, 2, 0, 1, 1)
        self.blocks_in_last_curve_in_horizon_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.blocks_in_last_curve_in_horizon_spinBox.setObjectName("blocks_in_last_curve_in_horizon_spinBox")
        self.gridLayout_2.addWidget(self.blocks_in_last_curve_in_horizon_spinBox, 2, 1, 1, 1)
        self.slicing_method_groupBox = QGroupBox(self.one_duration_curve_each_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slicing_method_groupBox.sizePolicy().hasHeightForWidth())
        self.slicing_method_groupBox.setSizePolicy(sizePolicy)
        self.slicing_method_groupBox.setObjectName("slicing_method_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.slicing_method_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.peak_offpeak_bias_radioButton = QRadioButton(self.slicing_method_groupBox)
        self.peak_offpeak_bias_radioButton.setObjectName("peak_offpeak_bias_radioButton")
        self.verticalLayout_3.addWidget(self.peak_offpeak_bias_radioButton)
        self.weighted_leastsquares_fit_radioButton = QRadioButton(self.slicing_method_groupBox)
        self.weighted_leastsquares_fit_radioButton.setObjectName("weighted_leastsquares_fit_radioButton")
        self.verticalLayout_3.addWidget(self.weighted_leastsquares_fit_radioButton)
        self.gridLayout_2.addWidget(self.slicing_method_groupBox, 3, 0, 1, 2)
        self.pin_top_label = QLabel(self.one_duration_curve_each_groupBox)
        self.pin_top_label.setObjectName("pin_top_label")
        self.gridLayout_2.addWidget(self.pin_top_label, 4, 0, 1, 1)
        self.pin_bottom_label = QLabel(self.one_duration_curve_each_groupBox)
        self.pin_bottom_label.setObjectName("pin_bottom_label")
        self.gridLayout_2.addWidget(self.pin_bottom_label, 5, 0, 1, 1)
        self.pin_top_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.pin_top_spinBox.setMinimum(-1)
        self.pin_top_spinBox.setProperty("value", -1)
        self.pin_top_spinBox.setObjectName("pin_top_spinBox")
        self.gridLayout_2.addWidget(self.pin_top_spinBox, 4, 1, 1, 1)
        self.pin_bottom_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.pin_bottom_spinBox.setMinimum(-1)
        self.pin_bottom_spinBox.setProperty("value", -1)
        self.pin_bottom_spinBox.setObjectName("pin_bottom_spinBox")
        self.gridLayout_2.addWidget(self.pin_bottom_spinBox, 5, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.one_duration_curve_each_groupBox)
        self.sample_groupBox = QGroupBox(self.chronology_groupBox)
        self.sample_groupBox.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_groupBox.sizePolicy().hasHeightForWidth())
        self.sample_groupBox.setSizePolicy(sizePolicy)
        self.sample_groupBox.setObjectName("sample_groupBox")
        self.gridLayout_4 = QGridLayout(self.sample_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.sample_day_radioButton = QRadioButton(self.sample_groupBox)
        self.sample_day_radioButton.setObjectName("sample_day_radioButton")
        self.gridLayout_4.addWidget(self.sample_day_radioButton, 0, 0, 1, 1)
        self.samples_per_year_spinBox = QSpinBox(self.sample_groupBox)
        self.samples_per_year_spinBox.setProperty("value", 4)
        self.samples_per_year_spinBox.setObjectName("samples_per_year_spinBox")
        self.gridLayout_4.addWidget(self.samples_per_year_spinBox, 1, 1, 1, 1)
        self.samples_per_year_label = QLabel(self.sample_groupBox)
        self.samples_per_year_label.setObjectName("samples_per_year_label")
        self.gridLayout_4.addWidget(self.samples_per_year_label, 1, 0, 1, 1)
        self.sample_week_radioButton = QRadioButton(self.sample_groupBox)
        self.sample_week_radioButton.setChecked(True)
        self.sample_week_radioButton.setObjectName("sample_week_radioButton")
        self.gridLayout_4.addWidget(self.sample_week_radioButton, 0, 1, 1, 1)
        self.sample_month_radioButton = QRadioButton(self.sample_groupBox)
        self.sample_month_radioButton.setObjectName("sample_month_radioButton")
        self.gridLayout_4.addWidget(self.sample_month_radioButton, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.sample_groupBox)
        self.verticalLayout.addWidget(self.chronology_groupBox)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.discounting_groupBox = QGroupBox(self.groupBox_2)
        self.discounting_groupBox.setObjectName("discounting_groupBox")
        self.gridLayout_5 = QGridLayout(self.discounting_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.discounting_rate_label = QLabel(self.discounting_groupBox)
        self.discounting_rate_label.setObjectName("discounting_rate_label")
        self.gridLayout_5.addWidget(self.discounting_rate_label, 2, 0, 1, 1)
        self.end_effects_methods_label = QLabel(self.discounting_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_effects_methods_label.sizePolicy().hasHeightForWidth())
        self.end_effects_methods_label.setSizePolicy(sizePolicy)
        self.end_effects_methods_label.setObjectName("end_effects_methods_label")
        self.gridLayout_5.addWidget(self.end_effects_methods_label, 8, 0, 1, 2)
        self.depreciation_method_label = QLabel(self.discounting_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depreciation_method_label.sizePolicy().hasHeightForWidth())
        self.depreciation_method_label.setSizePolicy(sizePolicy)
        self.depreciation_method_label.setObjectName("depreciation_method_label")
        self.gridLayout_5.addWidget(self.depreciation_method_label, 10, 0, 1, 3)
        self.none_radioButton = QRadioButton(self.discounting_groupBox)
        self.none_radioButton.setChecked(True)
        self.none_radioButton.setObjectName("none_radioButton")
        self.gridLayout_5.addWidget(self.none_radioButton, 11, 0, 1, 1)
        self.none_radioButton_2 = QRadioButton(self.discounting_groupBox)
        self.none_radioButton_2.setObjectName("none_radioButton_2")
        self.gridLayout_5.addWidget(self.none_radioButton_2, 9, 0, 1, 1)
        self.tax_rate_label = QLabel(self.discounting_groupBox)
        self.tax_rate_label.setObjectName("tax_rate_label")
        self.gridLayout_5.addWidget(self.tax_rate_label, 14, 0, 1, 1)
        self.inflation_rate_label = QLabel(self.discounting_groupBox)
        self.inflation_rate_label.setObjectName("inflation_rate_label")
        self.gridLayout_5.addWidget(self.inflation_rate_label, 15, 0, 1, 1)
        self.straight_line_radioButton = QRadioButton(self.discounting_groupBox)
        self.straight_line_radioButton.setObjectName("straight_line_radioButton")
        self.gridLayout_5.addWidget(self.straight_line_radioButton, 11, 1, 1, 1)
        self.declining_radioButton = QRadioButton(self.discounting_groupBox)
        self.declining_radioButton.setObjectName("declining_radioButton")
        self.gridLayout_5.addWidget(self.declining_radioButton, 11, 2, 1, 1)
        self.perpetuity_radioButton = QRadioButton(self.discounting_groupBox)
        self.perpetuity_radioButton.setChecked(False)
        self.perpetuity_radioButton.setObjectName("perpetuity_radioButton")
        self.gridLayout_5.addWidget(self.perpetuity_radioButton, 9, 1, 1, 1)
        self.discounting_rate_spinBox = QSpinBox(self.discounting_groupBox)
        self.discounting_rate_spinBox.setObjectName("discounting_rate_spinBox")
        self.gridLayout_5.addWidget(self.discounting_rate_spinBox, 14, 1, 1, 1)
        self.tax_rate_spinBox = QSpinBox(self.discounting_groupBox)
        self.tax_rate_spinBox.setObjectName("tax_rate_spinBox")
        self.gridLayout_5.addWidget(self.tax_rate_spinBox, 2, 1, 1, 1)
        self.inflation_rate_spinBox = QSpinBox(self.discounting_groupBox)
        self.inflation_rate_spinBox.setObjectName("inflation_rate_spinBox")
        self.gridLayout_5.addWidget(self.inflation_rate_spinBox, 15, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.discounting_groupBox)
        self.expansion_algorithm_groupBox = QGroupBox(self.groupBox_2)
        self.expansion_algorithm_groupBox.setObjectName("expansion_algorithm_groupBox")
        self.gridLayout_6 = QGridLayout(self.expansion_algorithm_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.explansion_decisions_integer_optimality_label = QLabel(self.expansion_algorithm_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.explansion_decisions_integer_optimality_label.sizePolicy().hasHeightForWidth())
        self.explansion_decisions_integer_optimality_label.setSizePolicy(sizePolicy)
        self.explansion_decisions_integer_optimality_label.setObjectName("explansion_decisions_integer_optimality_label")
        self.gridLayout_6.addWidget(self.explansion_decisions_integer_optimality_label, 0, 0, 1, 3)
        self.linear_radioButton = QRadioButton(self.expansion_algorithm_groupBox)
        self.linear_radioButton.setObjectName("linear_radioButton")
        self.gridLayout_6.addWidget(self.linear_radioButton, 1, 0, 1, 1)
        self.integer_radioButton = QRadioButton(self.expansion_algorithm_groupBox)
        self.integer_radioButton.setObjectName("integer_radioButton")
        self.gridLayout_6.addWidget(self.integer_radioButton, 1, 1, 1, 1)
        self.allow_capacity_sharing_checkBox = QCheckBox(self.expansion_algorithm_groupBox)
        self.allow_capacity_sharing_checkBox.setObjectName("allow_capacity_sharing_checkBox")
        self.gridLayout_6.addWidget(self.allow_capacity_sharing_checkBox, 3, 0, 1, 2)
        self.integration_horizon_years_label = QLabel(self.expansion_algorithm_groupBox)
        self.integration_horizon_years_label.setObjectName("integration_horizon_years_label")
        self.gridLayout_6.addWidget(self.integration_horizon_years_label, 2, 0, 1, 1)
        self.integration_horizon_years_spinBox = QSpinBox(self.expansion_algorithm_groupBox)
        self.integration_horizon_years_spinBox.setMinimum(-1)
        self.integration_horizon_years_spinBox.setProperty("value", -1)
        self.integration_horizon_years_spinBox.setObjectName("integration_horizon_years_spinBox")
        self.gridLayout_6.addWidget(self.integration_horizon_years_spinBox, 2, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.expansion_algorithm_groupBox)
        self.solution_hierarchy_groupBox = QGroupBox(self.groupBox_2)
        self.solution_hierarchy_groupBox.setObjectName("solution_hierarchy_groupBox")
        self.gridLayout_7 = QGridLayout(self.solution_hierarchy_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.number_of_solutions_label = QLabel(self.solution_hierarchy_groupBox)
        self.number_of_solutions_label.setObjectName("number_of_solutions_label")
        self.gridLayout_7.addWidget(self.number_of_solutions_label, 0, 0, 1, 1)
        self.number_of_solutions_spinBox = QSpinBox(self.solution_hierarchy_groupBox)
        self.number_of_solutions_spinBox.setProperty("value", 1)
        self.number_of_solutions_spinBox.setObjectName("number_of_solutions_spinBox")
        self.gridLayout_7.addWidget(self.number_of_solutions_spinBox, 0, 1, 1, 1)
        self.solution_quality_label = QLabel(self.solution_hierarchy_groupBox)
        self.solution_quality_label.setObjectName("solution_quality_label")
        self.gridLayout_7.addWidget(self.solution_quality_label, 1, 0, 1, 1)
        self.solution_quality_spinBox = QSpinBox(self.solution_hierarchy_groupBox)
        self.solution_quality_spinBox.setObjectName("solution_quality_spinBox")
        self.gridLayout_7.addWidget(self.solution_quality_spinBox, 1, 1, 1, 1)
        self.verticalLayout_4.addWidget(self.solution_hierarchy_groupBox)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 2, 1, 1)


        self.retranslateUi(Form)

        self.partial_radioButton.clicked.connect(self.enableSampleGroupBox)
        self.fitterd_radioButton.clicked.connect(self.enableSampleGroupBox)
        self.samples_radioButton.clicked.connect(self.enableSampleGroupBox)

        btn = self.buttonBox.button(QDialogButtonBox.Ok)
        btn.clicked.connect(self.saveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.Cancel)
        btn.clicked.connect(self.dontsaveandclose)
        btn = self.buttonBox.button(QDialogButtonBox.RestoreDefaults)
        btn.clicked.connect(self.restoredefaults)

    def saveandclose(self):
        self.saveltplanscreen()

    def dontsaveandclose(self):
        pass

    def restoredefaults(self):
        self.input = self.default_input
        self.loadltplanscreen()
        self.enableSampleGroupBox()
    
    def setInput(self, input):
        self.input = self.default_input | input
        self.loadltplanscreen()
        self.enableSampleGroupBox()
    
    def getOutput(self):
        return self.output

    def loadltplanscreen(self):
        self.step_size_years_spinBox.setValue(int(self.input["step_size_years"]))
        self.overlap_years_spinBox.setValue(int(self.input["overlap_years"]))
        self.blocks_in_each_duration_curve_spinBox.setValue(int(self.input["blocks_in_each_duration_curve"]))
        self.blocks_in_last_curve_in_horizon_spinBox.setValue(int(self.input["blocks_in_last_curve_in_horizon"]))
        self.discounting_rate_spinBox.setValue(int(self.input["discounting_rate"]))
        self.inflation_rate_spinBox.setValue(int(self.input["inflation_rate"]))
        self.pin_top_spinBox.setValue(int(self.input["pin_top"]))
        self.pin_bottom_spinBox.setValue(int(self.input["pin_bottom"]))
        self.integration_horizon_years_spinBox.setValue(int(self.input["integration_horizon_years"]))
        self.number_of_solutions_spinBox.setValue(int(self.input["number_of_solutions"]))
        self.solution_quality_spinBox.setValue(int(self.input["solution_quality"]))
        self.outage_increment_spinBox.setValue(int(self.input["outage_increment"]))
        self.start_cost_amortization_hrs_spinBox.setValue(int(self.input["start_cost_amortization_hrs"]))
        self.samples_per_year_spinBox.setValue(int(self.input["samples_per_year"]))
        self.tax_rate_spinBox.setValue(int(self.input["tax_rate"]))
        self.allow_capacity_sharing_checkBox.setChecked(self.input["allow_capacity_sharing"])
        self.use_effective_load_approach_checkBox.setChecked(self.input["use_effective_load_approach"])
        self.compute_reliability_indices_checkBox.setChecked(self.input["compute_reliability_indices"])
        self.compute_multiarea_reliability_incides_checkBox.setChecked(self.input["compute_multiarea_reliability_incides"])
        self.maintenance_sculpting_checkBox.setChecked(self.input["maintenance_sculpting"])
        self.make_capacity_payments_checkBox.setChecked(self.input["make_capacity_payments"])
        self.write_expansion_plan_to_text_files_checkBox.setChecked(self.input["write_expansion_plan_to_text_files"])

        self.partial_radioButton.setChecked(self.input["chronology"] == "Partial")
        self.fitterd_radioButton.setChecked(self.input["chronology"] == "Fitted")
        self.samples_radioButton.setChecked(self.input["chronology"] == "Sampled")

        self.day_radioButton.setChecked(self.input["one_duration_curve"] == "Day")
        self.week_radioButton.setChecked(self.input["one_duration_curve"] == "Week")
        self.month_radioButton.setChecked(self.input["one_duration_curve"] == "Month")
        self.year_radioButton.setChecked(self.input["one_duration_curve"] == "Year")

        self.peak_offpeak_bias_radioButton.setChecked(self.input["slicing_method"] == "Peak/Off-peak Bias")
        self.weighted_leastsquares_fit_radioButton.setChecked(self.input["slicing_method"] == "Weighted Least-squares Fit")

        self.sample_day_radioButton.setChecked(self.input["sample"] == "Day")
        self.sample_week_radioButton.setChecked(self.input["sample"] == "Week")
        self.sample_month_radioButton.setChecked(self.input["sample"] == "Month")

        self.none_radioButton_2.setChecked(self.input["end_effects_method"] == "None")
        self.perpetuity_radioButton.setChecked(self.input["end_effects_method"] == "Perpetuity")

        self.none_radioButton.setChecked(self.input["depreciation_method"] == "None")
        self.straight_line_radioButton.setChecked(self.input["depreciation_method"] == "Straight-Line")
        self.declining_radioButton.setChecked(self.input["depreciation_method"] == "Declining")

        self.linear_radioButton.setChecked(self.input["expansions_decisions_integer_optimality"] == "Linear")
        self.integer_radioButton.setChecked(self.input["expansions_decisions_integer_optimality"] == "Integer")

        self.deterministic_radioButton.setChecked(self.input["stochastic_method"] == "Deterministic")
        self.independant_samples_sequential_radioButton.setChecked(self.input["stochastic_method"] == "Indepentent Samples (Sequential)")
        self.independant_samples_partial_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Partial)")
        self.scenariowise_decomposition_radioButton.setChecked(self.input["stochastic_method"] == "Scenario-wise Decomposition")

        self.regional_radioButton.setChecked(self.input["transmission"] == "Regional")
        self.zonal_radioButton.setChecked(self.input["transmission"] == "Zonal")
        self.nodal_radioButton.setChecked(self.input["transmission"] == "Nodal")

        self.detailed_radioButton.setChecked(self.input["heat_rate"] == "Detailed")
        self.simple_radioButton.setChecked(self.input["heat_rate"] == "Simple")
        self.simplest_radioButton.setChecked(self.input["heat_rate"] == "Simplest")

        self.average_radioButton.setChecked(self.input["generation_pricing_method"] == "Average")
        self.marginal_radioButton.setChecked(self.input["generation_pricing_method"] == "Marginal")

    def saveltplanscreen(self):
        self.output = {
            "step_size_years": str(self.step_size_years_spinBox.value()),
            "overlap_years": str(self.overlap_years_spinBox.value()),
            "blocks_in_each_duration_curve": str(self.blocks_in_each_duration_curve_spinBox.value()),
            "blocks_in_last_curve_in_horizon": str(self.blocks_in_last_curve_in_horizon_spinBox.value()),
            "discounting_rate": str(self.discounting_rate_spinBox.value()),
            "inflation_rate": str(self.inflation_rate_spinBox.value()),
            "pin_top": str(self.pin_top_spinBox.value()),
            "pin_bottom": str(self.pin_bottom_spinBox.value()),
            "integration_horizon_years": str(self.integration_horizon_years_spinBox.value()),
            "number_of_solutions": str(self.number_of_solutions_spinBox.value()),
            "solution_quality": str(self.solution_quality_spinBox.value()),
            "outage_increment": str(self.outage_increment_spinBox.value()),
            "start_cost_amortization_hrs": str(self.start_cost_amortization_hrs_spinBox.value()),
            "samples_per_year": str(self.samples_per_year_spinBox.value()),
            "tax_rate": str(self.tax_rate_spinBox.value()),
            "allow_capacity_sharing": self.allow_capacity_sharing_checkBox.isChecked(),
            "use_effective_load_approach": self.use_effective_load_approach_checkBox.isChecked(),
            "compute_reliability_indices": self.compute_reliability_indices_checkBox.isChecked(),
            "compute_multiarea_reliability_incides": self.compute_multiarea_reliability_incides_checkBox.isChecked(),
            "maintenance_sculpting": self.maintenance_sculpting_checkBox.isChecked(),
            "make_capacity_payments": self.make_capacity_payments_checkBox.isChecked(),
            "write_expansion_plan_to_text_files": self.write_expansion_plan_to_text_files_checkBox.isChecked()
        }

        if self.partial_radioButton.isChecked()==True:
            self.output["chronology"] = "Partial"
        if self.fitterd_radioButton.isChecked()==True:
            self.output["chronology"] = "Fitted"
        if self.samples_radioButton.isChecked()==True:
            self.output["chronology"] = "Sampled"

        if self.day_radioButton.isChecked()==True:
            self.output["one_duration_curve"] = "Day"
        if self.week_radioButton.isChecked()==True:
            self.output["one_duration_curve"] = "Week"
        if self.month_radioButton.isChecked()==True:
            self.output["one_duration_curve"] = "Month"
        if self.year_radioButton.isChecked()==True:
            self.output["one_duration_curve"] = "Year"

        if self.peak_offpeak_bias_radioButton.isChecked()==True:
            self.output["slicing_method"] = "Peak/Off-peak Bias"
        if self.weighted_leastsquares_fit_radioButton.isChecked()==True:
            self.output["slicing_method"] = "Weighted Least-squares Fit"

        if self.sample_day_radioButton.isChecked()==True:
            self.output["sample"] = "Day"
        if self.sample_week_radioButton.isChecked()==True:
            self.output["sample"] = "Week"
        if self.sample_month_radioButton.isChecked()==True:
            self.output["sample"] = "Month"

        if  self.none_radioButton_2.isChecked()==True:
            self.output["end_effects_method"] = "None"
        if self.perpetuity_radioButton.isChecked()==True:
            self.output["end_effects_method"] = "Perpetuity"

        if self.none_radioButton.isChecked()==True:
            self.output["depreciation_method"] = "None"
        if self.straight_line_radioButton.isChecked()==True:
            self.output["depreciation_method"] = "Straight-Line"
        if self.declining_radioButton.isChecked()==True:
            self.output["depreciation_method"] = "Declining"

        if self.linear_radioButton.isChecked()==True:
            self.output["expansions_decisions_integer_optimality"] = "Linear"
        if self.integer_radioButton.isChecked()==True:
            self.output["expansions_decisions_integer_optimality"] = "Integer"

        if self.deterministic_radioButton.isChecked()==True:
            self.output["stochastic_method"] = "Deterministic"
        if self.independant_samples_sequential_radioButton.isChecked()==True:
            self.output["stochastic_method"] = "Indepentent Samples (Sequential)"
        if self.independant_samples_partial_radioButton.isChecked()==True:
            self.output["stochastic_method"] = "Independent Samples (Partial)"
        if self.scenariowise_decomposition_radioButton.isChecked()==True:
            self.output["stochastic_method"] = "Scenario-wise Decomposition"

        if self.regional_radioButton.isChecked()==True:
            self.output["transmission"] = "Regional"
        if self.zonal_radioButton.isChecked()==True:
            self.output["transmission"] = "Zonal"
        if self.nodal_radioButton.isChecked()==True:
            self.output["transmission"] = "Nodal"

        if self.detailed_radioButton.isChecked()==True:
            self.output["heat_rate"] = "Detailed"
        if self.simple_radioButton.isChecked()==True:
            self.output["heat_rate"] = "Simple"
        if self.simplest_radioButton.isChecked()==True:
            self.output["heat_rate"] = "Simplest"

        if self.average_radioButton.isChecked()==True:
            self.output["generation_pricing_method"] = "Average"
        if self.marginal_radioButton.isChecked()==True:
            self.output["generation_pricing_method"] = "Marginal"

        self.dataSaved.emit(self.output)

    def enableSampleGroupBox(self):
        if self.samples_radioButton.isChecked() == True:
            self.sample_groupBox.setEnabled(True)
        else:
            self.sample_groupBox.setEnabled(False)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.outages_groupBox.setTitle(QApplication.translate("Form", "Outages"))
        self.use_effective_load_approach_checkBox.setText(QApplication.translate("Form", "Use Effect,ve Load Approach"))
        self.compute_reliability_indices_checkBox.setText(QApplication.translate("Form", "Compute Reliability Indices"))
        self.compute_multiarea_reliability_incides_checkBox.setText(QApplication.translate("Form", "Compute Multi-area Reliability Indices"))
        self.outage_increment_mw_label.setText(QApplication.translate("Form", "Outage Increment (MW)"))
        self.maintenance_sculpting_checkBox.setText(QApplication.translate("Form", "Maintenance Sculpting"))
        self.stochastic_method_groupBox.setTitle(QApplication.translate("Form", "Stochastic Method"))
        self.deterministic_radioButton.setText(QApplication.translate("Form", "Deterministic"))
        self.independant_samples_sequential_radioButton.setText(QApplication.translate("Form", "Indepentent Samples (Sequential)"))
        self.independant_samples_partial_radioButton.setText(QApplication.translate("Form", "Independent Samples (Partial)"))
        self.scenariowise_decomposition_radioButton.setText(QApplication.translate("Form", "Scenario-wise Decomposition"))
        self.transmission_groupBox.setTitle(QApplication.translate("Form", "Transmission"))
        self.regional_radioButton.setText(QApplication.translate("Form", "Regional"))
        self.zonal_radioButton.setText(QApplication.translate("Form", "Zonal"))
        self.nodal_radioButton.setText(QApplication.translate("Form", "Nodal"))
        self.heat_rate_groupBox.setTitle(QApplication.translate("Form", "Heat Rate"))
        self.detailed_radioButton.setText(QApplication.translate("Form", "Detailed"))
        self.simple_radioButton.setText(QApplication.translate("Form", "Simple"))
        self.simplest_radioButton.setText(QApplication.translate("Form", "Simplest"))
        self.pricing_groupBox.setTitle(QApplication.translate("Form", "Pricing"))
        self.average_radioButton.setText(QApplication.translate("Form", "Average"))
        self.marginal_radioButton.setText(QApplication.translate("Form", "Marginal"))
        self.generation_pricing_method_label.setText(QApplication.translate("Form", "Generation Pricing Method:"))
        self.make_capacity_payments_checkBox.setText(QApplication.translate("Form", "Make Capacity Payments"))
        self.start_cost_amortization_hrs_label.setText(QApplication.translate("Form", "Start Cost Amortization (hrs):"))
        self.output_groupBox.setTitle(QApplication.translate("Form", "Output"))
        self.write_expansion_plan_to_text_files_checkBox.setText(QApplication.translate("Form", "Write Expansion Plan to Text Files"))
        self.step_size_groupBox.setTitle(QApplication.translate("Form", "Step Size"))
        self.step_size_years_label.setText(QApplication.translate("Form", "Step Size (years):"))
        self.overlap_years_label.setText(QApplication.translate("Form", "Overlap (years):"))
        self.chronology_groupBox.setTitle(QApplication.translate("Form", "Chronology"))
        self.partial_radioButton.setText(QApplication.translate("Form", "Partial"))
        self.fitterd_radioButton.setText(QApplication.translate("Form", "Fitted"))
        self.samples_radioButton.setText(QApplication.translate("Form", "Sampled"))
        self.one_duration_curve_each_groupBox.setTitle(QApplication.translate("Form", "One Duration Curve Each"))
        self.day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.month_radioButton.setText(QApplication.translate("Form", "Month"))
        self.year_radioButton.setText(QApplication.translate("Form", "Year"))
        self.blocks_in_each_duration_curve_label.setText(QApplication.translate("Form", "Blocks in each Duration Curve:"))
        self.blocks_in_last_curve_in_horizon_label.setText(QApplication.translate("Form", "Blocks in last curve in Horizon"))
        self.slicing_method_groupBox.setTitle(QApplication.translate("Form", "Slicing Method"))
        self.peak_offpeak_bias_radioButton.setText(QApplication.translate("Form", "Peak/Off-peak Bias"))
        self.weighted_leastsquares_fit_radioButton.setText(QApplication.translate("Form", "Weighted Least-squares Fit"))
        self.pin_top_label.setText(QApplication.translate("Form", "Pin Top:"))
        self.pin_bottom_label.setText(QApplication.translate("Form", "Pin Bottom:"))
        self.sample_groupBox.setTitle(QApplication.translate("Form", "Sample"))
        self.sample_day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.samples_per_year_label.setText(QApplication.translate("Form", "Samples per Year"))
        self.sample_week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.sample_month_radioButton.setText(QApplication.translate("Form", "Month"))
        self.discounting_groupBox.setTitle(QApplication.translate("Form", "Discounting"))
        self.discounting_rate_label.setText(QApplication.translate("Form", "Discounting Rate (%)"))
        self.end_effects_methods_label.setText(QApplication.translate("Form", "End Effects Method"))
        self.depreciation_method_label.setText(QApplication.translate("Form", "Depreciation Method"))
        self.none_radioButton.setText(QApplication.translate("Form", "None"))
        self.none_radioButton_2.setText(QApplication.translate("Form", "None"))
        self.tax_rate_label.setText(QApplication.translate("Form", "Tax Rate (%)"))
        self.inflation_rate_label.setText(QApplication.translate("Form", "Inflation Rate (%)"))
        self.straight_line_radioButton.setText(QApplication.translate("Form", "Straight-Line"))
        self.declining_radioButton.setText(QApplication.translate("Form", "Declining"))
        self.perpetuity_radioButton.setText(QApplication.translate("Form", "Perpetuity"))
        self.expansion_algorithm_groupBox.setTitle(QApplication.translate("Form", "Expansion Algorithm"))
        self.explansion_decisions_integer_optimality_label.setText(QApplication.translate("Form", "Expansion Decisions Integer Optimality:"))
        self.linear_radioButton.setText(QApplication.translate("Form", "Linear"))
        self.integer_radioButton.setText(QApplication.translate("Form", "Integer"))
        self.allow_capacity_sharing_checkBox.setText(QApplication.translate("Form", "Allow Capacity Sharing"))
        self.integration_horizon_years_label.setText(QApplication.translate("Form", "Integerization Horizon (years):"))
        self.solution_hierarchy_groupBox.setTitle(QApplication.translate("Form", "Solution Hierachy"))
        self.number_of_solutions_label.setText(QApplication.translate("Form", "Number of Solutions:"))
        self.solution_quality_label.setText(QApplication.translate("Form", "Solution Quality (%):"))
