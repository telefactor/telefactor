import subprocess

from tfr.io_utils import echo_info
from tfr.tfr import TFR

from .base import click
from .game import game


@game.command()
@click.argument("COMMAND", nargs=-1)
@click.pass_obj
def exec_all(tfr: TFR, command):
    for phase, local in tfr.iter_phase_locals():
        echo_info(f"Running {command} in {local.directory}")
        subprocess.run(command, cwd=local.directory)
