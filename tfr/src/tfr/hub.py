from github import Github

from . import secret_store
from .io_utils import echo_info
from .tfr import TFR


class Hub:
    def __init__(self, tfr: TFR):
        self.tfr = tfr

    def login(self, secrets_path: str):
        self.tfr.secrets = secret_store.load(secrets_path)
        if self.tfr.secrets.github.access_token in (None, ""):
            raise Exception("No access token!")

        self.tfr.github = Github(self.tfr.secrets.github.access_token)
        self.tfr.user = self.tfr.github.get_user()

    def fetch(self) -> int:
        echo_info("Fetching remotes from GitHub...")
        self.tfr.get_remotes()

        echo_info("Diffing metadata.")
        changed_count = 0
        for local in self.tfr.game.repositories:
            remotes = self.tfr.ls(local.name)
            if not remotes:
                echo_info(f"No remote for {local.name}")
                continue

            remote = remotes[0]
            echo_info(f"Found {remote.name} for {local.name}")

            incoming_metadata = {
                "id": remote.id,
                "name": remote.name,
                "full_name": remote.full_name,
                "html_url": remote.clone_url,
                "clone_url": remote.clone_url,
                "ssh_url": remote.ssh_url,
                "isPrivate": remote.private,
            }
            if local.metadata == incoming_metadata:
                echo_info("No difference.")
                continue

            if local.metadata:
                echo_info("Original metadata:", local.metadata)
                echo_info("Incoming metadata:", incoming_metadata)

            local.metadata = incoming_metadata
            changed_count += 1

        return changed_count

    def push(self):
        self.fetch()
        for local in self.tfr.game.repositories:
            if local.metadata:
                echo_info(f"Repo {local.name} up to date")
                continue

            echo_info(f"Creating remote for {local.name}")
            remote = self.tfr.user.create_repo(
                name=local.name, private=True, auto_init=True
            )
            self.tfr.add_remote(remote)
