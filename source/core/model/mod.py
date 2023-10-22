from core.util import tl_file
from core.model import tts_manifest

import os

class Mod:
    def __init__(self, source, name, manifest_path):
        self.source = source
        self.name = name
        import os
        self.path = tl_file.path(manifest_path)
        self.file_name = os.path.basename(self.path)
        self.data_kind = 'mod'
        self.assets = []
        self.haystack = self.path.lower() + '-' + self.name.lower()

    def search(self, needle):
        return needle in self.haystack

    def parse_manifest(self):
        # TODO Detect type of manifest and call target specific handler
        if '.json' in self.path:
            with open(self.path, 'r', encoding='UTF-8') as manifest_data:
                self.manifest = tts_manifest.TTSManifest(self, manifest_data.read())
                self.asset_locations = self.manifest.parse_locations()
