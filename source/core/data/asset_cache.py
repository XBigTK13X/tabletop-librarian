from core.settings import config
from core.data import tts

import filetype
import hashlib
import requests
import os
import glob

# https://stackoverflow.com/a/7392391
textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
is_binary = lambda bytes: bool(bytes.translate(None, textchars))

class AssetCache:
    def __init__(self):
        self.downloads = {}
        self.hasher = hashlib.new('sha1')

    def download(self, mod):
        downloads = {}
        for location in mod.asset_locations:
            if tts.get_local_glob(mod, location):
                continue
            self.hasher.update(location.encode())
            local_id = self.hasher.hexdigest()
            temp_path = self.temp_path(local_id)
            on_disk = glob.glob(temp_path+'*')
            if on_disk and len(on_disk) > 0:
                downloads[location] = {
                    'local_id': local_id,
                    'path': on_disk[0],
                    'extension': os.path.splitext(on_disk[0])[1].strip('.')
                }
                continue
            if not location in self.downloads:
                self.downloads[location] = {}
            if not mod.source.kind in self.downloads[location]:
                self.downloads[location][mod.source.kind] = ""
            self.downloads[location][mod.source.kind] = {
                'local_id': local_id
            }

            try:
                response = requests.get(location, allow_redirects=True)
                open(temp_path, 'wb').write(response.content)
            except Exception as e:
                import pprint
                pprint.pprint(e)
                # TODO handle separate exception types, like 403 being a rate limiter on drive links
                swallow = True
            downloads[location] = {
                'path': temp_path,
                'local_id': local_id,
                'extension': None
            }
            kind = filetype.guess(temp_path)
            if kind != None:
                extended_path = temp_path + '.' + kind.extension
                os.rename(temp_path, extended_path)
                downloads[location] = {
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
                    os.rename(temp_path, extended_path)
                    downloads[location] = {
                        'path': extended_path,
                        'local_id': local_id,
                        'extension': 'unity3d'
                    }
                else:
                    extended_path = temp_path + '.obj'
                    os.rename(temp_path, extended_path)
                    downloads[location] = {
                        'path': extended_path,
                        'local_id': local_id,
                        'extension': 'obj'
                    }
        return downloads

    def temp_path(self, local_id):
        return os.path.join(config.AssetCacheDir, local_id)

asset_cache = AssetCache()