from textwrap import dedent as dd

import click

from .app import get_app


def echo(*msgs):
    click.echo("\n".join(map(dd, msgs)))


@click.group()
@click.pass_context
def cli(ctx):
    app = get_app()
    app.login()
    ctx.obj = app


@cli.command()
@click.pass_obj
def login(app):
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
@click.pass_obj
def ls(app, pattern, details):
    """List repositories matching PATTERN regular expression."""
    for repo in app.ls(pattern):
        click.echo(repo.name)
        if details:
            click.echo(repo.html_url)
            click.echo(repo.ssh_url)


@repos.command()
@click.argument("name")
@click.pass_obj
def new(app, name):
    """Create a private repository with the given NAME."""
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
@click.pass_obj
def load(app, path):
    """Load a game definition."""
    app.load_game(path)
    echo(app.game.name)


if __name__ == "__main__":
    cli()
