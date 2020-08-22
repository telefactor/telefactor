import click
from tfr.io_utils import definition_list, echo, echo_info

from .base import cli


@cli.group()
@click.option(
    "--path",
    default="./game.yaml",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_obj
def game(app, path):
    app.load_game(path)


@game.command()
@click.pass_obj
def info(app):
    echo(
        definition_list(
            (
                ("Name", app.game.name),
                ("Id", app.game.id),
                ("GM", app.game.gm.name),
                ("Apps", ",".join(app.name for app in app.game.apps)),
                ("Num Players", len(app.game.players)),
                ("Num Repos", len(app.game.repositories)),
            )
        )
    )


@game.command()
@click.pass_obj
def fetch_metadata(app):
    echo_info("Loading all repos...")
    app.get_repos()
    echo_info("Game time.")

    changed_count = 0
    for local in app.game.repositories:
        remotes = app.ls(local.id)
        if not remotes:
            echo_info(f"No remote for {local.id}")
            continue

        remote = remotes[0]
        echo_info(f"Found {remote.name} for {local.id}")

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

    echo_info("Writing changes to game file:", app.game_path)
    app.save_game()


@game.command()
@click.pass_obj
def publicize(app):
    for local, remote in app.iter_locals_remotes():
        echo_info(f"Making {remote.name} public.")
        remote.edit(private=False)


@game.command()
@click.pass_obj
def links(app):
    echo(f"|name|url|")
    echo(f"|--  |-- |")
    for local in app.game.repositories:
        name = local.metadata["name"]
        html_url = local.metadata["html_url"]
        echo(f"|{name} |{html_url}|")
