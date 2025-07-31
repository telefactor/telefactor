from typing import Union
from functools import lru_cache
from pathlib import Path

import yaml

from .git_utils import PathLike


def load(path: PathLike) -> dict:
    real_path = Path(path)
    if not real_path.exists():
        raise FileNotFoundError(f"File store cannot load file. Expected: {real_path}")

    with real_path.open() as yaml_file:
        return yaml.full_load(yaml_file)


def save(path: PathLike, data: dict) -> Path:
    real_path = Path(path)

    # default_flow_style
    with real_path.open("w") as yaml_file:
        yaml.dump(data, yaml_file)

    return real_path
