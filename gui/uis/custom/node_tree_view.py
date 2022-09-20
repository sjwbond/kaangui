from qt_core import *

class NodeTreeView(QTreeView):
    def __init__(self):
        super().__init__()

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
