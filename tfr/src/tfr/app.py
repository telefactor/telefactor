import typing as t
from functools import lru_cache
from pathlib import Path
import git


from tfr import game_store
from tfr import constants
from tfr.git_utils import PathLike, is_git_repo
from tfr.constants import TFR_FILENAME
from tfr.io_utils import echo, echo_error, echo_info
from tfr.tree_manager import make_phase_name


class TfrApp:
    _game: game_store.Game | None = None
    _game_path: Path | None = None

    def __repr__(self):
        return f"TFR(game_path='{self._game_path}')"

    ##
    # Accessors

    @property
    def game(self):
        if not self._game:
            raise AttributeError()

        return self._game

    ##
    # Init

    def init_game(
        self,
        *,
        root_dir: str,
        name: str,
        gm_username: str,
        player_usernames: list[str],
    ):
        root_path = Path(root_dir).absolute()
        echo_info("Initializing game at", root_path)
        analysis = self._analyze_initial_dir(root_path)

        if analysis.game_path_existed:
            echo_info(f"{TFR_FILENAME} exists. Loading existing game.")
            self.load_game(analysis.game_path)
        else:
            self._init_from_blank(
                name=name,
                gm_username=gm_username,
                player_usernames=player_usernames,
            )
            self._game_path = analysis.game_path

        if analysis.root_is_repo and not analysis.game_path_existed:
            self._echo_warn_repo(root_path)

        if analysis.root_is_repo and not analysis.phase_base_dir:
            self._echo_error_base(analysis.expected_phase_base_dir)
            exit(1)

        self._make_phase_base()

        self.save_game()

    def _init_from_blank(
        self,
        *,
        name: str,
        gm_username: str,
        player_usernames: list[str],
    ):
        self._game = game_store.Game(
            name=(name or constants.DEFAULT_NAME),
            gm=game_store.User(
                username=(gm_username or constants.DEFAULT_GM_USERNAME),
                name=None,
            ),
            players=(
                [
                    game_store.User(username=username, name=None)
                    for username in player_usernames
                ]
            ),
        )

    class Analysis(t.NamedTuple):
        root_path: Path
        root_is_repo: bool
        game_path: Path
        game_path_existed: bool
        repos_dir: Path | None
        phase_dirs: list[Path] | None
        phase_base_dir: Path | None
        expected_phase_base_dir: Path

    def _analyze_initial_dir(self, root_path: Path) -> Analysis:
        game_path = root_path / TFR_FILENAME
        game_path_existed = game_path.exists()

        root_is_repo = False
        if is_git_repo(root_path):
            root_is_repo = True

        repos_dir = root_path / constants.REPOS_DIRNAME
        expected_phase_base_dir = repos_dir / make_phase_name(0)

        if repos_dir.exists() and repos_dir.is_dir():
            phase_dirs = [
                sub_dir for sub_dir in repos_dir.iterdir() if sub_dir.is_dir()
            ]
            phase_base_dir = None
            for phase_dir in phase_dirs:
                if phase_dir.name == make_phase_name(0):
                    phase_base_dir = phase_dir
        else:
            repos_dir = None
            phase_dirs = None
            phase_base_dir = None

        return self.Analysis(
            root_path=root_path,
            root_is_repo=root_is_repo,
            game_path=game_path,
            game_path_existed=game_path_existed,
            repos_dir=repos_dir,
            phase_dirs=phase_dirs,
            phase_base_dir=phase_base_dir,
            expected_phase_base_dir=expected_phase_base_dir,
        )

    def _echo_warn_repo(self, root_path: Path):
        echo_error(
            f"""
            Warning! Root directory at:
                {root_path.relative_to(Path.cwd())}
            is already tracked by git. That is fine if you are planning to keep your game management
            files (tfr.yaml) in source control. Tfr will make sure to git-ignore the phase repos.

            However, **do not use your reference implementation base repo** as your root directory. 
            """
        )

    def _echo_error_base(self, expected_phase_base_dir: Path):
        echo_error(
            f"""
            I couldn't find the base repo, so to be safe I'm assuming you don't want to initialize
            here. Expected:
                {expected_phase_base_dir}
            to be a directory with your reference implementation. Either restructure your root
            directory or run init in an empty directory and add copy your files in later.
            """
        )

    def _make_phase_base(self):
        # self.game.repositories
        pass

    def load_game(self, path: PathLike):
        self._game_path = Path(path)
        self._game = game_store.load(self._game_path)
        return self.game

    def save_game(self):
        if not self._game_path:
            raise ValueError("No game path")

        game_store.save(self._game_path, self.game)

    def summarize(self):
        return {
            "name": self.game.name,
            "gm": self.game.gm.username,
            "players": sorted([player.username for player in self.game.players]),
        }

    def summarizeStatus(self):
        pass

    ##
    # Stuff that requires auth
    def with_secrets(self, *_):
        raise NotImplemented


@lru_cache()
def get_app() -> TfrApp:
    return TfrApp()
