import click
from tfr.hub import Hub
from tfr.io_utils import definition_list, echo, echo_info
from tfr.app import TfrApp

from .base import cli


@cli.group()
@click.option(
    "--path",
    default="./tfr.yaml",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_obj
def game(tfr: TfrApp, path):
    tfr.load_game(path)


@game.command()
@click.pass_obj
def info(tfr: TfrApp):
    echo(
        definition_list(
            (
                ("Name", tfr.game.name),
                ("GM", tfr.game.gm.name),
                ("Apps", ",".join(app.name for app in tfr.game.apps)),
                ("Num Players", len(tfr.game.players)),
                ("Num Repos", len(tfr.game.repositories)),
            )
        )
    )


@game.command()
@click.pass_obj
def fetch(tfr: TfrApp):
    changed_count = tfr.hub.fetch(tfr.game)
    if changed_count < 1:
        echo_info("Nothing changed.")
        return

    echo_info("Writing changes to game file:", tfr.game_path)
    tfr.save_game()


@game.command()
@click.pass_obj
def push(tfr: TfrApp):
    tfr.hub.push(tfr.game)


@game.command()
@click.pass_obj
def publicize(tfr: TfrApp):
    for local, remote in tfr.iter_locals_remotes():
        echo_info(f"Making {remote.name} public.")
        remote.edit(private=False)


@game.command()
@click.pass_obj
def links(tfr: TfrApp):
    echo(f"|name|url|")
    echo(f"|--  |-- |")
    for local in tfr.game.repositories:
        name = local.metadata["name"]
        html_url = local.metadata["html_url"]
        echo(f"|{name} |{html_url}|")
