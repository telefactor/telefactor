from textwrap import dedent as dd

import click

from .app import get_app


def echo(*msgs):
    click.echo("\n".join(map(dd, msgs)))


@click.group()
def cli():
    pass


@cli.command()
def login():
    app = get_app()
    app.login()
    click.echo(f"Logged in with user: {app.user.login}")


@cli.command()
@click.argument("WORDS", nargs=-1)
def say(words):
    echo(*words)


@cli.group()
def repos():
    pass


@repos.command()
@click.argument("pattern")
@click.option("--details/--no-details", default=False)
def ls(pattern, details):
    """List repositories matching PATTERN regular expression."""
    app = get_app()
    app.login()
    for repo in app.ls(pattern):
        click.echo(repo.name)
        if details:
            click.echo(repo.html_url)
            click.echo(repo.ssh_url)


@repos.command()
@click.argument("name")
def new(name):
    """Create a private repository with the given NAME."""
    app = get_app()
    app.login()
    if not click.confirm(f"Create a new repository named {repr(name)}?"):
        click.echo("Okay nevermind")

    created_repo = app.new_repo(name)
    click.echo(
        dd(
            f"""
                Created!
                HTML URL: {created_repo.html_url}
                Clone URL: {created_repo.clone_url}
            """
        )
    )


@cli.group()
def game():
    pass


@game.command()
@click.option(
    "--path",
    default="./game.yaml",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
def load(path):
    """Load a game definition."""
    with open(path) as f:
        click.echo(f"Len: {len(f.readlines())}")


if __name__ == "__main__":
    cli()
