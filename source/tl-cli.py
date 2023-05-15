from cli import main_app
from core.settings import config

__version__ = config.Version

import argparse

parser = argparse.ArgumentParser(
    prog="Tabletop Librarian",
    description="Manage digital board game mods"
)

parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s {version}'.format(version=__version__))

parser.add_argument(
    '--show',
    help="'all' to see every known mod, otherwise specify subset id"
)

if __name__ == '__main__':
    main_app.execute(parser, parser.parse_args())