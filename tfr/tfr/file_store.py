from typing import Union
from functools import lru_cache
from pathlib import Path

import yaml


@lru_cache()
def load(path: Union[str, Path]) -> dict:
    real_path = Path(path)
    if not real_path.exists():
        raise FileNotFoundError(f"File store cannot load file. Expected: {real_path}")

    with real_path.open() as yaml_file:
        return yaml.full_load(yaml_file)
