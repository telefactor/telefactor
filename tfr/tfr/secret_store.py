from typing import NamedTuple

from .constants import PATHS
from . import vlad
from . import file_store


class GitHub(NamedTuple):
    access_token: str


class Secrets(NamedTuple):
    github: GitHub


def load() -> Secrets:
    content = file_store.load(PATHS.SECRETS)

    return normer(content)


normer = vlad.normer(Secrets)
