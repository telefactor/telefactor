import typing as t
from functools import lru_cache
from pathlib import Path

from tfr import game_store
from tfr import constants
from tfr.constants import TFR_FILENAME
from tfr.io_utils import echo, echo_info
from tfr.file_store import Pathish


class TfrApp:
    game: game_store.Game
    game_path: str

    def __repr__(self):
        return f"TFR(game_path='{self.game_path}')"

    ##
    # Storage Helpers

    def init_game(
        self,
        *,
        root_dir: str,
        name: str,
        gm_username: str,
        player_usernames: list[str],
    ):
        root_path = Path(root_dir)
        echo_info("Initializing game at", root_path.absolute())

        maybe_game_path = root_path / TFR_FILENAME
        if maybe_game_path.exists():
            echo_info(f"{TFR_FILENAME} exists. Loading existing game.")
            self.load_game(maybe_game_path)
        else:
            self.game = game_store.Game(
                name=(name or constants.DEFAULT_NAME),
                gm=(
                    game_store.User(
                        username=(gm_username or constants.DEFAULT_GM_USERNAME)
                        name=None
                    )
                ),
            )

    def load_game(self, path: Pathish):
        self.game_path = str(path)
        self.game = game_store.load(path)
        return self.game

    def save_game(self):
        game_store.save(self.game_path, self.game)

    ##
    # Traversal

    # def get_phase_repo(
    #     self, phase: game_store.Phase
    # ) -> t.Optional[game_store.Repository]:
    #     return self.get_name_to_repo().get(phase.repository)

    # def get_name_to_repo(self):
    #     return {repo.name: repo for repo in self.game.repositories}

    def summarize(self):
        return {
            "name": self.game.name,
            "gm": self.game.gm.username,
            "players": sorted([player.username for player in self.game.players]),
        }

    def summarizeStatus(self):
        pass

    ##
    # Stuff that requires auth
    def with_secrets(self, *_):
        pass


@lru_cache()
def get_app() -> TfrApp:
    return TfrApp()
