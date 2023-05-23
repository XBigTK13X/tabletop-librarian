from gui.component.archives_tab import ArchivesTab
from gui.component.mods_tab import ModsTab
from gui.component.mod_tab import ModTab
from gui.component.paths_tab import PathsTab
from gui.component.about_dialog import AboutDialog

from core.data.mod_cache import mod_cache
from core.data.asset_cache import asset_cache
from core.data.refresh import refresher

import PyQt6.QtWidgets as qt

class MainWindow(qt.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Tabletop Librarian")
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("&Help")
        about_action = help_menu.addAction("&About")
        about_action.triggered.connect(self.about)

        refresher.scan_all()

        central_widget = qt.QWidget(self)
        root_layout = qt.QVBoxLayout(central_widget)
        self.tabs = qt.QTabWidget()
        self.mod_tab = ModTab(parent=self)
        self.tabs.addTab(ModsTab(parent=self), "Mods")
        self.tabs.addTab(self.mod_tab, "Selected Mod")
        self.selected_mod_tab_index = self.tabs.count() - 1
        self.tabs.addTab(ArchivesTab(parent=self), "Archives")
        self.tabs.addTab(PathsTab(parent=self), "Paths")
        root_layout.addWidget(self.tabs)
        self.setCentralWidget(central_widget)
        self.resize(800,600)

    def about(self):
        AboutDialog().widget.exec()

    def select_mod(self, mod_path):
        mod_cache.select_mod(mod_path)
        self.mod_tab.refresh()
        self.tabs.setCurrentIndex(self.selected_mod_tab_index)
