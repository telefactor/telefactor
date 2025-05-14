import typing as t
from functools import lru_cache

from tfr import game_store


class TfrApp:
    game: game_store.Game
    game_path: str

    def __repr__(self):
        return f"TFR(game_path='{self.game_path}')"

    ##
    # Storage Helpers

    def load_game(self, path):
        self.game = game_store.load(path)
        self.game_path = path
        return self.game

    def save_game(self):
        game_store.save(self.game_path, self.game)

    ##
    # Traversal

    def get_phase_repo(
        self, phase: game_store.Phase
    ) -> t.Optional[game_store.Repository]:
        return self.get_name_to_repo().get(phase.repository)

    def get_name_to_repo(self):
        return {repo.name: repo for repo in self.game.repositories}

    def summarize(self):
        return {
            "name": self.game.name,
            "gm": self.game.gm.username,
            "players": sorted([player.username for player in self.game.players]),
        }


@lru_cache()
def get_app() -> TfrApp:
    return TfrApp()
