# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diagnosticscreen.ui'
#
# Created: Thu Jun 23 14:17:45 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

diagnostics_default_input = {
    "clear_existing_diagnostics": True,
    "task_size": True,
    "task_components": False,
    "lp_solver": False,
    "mip_solver": True,
    "solver_summary": False,
    "execution_times": True,
    "summary_each_sample": False,
    "summary_each_step": True,
    "step_from": "1",
    "step_to": "-1",
    "lp_files": False,
    "mps_files": False,
    "solution_files": False,
    "write_with_generic_names": False,
    "binary_files": False,
    "infeasibility_diagnostic_files": False,
    "max_infeasibility_log_lines": "-1",
    "bertrand_pricing": False,
    "revenue_recovery": False,
    "nashcournot": False,
    "rsi_bidcost_markup": False,
    "mt_schedule_new_entry": False,
    "ptdf_shift_factors": False,
    "unserved_energy": False,
    "interrupsion_sharing": False,
    "transmission_loss_matrices_and_convergence": False,
    "congestion_charges": False,
    "marginal_loss_charges": False,
    "binding_contingencies": False,
    "unit_commitment": False,
    "constraint_decomposition": False,
    "constraint_rollover": False,
    "uniform_pricing": False,
    "marginal_unit": False,
    "load_increment": "-1",
    "marginal_expansion_unit": False,
    "load_increment_2": "100",
    "region_supply": False,
    "lt_plan_annuities": False,
    "lt_plan_npv": False,
    "load_includes_losses_iterations": False,
    "pasa_outage_patterns": False,
    "random_number_seed": False,
    "interleaved_run_mode": False,
    "heat_rate": False,
    "objective_function": False,
    "future_cost_function": False,
    "write_scenario_tree": False,
    "write_sample_weights": False,
    "marginal_unit_transmission_detail": "Regional"
}

