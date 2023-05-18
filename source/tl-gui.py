# This Python file uses the following encoding: utf-8
import sys
import PyQt6.QtWidgets as qt

from gui.component.main_window import MainWindow

if __name__ == "__main__":
    app = qt.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
