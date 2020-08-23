from pathlib import Path

import click
from tfr import data_utils, game_store
from tfr.app import App
from tfr.io_utils import definition_list, echo, echo_info

from .game import game


@game.group()
@click.pass_obj
def add(app):
    pass


@add.command()
@click.option("--name", prompt=True)
@click.option(
    "--path",
    help="Path to the template repository for the app.",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    prompt=True,
)
@click.pass_obj
def app(app: App, name: str, path: str):
    echo_info("App", app)
    game_dir = Path(app.game_path).resolve().parent
    repo_path = Path(path).expanduser().resolve()
    repo_relative = repo_path.relative_to(game_dir)
    repo = game_store.Repository(
        id=data_utils.name_to_id(repo_relative.name, "r"),
        name=repo_relative.name,
        directory=str(repo_relative),
        ssh_url=None,
        commit=None,
        metadata=None,
    )
    app.game.repositories.append(repo)

    phase = game_store.Phase(
        index=0,
        repository=repo.id,
        player=app.game.gm.username,
        role=game_store.Role.SOURCERER,
    )

    game_app = game_store.App(
        id=data_utils.name_to_id(name, pre="a"),
        name=name,
        editable_paths=[],
        phases=[phase],
    )
    app.game.apps.append(game_app)
    app.save_game()
