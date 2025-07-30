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
    test_output_path = test_path.parent / "test_output"

    if test_output_path.exists():
        print(f"Cleaning up existing output directory: {test_output_path}")
        shutil.rmtree(test_output_path)

    test_output_path.mkdir(exist_ok=True)
    yield test_output_path

    print(
        f"Output directory is kept after tests and is cleaned during next run: {test_output_path}"
    )


@pytest.fixture
def init_reference_repo(request, test_output_dir):
    test_path: Path = request.path
    repo_template_path = test_path.parent / "repo_template"
    if not repo_template_path.exists():
        raise Exception(f"Test needs template at: {repo_template_path}")

    reference_repo_path = test_output_dir / "repos" / "phase-0"

    if reference_repo_path.exists():
        print(f"Cleaning up existing repo path {reference_repo_path}")
        shutil.rmtree(reference_repo_path)

    reference_repo_path.mkdir(parents=True)

    shutil.copytree(
        repo_template_path,
        reference_repo_path,
        ignore=shutil.ignore_patterns("IS_TEMPLATE.txt"),
    )
    return reference_repo_path


# TODO: I think I actually want this to be implemented by teh CLI.
@pytest.fixture
def ensure_git_repo(init_reference_repo):
    repo = git.Repo.init(init_reference_repo)
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


class DescribeExampleInitFromBlank:
    def test_init_game(self, game_root_cwd):
        runner = CliRunner()
        result = runner.invoke(
            tfr.commands.init_game,
            [
                "--name=telefactor-test-cli",
            ],
        )
        assert not result.exception

        assert "Initializing game at" in result.output
        assert str(game_root_cwd) in result.output


@pytest.mark.skip
class DescribeExampleInitWhenRepoExists:
    def test_template_repo_fixtures(self, game_root_cwd, ensure_git_repo: git.Repo):
        git_repo = ensure_git_repo
        assert len(git_repo.untracked_files) == 0

    def test_init_game(self, game_root_cwd, ensure_git_repo: git.Repo):
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
        print("cli stdout:", result.stdout)

        app = tfr.app.TfrApp()
        app.load_game("./tfr.yaml")

        assert app.summarize() == {
            "name": "telefactor-test-cli",
            "gm": "test-ss",
            "players": ["test-tt", "test-uu", "test-vv"],
        }

        # assert app.summarizeStatus() == {}
