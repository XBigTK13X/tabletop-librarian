import PyQt6.QtWidgets as qt

class PathsTab:
    def __init__(self, games):
        self.widget = qt.QWidget()
        self.layout = qt.QVBoxLayout()
        self.games = games
        table = qt.QTableWidget(0, 3)
        table.setHorizontalHeaderLabels(['Name', 'Archive', 'Local'])
        table.horizontalHeader().setSectionResizeMode(0,qt.QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(1,qt.QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(2,qt.QHeaderView.ResizeMode.Stretch)
        for ii, game in enumerate(games):
            table.setRowCount(ii+1)
            table.setItem(ii, 0, qt.QTableWidgetItem(game.name))
            table.setItem(ii, 1, qt.QTableWidgetItem(game.archive_path))
            table.setItem(ii, 2, qt.QTableWidgetItem(game.local_path))
        self.widget = table