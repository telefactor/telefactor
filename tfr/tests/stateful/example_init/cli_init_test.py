import os
from pathlib import Path
import shutil

from click.testing import CliRunner
import git
import pytest

from tfr import commands


@pytest.fixture
def test_output_dir(request):
    test_path: Path = request.path
    # print("request node name", request.node.name)
    # print("test_path", test_path)
    test_output_path = test_path.parent / "test_output"
    test_output_path.mkdir(exist_ok=True)
    return test_output_path


@pytest.fixture
def ensure_output_repo_dir(request, test_output_dir):
    test_path: Path = request.path
    # print("test_path", test_path)
    repo_template_path = test_path.parent / "repo_template"
    if not repo_template_path.exists():
        raise Exception(f"Test needs template at: {repo_template_path}")

    output_repo_path = test_output_dir / "output_repo"

    if output_repo_path.exists():
        # Conditional auto-clean-up?
        # raise Exception(f"Repo output exists: {output_repo_path}")
        shutil.rmtree(output_repo_path)

    shutil.copytree(
        repo_template_path,
        output_repo_path,
        ignore=shutil.ignore_patterns("IS_TEMPLATE.txt"),
    )
    return output_repo_path


@pytest.fixture
def ensure_git_repo(ensure_output_repo_dir):
    repo = git.Repo.init(ensure_output_repo_dir)
    repo.index.add(".")
    repo.index.commit("init")
    return repo


@pytest.fixture
def repo_cwd(ensure_output_repo_dir):
    prev_cwd = os.getcwd()

    try:
        os.chdir(ensure_output_repo_dir)
        yield ensure_output_repo_dir
    finally:
        os.chdir(prev_cwd)


class DescribeExampleInit:
    def it_works(self, repo_cwd, ensure_git_repo):
        git_repo = ensure_git_repo
        # breakpoint()
        print("Hello!!", {"repo_cwd": repo_cwd, "cwd": os.getcwd()})
        print(git_repo.index.diff(None))
        print(git_repo.untracked_files)
        pass

    # @pytest.fixture
    # def game(self):

    # with runner.isolated_filesystem():

    # def it_bootstraps(self):
    # def it_bootstraps(self):
    #     runner = CliRunner()
    #     result = runner.invoke(commands.init_game, [])
    #     print(result.output)
    #     assert result.exit_code == 0
    #     assert result.output == "Hello World!\n"
