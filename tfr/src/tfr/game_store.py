from enum import Enum
import typing as t
from dataclasses import dataclass

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
    phases: t.List[Phase]


@dataclass
class Repository:
    id: str
    name: t.Optional[str]
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
