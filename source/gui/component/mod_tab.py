import PyQt6.QtWidgets as qt
import PyQt6.QtGui as gui

from core.data.mod_cache import mod_cache
from core.data.asset_cache import asset_cache

from core.data import tts

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
        assets = asset_cache.scan(self.mod, tts.sanitize)
        self.asset_table.setRowCount(len(assets) + 1)
        row_colors = [
            gui.QColor(245, 130, 130),
            gui.QColor(255, 140, 140),
            gui.QColor(130, 245, 130),
            gui.QColor(140, 255, 140)
        ]
        for ii, entry in enumerate(assets):
            row_color = row_colors[ii%2]
            if entry['local_file']:
                row_color = row_colors[(ii%2)+2]
            remote_location = qt.QTableWidgetItem(entry['remote_location'])
            remote_location.setBackground(row_color)
            self.asset_table.setItem(ii, 0, remote_location)
            local_file = qt.QTableWidgetItem(entry['local_file'])
            local_file.setBackground(row_color)
            self.asset_table.setItem(ii, 1, local_file)
        self.layout.addWidget(self.asset_table)
        self.update()