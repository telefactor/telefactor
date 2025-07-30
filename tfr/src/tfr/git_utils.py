import git
import git.repo.fun
from pathlib import Path

PathLike = git.PathLike


def is_git_repo(pathl: PathLike):
    return git.repo.fun.is_git_dir(Path(pathl) / ".git")
