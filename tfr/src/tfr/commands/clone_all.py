from pathlib import Path

import git
from tfr.io_utils import echo_info
from tfr.tfr import TFR

from .base import click
from .game import game


@game.command()
@click.pass_obj
def clone_all(tfr: TFR):
    Cloner(tfr).clone_all()


class Cloner:
    tfr: TFR = None
    root_dir: Path = None
    repos_dir: Path = None
    name_to_local: dict = None

    def __init__(self, tfr: TFR):
        self.tfr = tfr
        self.root_dir = Path(tfr.game_path).parent

    def clone_all(self):
        self.name_to_local = self.tfr.get_name_to_local()
        self.repos_dir = self.root_dir / "repos"
        self.repos_dir.mkdir(exist_ok=True)

        for game_app in self.tfr.game.tfrs:
            game_app_dir = self.repos_dir / game_app.name
            game_app_dir.mkdir(exist_ok=True)

            for phase in game_app.phases:
                self.handle_phase(phase, game_app_dir)

        self.tfr.save_game()

    def handle_phase(self, phase, game_app_dir):
        local = self.name_to_local[phase.repository]
        name = local.metadata["name"]
        ssh_url = local.metadata["ssh_url"]

        phase_repo_dir = game_app_dir / local.id
        if phase_repo_dir.is_dir():
            echo_info(f"Found existing {game_app_dir}")
            cloned_repo = git.Repo(phase_repo_dir)
        else:
            echo_info(f"Cloning: {ssh_url} into {game_app_dir}")
            cloned_repo = git.Repo.clone_from(ssh_url, phase_repo_dir)

        echo_info(f"Phase repo commit: {cloned_repo.head.commit.hexsha}")
        local.name = name
        local.ssh_url = ssh_url
        local.directory = str(phase_repo_dir)
        local.commit = cloned_repo.head.commit.hexsha
