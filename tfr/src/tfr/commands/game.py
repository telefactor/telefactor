import click
from tfr.hub import Hub
from tfr.io_utils import definition_list, echo, echo_info
from tfr.tfr import TFR

from .base import cli


@cli.group()
@click.option(
    "--path",
    default="./tfr.yaml",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_obj
def game(tfr: TFR, path):
    tfr.load_game(path)


@game.command()
@click.pass_obj
def info(tfr: TFR):
    echo(
        definition_list(
            (
                ("Name", tfr.game.name),
                ("Id", tfr.game.id),
                ("GM", tfr.game.gm.name),
                ("Apps", ",".join(tfr.name for app in tfr.game.apps)),
                ("Num Players", len(tfr.game.players)),
                ("Num Repos", len(tfr.game.repositories)),
            )
        )
    )


@game.command()
@click.pass_obj
def fetch_metadata(tfr: TFR):
    hub = Hub(tfr)

    changed_count = hub.fetch()
    if changed_count < 1:
        echo_info("Nothing changed.")
        return

    echo_info("Writing changes to game file:", tfr.game_path)
    tfr.save_game()


@game.command()
@click.pass_obj
def push(tfr: TFR):
    hub = Hub(tfr)
    hub.fetch_metadata()


@game.command()
@click.pass_obj
def publicize(tfr: TFR):
    for local, remote in tfr.iter_locals_remotes():
        echo_info(f"Making {remote.name} public.")
        remote.edit(private=False)


@game.command()
@click.pass_obj
def links(tfr: TFR):
    echo(f"|name|url|")
    echo(f"|--  |-- |")
    for local in tfr.game.repositories:
        name = local.metadata["name"]
        html_url = local.metadata["html_url"]
        echo(f"|{name} |{html_url}|")
