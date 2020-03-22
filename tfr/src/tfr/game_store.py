from enum import Enum
from typing import List, Optional
from dataclasses import dataclass

import dacite

from . import file_store


@dataclass
class User:
    name: str
    username: str


class Role(Enum):
    SOURCERER = "sourcerer"
    EXAMINER = "examiner"


@dataclass
class Phase:
    index: int
    role: int
    player: int
    url: Optional[int]


@dataclass
class App:
    id: str
    name: str


@dataclass
class Game:
    name: str
    id: str
    gm: User
    players: List[User]
    apps: List[App]


def load(path: str) -> Game:
    return normer(file_store.load(path))


def normer(data: dict) -> Game:
    return dacite.from_dict(data_class=Game, data=data)
