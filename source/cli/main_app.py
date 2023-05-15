from core.data.game_list import game_list

def execute(cli_args):
    if cli_args.show:
        print(f"Going to show [{cli_args.show}]")
        for game in game_list:
            print(f'{game.name} | {game.archive_path} | {game.local_path}')