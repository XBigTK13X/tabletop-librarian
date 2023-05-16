from core.data.mod_cache import mod_cache
from core.settings import config

class ModCommand:
    def __init__(self):
        self.name = 'mod'

    def prepare_parser(self, parser):
        self.parser = parser
        self.parser.add_argument(
            '--id',
            help="'all' to see every known mod, otherwise specify subset id",
            nargs="?",
            const="all"
        )
        self.parser.add_argument(
            '--config',
            help="Show active configuration values",
            action="store_true"
        )
        self.parser.add_argument(
            '--search_archives',
            help="Find an archive matching the needle"
        )

    def handle(self, cli_args):
        # TODO Hoist out of this place to parent
        if cli_args.config:
            print("Active configuration")
            print(f"TTS Binary Path: {config.TTSBinaryPath}")
            print(f"TTS Mods Path: {config.TTSModsPath}")
            if len(config.ArchivePaths) > 0:
                print(f"Archive Paths")
                for archive_path in config.ArchivePaths:
                    print(f"  - Name: {archive_path['Name']}\n    Location: {archive_path['Location']}\n    Source: {archive_path['Source']}\n    Content: {archive_path['Content']}")
        else:
            mod_cache.refresh()
            if cli_args.search_archives:
                archives = mod_cache.search_archives(cli_args.search_archives)
                if len(archives) == 0:
                    print(f"No archives found matching [{cli_args.search_archives}]")
                else:
                    for archive in archives:
                        print(archive)
            else:
                if not cli_args.id or cli_args.id == 'all':
                    mod_cache.all_mods
                else:
                    print(f"TODO Only showing subset {cli_args.id}")