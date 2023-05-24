from core.data.mod_cache import mod_cache
from core.data.asset_cache import asset_cache
from core.settings import config
from core.model import source
from core.data import tts

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
            '--search',
            help="Find a mod or archive matching the needle"
        )
        self.parser.add_argument(
            '--download',
            help="Obtain remote resources for a mod and store them locally"
        )
        self.parser.add_argument(
            '--backup',
            help="Copy an active mod to an archive source"
        )
        self.parser.add_argument(
            '--source',
            help="Where the created archive should be copied"
        )
        self.parser.add_argument(
            '--restore',
            help="Restore an archived mod to an active source"
        )

    def handle(self, cli_args):
        # TODO Hoist config command out of this place to root command
        if cli_args.config:
            print("Active configuration")
            print(f"TTS Binary Path: {config.TTSBinaryPath}")
            if len(config.Sources) > 0:
                print(f"Sources")
                for ss in config.Sources:
                    print(f"  - Name: {ss['Name']}\n    Location: {ss['Location']}\n    Kind: {ss['Kind']}\n    Content: {ss['Content']}")
        else:
            if cli_args.search:
                results = mod_cache.search(cli_args.search)
                if len(results) == 0:
                    print(f"No results found matching [{cli_args.search}]")
                else:
                    for entry in results:
                        print(entry.path)
            elif cli_args.download:
                print(f"Searching for [{cli_args.download}]")
                results = mod_cache.search(cli_args.download)
                if len(results) == 0:
                    print(f"TODO: Downloading all mods content")
                else:
                    for entry in results:
                        if entry.data_kind == 'mod':
                            print(f"Downloading assets for [{entry.name}]")
                            entry.parse_manifest()
                            cached_assets = asset_cache.download(entry)
                            entry.persist_assets(cached_assets)
            elif cli_args.backup:
                if not cli_args.source:
                    print("--source arg required when making backups")
                    import sys
                    sys.exit(1)
                print(f"Backup mods matching query [{cli_args.backup}]")
                results = mod_cache.search(cli_args.backup)
                if len(results) == 0:
                    print(f"TODO: Archiving all mods content")
                else:
                    for entry in results:
                        if entry.data_kind == 'mod':
                            source_info = None
                            for ss in config.Sources:
                                if cli_args.source == ss['Name'] or cli_args.source == ss['Id'] or cli_args.source == ss['Location']:
                                    source_info = ss
                            if source_info == None:
                                print(f"No sources found matching [{cli_args.source}]")
                            else:
                                source_info = source.Source(source_info)
                                print(f"Backing up: [{entry.name}]")
                                tts.backup_mod(source_info, entry)
            elif cli_args.restore:
                if not cli_args.source:
                    print("--source arg required when restoring backups")
                    import sys
                    sys.exit(1)
                print(f"Restore mods matching query [{cli_args.restore}]")
                results = mod_cache.search(cli_args.restore)
                if len(results) == 0:
                    print(f"TODO: Restoring all mods content")
                else:
                    for entry in results:
                        if entry.data_kind == 'archive':
                            source_info = None
                            for ss in config.Sources:
                                if cli_args.source == ss['Name'] or cli_args.source == ss['Id'] or cli_args.source == ss['Location']:
                                    source_info = ss
                            if source_info == None:
                                print(f"No sources found matching [{cli_args.source}]")
                            else:
                                source_info = source.Source(source_info)
                                print(f"Restoring backup: [{entry.file_name}]")
                                tts.restore_archive(entry, source_info)
            else:
                if not cli_args.id or cli_args.id == 'all':
                    results = mod_cache.all()
                    if len(results) == 0:
                        print(f"No mods found. Set paths and rescan.")
                    else:
                        for entry in results:
                            print(entry.path)
                else:
                    print(f"TODO Only showing subset {cli_args.id}")