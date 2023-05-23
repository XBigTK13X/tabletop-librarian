from core.settings import config
from core.model import mod
from core.model import archive
from core.model import source

import os
import json

class ModCache:
    def __init__(self):
        self.archives = []
        self.mods = []
        self.selected_mod = None

    def refresh(self):
        if config.Sources:
            for ss in config.Sources:
                parent = source.Source(ss)
                if parent.content == 'archive':
                    for root, dirs, files in os.walk(parent.location):
                        for ff in files:
                            self.archives.append(archive.Archive(parent, os.path.join(root, ff)))
                if parent.content == 'mod':
                    if parent.kind == 'tts':
                        for root, dirs, files, in os.walk(os.path.join(parent.location, "Workshop")):
                            for ff in files:
                                if 'WorkshopFileInfos.json' == ff:
                                    with open(os.path.join(root, ff), 'r') as json_file:
                                        mod_list = json.load(json_file)
                                        for item in mod_list:
                                            self.mods.append(mod.Mod(parent, item["Name"],item["Directory"]))

    def search(self, needle):
        needle = None if needle == None else needle.lower()
        results = []
        for aa in self.archives:
            if needle == None or aa.search(needle):
                results.append(aa)
        for mm in self.mods:
            if needle == None or mm.search(needle):
                results.append(mm)
        return results

    def all(self):
        return self.search(None)

    def kind(self, needle):
        if needle == 'mod':
            return self.mods
        if needle == 'archive':
            return self.archives
        return self.all()

    def select_mod(self, mod_path):
        for mm in self.mods:
            if mm.path == mod_path:
                self.selected_mod = mm

    def get_selected_mod(self):
        return self.selected_mod

mod_cache = ModCache()