from pathlib import Path

import git

from .base import game, click
from .io_utils import echo, echo_info


@game.command()
@click.pass_obj
def clone_all(app):
    Cloner(app).clone_all()


class Cloner:
    app: "App" = None
    root_dir: Path = None
    repos_dir: Path = None
    name_to_local: dict = None

    def __init__(self, app):
        self.app = app
        self.root_dir = Path(app.game_path).parent

    def clone_all(self):
        self.name_to_local = self.app.get_name_to_local()
        self.repos_dir = self.root_dir / "repos"
        self.repos_dir.mkdir(exist_ok=True)

        for game_app in self.app.game.apps:
            game_app_dir = self.repos_dir / game_app.name
            game_app_dir.mkdir(exist_ok=True)

            for phase in game_app.phases:
                self.handle_phase(phase, game_app_dir)

        self.app.save_game()

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
