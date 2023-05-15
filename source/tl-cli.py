from cli import main_app

import argparse

parser = argparse.ArgumentParser(
    prog="Tabletop Librarian",
    description="Manage digital board game mods"
)
parser.add_argument(
    '--show',
    help="'all' to see every known mod, otherwise specify subset id"
)

if __name__ == '__main__':
    main_app.execute(parser.parse_args())