import PyQt6.QtWidgets as qt
from gui.games_tab import GamesTab
from gui.paths_tab import PathsTab

class MainWindow(qt.QMainWindow):
    def __init__(self, games, parent=None):
        super(MainWindow, self).__init__()
        central_widget = qt.QWidget(self)
        root_layout = qt.QVBoxLayout(central_widget)
        tabs = qt.QTabWidget()
        tabs.addTab(GamesTab(games).widget,"Games")
        tabs.addTab(PathsTab(games).widget, "Paths")
        root_layout.addWidget(tabs)
        self.setCentralWidget(central_widget)
