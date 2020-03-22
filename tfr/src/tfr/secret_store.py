from dataclasses import dataclass

import dacite

from .constants import PATHS
from . import file_store


@dataclass
class GitHub:
    access_token: str


@dataclass
class Secrets:
    github: GitHub


def load() -> Secrets:
    content = file_store.load(PATHS.SECRETS)

    return normer(content)


def normer(data: dict) -> Secrets:
    return dacite.from_dict(data_class=Secrets, data=data)
