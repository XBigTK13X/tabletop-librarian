import PyQt6.QtWidgets as qt

from core.data.mod_cache import mod_cache

class ModTab(qt.QWidget):
    def __init__(self,parent=None):
        super(ModTab, self).__init__()

        layout = qt.QVBoxLayout()
        self.setLayout(layout)

    def select_mod(self, mod):
        print("Oh yeah")