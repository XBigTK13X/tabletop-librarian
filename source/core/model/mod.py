import os

class Mod:
    def __init__(self, source, name, manifest_path):
        self.source = source
        self.name = name
        self.path =  manifest_path
        self.file_name = os.path.basename(self.path)
        self.data_kind = 'mod'

    def search(self, needle):
        return needle in self.path.lower() or needle in self.name.lower()
