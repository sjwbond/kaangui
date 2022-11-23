from gui.uis.custom.combo_delegate import ComboDelegate
from gui.uis.custom.text_delegate import TextDelegate
from qt_core import *
from gui.widgets.py_table_widget.style import style


class PropertiesTableView(QTableView):
  def __init__(self, theme):
    super().__init__()
    self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.setSelectionMode(QAbstractItemView.ExtendedSelection)
    self.setSelectionBehavior(QAbstractItemView.SelectRows)

    self.comboDelegate = ComboDelegate([])
    self.setItemDelegateForColumn(2, self.comboDelegate)
        
    self.textDelegate = TextDelegate()
    self.setItemDelegateForColumn(0, self.textDelegate)
    self.setItemDelegateForColumn(1, self.textDelegate)
    self.setItemDelegateForColumn(3, self.textDelegate)
    self.setItemDelegateForColumn(4, self.textDelegate)
    self.setItemDelegateForColumn(5, self.textDelegate)
    self.setItemDelegateForColumn(6, self.textDelegate)
    self.setItemDelegateForColumn(7, self.textDelegate)
    self.setItemDelegateForColumn(8, self.textDelegate)
    self.setItemDelegateForColumn(9, self.textDelegate)
    self.setItemDelegateForColumn(10, self.textDelegate)
    self.setItemDelegateForColumn(11, self.textDelegate)
    self.setItemDelegateForColumn(12, self.textDelegate)

    # SET STYLESHEET
    self.set_stylesheet(
        radius = 8,
        color = theme["text_foreground"],
        selection_color = theme["context_color"],
        bg_color = theme["bg_two"],
        header_horizontal_color = theme["dark_two"],
        header_vertical_color = theme["bg_three"],
        bottom_line_color = theme["bg_three"],
        grid_line_color = theme["bg_one"],
        scroll_bar_bg_color = theme["bg_one"],
        scroll_bar_btn_color = theme["dark_four"],
        context_color = theme["context_color"]
    )
    
  def setComboProps(self, props: list[str]):
      self.comboDelegate.setItems(props)

  # SET STYLESHEET
  def set_stylesheet(
      self,
      radius,
      color,
      bg_color,
      header_horizontal_color,
      header_vertical_color,
      selection_color,
      bottom_line_color,
      grid_line_color,
      scroll_bar_bg_color,
      scroll_bar_btn_color,
      context_color
  ):
      # APPLY STYLESHEET
      style_format = style.format(
          _radius = radius,          
          _color = color,
          _bg_color = bg_color,
          _header_horizontal_color = header_horizontal_color,
          _header_vertical_color = header_vertical_color,
          _selection_color = selection_color,
          _bottom_line_color = bottom_line_color,
          _grid_line_color = grid_line_color,
          _scroll_bar_bg_color = scroll_bar_bg_color,
          _scroll_bar_btn_color = scroll_bar_btn_color,
          _context_color = context_color
      )
      self.setStyleSheet(style_format)
