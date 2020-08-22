import click
from tfr.io_utils import echo

from .base import cli


@cli.group()
def repos():
    pass


@repos.command()
@click.argument("pattern")
@click.option("--details/--no-details", default=False)
@click.pass_obj
def ls(app, pattern, details):
    """List repositories matching PATTERN regular expression."""
    for repo in app.ls(pattern):
        echo(repo.name)
        if details:
            echo(repo.html_url)
            echo(repo.ssh_url)


@repos.command()
@click.argument("name")
@click.pass_obj
def new(app, name):
    """Create a private repository with the given NAME."""
    if not click.confirm(f"Create a new repository named {repr(name)}?"):
        echo("Okay nevermind")
        return

    created_repo = app.new_repo(name)
    echo(
        f"""
        Created!
        HTML URL: {created_repo.html_url}
        Clone URL: {created_repo.clone_url}
        """
    )
