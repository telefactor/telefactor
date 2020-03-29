from .base import cli, click
from .io_utils import echo, echo_info


@cli.group()
def init():
    echo("k")


@init.command("game")
def init_game():
    echo("kool")
