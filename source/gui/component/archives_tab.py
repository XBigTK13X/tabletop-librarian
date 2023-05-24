import PyQt6.QtWidgets as qt

from core.data.mod_cache import mod_cache

class ArchivesTab(qt.QTableWidget):
    def __init__(self, parent=None):
        super(ArchivesTab, self).__init__()
        headers = ['Name', 'Source']
        self.setRowCount(0)
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)
        self.setEditTriggers(qt.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSelectionBehavior(qt.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(True)
        for ii in range(0, self.columnCount()):
            self.horizontalHeader().setSectionResizeMode(ii,qt.QHeaderView.ResizeMode.Stretch)
        for ii, entry in enumerate(mod_cache.kind('archive')):
            self.setRowCount(ii+1)
            self.setItem(ii, 0, qt.QTableWidgetItem(entry.file_name))
            self.setItem(ii, 1, qt.QTableWidgetItem(entry.source.location))

    def update_filter(self, filter_text):
        pass