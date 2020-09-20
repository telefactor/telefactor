import re
import typing as t

from github import Github
from github.NamedUser import NamedUser as GhNamedUser
from github.Repository import Repository as GhRepository

from . import game_store, secret_store
from .io_utils import echo_info


class Hub:
    user: GhNamedUser = None
    remotes: t.List[GhRepository] = None
    name_to_remote: t.Dict[str, GhRepository]

    def __init__(self):
        self.remotes = []
        self.name_to_remote = {}

    def login(self, secrets_path: str):
        secrets = secret_store.load(secrets_path)
        if secrets.github.access_token in (None, ""):
            raise Exception("No access token!")

        # github = Github(secrets.github.access_token)
        github = Github(secrets.github.access_token)
        self.user = github.get_user()
        return self

    def fetch_remotes(self):
        """Freshly populates remotes."""
        self.remotes = []
        self.add_remote(*self.user.get_repos())

    def add_remote(self, *remotes: t.List[GhRepository]):
        self.remotes += remotes
        self.name_to_remote = {remote.name: remote for remote in self.remotes}

    def ls(self, pattern) -> t.List[GhRepository]:
        regex = re.compile(pattern)

        def matcher(repo):
            return regex.match(repo.name) is not None

        return sorted(filter(matcher, self.remotes), key=(lambda r: r.name))

    def fetch(self, game: game_store.Game) -> int:
        """Populates a game with remote metadata."""
        echo_info("Fetching remotes from GitHub")
        self.fetch_remotes()

        echo_info("Diffing metadata")
        changed_count = 0
        for local in game.repositories:
            remote = self.name_to_remote.get(local.name, None)
            if not remote:
                echo_info(f'No remote for "{local.name}"')
                continue

            echo_info(f'Found "{remote.full_name}" for "{local.name}"')

            incoming_metadata = extract_metadata(remote)
            if local.metadata == incoming_metadata:
                echo_info("No difference.")
                continue

            echo_info("Original metadata:", local.metadata)
            echo_info("Incoming metadata:", incoming_metadata)

            if not local.metadata:
                local.metadata = {}

            local.metadata.update(incoming_metadata)
            changed_count += 1

        return changed_count

    def push(self, game: game_store.Game) -> int:
        echo_info("Fetching before push")

        self.fetch(game)
        changed_count = 0
        for local in game.repositories:
            if local.metadata:
                echo_info(f'Repo "{local.name}" up to date')
                continue

            echo_info(f'Creating remote for "{local.name}"')
            remote = self.user.create_repo(
                name=local.name, private=True, auto_init=True
            )
            self.add_remote(remote)
            local.metadata = remote
            local.ssh_url = remote.ssh_url
            echo_info(f'Created remote "{remote.full_name}"')
            changed_count += 1

        return changed_count


def extract_metadata(remote: GhRepository) -> t.Dict:
    return {
        "id": remote.id,
        "name": remote.name,
        "full_name": remote.full_name,
        "html_url": remote.clone_url,
        "clone_url": remote.clone_url,
        "ssh_url": remote.ssh_url,
        "isPrivate": remote.private,
    }
