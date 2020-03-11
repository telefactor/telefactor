import click

from .app import get_app


@click.group()
def cli():
    pass


@cli.command()
def login():
    app = get_app()
    app.login()
    click.echo(f"Logged in with user: {app.user.login}")


@cli.group()
def repos():
    pass


@repos.command()
@click.argument("pattern")
def ls(pattern):
    """List repositories matching PATTERN regular expression."""
    app = get_app()
    app.login()
    for repo in app.ls(pattern):
        click.echo(repo.name)


@repos.command()
@click.argument("repo_name")
def new(repo_name):
    """Create a private repository with the given REPO_NAME."""
    app = get_app()
    app.login()
    app.new_repo(repo_name)


if __name__ == "__main__":
    cli()
