import PyQt6.QtWidgets as qt
import PyQt6.QtCore as core

from core.data.mod_cache import mod_cache

class SimpleTableModel(core.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self.headers = [
            'Name',
            'Path'
        ]

    def data(self, index, role):
        if role == core.Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()].get_data_index(index.column())

    def get_path(self, index):
        return self._data[index.row()].path

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if orientation == core.Qt.Orientation.Horizontal and role == core.Qt.ItemDataRole.DisplayRole:
            return self.headers[section]

# https://raw.githubusercontent.com/PyQt5/Examples/master/PyQt5/itemviews/customsortfiltermodel.py
class ModsTab(qt.QTableView):
    def __init__(self, headers, parent=None):
        super(ModsTab, self).__init__()
        model = SimpleTableModel(mod_cache.kind('mod'))
        self.proxyModel = core.QSortFilterProxyModel()
        self.proxyModel.setDynamicSortFilter(True)
        self.proxyModel.setSourceModel(model)
        self.setModel(self.proxyModel)
        self.horizontalHeader().setSectionResizeMode(qt.QHeaderView.ResizeMode.Stretch)
        self.setEditTriggers(qt.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setSortingEnabled(True)
        self.setSelectionBehavior(qt.QAbstractItemView.SelectionBehavior.SelectRows)
        self.setAlternatingRowColors(True)
        self.selectionModel().selectionChanged.connect(self.bulk_operation)
        self.doubleClicked.connect(self.select_mod)

    def select_mod(self, qt_index):
        self.window().select_mod(self.model().get_path(qt_index))

    #TODO Handle multiple mods at once
    def bulk_operation(self):
        pass

    def update_filter(self, filter_text):
        self.proxyModel.setFilterFixedString(filter_text)
        self.proxyModel.setFilterCaseSensitivity(core.Qt.CaseSensitivity.CaseInsensitive)
