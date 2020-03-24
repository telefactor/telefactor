import re
from functools import lru_cache
from typing import List

from github.Repository import Repository

from . import game_store
from . import secret_store
from . import hub


class App:
    secrets = None
    github = None
    user = None
    repos = None
    game = None
    game_path: str = None

    def login(self, secrets_path: str):
        self.secrets = secret_store.load(secrets_path)
        if self.secrets.github.access_token in (None, ""):
            raise Exception("No access token!")

        self.github = hub.login(self.secrets.github)
        self.user = self.github.get_user()

    def ls(self, pattern) -> List[Repository]:
        regex = re.compile(pattern)

        def matcher(repo):
            return regex.match(repo.name) is not None

        return sorted(filter(matcher, self.get_repos()), key=(lambda r: r.name))

    def get_repos(self):
        if self.repos is None:
            self.repos = self.user.get_repos()
        return self.repos

    def new_repo(self, name) -> Repository:
        created_repo = self.user.create_repo(name=name, private=True, auto_init=True,)
        self.repos = None
        return created_repo

    def load_game(self, path):
        self.game = game_store.load(path)
        self.game_path = path
        return self.game

    def save_game(self):
        game_store.save(self.game_path, self.game)


@lru_cache()
def get_app() -> App:
    return App()
