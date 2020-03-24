from pathlib import Path


class PATHS:
    CONFIG = Path.home() / ".config" / "tfr"
    SECRETS = CONFIG / "secrets.yaml"
