from core.settings import config

import os
import json

class ModCache:
    def __init__(self):
        self.archives = []
        self.mods = []

    def refresh(self):
        if config.Directories:
            for dd in config.Directories:
                if dd['Content'] == 'archive':
                    for root, dirs, files in os.walk(dd['Location']):
                        for ff in files:
                            self.archives.append(os.path.join(root, ff))
                if dd['Content'] == 'mod':
                    if dd['Source'] == 'tts':
                        for root, dirs, files, in os.walk(os.path.join(dd['Location'], "Workshop")):
                            for ff in files:
                                if 'WorkshopFileInfos.json' == ff:
                                    with open(os.path.join(root, ff), 'r') as json_file:
                                        mod_list = json.load(json_file)
                                        for mod in mod_list:
                                            self.mods.append(f'{mod["Name"]} - {mod["Directory"]}')

    def search(self, needle):
        results = []
        for dd in self.archives:
            if needle.lower() in dd.lower():
                results.append(f'arc: {dd}')
        for mm in self.mods:
            if needle.lower() in mm.lower():
                results.append(f'mod: {mm}')
        return results

mod_cache = ModCache()