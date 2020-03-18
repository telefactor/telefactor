from typing import NamedTuple
from functools import lru_cache

import yaml
from cerberus import Validator

from .constants import PATHS
from .vlad import make


class GitHub(NamedTuple):
    access_token: str


class Secrets(NamedTuple):
    github: GitHub


secrets_validator = Validator(
    {
        "secrets": {
            "type": "dict",
            "require_all": True,
            "schema": {
                "github": {
                    "type": "dict",
                    # "require_all": True,
                    # "schema:": {
                    #     "access_token": {"type": "string"}
                    # },
                },
            },
        }
    }
)

secrets_normalizer = Validator(
    {
        "secrets": {
            "coerce": [
                Validator({"github": {"coerce": make(GitHub)}}).normalized,
                make(Secrets),
            ]
        }
    }
)


@lru_cache()
def load() -> Secrets:
    if not PATHS.SECRETS.exists():
        raise Exception(f"Cannot locate secrets! Expected: {PATHS.SECRETS}")

    with PATHS.SECRETS.open() as secrets_file:
        parsed_secrets = yaml.full_load(secrets_file)

    is_valid = secrets_validator.validate({"secrets": parsed_secrets})
    if not is_valid:
        errors = repr(secrets_validator.errors)
        raise Exception(f"Invalid secrets: {errors}")

    normalized = secrets_normalizer.normalized(secrets_validator.document)
    return normalized["secrets"]
