import typing as t
from pathlib import Path

import click
from tfr import data_utils, game_store, wit
from tfr.io_utils import echo_error, echo_info
from tfr.tfr import TFR

from .game import game


@game.command()
@click.pass_obj
def lock(tfr: TFR):
    for app in tfr.game.apps:
        lock_app(tfr, app)

    # tfr.save_game()


def lock_app(tfr: TFR, app: game_store.App):
    echo_info(app.name)
    if len(app.phases) == 0:
        echo_error("App has no phases")
        raise click.UsageError(f"App '{app.name}' has no phases")
    elif len(app.phases) > 1:
        raise click.UsageError(f"App '{app.name}' cannot be locked after first phase")

    wit.list_lockables(tfr, app)
    echo_info("Cool")
