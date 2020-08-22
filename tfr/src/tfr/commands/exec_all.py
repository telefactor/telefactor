import subprocess

from tfr.io_utils import echo, echo_info

from .base import click
from .game import game


@game.command()
@click.argument("COMMAND", nargs=-1)
@click.pass_obj
def exec_all(app, command):
    for phase, local in app.iter_phase_locals():
        echo_info(f"Running {command} in {local.directory}")
        subprocess.run(command, cwd=local.directory)
