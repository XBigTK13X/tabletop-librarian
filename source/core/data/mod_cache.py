class ModCache:
    def __init__(self):
        self.archives = []
        self.mods = []
        self.selected_mod = None

    def track_archive(self, archive):
        self.archives.append(archive)

    def track_mod(self, mod):
        self.mods.append(mod)

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