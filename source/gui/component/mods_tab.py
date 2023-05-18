import PyQt6.QtWidgets as qt

from core.data.mod_cache import mod_cache

class ModsTab:
    def __init__(self):
        mod_cache.refresh()
        table = qt.QTableWidget(0, 4)
        table.setHorizontalHeaderLabels(['Name', 'Archive', 'Mod', 'Source'])
        table.horizontalHeader().setSectionResizeMode(0,qt.QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(1,qt.QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(2,qt.QHeaderView.ResizeMode.Stretch)
        table.horizontalHeader().setSectionResizeMode(3,qt.QHeaderView.ResizeMode.Stretch)
        for ii, entry in enumerate(mod_cache.all()):
            table.setRowCount(ii+1)
            table.setItem(ii, 0, qt.QTableWidgetItem(entry.file_name))
            table.setItem(ii, 1, qt.QTableWidgetItem('Archive' if entry.data_kind == 'archive' else ''))
            table.setItem(ii, 2, qt.QTableWidgetItem('Mod' if entry.data_kind == 'mod' else ''))
            table.setItem(ii, 3, qt.QTableWidgetItem(entry.source.location))
        self.widget = table