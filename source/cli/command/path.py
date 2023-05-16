name = 'path'

from core.settings import config

class PathCommand:
    def __init__(self):
        self.name = 'path'

    def prepare_parser(self, parser):
        self.parser = parser
        parser.add_argument(
            '--add',
            help='create a new path'
        )
        parser.add_argument(
            '--name',
            help="What to display when referencing this path",
            required=False
        )
        # tts -> Tabletop Simulator
        # tmm -> Tabletop Simulator Mod Manager
        # tc -> Tabletop Club
        parser.add_argument(
            '--source',
            help="The type of path being added",
            choices=['tts', 'tmm', 'tc']
        )
        parser.add_argument(
            '--content',
            help="How the path should be treated",
            choices=['executable', 'archive', 'mod', 'save']
        )

    def handle(self, cli_args):
        if cli_args.add:
            if cli_args.source == 'tts':
                if cli_args.content == "executable":
                    config.set_tts_binary(cli_args.add)
                    config.save()
                    return
                if cli_args.content == "mod":
                    config.add_directory(cli_args.name, cli_args.source, cli_args.content, cli_args.add)
                    config.save()
                    return
            if cli_args.source == 'tmm':
                if cli_args.content == "archive":
                    if config.add_directory(cli_args.name, cli_args.source, cli_args.content, cli_args.add):
                        config.save()
                    return

        self.parser.print_help()


