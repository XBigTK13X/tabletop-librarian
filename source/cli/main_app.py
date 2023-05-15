from core.data.game_list import game_list
from core.settings import config

def execute(arg_parser, cli_args):
    if cli_args.show:
        print(f"Going to show [{cli_args.show}]")
        for game in game_list:
            print(f'{game.name} | {game.archive_path} | {game.local_path}')
    else:
        print(f"Tabletop Librarian: {config.Version}")
        arg_parser.print_help()