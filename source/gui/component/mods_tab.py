from gui.component import simple_table

from core.data.mod_cache import mod_cache

class ModsTab(simple_table.SimpleTable):
    def __init__(self, parent=None):
        super(ModsTab, self).__init__()
        self.setup(
            ['Name', 'Path'],
            mod_cache.kind('mod'),
            self.get_model_data
        )
        self.doubleClicked.connect(self.select_mod)

    def select_mod(self, proxy_index):
        source_index = self.proxyModel.mapToSource(proxy_index)
        source_model = self.proxyModel.sourceModel()
        self.window().select_mod(source_model.get_path(source_index))

    def get_model_data(self, model, data_index):
        if data_index == 0:
            return model.name
        if data_index == 1:
            return model.path
        return None