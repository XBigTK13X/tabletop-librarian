import os

class Archive:
    def __init__(self, source, path):
        self.path = path
        self.data_kind = 'archive'
        self.source = source
        self.file_name = os.path.basename(self.path)

    def search(self, needle):
        return needle in self.path.lower()