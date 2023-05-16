from core.settings import config

from cli.command import mod,path

sub_commands = [
    mod.ModCommand,
    path.PathCommand
]

def execute(arg_parser):
    subparsers = arg_parser.add_subparsers()
    for Command in sub_commands:
        command = Command()
        subparser = subparsers.add_parser(command.name)
        command.prepare_parser(subparser)
        subparser.set_defaults(func=command.handle)
    cli_args = arg_parser.parse_args()
    if not 'func' in cli_args:
        print(f"Tabletop Librarian: {config.Version}")
        arg_parser.print_help()
    else:
        cli_args.func(cli_args)