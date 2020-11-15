import typing as t
from pathlib import Path

import click
from tfr import data_utils, game_store
from tfr.io_utils import echo_info
from tfr.tfr import TFR

from .game import game


@game.group()
@click.pass_obj
def add(tfr):
    pass


@add.command()
@click.option("--name", prompt=True)
@click.option(
    "--path",
    help="Path to the template repository for the add.",
    type=click.Path(file_okay=False, dir_okay=True, readable=True),
)
@click.pass_obj
def app(tfr: TFR, name: str, path: t.Optional[str]):
    echo_info("App", tfr)
    existing_apps = [existing for existing in tfr.game.apps if existing.name == name]
    if len(existing_apps):
        raise click.UsageError(f"App with name '{name}' already exists")

    phase_index = 0
    repo_name = data_utils.make_repo_name(app_name=name, phase_index=phase_index)

    game_dir = Path(tfr.game_path).resolve().parent
    repo_abs_dir = game_dir / repo_name
    if path is not None:
        repo_abs_dir = Path(path).expanduser().resolve()

    repo_dir = repo_abs_dir.relative_to(game_dir)

    # Create directory if it does not exist
    repo_dir.mkdir(exist_ok=True)

    repo = game_store.Repository(
        name=repo_name,
        directory=str(repo_dir),
        ssh_url=None,
        commit=None,
        metadata=None,
    )
    tfr.game.repositories.append(repo)

    phase = game_store.Phase(
        index=phase_index,
        repository=repo.name,
        player=tfr.game.gm.username,
        role=game_store.Role.SOURCERER,
    )

    game_app = game_store.App(name=name, editable_paths=[], phases=[phase],)
    tfr.game.apps.append(game_app)
    tfr.save_game()
