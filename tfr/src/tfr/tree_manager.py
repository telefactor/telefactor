from dataclasses import dataclass
import typing as t
from functools import lru_cache
from pathlib import Path
import git


from tfr import game_store
from tfr.game_store import Game, Repository
from tfr import constants
from tfr.git_utils import PathLike, is_git_repo, try_git_repo
from tfr.constants import REPOS_DIRNAME, TFR_FILENAME
from tfr.io_utils import echo, echo_error, echo_info


def make_phase_name(index: int) -> str:
    if index < 0:
        raise ValueError("Negative phase index")

    if index == 0:
        return "base"

    return f"phase-{index:02d}"


def parse_phase_name(dirname: str) -> int | None:
    if dirname == "base":
        return 0

    parts = dirname.split("-")
    if len(parts) != 2:
        return None

    (prefix, digits) = parts

    if prefix != "phase":
        return None

    if not digits.isalnum():
        return None

    return int(digits)


@dataclass
class RepoLocal:
    """Repo on disk"""

    phase_index: int
    directory: Path
    git_repo: git.Repo | None = None


@dataclass
class RepoState:
    """Repo game definition vs paired with repo on disk"""

    repo: Repository | None = None
    local: RepoLocal | None = None


class TreeManager:
    game: Game
    game_path: Path

    _repo_map: dict[str, RepoState]

    @property
    def repos_path(self):
        return self.game_path / REPOS_DIRNAME

    def __init__(self, game: Game, game_path: Path):
        self.game = game
        self.game_path = game_path

        self._repo_map = {}
        self._scan()

    def _scan(self):
        # First walk tree
        phases = []
        for phase_dir in self.repos_path.iterdir():
            if not phase_dir.is_dir():
                continue

            phase_index = parse_phase_name(phase_dir.name)
            if phase_index is None:
                continue

            repo_local = RepoLocal(
                phase_index=phase_index,
                directory=(phase_dir.relative_to(self.game_path)),
                git_repo=try_git_repo(phase_dir),
            )
            phases.append(repo_local)

        self._phases = phases
