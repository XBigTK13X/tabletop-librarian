import os, json

from core.model import tts_manifest

class Mod:
    def __init__(self, source, name, manifest_path):
        self.source = source
        self.name = name
        self.path =  manifest_path
        self.file_name = os.path.basename(self.path)
        self.data_kind = 'mod'
        self.assets = []

    def search(self, needle):
        return needle in self.path.lower() or needle in self.name.lower()

    def parse_manifest(self):
        # TODO Detect type of manifest and call target specific handler
        if '.json' in self.path:
            with open(self.path, 'r', encoding='UTF-8') as manifest_data:
                self.manifest = tts_manifest.TTSManifest(self, manifest_data.read())
                self.asset_locations = self.manifest.parse_locations()

    def persist_assets(self, assets):
        self.manifest.write_assets(assets)

    def get_data_index(self, index):
        if index == 0:
            return self.name
        if index == 1:
            return self.path
        return None
