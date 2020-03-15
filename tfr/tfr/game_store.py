from enum import Enum
from typing import NamedTuple, List, Optional

import yaml
from cerberus import Validator

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


def parse():
    pass

normer = vlad.normer(Game)

def normalize():
    pass


def load(path):
    return normalize(parse(path))
