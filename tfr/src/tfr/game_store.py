import typing as t
from dataclasses import asdict, dataclass
from enum import Enum

import dacite

from . import file_store


@dataclass
class User:
    username: str
    name: t.Optional[str]


class Role(Enum):
    SOURCERER = "sourcerer"
    EXAMINER = "examiner"


@dataclass
class Phase:
    index: int
    repository: t.Optional[str]
    player: t.Optional[str]
    role: t.Optional[Role]


@dataclass
class App:
    id: str
    name: str
    editable_paths: t.List[str]
    phases: t.List[Phase]


@dataclass
class Repository:
    id: str
    name: t.Optional[str]
    directory: t.Optional[str]
    ssh_url: t.Optional[str]
    commit: t.Optional[str]
    metadata: t.Optional[dict]


@dataclass
class Game:
    name: str
    id: str
    gm: User
    players: t.List[User]
    apps: t.List[App]
    repositories: t.List[Repository]


def load(path: str) -> Game:
    return normer(file_store.load(path))


def normer(data: dict) -> Game:
    return dacite.from_dict(
        data_class=Game,
        data=data,
        config=dacite.Config(cast=[Role]),
    )


def save(path: str, game: Game) -> None:
    file_store.save(path, as_dict(game))


def as_dict(root):
    d = asdict(root)
    return clean(d)


def clean(d):
    if isinstance(d, dict):
        for (key, value) in d.items():
            d[key] = clean(value)
    elif isinstance(d, list):
        for (i, value) in enumerate(d):
            d[i] = clean(value)
    elif isinstance(d, Enum):
        # This is the reason for this in the first place!
        return d.value
    return d
