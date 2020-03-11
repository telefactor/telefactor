import re
from functools import lru_cache

from github import Repository

from . import secret_store
from . import hub


class App:
    secrets = None
    github = None
    user = None
    repos = None

    def login(self):
        self.secrets = secret_store.load()
        if self.secrets.github.access_token in (None, ""):
            raise Exception("No access token!")

        self.github = hub.login(self.secrets.github)
        self.user = self.github.get_user()

    def ls(self, pattern) -> Repository:
        if self.repos is None:
            self.repos = self.user.get_repos()

        regex = re.compile(pattern)

        def matcher(repo):
            return regex.match(repo.name) is not None

        return filter(matcher, self.repos)


@lru_cache()
def get_app() -> App:
    return App()
