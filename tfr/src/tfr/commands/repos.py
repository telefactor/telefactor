import click
from tfr.io_utils import echo
from tfr.tfr import TFR

from .base import cli


@cli.group()
def repos():
    pass


@repos.command()
@click.argument("pattern")
@click.option("--details/--no-details", default=False)
@click.pass_obj
def ls(tfr: TFR, pattern, details):
    """List repositories matching PATTERN regular expression."""
    for repo in tfr.ls(pattern):
        echo(repo.name)
        if details:
            echo(repo.html_url)
            echo(repo.ssh_url)


@repos.command()
@click.argument("name")
@click.pass_obj
def new(tfr: TFR, name):
    """Create a private repository with the given NAME."""
    if not click.confirm(f"Create a new repository named {repr(name)}?"):
        echo("Okay nevermind")
        return

    created_repo = tfr.new_repo(name)
    echo(
        f"""
        Created!
        HTML URL: {created_repo.html_url}
        Clone URL: {created_repo.clone_url}
        """
    )
