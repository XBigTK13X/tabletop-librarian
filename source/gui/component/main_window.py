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
        filter_layout = qt.QHBoxLayout()
        self.filter_input = qt.QLineEdit()
        self.filter_input.returnPressed.connect(self.filter_lists)
        self.filter_button = qt.QPushButton("Filter")
        self.filter_button.clicked.connect(self.filter_lists)
        self.tabs = qt.QTabWidget()
        self.mods_tab = ModsTab(parent=self)
        self.mod_tab = ModTab(parent=self)
        self.archives_tab = ArchivesTab(parent=self)
        self.tabs.addTab(self.mods_tab, "Mods")
        self.tabs.addTab(self.mod_tab, "Selected Mod")
        self.selected_mod_tab_index = self.tabs.count() - 1
        self.tabs.addTab(self.archives_tab, "Archives")
        self.tabs.addTab(PathsTab(parent=self), "Paths")

        filter_layout.addWidget(self.filter_input)
        filter_layout.addWidget(self.filter_button)
        root_layout.addLayout(filter_layout)
        root_layout.addWidget(self.tabs)
        self.setCentralWidget(central_widget)
        self.resize(800,600)

    def about(self):
        AboutDialog().widget.exec()

    def select_mod(self, mod_path):
        mod_cache.select_mod(mod_path)
        self.mod_tab.refresh()
        self.tabs.setCurrentIndex(self.selected_mod_tab_index)

    def filter_lists(self):
        filter_text = self.filter_input.text()
        self.mods_tab.update_filter(filter_text)
        self.archives_tab.update_filter(filter_text)
