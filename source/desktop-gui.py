# This Python file uses the following encoding: utf-8
import sys
import PyQt6.QtWidgets as qt

from gui.component.main_window import MainWindow

from core.model.game import Game

games = [
    Game('Dice Throne', 'Q:/software/game/tts/mods/d/Dice Throne.ttsmod', 'E:/tts/Mods/Workshop/Dice Throne Adventures Scripted.json')
]

if __name__ == "__main__":
    app = qt.QApplication([])
    window = MainWindow(games)
    window.show()
    sys.exit(app.exec())
