from dataclasses import dataclass
import typing as t
from functools import lru_cache
from pathlib import Path
import git


from tfr import game_store
from tfr.game_store import Game, Repository
from tfr import constants
from tfr.git_utils import PathLike, is_git_repo
from tfr.constants import TFR_FILENAME
from tfr.io_utils import echo, echo_error, echo_info


@dataclass
class RepoState:
    repo: Repository | None = None


class TreeManager:
    game: Game
    game_path: Path

    def __init__(self, game: Game, game_path: Path):
        self.game = game
        self.game_path = game_path

        self._scan()

    def _scan(self):
        self.repo_map = {}
