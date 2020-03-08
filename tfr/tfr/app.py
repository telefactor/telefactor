from pathlib import Path


class PATHS:
    ROOT = Path(__file__).parent.parent

    CONFIG = ROOT / "config"
    SECRETS = CONFIG / "secrets.yaml"

    SOURCE = ROOT / "tfr"
