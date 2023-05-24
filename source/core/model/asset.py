class Asset:
    def __init__(self, kind, location, name):
        self.kind = kind
        # Do not normalize these paths. Otherwise the caching won't match things like TTS
        self.location = location
        self.name = name