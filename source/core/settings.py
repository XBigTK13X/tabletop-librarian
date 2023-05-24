from core.util import tl_file

from pathlib import Path
import os
import json
import pprint
import uuid

class Config:
    def __init__(self):
        # Version value is token swapped by the build server
        self.Version = "TabletopLibrarianVersion"
        self.Sources = []
        self.TTSBinaryPath = ""
        self.ConfigDir = tl_file.path(Path.home(),'.tabletop-librarian')
        self.AssetCacheDir = tl_file.path(self.ConfigDir,'asset-cache/')
        self.ArchiveCreateDir = tl_file.path(self.ConfigDir,'archive/')
        if not os.path.isdir(self.ConfigDir):
            os.mkdir(self.ConfigDir)
        if not os.path.isdir(self.AssetCacheDir):
            os.mkdir(self.AssetCacheDir)
        if not os.path.isdir(self.ArchiveCreateDir):
            os.mkdir(self.ArchiveCreateDir)

    def get_path(self):
        return tl_file.path(self.ConfigDir, "tabletop-librarian.cfg")

    def load(self):
        if not Path(self.get_path()).is_file():
            return
        with open(self.get_path(),'r') as config_data:
            settings = json.load(config_data)
            self.Sources = settings['Sources']
            self.TTSBinaryPath = settings['TTSBinaryPath']

    def save(self):
        settings = {
            'Version': self.Version,
            'Sources': self.Sources,
            'TTSBinaryPath': self.TTSBinaryPath
        }
        with open(self.get_path(), 'w') as config_data:
            json.dump(settings, config_data, indent=4)

    def set_tts_binary(self, tts_path):
        self.TTSBinaryPath = tts_path

    def add_directory(self, name, kind, content, location):
        found = False
        for pp in self.Sources:
            if pp['Name'] == name:
                print("Name [{name}] already found")
                pprint.pprint(pp)
                return False
            if pp['Location'] == location:
                print("Location [{location}] already found")
                pprint.pprint(pp)
                return False
        self.Sources.append({
            'Id': str(uuid.uuid4()),
            'Name': name,
            'Location': location,
            'Kind': kind,
            'Content': content
        })
        return True


config = Config()
config.load()