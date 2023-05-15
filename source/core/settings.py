from pathlib import Path
import os

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
        # TODO: Loading data
        config_path = self.get_path()

    def write(self):
        # TODO: Saving data
        config_path = self.get_path()

    def set_tts_binary(self, tts_path):
        self.TTSBinaryPath = tts_path
        self.write()

config = Config()
config.load()