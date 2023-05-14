from core.data.game_list import game_list

def execute(show):
    print(f"Going to show [{show}]")
    for game in game_list:
        print(f'{game.name} | {game.archive_path} | {game.local_path}')