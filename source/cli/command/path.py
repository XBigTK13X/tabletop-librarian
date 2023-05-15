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
        parser.add_argument(
            '--kind',
            help="The type of path being added"
        )
        parser.add_argument(
            '--content',
            help="How the path should be treated"
        )

    def handle(self, cli_args):
        # --add-path --kind archive --source tts --content full --path
        if cli_args.add:
            if cli_args.kind == 'tts':
                if cli_args.content == "executable":
                    config.set_tts_binary(cli_args.add)
                    config.save()
                    return
        self.parser.print_help()


