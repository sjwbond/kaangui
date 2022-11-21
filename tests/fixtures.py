from main import MainWindow

test_model_1 = {
    "name": "Test Model",
    "Simulation": {
        "Competition": {},
        "Diagnostics": {},
        "Execution Plans": {},
        "Horizons": {},
        "LRMC Models": {},
        "MT Schedule": {},
        "PASA": {},
        "Performance": {},
        "Production": {},
        "Reports": {},
        "ST Schedule": {},
        "Settings": {},
        "Stochastics": {},
        "Transmission": {}
    },
    "SystemInputs": {
        "Currency": {
            "EUR": {
                "Object_Name": "EUR",
                "Object_Type": "Currency",
                "Parent Objects": [],
                "Properties": [
                    {
                        "Date_From": "2000-01-01",
                        "Date_To": "2100-01-01",
                        "Group_id": "",
                        "Parent Object": "",
                        "Priority": "",
                        "Property": "",
                        "Scenario": "",
                        "Target Object": "",
                        "Timeslice": "",
                        "Timeslice_Index": "",
                        "Value": "",
                        "Variable": "",
                        "Variable_Effect": ""
                    }
                ]
            },
            "USD": {
                "Object_Name": "USD",
                "Object_Type": "Currency",
                "Parent Objects": [],
                "Properties": []
            },
            "Subfolder": {
                "TRY": {
                    "Object_Name": "TRY",
                    "Object_Type": "Currency",
                    "Parent Objects": [],
                    "Properties": []
                }
            }
        },
        "DBDataSource": {},
        "DBTimeSeries": {},
        "DataSource": {},
        "Demand": {},
        "Emissions": {},
        "Fuel": {},
        "Generator": {},
        "Group": {},
        "Hydro_Generator": {},
        "Line": {},
        "Node": {},
        "Reservoir": {},
        "Storage": {},
        "Variable": {}
    }
}

test_simulation_1 = {
    "Competition": {},
    "Diagnostics": {
        "New Diagnostic": {
            "bertrand_pricing": False,
            "binary_files": False,
            "binding_contingencies": False,
            "clear_existing_diagnostics": True,
            "congestion_charges": False,
            "constraint_decomposition": False,
            "constraint_rollover": False,
            "execution_times": True,
            "future_cost_function": False,
            "heat_rate": False,
            "infeasibility_diagnostic_files": False,
            "interleaved_run_mode": False,
            "interrupsion_sharing": False,
            "load_includes_losses_iterations": False,
            "load_increment": "-1",
            "load_increment_2": "100",
            "lp_files": False,
            "lp_solver": False,
            "lt_plan_annuities": False,
            "lt_plan_npv": False,
            "marginal_expansion_unit": False,
            "marginal_loss_charges": False,
            "marginal_unit": False,
            "marginal_unit_transmission_detail": "Regional",
            "max_infeasibility_log_lines": "-1",
            "mip_solver": True,
            "mps_files": False,
            "mt_schedule_new_entry": False,
            "nashcournot": False,
            "objective_function": False,
            "pasa_outage_patterns": False,
            "ptdf_shift_factors": False,
            "random_number_seed": False,
            "region_supply": False,
            "revenue_recovery": False,
            "rsi_bidcost_markup": False,
            "solution_files": False,
            "solver_summary": False,
            "step_from": "1",
            "step_to": "-1",
            "summary_each_sample": False,
            "summary_each_step": True,
            "task_components": False,
            "task_size": True,
            "transmission_loss_matrices_and_convergence": False,
            "uniform_pricing": False,
            "unit_commitment": False,
            "unserved_energy": False,
            "write_sample_weights": False,
            "write_scenario_tree": False,
            "write_with_generic_names": False
        }
    },
    "Execution Plans": {
        "New Execution Plans": {
            "Settings": "",
            "Simulation": {
                "Horizons": "",
                "LRMC Model": "",
                "MT Schedule": "",
                "PASA": "",
                "Reports": "",
                "ST Schedule": "",
                "Scenarios": {}
            }
        }
    },
    "Horizons": {
        "New Horizon": {
            "End Date": "2022-01-01",
            "Granularity": 555,
            "Historic Sample Years": [],
            "Periodicity": {
                "Off": 2,
                "On": 1,
                "Type": "Year"
            },
            "Start Date": "2022-01-01"
        }
    },
    "LRMC Models": {},
    "MT Schedule": {},
    "PASA": {},
    "Performance": {},
    "Production": {},
    "Reports": {},
    "ST Schedule": {},
    "Settings": {},
    "Stochastics": {},
    "Transmission": {}
}

def create_test_widget(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    # Load test model
    widget.load_model(test_model_1)
    widget.controller.tree.expandAll()

    return widget
