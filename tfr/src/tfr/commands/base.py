import click
from tfr.app import get_app
from tfr.constants import PATHS
from tfr.io_utils import echo


@click.group()
@click.option(
    "-s",
    "--secrets-path",
    default=str(PATHS.SECRETS),
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_context
def cli(ctx, secrets_path):
    app = get_app()
    app.login(secrets_path)
    ctx.obj = app


@cli.command()
@click.pass_obj
def login(app):
    echo(f"Logged in with user: {app.user.login}")


@cli.command()
@click.argument("WORDS", nargs=-1)
def say(words):
    echo(*words)


if __name__ == "__main__":
    cli()
