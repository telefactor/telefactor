import click
from tfr.constants import PATHS
from tfr.hub import Hub
from tfr.io_utils import echo
from tfr.app import TfrApp, get_app


@click.group()
@click.option(
    "-s",
    "--secrets-path",
    default=str(PATHS.SECRETS),
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_context
def cli(ctx, secrets_path):
    tfr = get_app()
    ctx.obj = tfr

    tfr.hub = Hub()
    tfr.hub.login(secrets_path)


@cli.command()
@click.pass_obj
def login(tfr: TfrApp):
    echo(f"Logged in with user: {tfr.hub.user.login}")


@cli.command()
@click.argument("WORDS", nargs=-1)
def say(words):
    echo(*words)


if __name__ == "__main__":
    cli()
