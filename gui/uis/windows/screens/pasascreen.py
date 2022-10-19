# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pasascreen.ui'
#
# Created: Tue Jun 21 13:50:50 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from qt_core import *

pasa_default_input = {
    "demandsize_participation": True,
    "depand_purchaser_bids": False,
    "contract_generation": False,
    "contract_load": False,
    "market_purchases": False,
    "enforce_line_and_transformer_limits": True,
    "enforce_interface_limits": True,
    "maintenance_sculpting": "0",
    "compute_indices": False,
    "compute_multiarea_reliability_indices": False,
    "outage_increment_mw": "10",
    "write_outages_to_text_files": False,
    "resolution": "Day",
    "transmission": "Regional",
    "stochastic_method": "Deterministic"
}

class Ui_PASAScreen(QObject):
    input = pasa_default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 875)
        self.gridLayout_7 = QGridLayout(Form)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.resolution_groupBox = QGroupBox(self.groupBox)
        self.resolution_groupBox.setObjectName("resolution_groupBox")
        self.gridLayout_2 = QGridLayout(self.resolution_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.interval_radioButton = QRadioButton(self.resolution_groupBox)
        self.interval_radioButton.setObjectName("interval_radioButton")
        self.gridLayout_2.addWidget(self.interval_radioButton, 0, 0, 1, 1)
        self.day_radioButton = QRadioButton(self.resolution_groupBox)
        self.day_radioButton.setChecked(True)
        self.day_radioButton.setObjectName("day_radioButton")
        self.gridLayout_2.addWidget(self.day_radioButton, 0, 1, 1, 1)
        self.week_radioButton = QRadioButton(self.resolution_groupBox)
        self.week_radioButton.setObjectName("week_radioButton")
        self.gridLayout_2.addWidget(self.week_radioButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.resolution_groupBox)
        self.transmission_groupBox = QGroupBox(self.groupBox)
        self.transmission_groupBox.setObjectName("transmission_groupBox")
        self.gridLayout = QGridLayout(self.transmission_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.regional_radioButton = QRadioButton(self.transmission_groupBox)
        self.regional_radioButton.setChecked(True)
        self.regional_radioButton.setObjectName("regional_radioButton")
        self.gridLayout.addWidget(self.regional_radioButton, 0, 0, 1, 1)
        self.zonal_radioButton = QRadioButton(self.transmission_groupBox)
        self.zonal_radioButton.setObjectName("zonal_radioButton")
        self.gridLayout.addWidget(self.zonal_radioButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.transmission_groupBox)
        self.enforce_line_and_transformer_limits_checkBox = QCheckBox(self.groupBox)
        self.enforce_line_and_transformer_limits_checkBox.setChecked(True)
        self.enforce_line_and_transformer_limits_checkBox.setObjectName("enforce_line_and_transformer_limits_checkBox")
        self.verticalLayout.addWidget(self.enforce_line_and_transformer_limits_checkBox)
        self.enforce_interface_limits_checkBox = QCheckBox(self.groupBox)
        self.enforce_interface_limits_checkBox.setChecked(True)
        self.enforce_interface_limits_checkBox.setObjectName("enforce_interface_limits_checkBox")
        self.verticalLayout.addWidget(self.enforce_interface_limits_checkBox)
        self.stochastic_method_groupBox = QGroupBox(self.groupBox)
        self.stochastic_method_groupBox.setObjectName("stochastic_method_groupBox")
        self.gridLayout_3 = QGridLayout(self.stochastic_method_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.deterministic_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.deterministic_radioButton.setChecked(True)
        self.deterministic_radioButton.setObjectName("deterministic_radioButton")
        self.gridLayout_3.addWidget(self.deterministic_radioButton, 0, 0, 1, 1)
        self.independant_samples_sequential_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_sequential_radioButton.setObjectName("independant_samples_sequential_radioButton")
        self.gridLayout_3.addWidget(self.independant_samples_sequential_radioButton, 1, 0, 1, 1)
        self.independant_samples_parallel_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.independant_samples_parallel_radioButton.setObjectName("independant_samples_parallel_radioButton")
        self.gridLayout_3.addWidget(self.independant_samples_parallel_radioButton, 2, 0, 1, 1)
        self.scenariowise_decomposition_radioButton = QRadioButton(self.stochastic_method_groupBox)
        self.scenariowise_decomposition_radioButton.setObjectName("scenariowise_decomposition_radioButton")
        self.gridLayout_3.addWidget(self.scenariowise_decomposition_radioButton, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.stochastic_method_groupBox)
        self.load_and_supply_groupBox = QGroupBox(self.groupBox)
        self.load_and_supply_groupBox.setObjectName("load_and_supply_groupBox")
        self.gridLayout_4 = QGridLayout(self.load_and_supply_groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.demandsize_participation_checkBox = QCheckBox(self.load_and_supply_groupBox)
        self.demandsize_participation_checkBox.setChecked(True)
        self.demandsize_participation_checkBox.setObjectName("demandsize_participation_checkBox")
        self.gridLayout_4.addWidget(self.demandsize_participation_checkBox, 0, 0, 1, 1)
        self.depand_purchaser_bids_checkBox = QCheckBox(self.load_and_supply_groupBox)
        self.depand_purchaser_bids_checkBox.setObjectName("depand_purchaser_bids_checkBox")
        self.gridLayout_4.addWidget(self.depand_purchaser_bids_checkBox, 1, 0, 1, 1)
        self.contract_generation_checkBox = QCheckBox(self.load_and_supply_groupBox)
        self.contract_generation_checkBox.setObjectName("contract_generation_checkBox")
        self.gridLayout_4.addWidget(self.contract_generation_checkBox, 2, 0, 1, 1)
        self.contract_load_checkBox = QCheckBox(self.load_and_supply_groupBox)
        self.contract_load_checkBox.setObjectName("contract_load_checkBox")
        self.gridLayout_4.addWidget(self.contract_load_checkBox, 3, 0, 1, 1)
        self.market_purchases_checkBox = QCheckBox(self.load_and_supply_groupBox)
        self.market_purchases_checkBox.setObjectName("market_purchases_checkBox")
        self.gridLayout_4.addWidget(self.market_purchases_checkBox, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.load_and_supply_groupBox)
        self.reliability_groupBox = QGroupBox(self.groupBox)
        self.reliability_groupBox.setObjectName("reliability_groupBox")
        self.gridLayout_5 = QGridLayout(self.reliability_groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.compute_indices_checkBox = QCheckBox(self.reliability_groupBox)
        self.compute_indices_checkBox.setObjectName("compute_indices_checkBox")
        self.gridLayout_5.addWidget(self.compute_indices_checkBox, 0, 0, 1, 1)
        self.compute_multiarea_reliability_indices_checkBox = QCheckBox(self.reliability_groupBox)
        self.compute_multiarea_reliability_indices_checkBox.setObjectName("compute_multiarea_reliability_indices_checkBox")
        self.gridLayout_5.addWidget(self.compute_multiarea_reliability_indices_checkBox, 1, 0, 1, 1)
        self.outage_increment_label = QLabel(self.reliability_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outage_increment_label.sizePolicy().hasHeightForWidth())
        self.outage_increment_label.setSizePolicy(sizePolicy)
        self.outage_increment_label.setObjectName("outage_increment_label")
        self.gridLayout_5.addWidget(self.outage_increment_label, 2, 0, 1, 1)
        self.outage_increment_mw = QSpinBox(self.reliability_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outage_increment_mw.sizePolicy().hasHeightForWidth())
        self.outage_increment_mw.setSizePolicy(sizePolicy)
        self.outage_increment_mw.setProperty("value", 10)
        self.outage_increment_mw.setObjectName("outage_increment_mw")
        self.gridLayout_5.addWidget(self.outage_increment_mw, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.reliability_groupBox)
        self.output_groupBox = QGroupBox(self.groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_groupBox.sizePolicy().hasHeightForWidth())
        self.output_groupBox.setSizePolicy(sizePolicy)
        self.output_groupBox.setObjectName("output_groupBox")
        self.gridLayout_6 = QGridLayout(self.output_groupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.maintenance_sculpting_label = QLabel(self.output_groupBox)
        self.maintenance_sculpting_label.setObjectName("maintenance_sculpting_label")
        self.gridLayout_6.addWidget(self.maintenance_sculpting_label, 0, 0, 1, 1)
        self.horizontalSlider = QSlider(self.output_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_6.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.maintenance_sculpting_label = QLabel(self.output_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maintenance_sculpting_label.sizePolicy().hasHeightForWidth())
        self.maintenance_sculpting_label.setSizePolicy(sizePolicy)
        self.maintenance_sculpting_label.setObjectName("maintenance_sculpting_label")
        self.gridLayout_6.addWidget(self.maintenance_sculpting_label, 1, 1, 1, 1)
        self.write_outages_to_text_files_checkBox = QCheckBox(self.output_groupBox)
        self.write_outages_to_text_files_checkBox.setObjectName("write_outages_to_text_files_checkBox")
        self.gridLayout_6.addWidget(self.write_outages_to_text_files_checkBox, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.output_groupBox)
        self.gridLayout_7.addWidget(self.groupBox, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QObject.connect(self.horizontalSlider, SIGNAL("valueChanged(int)"), self.maintenance_sculpting_label.setNum)
        QMetaObject.connectSlotsByName(Form)
    
    def setInput(self, input):
        self.input = input
        self.loadpasascreen()
    
    def getOutput(self):
        self.savepasascreen()
        return self.output

    def loadpasascreen(self):
        self.demandsize_participation_checkBox.setChecked(self.input["demandsize_participation"])
        self.depand_purchaser_bids_checkBox.setChecked(self.input["depand_purchaser_bids"])
        self.contract_generation_checkBox.setChecked(self.input["contract_generation"])
        self.contract_load_checkBox.setChecked(self.input["contract_load"])
        self.market_purchases_checkBox.setChecked(self.input["market_purchases"])
        self.enforce_line_and_transformer_limits_checkBox.setChecked(self.input["enforce_line_and_transformer_limits"])
        self.enforce_interface_limits_checkBox.setChecked(self.input["enforce_interface_limits"])
        self.maintenance_sculpting_label.setText(self.input["maintenance_sculpting"])
        self.horizontalSlider.setValue(int(self.input["maintenance_sculpting"]))
        self.compute_indices_checkBox.setChecked(self.input["compute_indices"])
        self.compute_multiarea_reliability_indices_checkBox.setChecked(self.input["compute_multiarea_reliability_indices"])
        self.outage_increment_mw.setValue(int(self.input["outage_increment_mw"]))
        self.write_outages_to_text_files_checkBox.setChecked(self.input["write_outages_to_text_files"])

        self.interval_radioButton.setChecked(self.input["resolution"] == "Interval")
        self.day_radioButton.setChecked(self.input["resolution"] == "Day")
        self.week_radioButton.setChecked(self.input["resolution"] == "Week")

        self.regional_radioButton.setChecked(self.input["transmission"] == "Regional")
        self.zonal_radioButton.setChecked(self.input["transmission"] == "Zonal")

        self.deterministic_radioButton.setChecked(self.input["stochastic_method"] == "Deterministic")
        self.independant_samples_sequential_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Sequential)")
        self.independant_samples_parallel_radioButton.setChecked(self.input["stochastic_method"] == "Independent Samples (Parallel)")
        self.scenariowise_decomposition_radioButton.setChecked(self.input["stochastic_method"] == "Scenario-wise Decomposition")

    def savepasascreen(self):
        self.output = pasa_default_input | {
            "demandsize_participation": self.demandsize_participation_checkBox.isChecked(),
            "depand_purchaser_bids": self.depand_purchaser_bids_checkBox.isChecked(),
            "contract_generation": self.contract_generation_checkBox.isChecked(),
            "contract_load": self.contract_load_checkBox.isChecked(),
            "market_purchases": self.market_purchases_checkBox.isChecked(),
            "enforce_line_and_transformer_limits": self.enforce_line_and_transformer_limits_checkBox.isChecked(),
            "enforce_interface_limits": self.enforce_interface_limits_checkBox.isChecked(),
            "maintenance_sculpting": self.maintenance_sculpting_label.text(),
            "compute_indices": self.compute_indices_checkBox.isChecked(),
            "compute_multiarea_reliability_indices": self.compute_multiarea_reliability_indices_checkBox.isChecked(),
            "outage_increment_mw": str(self.outage_increment_mw.value()),
            "write_outages_to_text_files": self.write_outages_to_text_files_checkBox.isChecked()
        }

        if self.interval_radioButton.isChecked():
            self.output["resolution"] = "Interval"
        if self.day_radioButton.isChecked():
            self.output["resolution"] = "Day"
        if self.week_radioButton.isChecked():
            self.output["resolution"] = "Week"

        if self.regional_radioButton.isChecked():
            self.output["transmission"] = "Regional"
        if self.zonal_radioButton.isChecked():
            self.output["transmission"] = "Zonal"

        if self.deterministic_radioButton.isChecked():
            self.output["stochastic_method"] = "Deterministic"
        if self.independant_samples_sequential_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Sequential)"
        if self.independant_samples_parallel_radioButton.isChecked():
            self.output["stochastic_method"] = "Independent Samples (Parallel)"
        if self.scenariowise_decomposition_radioButton.isChecked():
            self.output["stochastic_method"] = "Scenario-wise Decomposition"

    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.resolution_groupBox.setTitle(QApplication.translate("Form", "Resolution (peak period every)"))
        self.interval_radioButton.setText(QApplication.translate("Form", "Interval"))
        self.day_radioButton.setText(QApplication.translate("Form", "Day"))
        self.week_radioButton.setText(QApplication.translate("Form", "Week"))
        self.transmission_groupBox.setTitle(QApplication.translate("Form", "Transmission"))
        self.regional_radioButton.setText(QApplication.translate("Form", "Regional"))
        self.zonal_radioButton.setText(QApplication.translate("Form", "Zonal"))
        self.enforce_line_and_transformer_limits_checkBox.setText(QApplication.translate("Form", "Enforce Line and Transformer Limits"))
        self.enforce_interface_limits_checkBox.setText(QApplication.translate("Form", "Enforce Interface Limits"))
        self.stochastic_method_groupBox.setTitle(QApplication.translate("Form", "Stochastic Method"))
        self.deterministic_radioButton.setText(QApplication.translate("Form", "Deterministic"))
        self.independant_samples_sequential_radioButton.setText(QApplication.translate("Form", "Independent Samples (Sequential)"))
        self.independant_samples_parallel_radioButton.setText(QApplication.translate("Form", "Independent Samples (Parallel)"))
        self.scenariowise_decomposition_radioButton.setText(QApplication.translate("Form", "Scenario-wise Decomposition"))
        self.load_and_supply_groupBox.setTitle(QApplication.translate("Form", "Load and Supply"))
        self.demandsize_participation_checkBox.setText(QApplication.translate("Form", "Demand-side Participation"))
        self.depand_purchaser_bids_checkBox.setText(QApplication.translate("Form", "Demand (Purchaser) Bids"))
        self.contract_generation_checkBox.setText(QApplication.translate("Form", "Contract Generation"))
        self.contract_load_checkBox.setText(QApplication.translate("Form", "Contract Load"))
        self.market_purchases_checkBox.setText(QApplication.translate("Form", "Market Purchases"))
        self.reliability_groupBox.setTitle(QApplication.translate("Form", "Reliability"))
        self.compute_indices_checkBox.setText(QApplication.translate("Form", "Compute Indices"))
        self.compute_multiarea_reliability_indices_checkBox.setText(QApplication.translate("Form", "Compute Multi-area Reliability Indices"))
        self.outage_increment_label.setText(QApplication.translate("Form", "Outage Increment (MW)"))
        self.output_groupBox.setTitle(QApplication.translate("Form", "Output"))
        self.maintenance_sculpting_label.setText(QApplication.translate("Form", "Maintenance Sculpting"))
        self.maintenance_sculpting_label.setText(QApplication.translate("Form", "0"))
        self.write_outages_to_text_files_checkBox.setText(QApplication.translate("Form", "Write Outages to Text Files"))

