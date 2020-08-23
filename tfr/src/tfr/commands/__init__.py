from .base import cli
from .clone_all import clone_all
from .exec_all import exec_all
from .game import game
from .game_add import add as game_add
from .init_game import init_game
from .repos import repos

__all__ = [
    cli,
    clone_all,
    exec_all,
    game,
    game_add,
    init_game,
    repos,
]
