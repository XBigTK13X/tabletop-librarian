import PyQt6.QtWidgets as qt
import PyQt6.QtCore as core

# https://raw.githubusercontent.com/PyQt5/Examples/master/PyQt5/itemviews/customsortfiltermodel.py

class SimpleTableModel(core.QAbstractTableModel):
    def __init__(self, headers, data, cell_handler):
        super().__init__()
        self._data = data
        self.headers = headers
        self.cell_handler = cell_handler

    def data(self, index, role):
        if role == core.Qt.ItemDataRole.DisplayRole:
            return self.cell_handler(self._data[index.row()], index.column())

    def get_path(self, index):
        return self._data[index.row()].path

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if orientation == core.Qt.Orientation.Horizontal and role == core.Qt.ItemDataRole.DisplayRole:
            return self.headers[section]

class SimpleTable(qt.QTableView):
    def __init__(self, parent=None):
        super(SimpleTable, self).__init__()

    def setup(self, headers, data, cell_handler):
        model = SimpleTableModel(headers, data, cell_handler)
        self.proxyModel = core.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel.setSourceModel(model)
        self.setModel(self.proxyModel)
        self.horizontalHeader().setSectionResizeMode(qt.QHeaderView.ResizeMode.Stretch)
        self.setEditTriggers(qt.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(qt.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(True)

    def update_filter(self, filter_text):
        self.proxyModel.setFilterFixedString(filter_text)
        self.proxyModel.setFilterCaseSensitivity(core.Qt.CaseSensitivity.CaseInsensitive)
