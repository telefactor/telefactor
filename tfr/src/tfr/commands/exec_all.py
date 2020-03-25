from pathlib import Path

import git

from .base import game, click
from .io_utils import echo, echo_info


@game.command()
@click.pass_obj
def exec_all(app):
    pass
