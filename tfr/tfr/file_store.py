from functools import lru_cache
from pathlib import Path

from .constants import PATHS
import yaml


@lru_cache()
def load(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"File store cannot load file. Expected: {PATHS.SECRETS}"
        )

    with PATHS.SECRETS.open() as secrets_file:
        return yaml.full_load(secrets_file)
