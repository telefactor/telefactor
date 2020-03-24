from dataclasses import dataclass

import dacite

from . import file_store


@dataclass
class GitHub:
    access_token: str


@dataclass
class Secrets:
    github: GitHub


def load(path: str) -> Secrets:
    content = file_store.load(path)

    return normer(content)


def normer(data: dict) -> Secrets:
    return dacite.from_dict(data_class=Secrets, data=data)
