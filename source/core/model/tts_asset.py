import os
from core.data import tts

class TTSAsset:
    def __init__(self, mod, cache_path, cache_id, remote_path, extension):
        self.mod = mod
        self.cache_path = cache_path
        self.cache_id = cache_id
        self.remote_path = remote_path
        self.extension = extension
        self.local_path = tts.get_local_path(mod, remote_path, extension)
