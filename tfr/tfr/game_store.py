from enum import Enum
from typing import NamedTuple, List, Optional

from . import file_store
from . import vlad


class User(NamedTuple):
    name: str
    username: str


class Role(Enum):
    SOURCERER = "sourcerer"
    EXAMINER = "examiner"


class Phase(NamedTuple):
    index: int
    role: int
    player: int
    url: Optional[int]


class App(NamedTuple):
    index: int
    name: str


class Game(NamedTuple):
    name: str
    id: str
    gm: User
    players: List[User]
    apps: List[App]


def load(path: str):
    return normer(file_store.load(path))


normer = vlad.normer(Game)
