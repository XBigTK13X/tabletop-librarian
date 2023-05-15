import PyQt6 as qt
from core.settings import config

class AboutDialog:
    def __init__(self):
        self.widget = qt.QtWidgets.QMessageBox()
        self.widget.setWindowTitle("About Tabletop Librarian")
        self.widget.setText(f"Version: {config.Version}")