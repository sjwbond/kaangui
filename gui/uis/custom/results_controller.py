from gui.uis.custom.api import WebAPI
from gui.uis.custom.result_tree_view import ResultTreeView
from qt_core import *

class ResultsController:
    def __init__(self, api: WebAPI, list: ResultTreeView) -> None:
        self.api = api
        self.list = list

        self.results = api.list_results()
        self.list.rootModel.clear()
        for result in self.results:
            self.list.rootModel.invisibleRootItem().appendRow(QStandardItem(result))
