import PyQt6.QtWidgets as qt

from core.data.mod_cache import mod_cache
from core.data.asset_cache import asset_cache

class ModTab(qt.QWidget):
    def __init__(self,parent=None):
        super(ModTab, self).__init__()

        self.asset_table = None

        self.layout = qt.QVBoxLayout()
        self.mod_name = qt.QLabel()
        self.mod_name.setText('No mod selected.')
        self.layout.addWidget(self.mod_name)

        self.setLayout(self.layout)

    def refresh(self):
        self.mod = mod_cache.get_selected_mod()
        self.mod.parse_manifest()
        self.mod_name.setText(self.mod.name)
        if self.asset_table:
            self.layout.removeWidget(self.asset_table)
        self.asset_table = qt.QTableWidget()
        headers = ['Remote', 'Local']
        self.asset_table.setRowCount(0)
        self.asset_table.setColumnCount(len(headers))
        self.asset_table.setHorizontalHeaderLabels(headers)
        self.asset_table.setEditTriggers(qt.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.asset_table.setSelectionBehavior(qt.QAbstractItemView.SelectionBehavior.SelectRows)
        self.asset_table.setAlternatingRowColors(True)
        for ii in range(0, self.asset_table.columnCount()):
            self.asset_table.horizontalHeader().setSectionResizeMode(ii,qt.QHeaderView.ResizeMode.Stretch)
        assets = asset_cache.scan(self.mod)
        self.asset_table.setRowCount(len(assets) + 1)
        for ii, entry in enumerate(assets):
            self.asset_table.setItem(ii, 0, qt.QTableWidgetItem(entry['remote_location']))
            self.asset_table.setItem(ii, 1, qt.QTableWidgetItem(entry['local_file']))
        self.layout.addWidget(self.asset_table)
        self.update()