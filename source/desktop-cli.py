import click

from cli import main_app

@click.command()

@click.option("--show", help="Display high level details of mods")
def show(show):
    main_app.execute(show)

if __name__ == '__main__':
    show()