import csv
import datetime
import time
from gui.uis.custom.api import WebAPI
from gui.uis.custom.node_sort_filter_proxy_model import NodeSortFilterProxyModel
from gui.uis.custom.result_tree_view import ResultTreeView
from gui.uis.custom.styled_button import StyledButton
from gui.uis.custom.time_series_table_model import TimeSeriesTableModel
from gui.uis.custom.time_series_table_view import TimeSeriesTableView
from gui.uis.custom.time_series_tree_view import TimeSeriesTreeView
from gui.uis.custom.constants import plot_colors
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from pyqtgraph import DateAxisItem, PlotWidget, mkPen
from qt_core import *

class ResultsController:
    def __init__(self, api: WebAPI, layout: QBoxLayout, themes: dict) -> None:
        self.setup_layout(layout, themes)

        self.api = api
        self.current_sample_from = ""
        self.current_sample_to = ""

        self.load_results()

    def load_results(self):
        self.results = self.api.list_results()
        self.results_tree.rootModel.clear()
        for result in self.results:
            self.results_tree.rootModel.invisibleRootItem().appendRow(QStandardItem(result))

    def results_selection_changed(self):
        selected_index = self.results_tree.currentIndex()
        if selected_index is None:
            return

        self.time_series_tree.rootModel = QStandardItemModel()
        
        self.tsns = self.api.list_tsn_for_result(selected_index.data(Qt.DisplayRole))
        for tsn in self.tsns:
            item = QStandardItem(tsn["tsn_name"])
            item.setData(tsn["tsn_id"], Qt.UserRole)
            self.time_series_tree.rootModel.invisibleRootItem().appendRow(item)

        self.time_series_tree.proxyModel = NodeSortFilterProxyModel(self.time_series_tree, self.time_series_tree.rootModel)
        self.time_series_tree.setModel(self.time_series_tree.proxyModel)
        self.set_time_series_filter(self.time_series_filter_edit.text())
    
    def set_results_filter(self, text: str):
        self.results_tree.proxyModel.setFilterRegularExpression(text)

    def set_time_series_filter(self, text: str):
        self.time_series_tree.proxyModel.setFilterRegularExpression(text)

    def set_sample_from(self, text: str):
        self.current_sample_from = text

    def set_sample_to(self, text: str):
        self.current_sample_to = text

    def add_time_series(self):
        selected_results_index = self.results_tree.currentIndex()
        selected_time_series_index = self.time_series_tree.currentIndex()
        if selected_results_index is None or selected_time_series_index is None or \
                selected_results_index.data(Qt.DisplayRole) is None or selected_time_series_index.data(Qt.DisplayRole) is None or \
                self.current_sample_from == "" or self.current_sample_to == "":
            return

        self.time_series_table_model.appendRow([
            selected_results_index.data(Qt.DisplayRole),
            selected_time_series_index.data(Qt.DisplayRole),
            self.current_sample_from,
            self.current_sample_to,
            selected_time_series_index.data(Qt.UserRole)
        ])
    
    def delete_rows(self):
        selected_rows = self.time_series_table_view.selectionModel().selectedRows()
        self.time_series_table_model.removeRows(selected_rows)
    
    def get_time_series_data(self):
        queries = []
        rows = self.time_series_table_model.getData()
        for row in rows:
            queries.append({
                "result": row[0],
                "time_series_id": int(row[4]),
                "sample_from": int(row[2]),
                "sample_to": int(row[3])
            })
        data = self.api.get_time_series_data(queries)
        return queries, data
    
    def draw_chart(self):
        queries, data = self.get_time_series_data()
        self.plot_widget.clear()
        for i in range(len(data)):
            result = data[i]
            color = plot_colors[i % len(plot_colors)]
            xs = []
            ys = []
            for item in result:
                days = int(item["tsd_tim_id_start"])
                date = datetime.date(2000, 1, 1) + datetime.timedelta(days=days)
                xs.append(time.mktime(date.timetuple()))
                ys.append(item["tsd_value"])
            self.plot_widget.plot(xs, ys, pen=mkPen(color=color))
    
    def export_csv(self):
        queries, data = self.get_time_series_data()
        (name, _) = QFileDialog.getSaveFileName(None, "Select CSV File", dir=f"results.csv")
        if name != '':
            with open(name, "w", encoding="utf8", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["result", "time_series_id", "tsd_tim_id_start", "tsd_value"])
                for i in range(len(data)):
                    query = queries[i]
                    result = data[i]
                    for item in result:
                        writer.writerow([query["result"], int(query["time_series_id"]), int(item["tsd_tim_id_start"]), item["tsd_value"]])

    def setup_layout(self, layout: QBoxLayout, themes: dict):
        self.results_filter_edit = PyLineEdit(
            text = "",
            place_holder_text = "Filter results",
            radius = 8,
            border_size = 2,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["white"],
            bg_color = themes["app_color"]["dark_one"],
            bg_color_active = themes["app_color"]["dark_three"],
            context_color = themes["app_color"]["context_color"]
        )
        self.results_filter_edit.textChanged.connect(self.set_results_filter)

        self.results_tree = ResultTreeView(
            radius = 8,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["bg_one"],
            bg_color = themes["app_color"]["bg_two"],
            scroll_bar_bg_color = themes["app_color"]["bg_one"],
            scroll_bar_btn_color = themes["app_color"]["dark_four"],
            context_color = themes["app_color"]["context_color"]
        )
        self.results_tree.clicked.connect(self.results_selection_changed)

        self.time_series_filter_edit = PyLineEdit(
            text = "",
            place_holder_text = "Filter time series",
            radius = 8,
            border_size = 2,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["white"],
            bg_color = themes["app_color"]["dark_one"],
            bg_color_active = themes["app_color"]["dark_three"],
            context_color = themes["app_color"]["context_color"]
        )
        self.time_series_filter_edit.textChanged.connect(self.set_time_series_filter)

        self.time_series_tree = TimeSeriesTreeView(
            radius = 8,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["bg_one"],
            bg_color = themes["app_color"]["bg_two"],
            scroll_bar_bg_color = themes["app_color"]["bg_one"],
            scroll_bar_btn_color = themes["app_color"]["dark_four"],
            context_color = themes["app_color"]["context_color"]
        )

        self.sample_from_edit = PyLineEdit(
            text = "",
            place_holder_text = "Sample from",
            radius = 8,
            border_size = 2,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["white"],
            bg_color = themes["app_color"]["dark_one"],
            bg_color_active = themes["app_color"]["dark_three"],
            context_color = themes["app_color"]["context_color"]
        )
        self.sample_from_edit.textChanged.connect(self.set_sample_from)

        self.sample_to_edit = PyLineEdit(
            text = "",
            place_holder_text = "Sample to",
            radius = 8,
            border_size = 2,
            color = themes["app_color"]["text_foreground"],
            selection_color = themes["app_color"]["white"],
            bg_color = themes["app_color"]["dark_one"],
            bg_color_active = themes["app_color"]["dark_three"],
            context_color = themes["app_color"]["context_color"]
        )
        self.sample_to_edit.textChanged.connect(self.set_sample_to)

        self.add_time_series_button = StyledButton(text="Add Time Series", themes=themes)
        self.add_time_series_button.clicked.connect(self.add_time_series)

        self.time_series_table_view = TimeSeriesTableView(themes["app_color"])
        self.time_series_table_model = TimeSeriesTableModel([])
        self.time_series_table_view.setModel(self.time_series_table_model)

        self.delete_rows_button = StyledButton(text="Delete Selected Rows", themes=themes)
        self.delete_rows_button.clicked.connect(self.delete_rows)

        self.draw_chart_button = StyledButton(text="Draw Chart", themes=themes)
        self.draw_chart_button.clicked.connect(self.draw_chart)

        self.export_csv_button = StyledButton(text="Export CSV", themes=themes)
        self.export_csv_button.clicked.connect(self.export_csv)

        self.axis = DateAxisItem()
        self.plot_widget = PlotWidget(axisItems={'bottom': self.axis})

        self.results_left_layout = QVBoxLayout()
        self.results_left_layout.setObjectName(u"results_left_layout")
        layout.addLayout(self.results_left_layout, 1)
        
        self.results_right_layout = QVBoxLayout()
        self.results_right_layout.setObjectName(u"results_right_layout")
        layout.addLayout(self.results_right_layout, 2)
        
        self.results_left_layout.addWidget(self.results_filter_edit)
        self.results_left_layout.addWidget(self.results_tree)
        
        self.results_left_layout.addWidget(self.time_series_filter_edit)
        self.results_left_layout.addWidget(self.time_series_tree)

        self.sample_range_layout = QHBoxLayout()
        self.sample_range_layout.addWidget(self.sample_from_edit)
        self.sample_range_layout.addWidget(self.sample_to_edit)
        self.results_left_layout.addLayout(self.sample_range_layout)

        self.results_left_layout.addWidget(self.add_time_series_button)

        self.results_right_layout.addWidget(self.time_series_table_view)
        
        self.time_series_controls_layout = QHBoxLayout()
        self.time_series_controls_layout.addWidget(self.delete_rows_button)
        self.time_series_controls_layout.addWidget(self.draw_chart_button)
        self.time_series_controls_layout.addWidget(self.export_csv_button)
        self.results_right_layout.addLayout(self.time_series_controls_layout)

        self.results_right_layout.addWidget(self.plot_widget)
