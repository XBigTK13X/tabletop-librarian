# This Python file uses the following encoding: utf-8
import sys
import PyQt6.QtWidgets as qt

from gui.component.main_window import MainWindow

from core.data.game_list import game_list

if __name__ == "__main__":
    app = qt.QApplication([])
    window = MainWindow(game_list)
    window.show()
    sys.exit(app.exec())
