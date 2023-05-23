from gui.component.archives_tab import ArchivesTab
from gui.component.mods_tab import ModsTab
from gui.component.mod_tab import ModTab
from gui.component.paths_tab import PathsTab
from gui.component.about_dialog import AboutDialog

from core.data.mod_cache import mod_cache

import PyQt6.QtWidgets as qt

class MainWindow(qt.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Tabletop Librarian")
        menu_bar = self.menuBar()
        help_menu = menu_bar.addMenu("&Help")
        about_action = help_menu.addAction("&About")
        about_action.triggered.connect(self.about)

        mod_cache.refresh()

        central_widget = qt.QWidget(self)
        root_layout = qt.QVBoxLayout(central_widget)
        tabs = qt.QTabWidget()
        mod_tab = ModTab()
        tabs.addTab(ModsTab(mod_tab), "Mods")
        tabs.addTab(mod_tab, "Selected Mod")
        tabs.addTab(ArchivesTab(), "Archives")
        tabs.addTab(PathsTab(), "Paths")
        root_layout.addWidget(tabs)
        self.setCentralWidget(central_widget)
        self.resize(800,600)

    def about(self):
        AboutDialog().widget.exec()
