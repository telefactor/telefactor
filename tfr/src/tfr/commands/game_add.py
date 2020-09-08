import typing as t
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
    type=click.Path(file_okay=False, dir_okay=True, readable=True),
)
@click.pass_obj
def app(app: App, name: str, path: t.Optional[str]):
    echo_info("App", app)
    existing_apps = [existing for existing in app.game.apps if existing.name == name]
    if len(existing_apps):
        raise click.UsageError(f"App with name '{name}' already exists")

    phase_index = 0
    repo_name = data_utils.make_repo_name(app_name=name, phase_index=phase_index)

    game_dir = Path(app.game_path).resolve().parent
    repo_dir = game_dir / repo_name
    if path is not None:
        repo_path = Path(path).expanduser().resolve()
        repo_dir = repo_path.relative_to(game_dir)
    repo_dir.mkdir(exist_ok=True)

    repo = game_store.Repository(
        name=repo_name,
        directory=str(repo_dir),
        ssh_url=None,
        commit=None,
        metadata=None,
    )
    app.game.repositories.append(repo)

    phase = game_store.Phase(
        index=phase_index,
        repository=repo.name,
        player=app.game.gm.username,
        role=game_store.Role.SOURCERER,
    )

    game_app = game_store.App(name=name, editable_paths=[], phases=[phase],)
    app.game.apps.append(game_app)
    app.save_game()
