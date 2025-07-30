import typing as t
from dataclasses import asdict, dataclass, field
from enum import Enum

import dacite

from . import file_store
from .git_utils import PathLike


@dataclass
class User:
    # Unique key
    username: str
    name: t.Optional[str]


class Role(Enum):
    GM = "gm"
    SOURCERER = "sourcerer"
    EXAMINER = "examiner"


@dataclass
class FileConfig:
    glob: str
    editable: t.Optional[bool]
    ignore: t.Optional[bool]


@dataclass
class Phase:
    # Zero is initial phase for GM reference implementation.
    index: int
    # Repository to operate within.
    # - phase 0 => repos/base
    # - phase 1 => repos/phase-01
    # - phase 2 => repos/phase-02 ...
    repository: t.Optional[str]
    # Name of branch for phase.
    branch: t.Optional[str]
    # User.username
    player: t.Optional[str]
    role: t.Optional[Role]


@dataclass
class Repository:
    # Unique key
    name: str
    # Where to the repo is checked out, relative to game root.
    # - phase 0 => repos/base
    # - phase 1 => repos/phase-01
    # - phase 2 => repos/phase-02 ...
    directory: t.Optional[str]
    ssh_url: t.Optional[str]
    # Commit used as starting point for phase zero.
    initial_commit: t.Optional[str]
    metadata: t.Optional[dict]


@dataclass
class Game:
    ##
    # Unique key
    name: str

    ##
    # Configured by GM
    gm: User
    players: t.List[User] = field(default_factory=list)
    files: t.List[FileConfig] = field(default_factory=list)

    ##
    # Managed by Tfr (usually)

    # Repository definitions
    phases: t.List[Phase] = field(default_factory=list)
    repositories: t.List[Repository] = field(default_factory=list)


def load(path: PathLike) -> Game:
    return normer(file_store.load(path))


def normer(data: dict) -> Game:
    return dacite.from_dict(
        data_class=Game,
        data=data,
        config=dacite.Config(cast=[Role]),
    )


def save(path: PathLike, game: Game) -> None:
    file_store.save(path, as_dict(game))


def as_dict(root):
    d = asdict(root)
    return clean(d)


def clean(d):
    if isinstance(d, dict):
        for key, value in d.items():
            d[key] = clean(value)
    elif isinstance(d, list):
        for i, value in enumerate(d):
            d[i] = clean(value)
    elif isinstance(d, Enum):
        # This is the reason for this in the first place!
        return d.value
    return d
