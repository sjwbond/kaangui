from qt_core import *

class NodeSortFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, parent, model):
        super().__init__(parent, recursiveFilteringEnabled=True)
        self.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.setSourceModel(model)
    
    def lessThan(self, left, right):
        left_is_folder = left.data(Qt.UserRole) == "folder"
        left_data = left.data(Qt.DisplayRole)
        right_is_folder = right.data(Qt.UserRole) == "folder"
        right_data = right.data(Qt.DisplayRole)
        sort_order = self.sortOrder()

        if left_is_folder and not right_is_folder:
            result = sort_order == Qt.AscendingOrder
        elif not left_is_folder and right_is_folder:
            result = sort_order != Qt.AscendingOrder
        elif left_data is None:
            result = True
        elif right_data is None:
            result = False
        else:
            result = left_data < right_data
        return result