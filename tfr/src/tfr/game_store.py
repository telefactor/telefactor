import typing as t
from dataclasses import asdict, dataclass
from enum import Enum

import dacite

from . import file_store


@dataclass
class User:
    id: str
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
    return dacite.from_dict(data_class=Game, data=data)


def save(path: str, game: Game) -> None:
    file_store.save(path, asdict(game))
