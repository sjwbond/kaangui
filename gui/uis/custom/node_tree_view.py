from qt_core import *

style = """
QTreeView::branch:closed:has-children {
        border-image: none;
        image: url(gui/images/svg_icons/icon_chevron_right.svg);
}

QTreeView::branch:open:has-children {
        border-image: none;
        image: url(gui/images/svg_icons/icon_chevron_down.svg);
}
"""

class NodeTreeView(QTreeView):
    def __init__(self):
        super().__init__()

        self.setStyleSheet(style)

        self.setSortingEnabled(True)
        self.sortByColumn(0, Qt.AscendingOrder)

        self.rootModel = QStandardItemModel()
        self.proxyModel = QSortFilterProxyModel(
            self, recursiveFilteringEnabled=True
        )

        self.proxyModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxyModel.setSourceModel(self.rootModel)

        self.setModel(self.proxyModel)
        self.setDragDropMode(QAbstractItemView.InternalMove)

        self.rootNode = self.rootModel.invisibleRootItem()
