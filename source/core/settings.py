from pathlib import Path
import os
import json
import pprint

class Config:
    def __init__(self):
        # Version value is token swapped by the build server
        self.Version = "TabletopLibrarianVersion"
        self.Directories = []
        self.TTSBinaryPath = ""

    def get_path(self):
        return os.path.join(Path.home(), "tabletop-librarian.cfg")

    def load(self):
        if not Path(self.get_path()).is_file():
            return
        with open(self.get_path(),'r') as config_data:
            settings = json.load(config_data)
            self.Directories = settings['Directories']
            self.TTSBinaryPath = settings['TTSBinaryPath']

    def save(self):
        settings = {
            'Version': self.Version,
            'Directories': self.Directories,
            'TTSBinaryPath': self.TTSBinaryPath
        }
        with open(self.get_path(), 'w') as config_data:
            json.dump(settings, config_data, indent=4)

    def set_tts_binary(self, tts_path):
        self.TTSBinaryPath = tts_path

    def add_directory(self, name, source, content, location):
        found = False
        for pp in self.Directories:
            if pp['Name'] == name:
                print("Name [{name}] already found")
                pprint.pprint(pp)
                return False
            if pp['Location'] == location:
                print("Location [{location}] already found")
                pprint.pprint(pp)
                return False
        self.Directories.append({
            'Name': name,
            'Location': location,
            'Source': source,
            'Content': content
        })
        return True


config = Config()
config.load()