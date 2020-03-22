from textwrap import dedent as dd

import click

from .app import get_app


def echo(*msgs):
    """
    Handles lines and indentation!

        cli.echo(
           '''
              line
                 indented
           ''',
           'inline',
           '   inline indented',
           '''
           different indent
           '''
        )

    Output:
        line
              indented

        inline
           inline indented

        different indent
    """
    click.echo(str.strip(dd("\n".join(msgs))))


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


@cli.group()
@click.option(
    "--path",
    default="./game.yaml",
    type=click.Path(exists=True, dir_okay=False, readable=True),
)
@click.pass_obj
def game(app, path):
    app.load_game(path)


@game.command()
@click.pass_obj
def info(app):
    """Load a game definition."""
    echo(
        f"""
        {'Name ':-<15} {app.game.name}
        {'Id ':<15} {app.game.id}
        {'GM ':-<15} {app.game.gm.name}
        {'Players # ':<15} {len(app.game.players)}
        {'Apps ':-<15} {', '.join(app.name for app in app.game.apps)}
        """
    )


if __name__ == "__main__":
    cli()
