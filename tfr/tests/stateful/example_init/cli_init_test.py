import os
from pathlib import Path
import shutil

from click.testing import CliRunner, Result as ClickResult
import git
import pytest

import tfr.commands
import tfr.app
from tfr.constants import DEFAULT_GM_USERNAME, DEFAULT_NAME
from tfr.game_store import Game, User
from tfr.tree_manager import TreeManager


def assert_click_result(result: ClickResult):
    print(
        "\n$$ stdout start $$\n",
        result.stdout,
        "\n$$ stdout end $$\n",
    )
    assert not result.exception


def output_dir_name(request: pytest.FixtureRequest):
    return "_".join([request.node.parent.name, request.node.name])


@pytest.fixture
def test_output_dir(request: pytest.FixtureRequest):
    test_path: Path = request.path
    # print("\n>>>>> ", request.node.name)
    # test_output_path = test_path.parent / "test_output"
    test_output_path = test_path.parent / "test_output" / output_dir_name(request)
    # print("\n>>>>> test_output_path", test_output_path)

    if test_output_path.exists():
        print(f"Cleaning up existing output directory: {test_output_path}")
        shutil.rmtree(test_output_path)

    test_output_path.mkdir(exist_ok=True, parents=True)
    yield test_output_path

    print(
        f"Output directory is kept after tests and is cleaned during next run: {test_output_path}"
    )


@pytest.fixture
def game_root_cwd(test_output_dir):
    prev_cwd = os.getcwd()

    try:
        os.chdir(test_output_dir)
        yield test_output_dir
    finally:
        os.chdir(prev_cwd)


class DescribeTreeManager:
    def test_scan_empty(self, game_root_cwd: Path):

        (game_root_cwd / "repos").mkdir(parents=True)

        game = Game(
            name=DEFAULT_NAME,
            gm=User(username=DEFAULT_GM_USERNAME, name=None),
        )
        tree_manager = TreeManager(
            game=game,
            game_path=game_root_cwd,
        )

        assert sorted(
            [(p.phase_index, str(p.directory)) for p in tree_manager._phases]
        ) == [
            #
        ]

    def test_scan_phases_no_git(self, game_root_cwd: Path):
        (game_root_cwd / "repos" / "base").mkdir(parents=True)
        (game_root_cwd / "repos" / "phase-01").mkdir()
        (game_root_cwd / "repos" / "phase-02").mkdir()

        game = Game(
            name=DEFAULT_NAME,
            gm=User(username=DEFAULT_GM_USERNAME, name=None),
        )
        tree_manager = TreeManager(
            game=game,
            game_path=game_root_cwd,
        )

        assert sorted(
            [
                (
                    p.phase_index,
                    str(p.directory),
                    (p.git_repo.head.commit.summary if p.git_repo else None),
                )
                for p in tree_manager._phases
            ]
        ) == [
            (0, "repos/base", None),
            (1, "repos/phase-01", None),
            (2, "repos/phase-02", None),
        ]

    def test_scan_phases_base_git(self, game_root_cwd: Path, repo_template_path):
        (game_root_cwd / "repos" / "base").mkdir(parents=True)
        (game_root_cwd / "repos" / "phase-01").mkdir()
        (game_root_cwd / "repos" / "phase-02").mkdir()

        factory_template_to_repo(repo_template_path, game_root_cwd / "repos" / "base")
        factory_init_commit_repo(game_root_cwd / "repos" / "base")

        game = Game(
            name=DEFAULT_NAME,
            gm=User(username=DEFAULT_GM_USERNAME, name=None),
        )
        tree_manager = TreeManager(
            game=game,
            game_path=game_root_cwd,
        )

        assert sorted(
            [
                (
                    p.phase_index,
                    str(p.directory),
                    (p.git_repo.head.commit.summary if p.git_repo else None),
                )
                for p in tree_manager._phases
            ]
        ) == [
            (0, "repos/base", "init"),
            (1, "repos/phase-01", None),
            (2, "repos/phase-02", None),
        ]


class DescribeExampleInitFromBlank:
    def test_init_game(self, game_root_cwd: Path):
        runner = CliRunner()
        result = runner.invoke(
            tfr.commands.init_game,
            [
                "--name=telefactor-test-cli",
            ],
        )
        assert_click_result(result)

        assert "Initializing game at" in result.output
        assert str(game_root_cwd) in result.output

        assert (game_root_cwd / "repos" / "base").exists()

        ##
        app = tfr.app.TfrApp()
        app.load_game("./tfr.yaml")

        assert app.game.name == "telefactor-test-cli"


#####
#


def factory_template_to_repo(repo_template_path, repo_path):
    if not repo_template_path.exists():
        raise Exception(f"Test needs template at: {repo_template_path}")

    repo_path.mkdir(parents=True, exist_ok=True)

    shutil.copytree(
        repo_template_path,
        repo_path,
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("IS_TEMPLATE.txt"),
    )
    return repo_path


def factory_init_commit_repo(repo_path):
    repo = git.Repo.init(repo_path)
    repo.index.add(repo.untracked_files)
    repo.index.commit("init")
    return repo


@pytest.fixture
def repo_template_path(request):
    test_path: Path = request.path
    return test_path.parent / "repo_template"


@pytest.fixture
def init_reference_repo(repo_template_path, test_output_dir):
    reference_repo_path = test_output_dir / "repos" / "base"

    # if reference_repo_path.exists():
    #     print(f"Cleaning up existing repo path {reference_repo_path}")
    #     shutil.rmtree(reference_repo_path)

    return factory_template_to_repo(repo_template_path, reference_repo_path)


@pytest.fixture
def ensure_git_repo(init_reference_repo):
    return factory_init_commit_repo(init_reference_repo)


class DescribeExampleInitWhenRepoExists:
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

        assert_click_result(result)

        app = tfr.app.TfrApp()
        app.load_game("./tfr.yaml")

        assert app.summarize() == {
            "name": "telefactor-test-cli",
            "gm": "test-ss",
            "players": ["test-tt", "test-uu", "test-vv"],
        }

        # assert app.summarizeStatus() == {}
