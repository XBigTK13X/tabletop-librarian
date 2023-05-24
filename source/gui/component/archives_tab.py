from gui.component import simple_table

from core.data.mod_cache import mod_cache

class ArchivesTab(simple_table.SimpleTable):
    def __init__(self, parent=None):
        super(ArchivesTab, self).__init__()
        self.setup(
            ['Name', 'Source'],
            mod_cache.kind('archive'),
            self.get_model_data
        )

    def get_model_data(self, model, data_index):
        if data_index == 0:
            return model.file_name
        if data_index == 1:
            return model.source.name
        return None