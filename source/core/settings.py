from pathlib import Path
import os
import json
import pprint

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

    def set_tts_mods_dir(self, dir_path):
        self.TTSModsPath = dir_path

    def add_archive(self, name, source, content, location):
        found = False
        for archive_path in self.ArchivePaths:
            if archive_path['Name'] == name:
                print("Name [{name}] already found in archive_path")
                pprint.pprint(archive_path)
                return False
            if archive_path['Location'] == location:
                print("Location [{location}] already found in archive_path")
                pprint.pprint(archive_path)
                return False
        self.ArchivePaths.append({
            'Name': name,
            'Location': location,
            'Source': source,
            'Content': content
        })
        return True

config = Config()
config.load()