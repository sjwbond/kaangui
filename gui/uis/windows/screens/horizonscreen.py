# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'horizonscreen.ui'
#
# Created: Thu Jun  9 15:58:49 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import math
from datetime import datetime
from datetime import timedelta

from qt_core import *

horizons_default_input = {
    'interval_length': '24',
    'begin_on': '31 Dec 2016',
    'end_on': '31 Dec 2016',
    'day_begins': '12:00 AM',
    'year_ends': 'Automatic',
    'week_begins': 'Automatic',
    'typical_week_per_month': '4',
    'begin_at': '31 Dec 2016',
    'begin_at_interval': '1',
    'end_interval': 'TextLabel',
    'steps_of': 'Hour',
    'steps_of_count': '1',
    'schedule': '7',
    'additional_lockahead': False,
    'length': 'Day(s)',
    'length_count': '1',
    'resolution': '1',
    'chronological_phase': 'Typical Week'
}

class Ui_HorizonScreen(QObject):
    input = horizons_default_input
    output = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1120, 820)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.planning_horizaon_groupBox = QGroupBox(self.groupBox)
        self.planning_horizaon_groupBox.setObjectName("planning_horizaon_groupBox")
        self.gridLayout = QGridLayout(self.planning_horizaon_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.interval_length_label = QLabel(self.planning_horizaon_groupBox)
        self.interval_length_label.setObjectName("interval_length_label")
        self.gridLayout.addWidget(self.interval_length_label, 1, 0, 1, 1)
        self.end_on_label = QLabel(self.planning_horizaon_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.end_on_label.sizePolicy().hasHeightForWidth())
        self.end_on_label.setSizePolicy(sizePolicy)
        self.end_on_label.setObjectName("end_on_label")
        self.gridLayout.addWidget(self.end_on_label, 0, 3, 1, 1)
        self.begin_on_dateEdit = QDateEdit(self.planning_horizaon_groupBox)
        self.begin_on_dateEdit.setDateTime(QDateTime(QDate(2017, 1, 1), QTime(0, 0, 0)))
        self.begin_on_dateEdit.setObjectName("begin_on_dateEdit")
        self.gridLayout.addWidget(self.begin_on_dateEdit, 0, 1, 1, 1)
        self.year_ends_comboBox = QComboBox(self.planning_horizaon_groupBox)
        self.year_ends_comboBox.setObjectName("year_ends_comboBox")
        self.gridLayout.addWidget(self.year_ends_comboBox, 3, 1, 1, 1)
        self.day_begins_comboBox = QComboBox(self.planning_horizaon_groupBox)
        self.day_begins_comboBox.setObjectName("day_begins_comboBox")
        self.gridLayout.addWidget(self.day_begins_comboBox, 2, 1, 1, 1)
        self.begin_on_label = QLabel(self.planning_horizaon_groupBox)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.begin_on_label.sizePolicy().hasHeightForWidth())
        self.begin_on_label.setSizePolicy(sizePolicy)
        self.begin_on_label.setObjectName("begin_on_label")
        self.gridLayout.addWidget(self.begin_on_label, 0, 0, 1, 1)
        self.week_begins_comboBox = QComboBox(self.planning_horizaon_groupBox)
        self.week_begins_comboBox.setObjectName("week_begins_comboBox")
        self.gridLayout.addWidget(self.week_begins_comboBox, 4, 1, 1, 1)
        self.day_begins_label = QLabel(self.planning_horizaon_groupBox)
        self.day_begins_label.setObjectName("day_begins_label")
        self.gridLayout.addWidget(self.day_begins_label, 2, 0, 1, 1)
        self.end_on_dateEdit = QDateEdit(self.planning_horizaon_groupBox)
        self.end_on_dateEdit.setDateTime(QDateTime(QDate(2017, 1, 1), QTime(0, 0, 0)))
        self.end_on_dateEdit.setObjectName("end_on_dateEdit")
        self.gridLayout.addWidget(self.end_on_dateEdit, 0, 4, 1, 1)
        self.interval_length_comboBox = QComboBox(self.planning_horizaon_groupBox)
        self.interval_length_comboBox.setObjectName("interval_length_comboBox")
        self.gridLayout.addWidget(self.interval_length_comboBox, 1, 1, 1, 1)
        self.year_ends_label = QLabel(self.planning_horizaon_groupBox)
        self.year_ends_label.setObjectName("year_ends_label")
        self.gridLayout.addWidget(self.year_ends_label, 3, 0, 1, 1)
        self.week_begins_label = QLabel(self.planning_horizaon_groupBox)
        self.week_begins_label.setObjectName("week_begins_label")
        self.gridLayout.addWidget(self.week_begins_label, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.planning_horizaon_groupBox, 0, 0, 1, 1)
        self.chronological_phase_groupBox = QGroupBox(self.groupBox)
        self.chronological_phase_groupBox.setObjectName("chronological_phase_groupBox")
        self.full_chronology_radioButton = QRadioButton(self.chronological_phase_groupBox)
        self.full_chronology_radioButton.setGeometry(QRect(30, 40, 101, 17))
        self.full_chronology_radioButton.setObjectName("full_chronology_radioButton")
        self.typical_week_per_month_radioButton = QRadioButton(self.chronological_phase_groupBox)
        self.typical_week_per_month_radioButton.setGeometry(QRect(30, 70, 141, 17))
        self.typical_week_per_month_radioButton.setChecked(True)
        self.typical_week_per_month_radioButton.setObjectName("typical_week_per_month_radioButton")
        self.additional_lockahead = QCheckBox(self.chronological_phase_groupBox)
        self.additional_lockahead.setGeometry(QRect(30, 230, 131, 17))
        self.additional_lockahead.setObjectName("additional_lockahead")
        self.synchronize_pushButton = QPushButton(self.chronological_phase_groupBox)
        self.synchronize_pushButton.setGeometry(QRect(300, 60, 161, 31))
        self.synchronize_pushButton.setObjectName("synchronize_pushButton")
        self.layoutWidget = QWidget(self.chronological_phase_groupBox)
        self.layoutWidget.setGeometry(QRect(30, 110, 321, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.begin_at_interval_label = QLabel(self.layoutWidget)
        self.begin_at_interval_label.setObjectName("begin_at_interval_label")
        self.horizontalLayout_2.addWidget(self.begin_at_interval_label)
        self.begin_at_interval_spinBox = QSpinBox(self.layoutWidget)
        self.begin_at_interval_spinBox.setProperty("value", 1)
        self.begin_at_interval_spinBox.setObjectName("begin_at_interval_spinBox")
        self.horizontalLayout_2.addWidget(self.begin_at_interval_spinBox)
        self.begin_at_dateEdit = QDateEdit(self.layoutWidget)
        self.begin_at_dateEdit.setDateTime(QDateTime(QDate(2017, 1, 1), QTime(0, 0, 0)))
        self.begin_at_dateEdit.setObjectName("begin_at_dateEdit")
        self.horizontalLayout_2.addWidget(self.begin_at_dateEdit)
        self.layoutWidget1 = QWidget(self.chronological_phase_groupBox)
        self.layoutWidget1.setGeometry(QRect(30, 140, 321, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.schedule_label = QLabel(self.layoutWidget1)
        self.schedule_label.setObjectName("schedule_label")
        self.horizontalLayout_3.addWidget(self.schedule_label)
        self.schedule_spinBox = QSpinBox(self.layoutWidget1)
        self.schedule_spinBox.setProperty("value", 7)
        self.schedule_spinBox.setObjectName("schedule_spinBox")
        self.horizontalLayout_3.addWidget(self.schedule_spinBox)
        self.steps_of_label = QLabel(self.layoutWidget1)
        self.steps_of_label.setObjectName("steps_of_label")
        self.horizontalLayout_3.addWidget(self.steps_of_label)
        self.steps_of_spinBox = QSpinBox(self.layoutWidget1)
        self.steps_of_spinBox.setProperty("value", 1)
        self.steps_of_spinBox.setObjectName("steps_of_spinBox")
        self.horizontalLayout_3.addWidget(self.steps_of_spinBox)
        self.steps_of_comboBox = QComboBox(self.layoutWidget1)
        self.steps_of_comboBox.setObjectName("steps_of_comboBox")
        self.horizontalLayout_3.addWidget(self.steps_of_comboBox)
        self.layoutWidget2 = QWidget(self.chronological_phase_groupBox)
        self.layoutWidget2.setGeometry(QRect(30, 180, 321, 16))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.end_at_interval_label = QLabel(self.layoutWidget2)
        self.end_at_interval_label.setEnabled(True)
        self.end_at_interval_label.setObjectName("end_at_interval_label")
        self.horizontalLayout_6.addWidget(self.end_at_interval_label)
        self.end_interval_label = QLabel(self.layoutWidget2)
        self.end_interval_label.setEnabled(True)
        self.end_interval_label.setObjectName("end_interval_label")
        self.horizontalLayout_6.addWidget(self.end_interval_label)
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setEnabled(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_6.addWidget(self.label_12)
        self.typical_week_per_month_spinBox = QSpinBox(self.chronological_phase_groupBox)
        self.typical_week_per_month_spinBox.setGeometry(QRect(180, 70, 81, 22))
        self.typical_week_per_month_spinBox.setMinimum(1)
        self.typical_week_per_month_spinBox.setMaximum(5)
        self.typical_week_per_month_spinBox.setProperty("value", 4)
        self.typical_week_per_month_spinBox.setObjectName("typical_week_per_month_spinBox")
        self.groupBox_4 = QGroupBox(self.chronological_phase_groupBox)
        self.groupBox_4.setGeometry(QRect(20, 260, 471, 101))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setGeometry(QRect(10, 80, 75, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setObjectName("label_15")
        self.length_label = QLabel(self.groupBox_4)
        self.length_label.setGeometry(QRect(11, 21, 102, 20))
        self.length_label.setObjectName("length_label")
        self.length_comboBox = QComboBox(self.groupBox_4)
        self.length_comboBox.setGeometry(QRect(228, 21, 102, 20))
        self.length_comboBox.setObjectName("length_comboBox")
        self.resolution_label = QLabel(self.groupBox_4)
        self.resolution_label.setGeometry(QRect(11, 51, 77, 20))
        self.resolution_label.setObjectName("resolution_label")
        self.resolution_comboBox = QComboBox(self.groupBox_4)
        self.resolution_comboBox.setGeometry(QRect(120, 50, 101, 20))
        self.resolution_comboBox.setObjectName("resolution_comboBox")
        self.length_spinBox = QSpinBox(self.groupBox_4)
        self.length_spinBox.setGeometry(QRect(119, 21, 103, 20))
        self.length_spinBox.setProperty("value", 1)
        self.length_spinBox.setObjectName("length_spinBox")
        self.gridLayout_2.addWidget(self.chronological_phase_groupBox, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_4.setEnabled(False)




        self.begin_at_interval_spinBox.setEnabled(False)
        self.begin_at_dateEdit.setEnabled(False)

        self.begin_on_dateEdit.setCalendarPopup(True)
        self.begin_on_dateEdit.dateChanged.connect(self.beginDateChanged)
        self.end_on_dateEdit.setCalendarPopup(True)
        self.begin_at_dateEdit.setCalendarPopup(True)

        self.synchronize_pushButton.clicked.connect(self.syncToPlanningHorizon)
        self.begin_at_interval_spinBox.setMaximum(100000)

        self.intervallength = ["1 Hour","24 Hours","12 Hours","8 Hours","6 Hours","4 Hours","3 Hours","2 Hours","30 Minutes","20 Minutes","15 Minutes","10 Minutes","5 Minutes","1 Minute"]
        for value in self.intervallength:
            self.interval_length_comboBox.addItem(value)

        self.daybegins = ["12:00 AM",	"1:00 AM",	"2:00 AM",	"3:00 AM",	"4:00 AM",	"5:00 AM",	"6:00 AM",	"7:00 AM",	"8:00 AM",	"9:00 AM",	"10:00 AM",	"11:00 AM",	"12:00 PM",	"1:00 PM",	"2:00 PM",	"3:00 PM",	"4:00 PM",	"5:00 PM",	"6:00 PM",	"7:00 PM",	"8:00 PM",	"9:00 PM",	"10:00 PM",	"11:00 PM"]
        for value in self.daybegins:
            self.day_begins_comboBox.addItem(value)

        self.yearends = ["Automatic","January",	"February",	"March",	"April",	"May",	"June",	"July",	"August",	"September",	"October",	"November",	"December"]
        for value in self.yearends:
            self.year_ends_comboBox.addItem(value)

        self.weekbegins = ["Automatic","Sunday",	"Monday",	"Tuesday",	"Wednesday",	"Thursday",	"Friday",	"Saturday"]
        for value in self.weekbegins:
            self.week_begins_comboBox.addItem(value)

        self.chronosteptype = ["Hour","Day","Week"]
        for value in self.chronosteptype:
            self.steps_of_comboBox.addItem(value)

        self.chronolockaheadlength = ["Day(s)","Interval(s)","Week(s)"]
        for value in self.chronolockaheadlength:
            self.length_comboBox.addItem(value)

        self.chronolockaheadresolution = ["24 Hours","12 Hours","8 Hours","6 Hours","4 Hours","3 Hours","2 Hours","1 Hour","30 Minutes","20 Minutes","15 Minutes","10 Minutes","5 Minutes","1 Minute"]
        for value in self.chronolockaheadresolution:
            self.resolution_comboBox.addItem(value)


        self.retranslateUi(Form)
        self.full_chronology_radioButton.toggled.connect(self.fullChronologySelected)
        self.typical_week_per_month_radioButton.toggled.connect(self.typicalWeekPerMonthSelected)
        self.additional_lockahead.stateChanged.connect(self.additionalLockAhead)
        self.length_comboBox.currentIndexChanged.connect(self.additionalLockAhead)
        self.length_spinBox.valueChanged.connect(self.additionalLockAhead)


        self.begin_at_interval_spinBox.valueChanged.connect(self.calculateEndAtInterval)
        self.schedule_spinBox.valueChanged.connect(self.calculateEndAtInterval)
        self.steps_of_spinBox.valueChanged.connect(self.calculateEndAtInterval)
        self.steps_of_comboBox.currentIndexChanged.connect(self.calculateEndAtInterval)
        self.begin_at_dateEdit.dateChanged.connect(self.calculateEndAtInterval)

        QMetaObject.connectSlotsByName(Form)

        self.additional_lockahead.clicked.connect(self.enableSampleGroupBox)
    
    def setInput(self, input):
        self.input = input
        self.loadHorizon()
        self.enableSampleGroupBox()
    
    def getOutput(self):
        self.saveHorizon()
        return self.output

    def loadHorizon(self):
        temp=self.interval_length_comboBox.findText(self.numbersToStrings(self.input["interval_length"]))
        self.interval_length_comboBox.setCurrentIndex(temp)
        self.begin_on_dateEdit.setDate(QDate.fromString(self.input["begin_on"], "dd/MM/yyyy"))
        self.end_on_dateEdit.setDate(QDate.fromString(self.input["end_on"], "dd/MM/yyyy"))
        temp=self.day_begins_comboBox.findText(self.input["day_begins"])
        self.day_begins_comboBox.setCurrentIndex(temp)
        temp=self.year_ends_comboBox.findText(self.input["year_ends"])
        self.year_ends_comboBox.setCurrentIndex(temp)
        temp=self.week_begins_comboBox.findText(self.input["week_begins"])
        self.week_begins_comboBox.setCurrentIndex(temp)
        if self.input["chronological_phase"] == "Full":
            self.full_chronology_radioButton.setChecked(True)
        if self.input["chronological_phase"] == "Typical Week":
            self.typical_week_per_month_radioButton.setChecked(True)
        self.typical_week_per_month_spinBox.setValue(int(self.input["typical_week_per_month"]))
        self.begin_at_dateEdit.setDate(QDate.fromString(self.input["begin_at"], "dd MMM yyyy"))
        self.begin_at_interval_spinBox.setValue(int(self.input["begin_at_interval"]))
        self.end_interval_label.setText(self.input["end_interval"])
        temp=self.steps_of_comboBox.findText(self.input["steps_of"])
        self.steps_of_comboBox.setCurrentIndex(temp)
        self.steps_of_spinBox.setValue(int(self.input["steps_of_count"]))
        self.schedule_spinBox.setValue(int(self.input["schedule"]))
        if self.input["additional_lockahead"] == True:
            self.additional_lockahead.setChecked(True)
        if self.input["additional_lockahead"] == False:
            self.additional_lockahead.setChecked(False)
        temp=self.length_comboBox.findText(self.input["length"])
        self.length_comboBox.setCurrentIndex(temp)
        self.length_spinBox.setValue(int(self.input["length_count"]))
        temp=self.resolution_comboBox.findText(self.numbersToStrings(self.input["resolution"]))
        self.resolution_comboBox.setCurrentIndex(temp)

    def saveHorizon(self):
        self.output = horizons_default_input | {
          "interval_length": str(24//self.stringsToNumbers(self.interval_length_comboBox.currentText())),
          "begin_on": self.begin_on_dateEdit.date().toString("dd MMM yyyy"),
          "end_on": self.end_on_dateEdit.date().toString("dd MMM yyyy"),
          "day_begins": self.day_begins_comboBox.currentText(),
          "year_ends": self.year_ends_comboBox.currentText(),
          "week_begins": self.week_begins_comboBox.currentText(),
          "typical_week_per_month": str(self.typical_week_per_month_spinBox.value()),
          "begin_at": self.begin_at_dateEdit.date().toString("dd MMM yyyy"),
          "begin_at_interval": str(self.begin_at_interval_spinBox.value()),
          "end_interval": self.end_interval_label.text(),
          "steps_of": self.steps_of_comboBox.currentText(),
          "steps_of_count": str(self.steps_of_spinBox.value()),
          "schedule": str(self.schedule_spinBox.value()),
          "additional_lockahead": self.additional_lockahead.isChecked(),
          "length": self.length_comboBox.currentText(),
          "length_count": str(self.length_spinBox.value()),
          "resolution": str(24//self.stringsToNumbers(self.resolution_comboBox.currentText()))
        }

        if self.full_chronology_radioButton.isChecked():
            self.output["chronological_phase"] = "Full"
        if self.typical_week_per_month_radioButton.isChecked():
            self.output["chronological_phase"] = "Typical Week"

    def additionalLockAhead(self):
        if self.additional_lockahead.isChecked():
            if self.length_comboBox.currentText() == "Day(s)":
                temp = datetime.strptime(self.label_12.text(), "%d %b %Y")
                temp = temp + timedelta(days = self.length_spinBox.value())
                temp = datetime.strftime(temp, "%d %b %Y")
                self.label_15.setText(temp)

            if self.length_comboBox.currentText() == "Week(s)":
                temp = datetime.strptime(self.label_12.text(), "%d %b %Y")
                temp = temp + timedelta(weeks = self.length_spinBox.value())
                temp = datetime.strftime(temp, "%d %b %Y")
                self.label_15.setText(temp)

            if self.length_comboBox.currentText() == "Interval(s)":
                temp = datetime.strptime(self.label_12.text(), "%d %b %Y")
                temp = temp + timedelta(hours = self.length_spinBox.value()*self.stringsToNumbers(self.interval_length_comboBox.currentText()))
                temp = datetime.strftime(temp, "%d %b %Y")
                self.label_15.setText(temp)

    def syncToPlanningHorizon(self):
        self.label_12.setText(self.end_on_dateEdit.date().toString("dd MMM yyyy"))
        if str(self.steps_of_comboBox.currentText())=="Day":
            periodlegth = (self.end_on_dateEdit.date().toPython() - self.begin_on_dateEdit.date().toPython()).days
            stepsize = int(self.steps_of_spinBox.text())
            self.schedule_spinBox.setValue(periodlegth/stepsize+1)

    def beginDateChanged(self):
        self.begin_at_dateEdit.setDate(self.begin_on_dateEdit.date())

    def fullChronologySelected(self):
        self.typical_week_per_month_spinBox.setHidden(True)
        self.begin_at_interval_spinBox.setEnabled(True)
        self.begin_at_dateEdit.setEnabled(True)
        self.end_at_interval_label.setHidden(False)
        self.end_interval_label.setHidden(False)
        self.label_12.setHidden(False)
        self.calculateEndAtInterval()

    def typicalWeekPerMonthSelected(self):
        self.typical_week_per_month_spinBox.setHidden(False)
        self.begin_at_interval_spinBox.setEnabled(False)
        self.begin_at_dateEdit.setEnabled(False)
        self.end_at_interval_label.setHidden(True)
        self.end_interval_label.setHidden(True)
        self.label_12.setHidden(True)


    def stringsToNumbers(self,argument):
        return {
            "24 Hours":24,
            "12 Hours":12,
            "8 Hours":8,
            "6 Hours":6,
            "4 Hours":4,
            "3 Hours":3,
            "2 Hours":2,
            "1 Hour":1,
            "30 Minutes":0.5,
            "20 Minutes":1/3,
            "15 Minutes":0.25,
            "10 Minutes":1/6,
            "5 Minutes":1/12,
            "1 Minute":1/60,
        }[argument]

    def numbersToStrings(self,argument):
        return {
            "1":"24 Hours",
            "2":"12 Hours",
            "3":"8 Hours",
            "4":"6 Hours",
            "6":"4 Hours",
            "8":"3 Hours",
            "12":"2 Hours",
            "24":"1 Hour",
            "48":"30 Minutes",
            "72.0":"20 Minutes",
            "96":"15 Minutes",
            "144":"10 Minutes",
            "288":"5 Minutes",
            "1440":"1 Minute",
        }[argument]

    def calculateEndAtInterval(self):
        maxinterval = 24//self.stringsToNumbers(self.interval_length_comboBox.currentText())
        self.begin_at_interval_spinBox.setMaximum(maxinterval)
        self.steps_of_spinBox.setSingleStep(self.stringsToNumbers(self.interval_length_comboBox.currentText()))
        if str(self.steps_of_comboBox.currentText())=="Hour":
            add = math.ceil((self.schedule_spinBox.value() * self.steps_of_spinBox.value() + self.begin_at_interval_spinBox.value()-1) / 24)-1
            excesshours = self.schedule_spinBox.value() * self.steps_of_spinBox.value() - 24 * add
            newDate = self.begin_at_dateEdit.date().addDays(add)
            self.label_12.setText(newDate.toString("dd MMM yyyy"))
            endatinterval = (excesshours/self.stringsToNumbers(self.interval_length_comboBox.currentText())+self.begin_at_interval_spinBox.value()-1) % maxinterval
            if endatinterval == 0:
                endatinterval = maxinterval
            self.end_interval_label.setText(str(endatinterval))

        if str(self.steps_of_comboBox.currentText())=="Day":
            add = math.ceil((self.schedule_spinBox.value() * self.steps_of_spinBox.value() + self.begin_at_interval_spinBox.value()-1))-1
            newDate = self.begin_at_dateEdit.date().addDays(add)
            self.label_12.setText(newDate.toString("dd MMM yyyy"))
            endatinterval = (self.begin_at_interval_spinBox.value() + maxinterval - 1) % maxinterval
            if endatinterval == 0:
                endatinterval = maxinterval
            self.end_interval_label.setText(str(endatinterval))

        if str(self.steps_of_comboBox.currentText())=="Week":
            add = self.schedule_spinBox.value() * self.steps_of_spinBox.value() * 7
            newDate = self.begin_at_dateEdit.date().addDays(add)
            self.label_12.setText(newDate.toString("dd MMM yyyy"))
            endatinterval = self.begin_at_interval_spinBox.value()-1
            self.end_interval_label.setText(str(endatinterval))


    def enableSampleGroupBox(self):
        if self.additional_lockahead.isChecked() == True:
            self.groupBox_4.setEnabled(True)
        else:
            self.groupBox_4.setEnabled(False)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QApplication.translate("Form", "Form"))
        self.groupBox.setTitle(QApplication.translate("Form", "GroupBox"))
        self.planning_horizaon_groupBox.setTitle(QApplication.translate("Form", "Planning Horizon"))
        self.interval_length_label.setText(QApplication.translate("Form", "Interval Length:"))
        self.end_on_label.setText(QApplication.translate("Form", "End On:"))
        self.begin_on_label.setText(QApplication.translate("Form", "Begin On:"))
        self.day_begins_label.setText(QApplication.translate("Form", "Day Begins:"))
        self.year_ends_label.setText(QApplication.translate("Form", "Year Ends:"))
        self.week_begins_label.setText(QApplication.translate("Form", "Week Begins:"))
        self.chronological_phase_groupBox.setTitle(QApplication.translate("Form", "Chronological Phase"))
        self.full_chronology_radioButton.setText(QApplication.translate("Form", "Full Chronology"))
        self.typical_week_per_month_radioButton.setText(QApplication.translate("Form", "Typical week per month"))
        self.additional_lockahead.setText(QApplication.translate("Form", "Additional Lock-ahead"))
        self.synchronize_pushButton.setText(QApplication.translate("Form", "Synchronize to Planning Horizon"))
        self.begin_at_interval_label.setText(QApplication.translate("Form", "Begin at interval:"))
        self.schedule_label.setText(QApplication.translate("Form", "Schedule:"))
        self.steps_of_label.setText(QApplication.translate("Form", "step(s) of:"))
        self.end_at_interval_label.setText(QApplication.translate("Form", "End at interval:"))
        self.end_interval_label.setText(QApplication.translate("Form", "TextLabel"))
        self.label_12.setText(QApplication.translate("Form", "TextLabel"))
        self.label_15.setText(QApplication.translate("Form", "TextLabel"))
        self.length_label.setText(QApplication.translate("Form", "Length:"))
        self.resolution_label.setText(QApplication.translate("Form", "Resolution:"))
