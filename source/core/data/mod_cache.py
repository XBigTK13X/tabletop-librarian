from core.settings import config

import os

class ModCache:
    def __init__(self):
        self.mods = []
        self.archives = []

    def refresh(self):
        if config.TTSModsPath:
            for root, dirs, files in os.walk(config.TTSModsPath):
                for f in files:
                    print(os.path.join(root, f))
        if config.ArchivePaths:
            for archive_path in config.ArchivePaths:
                for root, dirs, files in os.walk(archive_path['Location']):
                    for f in files:
                        self.archives.append({
                            'Path': os.path.join(root, f)
                        })

    def search_archives(self, needle):
        results = []
        for archive in self.archives:
            if needle.lower() in archive['Path'].lower():
                results.append(archive)
        return results

mod_cache = ModCache()