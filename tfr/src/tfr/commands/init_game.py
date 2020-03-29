from tfr import data_utils, game_store

from .base import cli, click
from .io_utils import echo, echo_info


@cli.group()
def init():
    pass


@init.command("game")
def init_game():
    steps = Steps(["Name your game", "Add players"])
    steps.next()
    name = click.prompt("name")
    id = data_utils.name_to_id(name)

    game = game_store.Game(
        name=name, id=id, gm=None, players=[], apps=[], repositories=[]
    )
    game_store.save("./game.yaml", game)


class Steps:
    def __init__(self, names):
        self.names = names
        self.current = -1
        self.total = len(names)

    def next(self):
        self.current += 1
        name = self.names[self.current]
        echo_info(f"{name} ({self.current}/{self.total})")
