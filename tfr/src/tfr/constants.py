from pathlib import Path

TFR_FILENAME = "tfr.yaml"
DEFAULT_NAME = "telefactor-game"
DEFAULT_GM_USERNAME = "gm-username"


class PATHS:
    CONFIG = Path.home() / ".config" / "tfr"
    SECRETS = CONFIG / "secrets.yaml"
