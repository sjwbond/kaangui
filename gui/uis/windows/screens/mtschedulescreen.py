# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mtschedulescreen.ui'
#
# Created: Tue Jun 21 17:16:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

mtschedule_default_input = {
    "discount_rate": 0,
    "simulation_steps": 0,
    "use_effective_load_approach": False,
    "time_lag": 12,
    "blocks_in_each_duration_curve": 12,
    "blocks_in_last_curve_in_horizon": 0,
    "samples_per_year": 4,
    "pin_top": -1,
    "pin_bottom": -1,
    "weight_a_constant": 0,
    "weight_b_linear": 1,
    "weight_c_quadratic": 0,
    "weight_d_cubic": 0,
    "start_cost_amortization_hrs": 0,
    "outage_increment_mw": 0,
    "discount_period": "",
    "end_effects_method": "",
    "steps_in_each_simulation": "",
    "chronology": "",
    "one_duration_curve_each": "",
    "slicing_method": "",
    "sample": "Week",
    "new_entry_driver": "",
    "capacity_mechanism": "",
    "heat_rate": "",
    "generation_pricing_method": "",
    "transmission": "",
    "stochastic_method": ""
}

class Ui_MTScheaduleScreen(QObject):
    input = mtschedule_default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1643, 789)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.discounting_groupBox = QGroupBox(self.groupBox_2)
        self.discounting_groupBox.setObjectName("discounting_groupBox")
        self.gridLayout_5 = QGridLayout(self.discounting_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_19 = QGroupBox(self.discounting_groupBox)
        self.groupBox_19.setTitle("")
        self.groupBox_19.setObjectName("groupBox_19")
        self.gridLayout_19 = QGridLayout(self.groupBox_19)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.hour_radioButton = QRadioButton(self.groupBox_19)
        self.hour_radioButton.setObjectName("hour_radioButton")
        self.gridLayout_19.addWidget(self.hour_radioButton, 1, 2, 1, 1)
        self.week_radioButton = QRadioButton(self.groupBox_19)
        self.week_radioButton.setObjectName("week_radioButton")
        self.gridLayout_19.addWidget(self.week_radioButton, 1, 3, 1, 1)
        self.discount_period_label = QLabel(self.groupBox_19)
        self.discount_period_label.setObjectName("discount_period_label")
        self.gridLayout_19.addWidget(self.discount_period_label, 0, 0, 1, 1)
        self.month_radioButton = QRadioButton(self.groupBox_19)
        self.month_radioButton.setObjectName("month_radioButton")
        self.gridLayout_19.addWidget(self.month_radioButton, 1, 0, 1, 1)
        self.day_radioButton = QRadioButton(self.groupBox_19)
        self.day_radioButton.setObjectName("day_radioButton")
        self.gridLayout_19.addWidget(self.day_radioButton, 1, 1, 1, 1)
        self.year_radioButton = QRadioButton(self.groupBox_19)
        self.year_radioButton.setObjectName("year_radioButton")
        self.gridLayout_19.addWidget(self.year_radioButton, 1, 4, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_19, 2, 0, 1, 1)
        self.discount_rate_label = QLabel(self.discounting_groupBox)
        self.discount_rate_label.setObjectName("discount_rate_label")
        self.gridLayout_5.addWidget(self.discount_rate_label, 0, 0, 1, 2)
        self.discount_rate_spinBox = QSpinBox(self.discounting_groupBox)
        self.discount_rate_spinBox.setObjectName("discount_rate_spinBox")
        self.gridLayout_5.addWidget(self.discount_rate_spinBox, 0, 2, 1, 1)
        self.groupBox_18 = QGroupBox(self.discounting_groupBox)
        self.groupBox_18.setTitle("")
        self.groupBox_18.setObjectName("groupBox_18")
        self.gridLayout_18 = QGridLayout(self.groupBox_18)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.end_effects_method_label = QLabel(self.groupBox_18)
        self.end_effects_method_label.setObjectName("end_effects_method_label")
        self.gridLayout_18.addWidget(self.end_effects_method_label, 0, 0, 1, 1)
        self.none_radioButton = QRadioButton(self.groupBox_18)
        self.none_radioButton.setObjectName("none_radioButton")
        self.gridLayout_18.addWidget(self.none_radioButton, 1, 0, 1, 1)
        self.perpetuity_radioButton = QRadioButton(self.groupBox_18)
        self.perpetuity_radioButton.setObjectName("perpetuity_radioButton")
        self.gridLayout_18.addWidget(self.perpetuity_radioButton, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_18, 1, 0, 1, 2)
        self.gridLayout_7.addWidget(self.discounting_groupBox, 0, 0, 1, 1)
        self.generation_expansion_groupBox = QGroupBox(self.groupBox_2)
        self.generation_expansion_groupBox.setObjectName("generation_expansion_groupBox")
        self.gridLayout_6 = QGridLayout(self.generation_expansion_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.time_lag_label = QLabel(self.generation_expansion_groupBox)
        self.time_lag_label.setObjectName("time_lag_label")
        self.gridLayout_6.addWidget(self.time_lag_label, 3, 0, 1, 4)
        self.groupBox_20 = QGroupBox(self.generation_expansion_groupBox)
        self.groupBox_20.setTitle("")
        self.groupBox_20.setObjectName("groupBox_20")
        self.gridLayout_20 = QGridLayout(self.groupBox_20)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.new_entry_driver_label = QLabel(self.groupBox_20)
        self.new_entry_driver_label.setObjectName("new_entry_driver_label")
        self.gridLayout_20.addWidget(self.new_entry_driver_label, 0, 0, 1, 1)
        self.none_radioButton = QRadioButton(self.groupBox_20)
        self.none_radioButton.setChecked(False)
        self.none_radioButton.setObjectName("none_radioButton")
        self.gridLayout_20.addWidget(self.none_radioButton, 1, 0, 1, 1)
        self.reliability_enterpreneurial_radioButton = QRadioButton(self.groupBox_20)
        self.reliability_enterpreneurial_radioButton.setObjectName("reliability_enterpreneurial_radioButton")
        self.gridLayout_20.addWidget(self.reliability_enterpreneurial_radioButton, 2, 0, 1, 1)
        self.reliability_only_radioButton = QRadioButton(self.groupBox_20)
        self.reliability_only_radioButton.setObjectName("reliability_only_radioButton")
        self.gridLayout_20.addWidget(self.reliability_only_radioButton, 1, 1, 1, 1)
        self.enterpreneurial_only_radioButton = QRadioButton(self.groupBox_20)
        self.enterpreneurial_only_radioButton.setObjectName("enterpreneurial_only_radioButton")
        self.gridLayout_20.addWidget(self.enterpreneurial_only_radioButton, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_20, 0, 0, 1, 1)
        self.groupBox_21 = QGroupBox(self.generation_expansion_groupBox)
        self.groupBox_21.setTitle("")
        self.groupBox_21.setObjectName("groupBox_21")
        self.gridLayout_21 = QGridLayout(self.groupBox_21)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.none_radioButton_2 = QRadioButton(self.groupBox_21)
        self.none_radioButton_2.setCheckable(True)
        self.none_radioButton_2.setChecked(False)
        self.none_radioButton_2.setObjectName("none_radioButton_2")
        self.gridLayout_21.addWidget(self.none_radioButton_2, 1, 0, 1, 1)
        self.capacity_payment_radioButton = QRadioButton(self.groupBox_21)
        self.capacity_payment_radioButton.setObjectName("capacity_payment_radioButton")
        self.gridLayout_21.addWidget(self.capacity_payment_radioButton, 1, 1, 1, 1)
        self.capacity_mechanism_label = QLabel(self.groupBox_21)
        self.capacity_mechanism_label.setObjectName("capacity_mechanism_label")
        self.gridLayout_21.addWidget(self.capacity_mechanism_label, 0, 0, 1, 1)
        self.reserve_trader_radioButton = QRadioButton(self.groupBox_21)
        self.reserve_trader_radioButton.setObjectName("reserve_trader_radioButton")
        self.gridLayout_21.addWidget(self.reserve_trader_radioButton, 1, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_21, 4, 0, 1, 1)
        self.time_lag_spinBox = QSpinBox(self.generation_expansion_groupBox)
        self.time_lag_spinBox.setProperty("value", 12)
        self.time_lag_spinBox.setObjectName("time_lag_spinBox")
        self.gridLayout_6.addWidget(self.time_lag_spinBox, 3, 4, 1, 1)
        self.gridLayout_7.addWidget(self.generation_expansion_groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pricing_groupBox = QGroupBox(self.groupBox_3)
        self.pricing_groupBox.setObjectName("pricing_groupBox")
        self.gridLayout_9 = QGridLayout(self.pricing_groupBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.generation_pricing_method_label = QLabel(self.pricing_groupBox)
        self.generation_pricing_method_label.setObjectName("generation_pricing_method_label")
        self.gridLayout_9.addWidget(self.generation_pricing_method_label, 0, 0, 1, 2)
        self.start_cost_amortization_label = QLabel(self.pricing_groupBox)
        self.start_cost_amortization_label.setObjectName("start_cost_amortization_label")
        self.gridLayout_9.addWidget(self.start_cost_amortization_label, 2, 0, 1, 1)
        self.average_radioButton = QRadioButton(self.pricing_groupBox)
        self.average_radioButton.setObjectName("average_radioButton")
        self.gridLayout_9.addWidget(self.average_radioButton, 1, 0, 1, 1)
        self.start_cost_amortization_hrs_spinBox = QSpinBox(self.pricing_groupBox)
        self.start_cost_amortization_hrs_spinBox.setObjectName("start_cost_amortization_hrs_spinBox")
        self.gridLayout_9.addWidget(self.start_cost_amortization_hrs_spinBox, 2, 1, 1, 1)
        self.marginal_radioButton = QRadioButton(self.pricing_groupBox)
        self.marginal_radioButton.setObjectName("marginal_radioButton")
        self.gridLayout_9.addWidget(self.marginal_radioButton, 1, 1, 1, 2)
        self.gridLayout_8.addWidget(self.pricing_groupBox, 0, 0, 1, 1)
        self.reliability_groupBox = QGroupBox(self.groupBox_3)
        self.reliability_groupBox.setObjectName("reliability_groupBox")
        self.gridLayout_10 = QGridLayout(self.reliability_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.use_effective_load_approach_checkBox = QCheckBox(self.reliability_groupBox)
        self.use_effective_load_approach_checkBox.setObjectName("use_effective_load_approach_checkBox")
        self.gridLayout_10.addWidget(self.use_effective_load_approach_checkBox, 0, 0, 1, 1)
        self.outage_increment_label = QLabel(self.reliability_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outage_increment_label.sizePolicy().hasHeightForWidth())
        self.outage_increment_label.setSizePolicy(sizePolicy)
        self.outage_increment_label.setObjectName("outage_increment_label")
        self.gridLayout_10.addWidget(self.outage_increment_label, 1, 0, 1, 1)
        self.outage_increment_mw_spinBox = QSpinBox(self.reliability_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outage_increment_mw_spinBox.sizePolicy().hasHeightForWidth())
        self.outage_increment_mw_spinBox.setSizePolicy(sizePolicy)
        self.outage_increment_mw_spinBox.setObjectName("outage_increment_mw_spinBox")
        self.gridLayout_10.addWidget(self.outage_increment_mw_spinBox, 1, 1, 1, 1)
        self.gridLayout_8.addWidget(self.reliability_groupBox, 1, 0, 1, 1)
        self.stochastic_method_groupBox = QGroupBox(self.groupBox_3)
        self.stochastic_method_groupBox.setObjectName("stochastic_method_groupBox")
        self.gridLayout_11 = QGridLayout(self.stochastic_method_groupBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.deterministic_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.deterministic_radioButton.setObjectName("deterministic_radioButton")
        self.gridLayout_11.addWidget(self.deterministic_radioButton, 0, 0, 1, 1)
        self.independant_samples_sequential_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_sequential_radioButton.setObjectName("independant_samples_sequential_radioButton")
        self.gridLayout_11.addWidget(self.independant_samples_sequential_radioButton, 1, 0, 1, 1)
        self.independant_samples_parallel_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_parallel_radioButton.setObjectName("independant_samples_parallel_radioButton")
        self.gridLayout_11.addWidget(self.independant_samples_parallel_radioButton, 2, 0, 1, 1)
        self.scenariowise_decomposition_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.scenariowise_decomposition_radioButton.setObjectName("scenariowise_decomposition_radioButton")
        self.gridLayout_11.addWidget(self.scenariowise_decomposition_radioButton, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.stochastic_method_groupBox, 2, 0, 1, 1)
        self.heat_rate_groupBox = QGroupBox(self.groupBox_3)
        self.heat_rate_groupBox.setObjectName("heat_rate_groupBox")
        self.gridLayout_12 = QGridLayout(self.heat_rate_groupBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.detailed_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.detailed_radioButton.setObjectName("detailed_radioButton")
        self.gridLayout_12.addWidget(self.detailed_radioButton, 0, 0, 1, 1)
        self.simple_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simple_radioButton.setObjectName("simple_radioButton")
        self.gridLayout_12.addWidget(self.simple_radioButton, 0, 1, 1, 1)
        self.simplest_radioButton = QRadioButton(self.heat_rate_groupBox)
        self.simplest_radioButton.setObjectName("simplest_radioButton")
        self.gridLayout_12.addWidget(self.simplest_radioButton, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.heat_rate_groupBox, 3, 0, 1, 1)
        self.transmission_groupBox = QGroupBox(self.groupBox_3)
        self.transmission_groupBox.setObjectName("transmission_groupBox")
        self.gridLayout_13 = QGridLayout(self.transmission_groupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.regional_radioButton = QRadioButton(self.transmission_groupBox)
        self.regional_radioButton.setObjectName("regional_radioButton")
        self.gridLayout_13.addWidget(self.regional_radioButton, 0, 0, 1, 1)
        self.zonal_radioButton = QRadioButton(self.transmission_groupBox)
        self.zonal_radioButton.setObjectName("zonal_radioButton")
        self.gridLayout_13.addWidget(self.zonal_radioButton, 0, 1, 1, 1)
        self.nodal_radioButton = QRadioButton(self.transmission_groupBox)
        self.nodal_radioButton.setObjectName("nodal_radioButton")
        self.gridLayout_13.addWidget(self.nodal_radioButton, 0, 2, 1, 1)
        self.gridLayout_8.addWidget(self.transmission_groupBox, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 3, 1, 1)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_17 = QGridLayout(self.groupBox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.simulation_steps_groupBox = QGroupBox(self.groupBox)
        self.simulation_steps_groupBox.setObjectName("simulation_steps_groupBox")
        self.gridLayout_3 = QGridLayout(self.simulation_steps_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.day_radioButton_4 = QRadioButton(self.simulation_steps_groupBox)
        self.day_radioButton_4.setObjectName("day_radioButton_4")
        self.gridLayout_3.addWidget(self.day_radioButton_4, 0, 0, 1, 1)
        self.week_radioButton_4 = QRadioButton(self.simulation_steps_groupBox)
        self.week_radioButton_4.setObjectName("week_radioButton_4")
        self.gridLayout_3.addWidget(self.week_radioButton_4, 0, 1, 1, 1)
        self.month_radioButton_4 = QRadioButton(self.simulation_steps_groupBox)
        self.month_radioButton_4.setObjectName("month_radioButton_4")
        self.gridLayout_3.addWidget(self.month_radioButton_4, 0, 2, 1, 1)
        self.year_radioButton_4 = QRadioButton(self.simulation_steps_groupBox)
        self.year_radioButton_4.setCheckable(True)
        self.year_radioButton_4.setObjectName("year_radioButton_4")
        self.gridLayout_3.addWidget(self.year_radioButton_4, 0, 3, 1, 1)
        self.in_each_simulation_step_label = QLabel(self.simulation_steps_groupBox)
        self.in_each_simulation_step_label.setObjectName("in_each_simulation_step_label")
        self.gridLayout_3.addWidget(self.in_each_simulation_step_label, 0, 4, 1, 1)
        self.simulation_steps_spinBox = QSpinBox(self.simulation_steps_groupBox)
        self.simulation_steps_spinBox.setObjectName("simulation_steps_spinBox")
        self.simulation_steps_spinBox.setMaximum(10000000)
        self.gridLayout_3.addWidget(self.simulation_steps_spinBox, 1, 0, 1, 1)
        self.gridLayout_17.addWidget(self.simulation_steps_groupBox, 0, 0, 1, 1)
        self.chronology_groupBox = QGroupBox(self.groupBox)
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
        self.fitted_radioButton = QRadioButton(self.chronology_groupBox)
        self.fitted_radioButton.setObjectName("fitted_radioButton")
        self.verticalLayout_2.addWidget(self.fitted_radioButton)
        self.sampled_radioButton = QRadioButton(self.chronology_groupBox)
        self.sampled_radioButton.setObjectName("sampled_radioButton")
        self.verticalLayout_2.addWidget(self.sampled_radioButton)
        self.one_duration_curve_each_groupBox = QGroupBox(self.chronology_groupBox)
        self.one_duration_curve_each_groupBox.setObjectName("one_duration_curve_each_groupBox")
        self.gridLayout_2 = QGridLayout(self.one_duration_curve_each_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_17 = QGroupBox(self.one_duration_curve_each_groupBox)
        self.groupBox_17.setEnabled(False)
        self.groupBox_17.setTitle("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.gridLayout_16 = QGridLayout(self.groupBox_17)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.weight_a_constant_label = QLabel(self.groupBox_17)
        self.weight_a_constant_label.setObjectName("weight_a_constant_label")
        self.gridLayout_16.addWidget(self.weight_a_constant_label, 0, 0, 1, 1)
        self.weight_a_constant_spinBox = QSpinBox(self.groupBox_17)
        self.weight_a_constant_spinBox.setMinimum(-10000000)
        self.weight_a_constant_spinBox.setMaximum(10000000)
        self.weight_a_constant_spinBox.setObjectName("weight_a_constant_spinBox")
        self.gridLayout_16.addWidget(self.weight_a_constant_spinBox, 0, 1, 1, 1)
        self.weight_b_linear_label = QLabel(self.groupBox_17)
        self.weight_b_linear_label.setObjectName("weight_b_linear_label")
        self.gridLayout_16.addWidget(self.weight_b_linear_label, 1, 0, 1, 1)
        self.weight_b_linear_spinBox = QSpinBox(self.groupBox_17)
        self.weight_b_linear_spinBox.setMinimum(-1000000)
        self.weight_b_linear_spinBox.setMaximum(1000000)
        self.weight_b_linear_spinBox.setProperty("value", 1)
        self.weight_b_linear_spinBox.setObjectName("weight_b_linear_spinBox")
        self.gridLayout_16.addWidget(self.weight_b_linear_spinBox, 1, 1, 1, 1)
        self.weight_c_quadratic_label = QLabel(self.groupBox_17)
        self.weight_c_quadratic_label.setObjectName("weight_c_quadratic_label")
        self.gridLayout_16.addWidget(self.weight_c_quadratic_label, 2, 0, 1, 1)
        self.weight_c_quadratic_spinBox = QSpinBox(self.groupBox_17)
        self.weight_c_quadratic_spinBox.setMinimum(-1000000)
        self.weight_c_quadratic_spinBox.setMaximum(1000000)
        self.weight_c_quadratic_spinBox.setObjectName("weight_c_quadratic_spinBox")
        self.gridLayout_16.addWidget(self.weight_c_quadratic_spinBox, 2, 1, 1, 1)
        self.weight_d_cubic_spinBox_label = QLabel(self.groupBox_17)
        self.weight_d_cubic_spinBox_label.setObjectName("weight_d_cubic_spinBox_label")
        self.gridLayout_16.addWidget(self.weight_d_cubic_spinBox_label, 3, 0, 1, 1)
        self.weight_d_cubic_spinBox = QSpinBox(self.groupBox_17)
        self.weight_d_cubic_spinBox.setMinimum(-100000)
        self.weight_d_cubic_spinBox.setMaximum(100000)
        self.weight_d_cubic_spinBox.setObjectName("weight_d_cubic_spinBox")
        self.gridLayout_16.addWidget(self.weight_d_cubic_spinBox, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_17, 7, 0, 1, 2)
        self.slicing_method_groupBox = QGroupBox(self.one_duration_curve_each_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slicing_method_groupBox.sizePolicy().hasHeightForWidth())
        self.slicing_method_groupBox.setSizePolicy(sizePolicy)
        self.slicing_method_groupBox.setObjectName("slicing_method_groupBox")
        self.gridLayout_15 = QGridLayout(self.slicing_method_groupBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.weighted_least_squares_fit_radioButton = QRadioButton(self.slicing_method_groupBox)
        self.weighted_least_squares_fit_radioButton.setObjectName("weighted_least_squares_fit_radioButton")
        self.gridLayout_15.addWidget(self.weighted_least_squares_fit_radioButton, 1, 0, 1, 1)
        self.peak_offpear_bias_radioButton = QRadioButton(self.slicing_method_groupBox)
        self.peak_offpear_bias_radioButton.setObjectName("peak_offpear_bias_radioButton")
        self.gridLayout_15.addWidget(self.peak_offpear_bias_radioButton, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.slicing_method_groupBox, 6, 0, 1, 2)
        self.blocks_in_each_duration_curve_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.blocks_in_each_duration_curve_spinBox.setProperty("value", 12)
        self.blocks_in_each_duration_curve_spinBox.setObjectName("blocks_in_each_duration_curve_spinBox")
        self.gridLayout_2.addWidget(self.blocks_in_each_duration_curve_spinBox, 4, 1, 1, 1)
        self.pin_top_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.pin_top_spinBox.setMinimum(-1)
        self.pin_top_spinBox.setProperty("value", -1)
        self.pin_top_spinBox.setObjectName("pin_top_spinBox")
        self.gridLayout_2.addWidget(self.pin_top_spinBox, 8, 1, 1, 1)
        self.pin_bottom_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.pin_bottom_spinBox.setMinimum(-1)
        self.pin_bottom_spinBox.setProperty("value", -1)
        self.pin_bottom_spinBox.setObjectName("pin_bottom_spinBox")
        self.gridLayout_2.addWidget(self.pin_bottom_spinBox, 9, 1, 1, 1)
        self.pin_bottom_label = QLabel(self.one_duration_curve_each_groupBox)
        self.pin_bottom_label.setObjectName("pin_bottom_label")
        self.gridLayout_2.addWidget(self.pin_bottom_label, 9, 0, 1, 1)
        self.pin_top_button = QLabel(self.one_duration_curve_each_groupBox)
        self.pin_top_button.setObjectName("pin_top_button")
        self.gridLayout_2.addWidget(self.pin_top_button, 8, 0, 1, 1)
        self.blocks_in_last_curve_label = QLabel(self.one_duration_curve_each_groupBox)
        self.blocks_in_last_curve_label.setObjectName("blocks_in_last_curve_label")
        self.gridLayout_2.addWidget(self.blocks_in_last_curve_label, 5, 0, 1, 1)
        self.blocks_in_last_curve_in_horizon_spinBox = QSpinBox(self.one_duration_curve_each_groupBox)
        self.blocks_in_last_curve_in_horizon_spinBox.setObjectName("blocks_in_last_curve_in_horizon_spinBox")
        self.gridLayout_2.addWidget(self.blocks_in_last_curve_in_horizon_spinBox, 5, 1, 1, 1)
        self.blocks_in_each_duration_curve_label = QLabel(self.one_duration_curve_each_groupBox)
        self.blocks_in_each_duration_curve_label.setObjectName("blocks_in_each_duration_curve_label")
        self.gridLayout_2.addWidget(self.blocks_in_each_duration_curve_label, 4, 0, 1, 1)
        self.week_radioButton_2 = QRadioButton(self.one_duration_curve_each_groupBox)
        self.week_radioButton_2.setObjectName("week_radioButton_2")
        self.gridLayout_2.addWidget(self.week_radioButton_2, 1, 0, 1, 1)
        self.day_radioButton_2 = QRadioButton(self.one_duration_curve_each_groupBox)
        self.day_radioButton_2.setObjectName("day_radioButton_2")
        self.gridLayout_2.addWidget(self.day_radioButton_2, 0, 0, 1, 1)
        self.month_radioButton_2 = QRadioButton(self.one_duration_curve_each_groupBox)
        self.month_radioButton_2.setObjectName("month_radioButton_2")
        self.gridLayout_2.addWidget(self.month_radioButton_2, 0, 1, 1, 1)
        self.year_radioButton_2 = QRadioButton(self.one_duration_curve_each_groupBox)
        self.year_radioButton_2.setObjectName("year_radioButton_2")
        self.gridLayout_2.addWidget(self.year_radioButton_2, 1, 1, 1, 1)
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
        self.day_radioButton_3 = QRadioButton(self.sample_groupBox)
        self.day_radioButton_3.setObjectName("day_radioButton_3")
        self.gridLayout_4.addWidget(self.day_radioButton_3, 0, 0, 1, 1)
        self.samples_per_year_spinBox = QSpinBox(self.sample_groupBox)
        self.samples_per_year_spinBox.setProperty("value", 4)
        self.samples_per_year_spinBox.setObjectName("samples_per_year_spinBox")
        self.gridLayout_4.addWidget(self.samples_per_year_spinBox, 1, 1, 1, 1)
        self.samples_per_year_label = QLabel(self.sample_groupBox)
        self.samples_per_year_label.setObjectName("samples_per_year_label")
        self.gridLayout_4.addWidget(self.samples_per_year_label, 1, 0, 1, 1)
        self.week_radioButton_3 = QRadioButton(self.sample_groupBox)
        self.week_radioButton_3.setChecked(True)
        self.week_radioButton_3.setObjectName("week_radioButton_3")
        self.gridLayout_4.addWidget(self.week_radioButton_3, 0, 1, 1, 1)
        self.month_radioButton_3 = QRadioButton(self.sample_groupBox)
        self.month_radioButton_3.setObjectName("month_radioButton_3")
        self.gridLayout_4.addWidget(self.month_radioButton_3, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.sample_groupBox)
        self.gridLayout_17.addWidget(self.chronology_groupBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)


        self.retranslateUi(Form)

        self.partial_radioButton.clicked.connect(self.enableChoronology)
        self.fitted_radioButton.clicked.connect(self.enableChoronology)
        self.sampled_radioButton.clicked.connect(self.enableChoronology)

        self.peak_offpear_bias_radioButton.clicked.connect(self.enableWeights)
        self.weighted_least_squares_fit_radioButton.clicked.connect(self.enableWeights)

        self.day_radioButton.clicked.connect(self.simulationSteps)
        self.week_radioButton.clicked.connect(self.simulationSteps)
        self.month_radioButton.clicked.connect(self.simulationSteps)
        self.year_radioButton.clicked.connect(self.simulationSteps)



        QMetaObject.connectSlotsByName(Form)
    
    def setInput(self, input):
        self.input = input
        self.loadmtschedulescreen()
        self.enableChoronology()
        self.enableWeights()
    
    def getOutput(self):
        self.savemtschedulescreen()
        return self.output

    def savemtschedulescreen(self):
        self.output = mtschedule_default_input | {
            "discount_rate": self.discount_rate_spinBox.value(),
            "simulation_steps": self.simulation_steps_spinBox.value(),
            "use_effective_load_approach": self.use_effective_load_approach_checkBox.isChecked(),
            "time_lag": self.time_lag_spinBox.value(),
            "blocks_in_each_duration_curve": self.blocks_in_each_duration_curve_spinBox.value(),
            "blocks_in_last_curve_in_horizon": self.blocks_in_last_curve_in_horizon_spinBox.value(),
            "samples_per_year": self.samples_per_year_spinBox.value(),
            "pin_top": self.pin_top_spinBox.value(),
            "pin_bottom": self.pin_bottom_spinBox.value(),
            "weight_a_constant": self.weight_a_constant_spinBox.value(),
            "weight_b_linear": self.weight_b_linear_spinBox.value(),
            "weight_c_quadratic": self.weight_c_quadratic_spinBox.value(),
            "weight_d_cubic": self.weight_d_cubic_spinBox.value(),
            "start_cost_amortization_hrs": self.start_cost_amortization_hrs_spinBox.value(),
            "outage_increment_mw": self.outage_increment_mw_spinBox.value()
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

        if self.day_radioButton_4.isChecked():
            self.output["steps_in_each_simulation"] = "Day"
        if self.week_radioButton_4.isChecked():
            self.output["steps_in_each_simulation"] = "Week"
        if self.month_radioButton_4.isChecked():
            self.output["steps_in_each_simulation"] = "Month"
        if self.year_radioButton_4.isChecked():
            self.output["steps_in_each_simulation"] = "Year"

        if self.partial_radioButton.isChecked():
            self.output["chronology"] = "Partial"
        if self.fitted_radioButton.isChecked():
            self.output["chronology"] = "Fitted"
        if self.sampled_radioButton.isChecked():
            self.output["chronology"] = "Sampled"

        if self.day_radioButton_2.isChecked():
            self.output["one_duration_curve_each"] = "Day"
        if self.week_radioButton_2.isChecked():
            self.output["one_duration_curve_each"] = "Week"
        if self.month_radioButton_2.isChecked():
            self.output["one_duration_curve_each"] = "Month"
        if self.year_radioButton_2.isChecked():
            self.output["one_duration_curve_each"] = "Year"

        if self.peak_offpear_bias_radioButton.isChecked():
            self.output["slicing_method"] = "Peak/Off-peak Bias"
        if self.weighted_least_squares_fit_radioButton.isChecked():
            self.output["slicing_method"] = "Weighted Least-squares Fit"

        if self.day_radioButton_3.isChecked():
            self.output["sample"] = "Day"
        if self.week_radioButton_3.isChecked():
            self.output["sample"] = "Week"
        if self.month_radioButton_3.isChecked():
            self.output["sample"] = "Month"

        if self.none_radioButton.isChecked():
            self.output["new_entry_driver"] = "None"
        if self.reliability_only_radioButton.isChecked():
            self.output["new_entry_driver"] = "Reliability Only"
        if self.reliability_enterpreneurial_radioButton.isChecked():
            self.output["new_entry_driver"] = "Reliability+Enterpreneurial"
        if self.enterpreneurial_only_radioButton.isChecked():
            self.output["new_entry_driver"] = "Entrepreneurial Only"

        if self.none_radioButton_2.isChecked():
            self.output["capacity_mechanism"] = "None Only"
        if self.capacity_payment_radioButton.isChecked():
            self.output["capacity_mechanism"] = "Capacity Payment"
        if self.reserve_trader_radioButton.isChecked():
            self.output["capacity_mechanism"] = "Reserve Trader"

        if self.detailed_radioButton.isChecked():
            self.output["heat_rate"] = "Detailed"
        if self.simple_radioButton.isChecked():
            self.output["heat_rate"] = "Simple"
        if self.simplest_radioButton.isChecked():
            self.output["heat_rate"] = "Simplest"

        if self.average_radioButton.isChecked():
            self.output["generation_pricing_method"] = "Average"
        if self.marginal_radioButton.isChecked():
            self.output["generation_pricing_method"] = "Marginal"

        if self.regional_radioButton.isChecked():
            self.output["transmission"] = "Regional"
        if self.zonal_radioButton.isChecked():
            self.output["transmission"] = "Zonal"
        if self.nodal_radioButton.isChecked():
            self.output["transmission"] = "Nodal"

        if self.deterministic_radioButton.isChecked():
            self.output["stochastic_method"] = "Deterministic"
        if self.independant_samples_sequential_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Sequential)"
        if self.independant_samples_parallel_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Parallel)"
        if self.scenariowise_decomposition_radioButton.isChecked():
            self.output["stochastic_method"] = "Scenario-wise Decomposition"

    def loadmtschedulescreen(self):
        self.discount_rate_spinBox.setValue(self.input["discount_rate"])
        self.simulation_steps_spinBox.setValue(self.input["simulation_steps"])
        self.use_effective_load_approach_checkBox.setChecked(self.input["use_effective_load_approach"])
        self.time_lag_spinBox.setValue(self.input["time_lag"])
        self.blocks_in_each_duration_curve_spinBox.setValue(self.input["blocks_in_each_duration_curve"])
        self.blocks_in_last_curve_in_horizon_spinBox.setValue(self.input["blocks_in_last_curve_in_horizon"])
        self.samples_per_year_spinBox.setValue(self.input["samples_per_year"])
        self.pin_top_spinBox.setValue(self.input["pin_top"])
        self.pin_bottom_spinBox.setValue(self.input["pin_bottom"])
        self.weight_a_constant_spinBox.setValue(self.input["weight_a_constant"])
        self.weight_b_linear_spinBox.setValue(self.input["weight_b_linear"])
        self.weight_c_quadratic_spinBox.setValue(self.input["weight_c_quadratic"])
        self.weight_d_cubic_spinBox.setValue(self.input["weight_d_cubic"])
        self.start_cost_amortization_hrs_spinBox.setValue(self.input["start_cost_amortization_hrs"])
        self.outage_increment_mw_spinBox.setValue(self.input["outage_increment_mw"])

        self.hour_radioButton.setChecked(self.input["discount_period"] == "Hour")
        self.day_radioButton.setChecked(self.input["discount_period"] == "Day")
        self.week_radioButton.setChecked(self.input["discount_period"] == "Week")
        self.month_radioButton.setChecked(self.input["discount_period"] == "Month")
        self.year_radioButton.setChecked(self.input["discount_period"] == "Year")

        self.none_radioButton.setChecked(self.input["end_effects_method"] == "None")
        self.perpetuity_radioButton.setChecked(self.input["end_effects_method"] == "Perpetuity")

        self.day_radioButton_4.setChecked(self.input["steps_in_each_simulation"] == "Day")
        self.week_radioButton_4.setChecked(self.input["steps_in_each_simulation"] == "Week")
        self.month_radioButton_4.setChecked(self.input["steps_in_each_simulation"] == "Month")
        self.year_radioButton_4.setChecked(self.input["steps_in_each_simulation"] == "Year")

        self.partial_radioButton.setChecked(self.input["chronology"] == "Partial")
        self.fitted_radioButton.setChecked(self.input["chronology"] == "Fitted")
        self.sampled_radioButton.setChecked(self.input["chronology"] == "Sampled")

        self.day_radioButton_2.setChecked(self.input["one_duration_curve_each"] == "Day")
        self.week_radioButton_2.setChecked(self.input["one_duration_curve_each"] == "Week")
        self.month_radioButton_2.setChecked(self.input["one_duration_curve_each"] == "Month")
        self.year_radioButton_2.setChecked(self.input["one_duration_curve_each"] == "Year")

        self.peak_offpear_bias_radioButton.setChecked(self.input["slicing_method"] == "Peak/Off-peak Bias")
        self.weighted_least_squares_fit_radioButton.setChecked(self.input["slicing_method"] == "Weighted Least-squares Fit")

        self.day_radioButton_3.setChecked(self.input["sample"] == "Day")
        self.week_radioButton_3.setChecked(self.input["sample"] == "Week")
        self.month_radioButton_3.setChecked(self.input["sample"] == "Month")

        self.none_radioButton.setChecked(self.input["new_entry_driver"] == "None")
        self.reliability_only_radioButton.setChecked(self.input["new_entry_driver"] == "Reliability Only")
        self.reliability_enterpreneurial_radioButton.setChecked(self.input["new_entry_driver"] == "Reliability+Enterpreneurial")
        self.enterpreneurial_only_radioButton.setChecked(self.input["new_entry_driver"] == "Entrepreneurial Only")

        self.none_radioButton_2.setChecked(self.input["capacity_mechanism"] == "None Only")
        self.capacity_payment_radioButton.setChecked(self.input["capacity_mechanism"] == "Capacity Payment")
        self.reserve_trader_radioButton.setChecked(self.input["capacity_mechanism"] == "Reserve Trader")

        self.detailed_radioButton.setChecked(self.input["heat_rate"] == "Detailed")
        self.simple_radioButton.setChecked(self.input["heat_rate"] == "Simple")
        self.simplest_radioButton.setChecked(self.input["heat_rate"] == "Simplest")

        self.average_radioButton.setChecked(self.input["generation_pricing_method"] == "Average")
        self.marginal_radioButton.setChecked(self.input["generation_pricing_method"] == "Marginal")

        self.regional_radioButton.setChecked(self.input["transmission"] == "Regional")
        self.zonal_radioButton.setChecked(self.input["transmission"] == "Zonal")
        self.nodal_radioButton.setChecked(self.input["transmission"] == "Nodal")

        self.deterministic_radioButton.setChecked(self.input["stochastic_method"] == "Deterministic")
        self.independant_samples_sequential_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Sequential)")
        self.independant_samples_parallel_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Parallel)")
        self.scenariowise_decomposition_radioButton.setChecked(self.input["stochastic_method"] == "Scenario-wise Decomposition")

    def enableChoronology(self):
        if self.sampled_radioButton.isChecked() == True:
            self.one_duration_curve_each_groupBox.setEnabled(False)
            self.sample_groupBox.setEnabled(True)
        else:
            self.one_duration_curve_each_groupBox.setEnabled(True)
            self.sample_groupBox.setEnabled(False)

    def enableWeights(self):
        if self.weighted_least_squares_fit_radioButton.isChecked() == True:
            self.groupBox_17.setEnabled(True)
        else:
            self.groupBox_17.setEnabled(False)

    def simulationSteps(self):
        if self.day_radioButton.isChecked() == True:
            self.simulation_steps_spinBox.setValue(366)
        if self.week_radioButton.isChecked() == True:
            self.simulation_steps_spinBox.setValue(53)
        if self.month_radioButton.isChecked() == True:
            self.simulation_steps_spinBox.setValue(12)
        if self.year_radioButton.isChecked() == True:
            self.simulation_steps_spinBox.setValue(1)



    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.discounting_groupBox.setTitle(QApplication.translate("Form", "Discounting"))
        self.hour_radioButton.setText(QApplication.translate("Form", "Hour"))
        self.week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.discount_period_label.setText(QApplication.translate("Form", "Discount Period"))
        self.month_radioButton.setText(QApplication.translate("Form", "Month"))
        self.day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.year_radioButton.setText(QApplication.translate("Form", "Year"))
        self.discount_rate_label.setText(QApplication.translate("Form", "Discount Rate (%):"))
        self.end_effects_method_label.setText(QApplication.translate("Form", "End Effects Method"))
        self.none_radioButton.setText(QApplication.translate("Form", "None"))
        self.perpetuity_radioButton.setText(QApplication.translate("Form", "Perpetuity"))
        self.generation_expansion_groupBox.setTitle(QApplication.translate("Form", "Generation Expansion"))
        self.time_lag_label.setText(QApplication.translate("Form", "Time Lag for Entrepreneurial Entry (months):"))
        self.new_entry_driver_label.setText(QApplication.translate("Form", "New Entry Driver:"))
        self.none_radioButton.setText(QApplication.translate("Form", "None"))
        self.reliability_enterpreneurial_radioButton.setText(QApplication.translate("Form", "Reliability+Enterpreneurial"))
        self.reliability_only_radioButton.setText(QApplication.translate("Form", "Reliability Only"))
        self.enterpreneurial_only_radioButton.setText(QApplication.translate("Form", "Entrepreneurial Only"))
        self.none_radioButton_2.setText(QApplication.translate("Form", "None"))
        self.capacity_payment_radioButton.setText(QApplication.translate("Form", "Capacity Payment"))
        self.capacity_mechanism_label.setText(QApplication.translate("Form", "Capacity Mechanism:"))
        self.reserve_trader_radioButton.setText(QApplication.translate("Form", "Reserve Trader"))
        self.pricing_groupBox.setTitle(QApplication.translate("Form", "Pricing"))
        self.generation_pricing_method_label.setText(QApplication.translate("Form", "Generation Pricing Method:"))
        self.start_cost_amortization_label.setText(QApplication.translate("Form", "Start Cost Amortization (hrs):"))
        self.average_radioButton.setText(QApplication.translate("Form", "Average"))
        self.marginal_radioButton.setText(QApplication.translate("Form", "Marginal"))
        self.reliability_groupBox.setTitle(QApplication.translate("Form", "Reliability"))
        self.use_effective_load_approach_checkBox.setText(QApplication.translate("Form", "Use Effective Load Approach"))
        self.outage_increment_label.setText(QApplication.translate("Form", "Outage Increment (MW):"))
        self.stochastic_method_groupBox.setTitle(QApplication.translate("Form", "Stochastic Method"))
        self.deterministic_radioButton.setText(QApplication.translate("Form", "Deterministic"))
        self.independant_samples_sequential_radioButton.setText(QApplication.translate("Form", "Independent Samples (Sequential)"))
        self.independant_samples_parallel_radioButton.setText(QApplication.translate("Form", "Independent Samples (Parallel)"))
        self.scenariowise_decomposition_radioButton.setText(QApplication.translate("Form", "Scenario-wise Decomposition"))
        self.heat_rate_groupBox.setTitle(QApplication.translate("Form", "Heat Rate"))
        self.detailed_radioButton.setText(QApplication.translate("Form", "Detailed"))
        self.simple_radioButton.setText(QApplication.translate("Form", "Simple"))
        self.simplest_radioButton.setText(QApplication.translate("Form", "Simplest"))
        self.transmission_groupBox.setTitle(QApplication.translate("Form", "Transmission"))
        self.regional_radioButton.setText(QApplication.translate("Form", "Regional"))
        self.zonal_radioButton.setText(QApplication.translate("Form", "Zonal"))
        self.nodal_radioButton.setText(QApplication.translate("Form", "Nodal"))
        self.simulation_steps_groupBox.setTitle(QApplication.translate("Form", "Simulation Steps"))
        self.day_radioButton_4.setText(QApplication.translate("Form", "Day"))
        self.week_radioButton_4.setText(QApplication.translate("Form", "Week"))
        self.month_radioButton_4.setText(QApplication.translate("Form", "Month"))
        self.year_radioButton_4.setText(QApplication.translate("Form", "Year"))
        self.in_each_simulation_step_label.setText(QApplication.translate("Form", "in each simuation step"))
        self.chronology_groupBox.setTitle(QApplication.translate("Form", "Chronology"))
        self.partial_radioButton.setText(QApplication.translate("Form", "Partial"))
        self.fitted_radioButton.setText(QApplication.translate("Form", "Fitted"))
        self.sampled_radioButton.setText(QApplication.translate("Form", "Sampled"))
        self.one_duration_curve_each_groupBox.setTitle(QApplication.translate("Form", "One Duration Curve Each"))
        self.weight_a_constant_label.setText(QApplication.translate("Form", "Weight a (constant):"))
        self.weight_b_linear_label.setText(QApplication.translate("Form", "Weight b (linear):"))
        self.weight_c_quadratic_label.setText(QApplication.translate("Form", "Weight c (quadratic)"))
        self.weight_d_cubic_spinBox_label.setText(QApplication.translate("Form", "Weight d (cubic)"))
        self.slicing_method_groupBox.setTitle(QApplication.translate("Form", "Slicing Methodd"))
        self.weighted_least_squares_fit_radioButton.setText(QApplication.translate("Form", "Weighted Least-squares Fit"))
        self.peak_offpear_bias_radioButton.setText(QApplication.translate("Form", "Peak/Off-peak Bias"))
        self.pin_bottom_label.setText(QApplication.translate("Form", "Pin Bottom:"))
        self.pin_top_button.setText(QApplication.translate("Form", "Pin Top:"))
        self.blocks_in_last_curve_label.setText(QApplication.translate("Form", "Blocks in last curve in Horizon"))
        self.blocks_in_each_duration_curve_label.setText(QApplication.translate("Form", "Blocks in each Duration Curve:"))
        self.week_radioButton_2.setText(QApplication.translate("Form", "Week"))
        self.day_radioButton_2.setText(QApplication.translate("Form", "Day"))
        self.month_radioButton_2.setText(QApplication.translate("Form", "Month"))
        self.year_radioButton_2.setText(QApplication.translate("Form", "Year"))
        self.sample_groupBox.setTitle(QApplication.translate("Form", "Sample"))
        self.day_radioButton_3.setText(QApplication.translate("Form", "Day"))
        self.samples_per_year_label.setText(QApplication.translate("Form", "Samples per Year"))
        self.week_radioButton_3.setText(QApplication.translate("Form", "Week"))
        self.month_radioButton_3.setText(QApplication.translate("Form", "Month"))