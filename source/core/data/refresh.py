from core.settings import config
from core.model import mod
from core.model import archive
from core.model import source
from core.data import tts

from core.data.mod_cache import mod_cache
from core.data.asset_cache import asset_cache

import os
import json

class Refresh:
    def __init__(self, mod_cache, asset_cache):
        self.mod_cache = mod_cache
        self.asset_cache = asset_cache

    def scan_all(self):
        if config.Sources:
            for ss in config.Sources:
                parent = source.Source(ss)
                if parent.content == 'archive':
                    for root, dirs, files in os.walk(parent.location):
                        for ff in files:
                            self.mod_cache.track_archive(archive.Archive(parent, os.path.join(root, ff)))
                if parent.content == 'mod':
                    if parent.kind == 'tts':
                        for root, dirs, files, in os.walk(parent.location):
                            for ff in files:
                                file_path = os.path.join(root, ff)
                                if 'Models Raw' in file_path or 'Images Raw' in file_path:
                                    continue
                                if 'WorkshopFileInfos.json' == ff:
                                    with open(file_path, 'r') as json_file:
                                        mod_list = json.load(json_file)
                                        for item in mod_list:
                                            self.mod_cache.track_mod(mod.Mod(parent, item["Name"],item["Directory"]))
                                else:
                                    sanitized = tts.sanitize(ff)
                                    self.asset_cache.track_sparse_entry(sanitized, file_path)

refresher = Refresh(mod_cache, asset_cache)