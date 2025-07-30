from tfr.app import TfrApp
from tfr.constants import PATHS

from .base import cli, click


@cli.group()
@click.option(
    "-s",
    "--secrets-path",
    default=str(PATHS.SECRETS),
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_obj
def with_secrets(tfr: TfrApp, secrets_path):
    tfr.with_secrets(secrets_path)
