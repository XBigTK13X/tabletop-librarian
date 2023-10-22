from core.util import tl_file
from core.settings import config
from core.data import tts

import filetype
import hashlib
import requests
import os
import shutil
from pathlib import Path
import time

# https://stackoverflow.com/a/7392391
textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary = lambda bytes: bool(bytes.translate(None, textchars))

class AssetCache:
    def __init__(self):
        self.hasher = hashlib.new('sha1')
        self.sparse_lookup = {}

    def track_sparse_entry(self, local_key, local_path):
        self.sparse_lookup[local_key] = local_path

    def get_sparse_entry(self, local_key):
        if local_key in self.sparse_lookup:
            return self.sparse_lookup[local_key]
        return None

    def scan(self, mod, local_handler):
        assets = []
        for location in mod.asset_locations:
            assets.append({
                'remote_location': location,
                'local_file': self.get_sparse_entry(local_handler(location))
            })
        return assets

    def download(self, mod):
        mod.parse_manifest()
        asset_count = len(mod.asset_locations)
        index = 0
        for location in mod.asset_locations:
            cached_asset = {}
            index = index + 1
            print(f"({index}/{asset_count}) Checking asset {location}")
            local_path = self.get_sparse_entry(tts.sanitize(location))
            self.hasher.update(location.encode())
            local_id = self.hasher.hexdigest()
            if local_path:
                print(f"Asset is already cached {location} -> {local_path}")
                continue

            temp_path = self.temp_path(local_id)

            try:
                print(f"Asset not cached, downloading {location}")
                response = requests.get(location, allow_redirects=True)
                if '<html>' in str(response.content):
                    print("Google is blocking downloads")
                    continue
                else:
                    open(temp_path, 'wb').write(response.content)
            except Exception as e:
                import pprint
                pprint.pprint(e)
                # TODO handle separate exception types, like 403 being a rate limiter on drive links
                swallow = True

            time.sleep(3)

            if not Path(temp_path).is_file():
                print(f"Failed to download {location}")
                continue

            cached_asset = {
                'remote_path': location,
                'path': temp_path,
                'local_id': local_id,
                'extension': None
            }
            kind = filetype.guess(temp_path)
            if kind != None:
                extended_path = temp_path + '.' + kind.extension
                shutil.move(temp_path, extended_path)
                cached_asset = {
                    'remote_path': location,
                    'path': extended_path,
                    'local_id': local_id,
                    'extension': kind.extension
                }
            else:
                is_unity3d = False
                with open(temp_path, 'rb') as file_data:
                    is_unity3d = is_binary(file_data.read(1024))
                if is_unity3d:
                    extended_path = temp_path + '.unity3d'
                    shutil.move(temp_path, extended_path)
                    cached_asset = {
                        'remote_path': location,
                        'path': extended_path,
                        'local_id': local_id,
                        'extension': 'unity3d'
                    }
                else:
                    extended_path = temp_path + '.obj'
                    shutil.move(temp_path, extended_path)
                    cached_asset = {
                        'remote_path': location,
                        'path': extended_path,
                        'local_id': local_id,
                        'extension': 'obj'
                    }
            print(f"Asset saved as {cached_asset['path']}")
            mod.manifest.persist_asset(cached_asset)
            # TODO Move persist_assets to here, so that the whole mod doesn't need to be stored in temp cache

    def temp_path(self, local_id):
        return tl_file.path(config.AssetCacheDir, local_id)

asset_cache = AssetCache()