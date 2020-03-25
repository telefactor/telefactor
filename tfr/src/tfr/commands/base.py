import click

from tfr.app import get_app
from tfr.constants import PATHS
from .io_utils import echo, echo_info, definition_list


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
    echo(
        definition_list(
            (
                ("Name", app.game.name),
                ("Id", app.game.id),
                ("GM", app.game.gm.name),
                ("Apps", ",".join(app.name for app in app.game.apps)),
                ("Num Players", len(app.game.players)),
                ("Num Repos", len(app.game.repositories)),
            )
        )
    )


@game.command()
@click.pass_obj
def fetch_metadata(app):
    echo_info("Loading all repos...")
    app.get_repos()
    echo_info("Game time.")

    changed_count = 0
    for local in app.game.repositories:
        remotes = app.ls(local.id)
        if not remotes:
            echo_info(f"No remote for {local.id}")
            continue

        remote = remotes[0]
        echo_info(f"Found {remote.name} for {local.id}")

        incoming_metadata = {
            "id": remote.id,
            "name": remote.name,
            "full_name": remote.full_name,
            "html_url": remote.clone_url,
            "clone_url": remote.clone_url,
            "ssh_url": remote.ssh_url,
            "isPrivate": remote.private,
        }
        if local.metadata == incoming_metadata:
            echo_info("No difference.")
            continue

        if local.metadata:
            echo_info("Original metadata:", local.metadata)
            echo_info("Incoming metadata:", incoming_metadata)

        local.metadata = incoming_metadata
        changed_count += 1

    if changed_count < 1:
        echo_info("Nothing changed.")
        return

    echo_info("Writing changes to game file:", app.game_path)
    app.save_game()


@game.command()
@click.pass_obj
def publicize(app):
    for local, remote in app.iter_locals_remotes():
        echo_info(f"Making {remote.name} public.")
        remote.edit(private=False)


@game.command()
@click.pass_obj
def links(app):
    echo(f"|name|url|")
    echo(f"|--  |-- |")
    for local in app.game.repositories:
        name = local.metadata["name"]
        html_url = local.metadata["html_url"]
        echo(f"|{name} |{html_url}|")


if __name__ == "__main__":
    cli()
