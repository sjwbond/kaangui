from gui.uis.custom.node_sort_filter_proxy_model import NodeSortFilterProxyModel
from gui.widgets.py_tree_view.py_tree_view import PyTreeView
from qt_core import *

class NodeTreeView(PyTreeView):
    itemDropped = Signal()

    def __init__(
        self,
        radius = 8,
        color = "#FFF",
        bg_color = "#444",
        selection_color = "#FFF",
        scroll_bar_bg_color = "#FFF",
        scroll_bar_btn_color = "#3333",
        context_color = "#00ABE8"
    ):
        super().__init__(
            radius = radius,
            color = color,
            bg_color = bg_color,
            selection_color = selection_color,
            scroll_bar_bg_color = scroll_bar_bg_color,
            scroll_bar_btn_color = scroll_bar_btn_color,
            context_color = context_color
        )

        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)

        self.rootModel = QStandardItemModel()
        self.proxyModel = NodeSortFilterProxyModel(self, self.rootModel)

        self.setModel(self.proxyModel)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.rootNode = self.rootModel.invisibleRootItem()

        self.setSelectionMode(self.SingleSelection)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setDropIndicatorShown(True)

    def dropEvent(self, event):
        self.itemDropped.emit()
        super().dropEvent(event)