class Ui_DiagnosticsScreen(QObject):
    input = diagnostics_default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1068, 869)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.competetion_prixing_groupBox = QGroupBox(self.groupBox_2)
        self.competetion_prixing_groupBox.setObjectName("competetion_prixing_groupBox")
        self.gridLayout_10 = QGridLayout(self.competetion_prixing_groupBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.bertrand_pricing_checkBox = QCheckBox(self.competetion_prixing_groupBox)
        self.bertrand_pricing_checkBox.setObjectName("bertrand_pricing_checkBox")
        self.gridLayout_10.addWidget(self.bertrand_pricing_checkBox, 0, 0, 1, 1)
        self.revenue_recovery_checkBox = QCheckBox(self.competetion_prixing_groupBox)
        self.revenue_recovery_checkBox.setObjectName("revenue_recovery_checkBox")
        self.gridLayout_10.addWidget(self.revenue_recovery_checkBox, 1, 0, 1, 1)
        self.nashcournot_checkBox = QCheckBox(self.competetion_prixing_groupBox)
        self.nashcournot_checkBox.setObjectName("nashcournot_checkBox")
        self.gridLayout_10.addWidget(self.nashcournot_checkBox, 2, 0, 1, 1)
        self.rsi_bidcost_markup_checkBox = QCheckBox(self.competetion_prixing_groupBox)
        self.rsi_bidcost_markup_checkBox.setObjectName("rsi_bidcost_markup_checkBox")
        self.gridLayout_10.addWidget(self.rsi_bidcost_markup_checkBox, 3, 0, 1, 1)
        self.uniform_pricing_checkBox = QCheckBox(self.competetion_prixing_groupBox)
        self.uniform_pricing_checkBox.setObjectName("uniform_pricing_checkBox")
        self.gridLayout_10.addWidget(self.uniform_pricing_checkBox, 4, 0, 1, 1)
        self.gridLayout_8.addWidget(self.competetion_prixing_groupBox, 1, 0, 1, 1)
        self.constraint_diagnostics_checkBox = QGroupBox(self.groupBox_2)
        self.constraint_diagnostics_checkBox.setObjectName("constraint_diagnostics_checkBox")
        self.gridLayout_11 = QGridLayout(self.constraint_diagnostics_checkBox)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.constraint_decomposition_checkBox = QCheckBox(self.constraint_diagnostics_checkBox)
        self.constraint_decomposition_checkBox.setObjectName("constraint_decomposition_checkBox")
        self.gridLayout_11.addWidget(self.constraint_decomposition_checkBox, 0, 0, 1, 1)
        self.constraint_rollover_checkBox = QCheckBox(self.constraint_diagnostics_checkBox)
        self.constraint_rollover_checkBox.setObjectName("constraint_rollover_checkBox")
        self.gridLayout_11.addWidget(self.constraint_rollover_checkBox, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.constraint_diagnostics_checkBox, 2, 0, 1, 1)
        self.transmission_diagnostics_checkBox = QGroupBox(self.groupBox_2)
        self.transmission_diagnostics_checkBox.setObjectName("transmission_diagnostics_checkBox")
        self.gridLayout_12 = QGridLayout(self.transmission_diagnostics_checkBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.congestion_charges_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.congestion_charges_checkBox.setObjectName("congestion_charges_checkBox")
        self.gridLayout_12.addWidget(self.congestion_charges_checkBox, 1, 0, 1, 1)
        self.ptdf_shift_factors_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.ptdf_shift_factors_checkBox.setObjectName("ptdf_shift_factors_checkBox")
        self.gridLayout_12.addWidget(self.ptdf_shift_factors_checkBox, 0, 0, 1, 1)
        self.interrupsion_sharing_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.interrupsion_sharing_checkBox.setObjectName("interrupsion_sharing_checkBox")
        self.gridLayout_12.addWidget(self.interrupsion_sharing_checkBox, 5, 0, 1, 1)
        self.transmission_loss_matrices_and_convergence_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.transmission_loss_matrices_and_convergence_checkBox.setObjectName("transmission_loss_matrices_and_convergence_checkBox")
        self.gridLayout_12.addWidget(self.transmission_loss_matrices_and_convergence_checkBox, 6, 0, 1, 1)
        self.binding_contingencies_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.binding_contingencies_checkBox.setObjectName("binding_contingencies_checkBox")
        self.gridLayout_12.addWidget(self.binding_contingencies_checkBox, 3, 0, 1, 1)
        self.marginal_loss_charges_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.marginal_loss_charges_checkBox.setObjectName("marginal_loss_charges_checkBox")
        self.gridLayout_12.addWidget(self.marginal_loss_charges_checkBox, 2, 0, 1, 1)
        self.unserved_energy_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.unserved_energy_checkBox.setObjectName("unserved_energy_checkBox")
        self.gridLayout_12.addWidget(self.unserved_energy_checkBox, 4, 0, 1, 1)
        self.load_includes_losses_iterations_checkBox = QCheckBox(self.transmission_diagnostics_checkBox)
        self.load_includes_losses_iterations_checkBox.setObjectName("load_includes_losses_iterations_checkBox")
        self.gridLayout_12.addWidget(self.load_includes_losses_iterations_checkBox, 7, 0, 1, 1)
        self.gridLayout_8.addWidget(self.transmission_diagnostics_checkBox, 3, 0, 1, 1)
        self.capacity_expansion_diagnostics_checkBox = QGroupBox(self.groupBox_2)
        self.capacity_expansion_diagnostics_checkBox.setObjectName("capacity_expansion_diagnostics_checkBox")
        self.gridLayout_14 = QGridLayout(self.capacity_expansion_diagnostics_checkBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.lt_plan_annuities_checkBox = QCheckBox(self.capacity_expansion_diagnostics_checkBox)
        self.lt_plan_annuities_checkBox.setObjectName("lt_plan_annuities_checkBox")
        self.gridLayout_14.addWidget(self.lt_plan_annuities_checkBox, 0, 0, 1, 1)
        self.lt_plan_npv_checkBox = QCheckBox(self.capacity_expansion_diagnostics_checkBox)
        self.lt_plan_npv_checkBox.setObjectName("lt_plan_npv_checkBox")
        self.gridLayout_14.addWidget(self.lt_plan_npv_checkBox, 1, 0, 1, 1)
        self.mt_schedule_new_entry_checkBox = QCheckBox(self.capacity_expansion_diagnostics_checkBox)
        self.mt_schedule_new_entry_checkBox.setObjectName("mt_schedule_new_entry_checkBox")
        self.gridLayout_14.addWidget(self.mt_schedule_new_entry_checkBox, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.capacity_expansion_diagnostics_checkBox, 5, 0, 1, 1)
        self.production_diagnostics_checkBox = QGroupBox(self.groupBox_2)
        self.production_diagnostics_checkBox.setObjectName("production_diagnostics_checkBox")
        self.gridLayout_13 = QGridLayout(self.production_diagnostics_checkBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.heat_rate_checkBox = QCheckBox(self.production_diagnostics_checkBox)
        self.heat_rate_checkBox.setObjectName("heat_rate_checkBox")
        self.gridLayout_13.addWidget(self.heat_rate_checkBox, 0, 0, 1, 1)
        self.unit_commitment_checkBox = QCheckBox(self.production_diagnostics_checkBox)
        self.unit_commitment_checkBox.setObjectName("unit_commitment_checkBox")
        self.gridLayout_13.addWidget(self.unit_commitment_checkBox, 1, 0, 1, 1)
        self.pasa_outage_patterns_checkBox = QCheckBox(self.production_diagnostics_checkBox)
        self.pasa_outage_patterns_checkBox.setObjectName("pasa_outage_patterns_checkBox")
        self.gridLayout_13.addWidget(self.pasa_outage_patterns_checkBox, 2, 0, 1, 1)
        self.gridLayout_8.addWidget(self.production_diagnostics_checkBox, 4, 0, 1, 1)
        self.stochastic_diagnostics_checkBox = QGroupBox(self.groupBox_2)
        self.stochastic_diagnostics_checkBox.setObjectName("stochastic_diagnostics_checkBox")
        self.gridLayout_9 = QGridLayout(self.stochastic_diagnostics_checkBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.random_number_seed_checkBox = QCheckBox(self.stochastic_diagnostics_checkBox)
        self.random_number_seed_checkBox.setObjectName("random_number_seed_checkBox")
        self.gridLayout_9.addWidget(self.random_number_seed_checkBox, 0, 0, 1, 1)
        self.future_cost_function_checkBox = QCheckBox(self.stochastic_diagnostics_checkBox)
        self.future_cost_function_checkBox.setObjectName("future_cost_function_checkBox")
        self.gridLayout_9.addWidget(self.future_cost_function_checkBox, 1, 0, 1, 1)
        self.write_scenario_tree_checkBox = QCheckBox(self.stochastic_diagnostics_checkBox)
        self.write_scenario_tree_checkBox.setObjectName("write_scenario_tree_checkBox")
        self.gridLayout_9.addWidget(self.write_scenario_tree_checkBox, 2, 0, 1, 1)
        self.write_sample_weights_checkBox = QCheckBox(self.stochastic_diagnostics_checkBox)
        self.write_sample_weights_checkBox.setObjectName("write_sample_weights_checkBox")
        self.gridLayout_9.addWidget(self.write_sample_weights_checkBox, 3, 0, 1, 1)
        self.gridLayout_8.addWidget(self.stochastic_diagnostics_checkBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.solver_diagnostic_files_checkBox = QGroupBox(self.groupBox)
        self.solver_diagnostic_files_checkBox.setObjectName("solver_diagnostic_files_checkBox")
        self.gridLayout_4 = QGridLayout(self.solver_diagnostic_files_checkBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lp_files_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.lp_files_checkBox.setObjectName("lp_files_checkBox")
        self.gridLayout_4.addWidget(self.lp_files_checkBox, 0, 0, 1, 1)
        self.write_with_generic_names_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.write_with_generic_names_checkBox.setObjectName("write_with_generic_names_checkBox")
        self.gridLayout_4.addWidget(self.write_with_generic_names_checkBox, 0, 1, 1, 1)
        self.mps_files_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.mps_files_checkBox.setObjectName("mps_files_checkBox")
        self.gridLayout_4.addWidget(self.mps_files_checkBox, 1, 0, 1, 1)
        self.solution_files_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.solution_files_checkBox.setObjectName("solution_files_checkBox")
        self.gridLayout_4.addWidget(self.solution_files_checkBox, 2, 0, 1, 1)
        self.binary_files_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.binary_files_checkBox.setObjectName("binary_files_checkBox")
        self.gridLayout_4.addWidget(self.binary_files_checkBox, 3, 0, 1, 1)
        self.infeasibility_diagnostic_files_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.infeasibility_diagnostic_files_checkBox.setObjectName("infeasibility_diagnostic_files_checkBox")
        self.gridLayout_4.addWidget(self.infeasibility_diagnostic_files_checkBox, 4, 0, 1, 1)
        self.max_infeasibility_log_lines_checkBox = QLabel(self.solver_diagnostic_files_checkBox)
        self.max_infeasibility_log_lines_checkBox.setObjectName("max_infeasibility_log_lines_checkBox")
        self.gridLayout_4.addWidget(self.max_infeasibility_log_lines_checkBox, 5, 0, 1, 1)
        self.max_infeasibility_log_lines_spinBox = QSpinBox(self.solver_diagnostic_files_checkBox)
        self.max_infeasibility_log_lines_spinBox.setMinimum(-100000)
        self.max_infeasibility_log_lines_spinBox.setMaximum(100000)
        self.max_infeasibility_log_lines_spinBox.setProperty("value", -1)
        self.max_infeasibility_log_lines_spinBox.setObjectName("max_infeasibility_log_lines_spinBox")
        self.gridLayout_4.addWidget(self.max_infeasibility_log_lines_spinBox, 5, 1, 1, 1)
        self.objective_function_checkBox = QCheckBox(self.solver_diagnostic_files_checkBox)
        self.objective_function_checkBox.setObjectName("objective_function_checkBox")
        self.gridLayout_4.addWidget(self.objective_function_checkBox, 6, 0, 1, 1)
        self.gridLayout_2.addWidget(self.solver_diagnostic_files_checkBox, 3, 0, 1, 4)
        self.execution_diagnostics_groupBox = QGroupBox(self.groupBox)
        self.execution_diagnostics_groupBox.setObjectName("execution_diagnostics_groupBox")
        self.gridLayout_5 = QGridLayout(self.execution_diagnostics_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.interleaved_run_mode_checkBox = QCheckBox(self.execution_diagnostics_groupBox)
        self.interleaved_run_mode_checkBox.setObjectName("interleaved_run_mode_checkBox")
        self.gridLayout_5.addWidget(self.interleaved_run_mode_checkBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.execution_diagnostics_groupBox, 4, 0, 1, 4)
        self.step_from_label = QLabel(self.groupBox)
        self.step_from_label.setObjectName("step_from_label")
        self.gridLayout_2.addWidget(self.step_from_label, 1, 0, 1, 1)
        self.step_to_spinBox = QSpinBox(self.groupBox)
        self.step_to_spinBox.setMinimum(-1)
        self.step_to_spinBox.setProperty("value", -1)
        self.step_to_spinBox.setObjectName("step_to_spinBox")
        self.gridLayout_2.addWidget(self.step_to_spinBox, 1, 3, 1, 1)
        self.clear_existing_diagnostics_checkBox = QCheckBox(self.groupBox)
        self.clear_existing_diagnostics_checkBox.setChecked(True)
        self.clear_existing_diagnostics_checkBox.setObjectName("clear_existing_diagnostics_checkBox")
        self.gridLayout_2.addWidget(self.clear_existing_diagnostics_checkBox, 0, 0, 1, 2)
        self.step_from_spinBox = QSpinBox(self.groupBox)
        self.step_from_spinBox.setMinimum(1)
        self.step_from_spinBox.setProperty("value", 1)
        self.step_from_spinBox.setObjectName("step_from_spinBox")
        self.gridLayout_2.addWidget(self.step_from_spinBox, 1, 1, 1, 1)
        self.step_to_label = QLabel(self.groupBox)
        self.step_to_label.setObjectName("step_to_label")
        self.gridLayout_2.addWidget(self.step_to_label, 1, 2, 1, 1)
        self.show_progress_messages_groupBox = QGroupBox(self.groupBox)
        self.show_progress_messages_groupBox.setObjectName("show_progress_messages_groupBox")
        self.gridLayout_3 = QGridLayout(self.show_progress_messages_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.execution_times_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.execution_times_checkBox.setChecked(True)
        self.execution_times_checkBox.setObjectName("execution_times_checkBox")
        self.gridLayout_3.addWidget(self.execution_times_checkBox, 0, 0, 1, 1)
        self.summary_each_sample_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.summary_each_sample_checkBox.setObjectName("summary_each_sample_checkBox")
        self.gridLayout_3.addWidget(self.summary_each_sample_checkBox, 1, 0, 1, 1)
        self.summary_each_step_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.summary_each_step_checkBox.setChecked(True)
        self.summary_each_step_checkBox.setObjectName("summary_each_step_checkBox")
        self.gridLayout_3.addWidget(self.summary_each_step_checkBox, 2, 0, 1, 1)
        self.task_size_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.task_size_checkBox.setChecked(True)
        self.task_size_checkBox.setObjectName("task_size_checkBox")
        self.gridLayout_3.addWidget(self.task_size_checkBox, 3, 0, 1, 1)
        self.task_components_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.task_components_checkBox.setObjectName("task_components_checkBox")
        self.gridLayout_3.addWidget(self.task_components_checkBox, 4, 0, 1, 1)
        self.solver_summary_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.solver_summary_checkBox.setObjectName("solver_summary_checkBox")
        self.gridLayout_3.addWidget(self.solver_summary_checkBox, 5, 0, 1, 1)
        self.lp_solver_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.lp_solver_checkBox.setObjectName("lp_solver_checkBox")
        self.gridLayout_3.addWidget(self.lp_solver_checkBox, 6, 0, 1, 1)
        self.mip_solver_checkBox = QCheckBox(self.show_progress_messages_groupBox)
        self.mip_solver_checkBox.setChecked(True)
        self.mip_solver_checkBox.setObjectName("mip_solver_checkBox")
        self.gridLayout_3.addWidget(self.mip_solver_checkBox, 7, 0, 1, 1)
        self.gridLayout_2.addWidget(self.show_progress_messages_groupBox, 2, 0, 1, 4)
        self.active_diagnostics_groupBox = QGroupBox(self.groupBox)
        self.active_diagnostics_groupBox.setObjectName("active_diagnostics_groupBox")
        self.gridLayout_7 = QGridLayout(self.active_diagnostics_groupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.note_label = QLabel(self.active_diagnostics_groupBox)
        self.note_label.setObjectName("note_label")
        self.gridLayout_7.addWidget(self.note_label, 0, 0, 1, 2)
        self.marginal_unit_checkBox = QCheckBox(self.active_diagnostics_groupBox)
        self.marginal_unit_checkBox.setObjectName("marginal_unit_checkBox")
        self.gridLayout_7.addWidget(self.marginal_unit_checkBox, 1, 0, 1, 1)
        self.load_increment_label = QLabel(self.active_diagnostics_groupBox)
        self.load_increment_label.setEnabled(False)
        self.load_increment_label.setObjectName("load_increment_label")
        self.gridLayout_7.addWidget(self.load_increment_label, 3, 0, 1, 1)
        self.load_increment_spinBox = QSpinBox(self.active_diagnostics_groupBox)
        self.load_increment_spinBox.setEnabled(False)
        self.load_increment_spinBox.setMinimum(-1000)
        self.load_increment_spinBox.setMaximum(1000)
        self.load_increment_spinBox.setProperty("value", -1)
        self.load_increment_spinBox.setObjectName("load_increment_spinBox")
        self.gridLayout_7.addWidget(self.load_increment_spinBox, 3, 1, 1, 1)
        self.marginal_expansion_unit_checkBox = QCheckBox(self.active_diagnostics_groupBox)
        self.marginal_expansion_unit_checkBox.setObjectName("marginal_expansion_unit_checkBox")
        self.gridLayout_7.addWidget(self.marginal_expansion_unit_checkBox, 4, 0, 1, 1)
        self.load_increment_label_2 = QLabel(self.active_diagnostics_groupBox)
        self.load_increment_label_2.setEnabled(False)
        self.load_increment_label_2.setObjectName("load_increment_label_2")
        self.gridLayout_7.addWidget(self.load_increment_label_2, 5, 0, 1, 1)
        self.load_increment_spinBox_2 = QSpinBox(self.active_diagnostics_groupBox)
        self.load_increment_spinBox_2.setEnabled(False)
        self.load_increment_spinBox_2.setMinimum(-100000)
        self.load_increment_spinBox_2.setMaximum(100000)
        self.load_increment_spinBox_2.setProperty("value", 1000)
        self.load_increment_spinBox_2.setObjectName("load_increment_spinBox_2")
        self.gridLayout_7.addWidget(self.load_increment_spinBox_2, 5, 1, 1, 1)
        self.region_supply_checkBox = QCheckBox(self.active_diagnostics_groupBox)
        self.region_supply_checkBox.setObjectName("region_supply_checkBox")
        self.gridLayout_7.addWidget(self.region_supply_checkBox, 6, 0, 1, 1)
        self.marginal_unit_transmission_detail_groupBox = QGroupBox(self.active_diagnostics_groupBox)
        self.marginal_unit_transmission_detail_groupBox.setEnabled(False)
        self.marginal_unit_transmission_detail_groupBox.setObjectName("marginal_unit_transmission_detail_groupBox")
        self.gridLayout_6 = QGridLayout(self.marginal_unit_transmission_detail_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.regional_radioBox = QRadioButton(self.marginal_unit_transmission_detail_groupBox)
        self.regional_radioBox.setChecked(True)
        self.regional_radioBox.setObjectName("radioButton")
        self.gridLayout_6.addWidget(self.regional_radioBox, 0, 0, 1, 1)
        self.system_radioButton = QRadioButton(self.marginal_unit_transmission_detail_groupBox)
        self.system_radioButton.setObjectName("system_radioButton")
        self.gridLayout_6.addWidget(self.system_radioButton, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.marginal_unit_transmission_detail_groupBox, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.active_diagnostics_groupBox, 5, 0, 10, 4)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        self.marginal_unit_checkBox.clicked.connect(self.enablemarginalunittransmissiondetail)
        self.marginal_expansion_unit_checkBox.clicked.connect(self.enableloadincrement)
    
    def setInput(self, input):
        self.input = input
        self.loaddiagnosticsscreen()
        self.enableloadincrement()
        self.enablemarginalunittransmissiondetail()
    
    def getOutput(self):
        self.savediagnosticsscreen()
        return self.output

    def loaddiagnosticsscreen(self):
        self.clear_existing_diagnostics_checkBox.setChecked(self.input["clear_existing_diagnostics"])
        self.task_size_checkBox.setChecked(self.input["task_size"])
        self.task_components_checkBox.setChecked(self.input["task_components"])
        self.lp_solver_checkBox.setChecked(self.input["lp_solver"])
        self.mip_solver_checkBox.setChecked(self.input["mip_solver"])
        self.solver_summary_checkBox.setChecked(self.input["solver_summary"])
        self.execution_times_checkBox.setChecked(self.input["execution_times"])
        self.summary_each_sample_checkBox.setChecked(self.input["summary_each_sample"])
        self.summary_each_step_checkBox.setChecked(self.input["summary_each_step"])
        self.step_from_spinBox.setValue(int(self.input["step_from"]))
        self.step_to_spinBox.setValue(int(self.input["step_to"]))
        self.lp_files_checkBox.setChecked(self.input["lp_files"])
        self.mps_files_checkBox.setChecked(self.input["mps_files"])
        self.solution_files_checkBox.setChecked(self.input["solution_files"])
        self.write_with_generic_names_checkBox.setChecked(self.input["write_with_generic_names"])
        self.binary_files_checkBox.setChecked(self.input["binary_files"])
        self.infeasibility_diagnostic_files_checkBox.setChecked(self.input["infeasibility_diagnostic_files"])
        self.max_infeasibility_log_lines_spinBox.setValue(int(self.input["max_infeasibility_log_lines"]))
        self.bertrand_pricing_checkBox.setChecked(self.input["bertrand_pricing"])
        self.revenue_recovery_checkBox.setChecked(self.input["revenue_recovery"])
        self.nashcournot_checkBox.setChecked(self.input["nashcournot"])
        self.rsi_bidcost_markup_checkBox.setChecked(self.input["rsi_bidcost_markup"])
        self.mt_schedule_new_entry_checkBox.setChecked(self.input["mt_schedule_new_entry"])
        self.ptdf_shift_factors_checkBox.setChecked(self.input["ptdf_shift_factors"])
        self.unserved_energy_checkBox.setChecked(self.input["unserved_energy"])
        self.interrupsion_sharing_checkBox.setChecked(self.input["interrupsion_sharing"])
        self.transmission_loss_matrices_and_convergence_checkBox.setChecked(self.input["transmission_loss_matrices_and_convergence"])
        self.congestion_charges_checkBox.setChecked(self.input["congestion_charges"])
        self.marginal_loss_charges_checkBox.setChecked(self.input["marginal_loss_charges"])
        self.binding_contingencies_checkBox.setChecked(self.input["binding_contingencies"])
        self.unit_commitment_checkBox.setChecked(self.input["unit_commitment"])
        self.constraint_decomposition_checkBox.setChecked(self.input["constraint_decomposition"])
        self.constraint_rollover_checkBox.setChecked(self.input["constraint_rollover"])
        self.uniform_pricing_checkBox.setChecked(self.input["uniform_pricing"])
        self.marginal_unit_checkBox.setChecked(self.input["marginal_unit"])
        self.load_increment_spinBox.setValue(int(self.input["load_increment"]))
        self.marginal_expansion_unit_checkBox.setChecked(self.input["marginal_expansion_unit"])
        self.load_increment_spinBox_2.setValue(int(self.input["load_increment_2"]))
        self.region_supply_checkBox.setChecked(self.input["region_supply"])
        self.lt_plan_annuities_checkBox.setChecked(self.input["lt_plan_annuities"])
        self.lt_plan_npv_checkBox.setChecked(self.input["lt_plan_npv"])
        self.load_includes_losses_iterations_checkBox.setChecked(self.input["load_includes_losses_iterations"])
        self.pasa_outage_patterns_checkBox.setChecked(self.input["pasa_outage_patterns"])
        self.random_number_seed_checkBox.setChecked(self.input["random_number_seed"])
        self.interleaved_run_mode_checkBox.setChecked(self.input["interleaved_run_mode"])
        self.heat_rate_checkBox.setChecked(self.input["heat_rate"])
        self.objective_function_checkBox.setChecked(self.input["objective_function"])
        self.future_cost_function_checkBox.setChecked(self.input["future_cost_function"])
        self.write_scenario_tree_checkBox.setChecked(self.input["write_scenario_tree"])
        self.write_sample_weights_checkBox.setChecked(self.input["write_sample_weights"])

        if self.input["marginal_unit_transmission_detail"] == "Regional":
            self.regional_radioBox.setChecked(True)
        elif self.input["marginal_unit_transmission_detail"] == "System":
            self.system_radioButton.setChecked(True)

    def savediagnosticsscreen(self):
        self.output = diagnostics_default_input | {
            "clear_existing_diagnostics": self.clear_existing_diagnostics_checkBox.isChecked(),
            "task_size": self.task_size_checkBox.isChecked(),
            "task_components": self.task_components_checkBox.isChecked(),
            "lp_solver": self.lp_solver_checkBox.isChecked(),
            "mip_solver": self.mip_solver_checkBox.isChecked(),
            "solver_summary": self.solver_summary_checkBox.isChecked(),
            "execution_times": self.execution_times_checkBox.isChecked(),
            "summary_each_sample": self.summary_each_sample_checkBox.isChecked(),
            "summary_each_step": self.summary_each_step_checkBox.isChecked(),
            "step_from": str(self.step_from_spinBox.value()),
            "step_to": str(self.step_to_spinBox.value()),
            "lp_files": self.lp_files_checkBox.isChecked(),
            "mps_files": self.mps_files_checkBox.isChecked(),
            "solution_files": self.solution_files_checkBox.isChecked(),
            "write_with_generic_names": self.write_with_generic_names_checkBox.isChecked(),
            "binary_files": self.binary_files_checkBox.isChecked(),
            "infeasibility_diagnostic_files": self.infeasibility_diagnostic_files_checkBox.isChecked(),
            "max_infeasibility_log_lines": str(self.max_infeasibility_log_lines_spinBox.value()),
            "bertrand_pricing": self.bertrand_pricing_checkBox.isChecked(),
            "revenue_recovery": self.revenue_recovery_checkBox.isChecked(),
            "nashcournot": self.nashcournot_checkBox.isChecked(),
            "rsi_bidcost_markup": self.rsi_bidcost_markup_checkBox.isChecked(),
            "mt_schedule_new_entry": self.mt_schedule_new_entry_checkBox.isChecked(),
            "ptdf_shift_factors": self.ptdf_shift_factors_checkBox.isChecked(),
            "unserved_energy": self.unserved_energy_checkBox.isChecked(),
            "interrupsion_sharing": self.interrupsion_sharing_checkBox.isChecked(),
            "transmission_loss_matrices_and_convergence": self.transmission_loss_matrices_and_convergence_checkBox.isChecked(),
            "congestion_charges": self.congestion_charges_checkBox.isChecked(),
            "marginal_loss_charges": self.marginal_loss_charges_checkBox.isChecked(),
            "binding_contingencies": self.binding_contingencies_checkBox.isChecked(),
            "unit_commitment": self.unit_commitment_checkBox.isChecked(),
            "constraint_decomposition": self.constraint_decomposition_checkBox.isChecked(),
            "constraint_rollover": self.constraint_rollover_checkBox.isChecked(),
            "uniform_pricing": self.uniform_pricing_checkBox.isChecked(),
            "marginal_unit": self.marginal_unit_checkBox.isChecked(),
            "load_increment": str(self.load_increment_spinBox.value()),
            "marginal_expansion_unit": self.marginal_expansion_unit_checkBox.isChecked(),
            "load_increment_2": str(self.load_increment_spinBox_2.value()),
            "region_supply": self.region_supply_checkBox.isChecked(),
            "lt_plan_annuities": self.lt_plan_annuities_checkBox.isChecked(),
            "lt_plan_npv": self.lt_plan_npv_checkBox.isChecked(),
            "load_includes_losses_iterations": self.load_includes_losses_iterations_checkBox.isChecked(),
            "pasa_outage_patterns": self.pasa_outage_patterns_checkBox.isChecked(),
            "random_number_seed": self.random_number_seed_checkBox.isChecked(),
            "interleaved_run_mode": self.interleaved_run_mode_checkBox.isChecked(),
            "heat_rate": self.heat_rate_checkBox.isChecked(),
            "objective_function": self.objective_function_checkBox.isChecked(),
            "future_cost_function": self.future_cost_function_checkBox.isChecked(),
            "write_scenario_tree": self.write_scenario_tree_checkBox.isChecked(),
            "write_sample_weights": self.write_sample_weights_checkBox.isChecked()
        }

        if self.regional_radioBox.isChecked() == True:
            self.output["marginal_unit_transmission_detail"] = "Regional"
        elif self.system_radioButton.isChecked() == True:
            self.output["marginal_unit_transmission_detail"] = "System"

    def enablemarginalunittransmissiondetail(self):
        if self.marginal_unit_checkBox.isChecked()  == True:
            self.marginal_unit_transmission_detail_groupBox.setEnabled(True)
        else:
            self.marginal_unit_transmission_detail_groupBox.setEnabled(False)

    def enableloadincrement(self):
        if self.marginal_expansion_unit_checkBox.isChecked()  == True:
            self.load_increment_label_2.setEnabled(True)
            self.load_increment_spinBox_2.setEnabled(True)
        else:
            self.load_increment_label_2.setEnabled(False)
            self.load_increment_spinBox_2.setEnabled(False)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.competetion_prixing_groupBox.setTitle(QApplication.translate("Form", "Competition & Pricing Diagnostics"))
        self.bertrand_pricing_checkBox.setText(QApplication.translate("Form", "Bertrand Pricing"))
        self.revenue_recovery_checkBox.setText(QApplication.translate("Form", "Revenue Recovery"))
        self.nashcournot_checkBox.setText(QApplication.translate("Form", "Nash-Cournot"))
        self.rsi_bidcost_markup_checkBox.setText(QApplication.translate("Form", "RSI Bid-Cost Mark-up"))
        self.uniform_pricing_checkBox.setText(QApplication.translate("Form", "Uniform Pricing"))
        self.constraint_diagnostics_checkBox.setTitle(QApplication.translate("Form", "Constraint Diagnostics"))
        self.constraint_decomposition_checkBox.setText(QApplication.translate("Form", "Constraint Decomposition"))
        self.constraint_rollover_checkBox.setText(QApplication.translate("Form", "Constraint Rollover"))
        self.transmission_diagnostics_checkBox.setTitle(QApplication.translate("Form", "Transmission Diagnostics"))
        self.congestion_charges_checkBox.setText(QApplication.translate("Form", "Congestion Charges"))
        self.ptdf_shift_factors_checkBox.setText(QApplication.translate("Form", "PTDF (Shift Factors)"))
        self.interrupsion_sharing_checkBox.setText(QApplication.translate("Form", "Interruption Sharing"))
        self.transmission_loss_matrices_and_convergence_checkBox.setText(QApplication.translate("Form", "Transmission Loss Matrices and Convergence"))
        self.binding_contingencies_checkBox.setText(QApplication.translate("Form", "Binding Contingencies"))
        self.marginal_loss_charges_checkBox.setText(QApplication.translate("Form", "Marginal Loss Charges"))
        self.unserved_energy_checkBox.setText(QApplication.translate("Form", "Unserved Energy"))
        self.load_includes_losses_iterations_checkBox.setText(QApplication.translate("Form", "Load Includes Losses Iterations"))
        self.capacity_expansion_diagnostics_checkBox.setTitle(QApplication.translate("Form", "Capacity Expansion Diagnostics"))
        self.lt_plan_annuities_checkBox.setText(QApplication.translate("Form", "LT Plan Annuities"))
        self.lt_plan_npv_checkBox.setText(QApplication.translate("Form", "LT Plan NPV"))
        self.mt_schedule_new_entry_checkBox.setText(QApplication.translate("Form", "MT Schedule New Entry"))
        self.production_diagnostics_checkBox.setTitle(QApplication.translate("Form", "Production Diagnostics"))
        self.heat_rate_checkBox.setText(QApplication.translate("Form", "Heat Rate"))
        self.unit_commitment_checkBox.setText(QApplication.translate("Form", "Unit Commitment"))
        self.pasa_outage_patterns_checkBox.setText(QApplication.translate("Form", "PASA Outage Patterns"))
        self.stochastic_diagnostics_checkBox.setTitle(QApplication.translate("Form", "Stochastic Diagnostics"))
        self.random_number_seed_checkBox.setText(QApplication.translate("Form", "Random Number Seed"))
        self.future_cost_function_checkBox.setText(QApplication.translate("Form", "Future Cost Function"))
        self.write_scenario_tree_checkBox.setText(QApplication.translate("Form", "Write Scenario Tree"))
        self.write_sample_weights_checkBox.setText(QApplication.translate("Form", "Write Sample Weights"))
        self.solver_diagnostic_files_checkBox.setTitle(QApplication.translate("Form", "Solver Diagnostic Files"))
        self.lp_files_checkBox.setText(QApplication.translate("Form", "LP Files"))
        self.write_with_generic_names_checkBox.setText(QApplication.translate("Form", "Write with Generic Names"))
        self.mps_files_checkBox.setText(QApplication.translate("Form", "MPS Files"))
        self.solution_files_checkBox.setText(QApplication.translate("Form", "Solution Files"))
        self.binary_files_checkBox.setText(QApplication.translate("Form", "Binary Files"))
        self.infeasibility_diagnostic_files_checkBox.setText(QApplication.translate("Form", "Infeasibility Diagnostic Files"))
        self.max_infeasibility_log_lines_checkBox.setText(QApplication.translate("Form", "Max Infeasibility Log Lines"))
        self.objective_function_checkBox.setText(QApplication.translate("Form", "Objective Function"))
        self.execution_diagnostics_groupBox.setTitle(QApplication.translate("Form", "Execution Diagnostics"))
        self.interleaved_run_mode_checkBox.setText(QApplication.translate("Form", "Interleaved Run Mode"))
        self.step_from_label.setText(QApplication.translate("Form", "Step From"))
        self.clear_existing_diagnostics_checkBox.setText(QApplication.translate("Form", "Clear Existing Diagnostics"))
        self.step_to_label.setText(QApplication.translate("Form", "Step To"))
        self.show_progress_messages_groupBox.setTitle(QApplication.translate("Form", "Show Progress Messages"))
        self.execution_times_checkBox.setText(QApplication.translate("Form", "Execution Times"))
        self.summary_each_sample_checkBox.setText(QApplication.translate("Form", "Summary Each Sample"))
        self.summary_each_step_checkBox.setText(QApplication.translate("Form", "Summary Each Step"))
        self.task_size_checkBox.setText(QApplication.translate("Form", "Task Size"))
        self.task_components_checkBox.setText(QApplication.translate("Form", "Task Components"))
        self.solver_summary_checkBox.setText(QApplication.translate("Form", "Solver Summary"))
        self.lp_solver_checkBox.setText(QApplication.translate("Form", "LP Solver"))
        self.mip_solver_checkBox.setText(QApplication.translate("Form", "MIP Solver"))
        self.active_diagnostics_groupBox.setTitle(QApplication.translate("Form", "Active Diagnostics"))
        self.note_label.setText(QApplication.translate("Form", "NOTE: These diagnostics can affect the simulation results!"))
        self.marginal_unit_checkBox.setText(QApplication.translate("Form", "Marginal Unit"))
        self.load_increment_label.setText(QApplication.translate("Form", "Load Increment"))
        self.marginal_expansion_unit_checkBox.setText(QApplication.translate("Form", "Marginal Expansion Unit"))
        self.load_increment_label_2.setText(QApplication.translate("Form", "Load Increment"))
        self.region_supply_checkBox.setText(QApplication.translate("Form", "Region Supply"))
        self.marginal_unit_transmission_detail_groupBox.setTitle(QApplication.translate("Form", "Marginal Unit Transmission Detail"))
        self.regional_radioBox.setText(QApplication.translate("Form", "Regional"))
        self.system_radioButton.setText(QApplication.translate("Form", "System"))
