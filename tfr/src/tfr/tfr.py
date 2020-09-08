import re
import typing as t
from functools import lru_cache

from github.NamedUser import NamedUser as GhNamedUser
from github.Repository import Repository as GhRepository

from . import game_store


class TFR:
    secrets = None
    github = None
    user: GhNamedUser = None
    remotes: t.List[GhRepository] = None
    name_to_remote: dict
    name_to_local: dict
    game: game_store.Game
    game_path: str

    def __init__(self):
        self.remotes = []
        self.name_to_remote = {}
        self.name_to_local = {}

    def __repr__(self):
        return f"TFR(game_path='{self.game_path}')"

    def ls(self, pattern) -> t.List[GhRepository]:
        regex = re.compile(pattern)

        def matcher(repo):
            return regex.match(repo.name) is not None

        return sorted(filter(matcher, self.remotes), key=(lambda r: r.name))

    def add_remotes(self, *remotes: t.List[GhRepository]):
        self.remotes += remotes

    def get_name_to_remote(self):
        return {remote.name: remote for remote in self.remotes}

    def get_name_to_local(self):
        return {local.name: local for local in self.game.repositories}

    def load_game(self, path):
        self.game = game_store.load(path)
        self.game_path = path
        return self.game

    def save_game(self):
        game_store.save(self.game_path, self.game)

    def iter_locals_remotes(self):
        name_to_remote = self.get_name_to_remote()
        for local in self.remotes:
            yield (local, name_to_remote[local.name])

    # def iter_phase_locals(self):
    #     for game_app in self.game.apps:
    #         for phase in game_app.phases:
    #             local = self.get_name_to_local()[phase.repository]
    #             yield (phase, local)


@lru_cache()
def get_tfr() -> TFR:
    return TFR()
