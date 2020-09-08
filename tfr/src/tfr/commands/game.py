import click
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
def fetch_metadata(tfr_app: TFR):
    echo_info("Loading all remotes...")
    tfr_app.get_remotes()
    echo_info("Game time.")

    changed_count = 0
    for local in tfr_app.game.repositories:
        remotes = tfr_app.ls(local.name)
        if not remotes:
            echo_info(f"No remote for {local.name}")
            continue

        remote = remotes[0]
        echo_info(f"Found {remote.name} for {local.name}")

        incoming_metadata = {
            "id": remote.id,
            "name": remote.name,
            "full_name": remote.full_name,
            "html_url": remote.clone_url,
            "clone_url": remote.clone_url,
            "ssh_url": remote.ssh_url,
            "isPrivate": remote.private,
        }
        if local.metadata == incoming_metadata:
            echo_info("No difference.")
            continue

        if local.metadata:
            echo_info("Original metadata:", local.metadata)
            echo_info("Incoming metadata:", incoming_metadata)

        local.metadata = incoming_metadata
        changed_count += 1

    if changed_count < 1:
        echo_info("Nothing changed.")
        return

    echo_info("Writing changes to game file:", tfr_app.game_path)
    tfr_app.save_game()


@game.command()
@click.pass_obj
def push(tfr: TFR):
    name_to_remote = tfr.get_name_to_repo()


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
