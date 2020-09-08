import re
import typing as t
from functools import lru_cache

from github.Repository import Repository

from . import game_store, hub, secret_store


class TFR:
    secrets = None
    github = None
    user = None
    repos = None
    name_to_remote: dict = None
    name_to_local: dict = None
    game: game_store.Game = None
    game_path: str = None

    def __repr__(self):
        return f"TFR(game_path='{self.game_path}')"

    def login(self, secrets_path: str):
        self.secrets = secret_store.load(secrets_path)
        if self.secrets.github.access_token in (None, ""):
            raise Exception("No access token!")

        self.github = hub.login(self.secrets.github)
        self.user = self.github.get_user()

    def ls(self, pattern) -> t.List[Repository]:
        regex = re.compile(pattern)

        def matcher(repo):
            return regex.match(repo.name) is not None

        return sorted(filter(matcher, self.get_remotes()), key=(lambda r: r.name))

    def get_remotes(self):
        if self.repos is None:
            self.repos = self.user.get_repos(affiliation="owner")
        return self.repos

    def get_name_to_remote(self):
        if self.name_to_remote is None:
            self.name_to_remote = {remote.name: remote for remote in self.get_remotes()}

        return self.name_to_remote

    def get_name_to_local(self):
        if self.name_to_local is None:
            self.name_to_local = {local.id: local for local in self.game.repositories}

        return self.name_to_local

    def new_remote(self, name) -> Repository:
        created_repo = self.user.create_repo(name=name, private=True, auto_init=True,)
        self.remotes = None
        return created_repo

    def load_game(self, path):
        self.game = game_store.load(path)
        self.game_path = path
        return self.game

    def save_game(self):
        game_store.save(self.game_path, self.game)

    def iter_locals_remotes(self):
        for local in self.game.get_remotes():
            yield (local, self.get_name_to_remote()[local.id])

    def iter_phase_locals(self):
        for game_app in self.game.apps:
            for phase in game_app.phases:
                local = self.get_name_to_local()[phase.repository]
                yield (phase, local)


@lru_cache()
def get_tfr() -> TFR:
    return TFR()