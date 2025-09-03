import git
import git.repo.fun
from pathlib import Path

PathLike = git.PathLike


def is_git_repo(pathl: PathLike):
    return git.repo.fun.is_git_dir(Path(pathl) / ".git")


def try_git_repo(pathl: PathLike) -> None | git.Repo:
    if not is_git_repo(pathl):
        return None

    return git.Repo(pathl)
