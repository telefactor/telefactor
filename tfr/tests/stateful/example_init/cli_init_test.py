import os
from pathlib import Path
import shutil

from click.testing import CliRunner
import git
import pytest

import tfr.commands
import tfr.app


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
    repo.index.add(repo.untracked_files)
    repo.index.commit("init")
    return repo


@pytest.fixture
def game_root_cwd(test_output_dir):
    prev_cwd = os.getcwd()

    try:
        os.chdir(test_output_dir)
        yield test_output_dir
    finally:
        os.chdir(prev_cwd)


class DescribeExampleInit:
    def test_template_repo_fixtures(self, game_root_cwd, ensure_git_repo: git.Repo):
        git_repo = ensure_git_repo
        # breakpoint()
        print("Hello!!", {"game_root_cwd": game_root_cwd, "cwd": os.getcwd()})
        assert len(git_repo.untracked_files) == 0

    def test_bootstrap(self, game_root_cwd, ensure_git_repo: git.Repo):
        git_repo = ensure_git_repo
        runner = CliRunner()
        result = runner.invoke(
            tfr.commands.init_game,
            [
                "--name=telefactor-test-cli",
                "--gm=test-ss",
                "--players=test-tt,test-uu,test-vv",
            ],
        )
        print("stdout:", result.output)

        app = tfr.app.TfrApp()
        app.load_game("./tfr.yaml")

        assert app.summarize() == {
            "name": "telefactor-test-cli",
            "gm": "test-ss",
            "players": ["test-tt", "test-uu", "test-vv"],
        }
