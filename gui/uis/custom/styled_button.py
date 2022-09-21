from qt_core import *
from gui.widgets import *
from gui.core.functions import *

class StyledButton(PyPushButton):
    def __init__(self, text, icon_name=None, themes=None):
        if icon_name is not None:
            text = "  " + text
        super().__init__(
            text=text,
            radius=8,
            color=themes["app_color"]["text_foreground"],
            bg_color=themes["app_color"]["dark_one"],
            bg_color_hover=themes["app_color"]["dark_three"],
            bg_color_pressed=themes["app_color"]["dark_four"],
        )
        self.setMinimumHeight(30)

        if icon_name is not None:
            self.icon = QIcon(Functions.set_svg_icon(icon_name))
            self.setIcon(self.icon)
