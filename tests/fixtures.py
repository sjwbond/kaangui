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

def create_test_widget(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    # Load test model
    widget.load_model(test_model_1)
    widget.controller.tree.expandAll()

    return widget
