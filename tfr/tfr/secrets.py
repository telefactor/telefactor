import yaml
from hamcrest import assert_that, has_entries, instance_of

from .app import PATHS

##
# Secrets


def load_secrets():
    if not PATHS.SECRETS.exists():
        raise Exception(f"Cannot locate secrets! Expected: {PATHS.SECRETS}")

    with PATHS.SECRETS.open() as secrets_file:
        parsed_secrets = yaml.full_load(secrets_file)

    assert_required_secrets_are_included(parsed_secrets)
    return parsed_secrets


def assert_required_secrets_are_included(secrets_dict):
    assert_that(
        secrets_dict,
        has_entries({"github": has_entries({"access_token": instance_of(str)}),}),
    )
