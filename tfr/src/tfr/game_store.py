import typing as t
from dataclasses import asdict, dataclass, field
from enum import Enum

import dacite

from . import file_store
from .file_store import Pathish


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
class Phase:
    # Zero is initial phase when GM is setting up game.
    index: int
    # Repository to operate within. Repository.name
    repository: t.Optional[str]
    # Name of branch for phase.
    branch: t.Optional[str]
    # User.username
    player: t.Optional[str]
    role: t.Optional[Role]


@dataclass
class App:
    # Unique key
    name: str
    editable_paths: t.List[str] = field(default_factory=list)
    phases: t.List[Phase] = field(default_factory=list)


@dataclass
class Repository:
    # Unique key
    name: str
    # Where to the repo is checked out, relative to game root.
    directory: t.Optional[str]
    ssh_url: t.Optional[str]
    # Commit used as starting point for phase zero.
    initial_commit: t.Optional[str]
    metadata: t.Optional[dict]


@dataclass
class Game:
    # Unique key
    name: str
    gm: User
    players: t.List[User] = field(default_factory=list)
    apps: t.List[App] = field(default_factory=list)
    # Repository definitions
    repositories: t.List[Repository] = field(default_factory=list)


def load(path: Pathish) -> Game:
    return normer(file_store.load(path))


def normer(data: dict) -> Game:
    return dacite.from_dict(
        data_class=Game,
        data=data,
        config=dacite.Config(cast=[Role]),
    )


def save(path: Pathish, game: Game) -> None:
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
