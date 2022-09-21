from qt_core import *
from gui.widgets.py_tree_view.style import style

# style = """
# QTreeView::branch:closed:has-children {
#         border-image: none;
#         image: url(gui/images/svg_icons/icon_chevron_right.svg);
# }

# QTreeView::branch:open:has-children {
#         border-image: none;
#         image: url(gui/images/svg_icons/icon_chevron_down.svg);
# }
# """

class NodeTreeView(QTreeView):
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
        super().__init__()

        # self.setStyleSheet(style)

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

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            color,
            bg_color,
            selection_color,
            scroll_bar_bg_color,
            scroll_bar_btn_color,
            context_color
        )

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        color,
        bg_color,
        selection_color,
        scroll_bar_bg_color,
        scroll_bar_btn_color,
        context_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,          
            _color = color,
            _bg_color = bg_color,
            _selection_color = selection_color,
            _scroll_bar_bg_color = scroll_bar_bg_color,
            _scroll_bar_btn_color = scroll_bar_btn_color,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)
