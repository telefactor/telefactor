from pathlib import Path

DEFAULT_NAME = "telefactor-game"
DEFAULT_GM_USERNAME = "gm-username"

TFR_FILENAME = "tfr.yaml"
REPOS_DIRNAME = "repos"


def make_phase_name(index: int) -> str:
    if index < 0:
        raise ValueError("Negative phase index")

    if index == 0:
        return "base"

    return "phase-{index:02d}"


class PATHS:
    CONFIG = Path.home() / ".config" / "tfr"
    SECRETS = CONFIG / "secrets.yaml"
