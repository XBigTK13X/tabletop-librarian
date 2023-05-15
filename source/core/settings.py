from pathlib import Path
import os
import json

class Config:
    def __init__(self):
        # Version value is token swapped by the build server
        self.Version = "TabletopLibrarianVersion"
        self.ArchivePaths = []
        self.TTSModsPath = ""
        self.TTSBinaryPath = ""

    def get_path(self):
        return os.path.join(Path.home(), "tabletop-librarian.cfg")

    def load(self):
        if not Path(self.get_path()).is_file():
            return
        with open(self.get_path(),'r') as config_data:
            settings = json.load(config_data)
            self.Version = settings['Version']
            self.ArchivePaths = settings['ArchivePaths']
            self.TTSModsPath = settings['TTSModsPath']
            self.TTSBinaryPath = settings['TTSBinaryPath']

    def save(self):
        settings = {
            'Version': self.Version,
            'ArchivePaths': self.ArchivePaths,
            'TTSModsPath': self.TTSModsPath,
            'TTSBinaryPath': self.TTSBinaryPath
        }
        with open(self.get_path(), 'w') as config_data:
            json.dump(settings, config_data, indent=4)

    def set_tts_binary(self, tts_path):
        self.TTSBinaryPath = tts_path

config = Config()
config.load()