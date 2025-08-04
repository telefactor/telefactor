from pathlib import Path

DEFAULT_NAME = "telefactor-game"
DEFAULT_GM_USERNAME = "gm-username"

TFR_FILENAME = "tfr.yaml"
REPOS_DIRNAME = "repos"


class PATHS:
    CONFIG = Path.home() / ".config" / "tfr"
    SECRETS = CONFIG / "secrets.yaml"
