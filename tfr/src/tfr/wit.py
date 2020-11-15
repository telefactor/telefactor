import git
from tfr import game_store
from tfr.tfr import TFR


def list_lockables(tfr: TFR, app: game_store.App):
    phase = app.phases[0]
    repo = tfr.get_phase_repo(phase)
    if repo is None:
        raise Exception(f"No repo for phase {phase.repository}")

    local = git.Repo(repo.directory)
    if local.is_dirty():
        raise Exception(f"Repo {repo.directory} has modified files")
