from core.data.game_list import game_list

name = 'show'

def prepare_parser(parser):
    parser.add_argument(
        '--id',
        help="'all' to see every known mod, otherwise specify subset id",
        nargs="?",
        const="all"
    )

def handle(cli_args):
    if not cli_args.id or cli_args.id == 'all':
        for game in game_list:
            print(f'{game.name} | {game.archive_path} | {game.local_path}')
    else:
        print(f"TODO Only showing subset {cli_args.id}")