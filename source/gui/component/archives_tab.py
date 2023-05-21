import PyQt6.QtWidgets as qt

from core.data.mod_cache import mod_cache

class ArchivesTab:
    def __init__(self):
        mod_cache.refresh()
        headers = ['Name', 'Source']
        column_count = len(headers)
        table = qt.QTableWidget(0, column_count)
        table.setHorizontalHeaderLabels(headers)
        for ii in range(0, column_count):
            table.horizontalHeader().setSectionResizeMode(ii,qt.QHeaderView.ResizeMode.Stretch)
        for ii, entry in enumerate(mod_cache.kind('archive')):
            table.setRowCount(ii+1)
            table.setItem(ii, 0, qt.QTableWidgetItem(entry.file_name))
            table.setItem(ii, 1, qt.QTableWidgetItem(entry.source.location))
        self.widget = table