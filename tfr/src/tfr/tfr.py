# import typing as t
from functools import lru_cache

from . import game_store
from .hub import Hub


class TFR:
    hub: Hub
    name_to_local: dict
    game: game_store.Game
    game_path: str

    def __init__(self):
        self.remotes = []
        self.name_to_local = {}

    def __repr__(self):
        return f"TFR(game_path='{self.game_path}')"

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
