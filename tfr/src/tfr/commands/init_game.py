from tfr.app import get_app

from .base import cli, click


@cli.command("init")
@click.option(
    "--root",
    default=".",
    type=click.Path(exists=True, file_okay=False, readable=True, writable=True),
    prompt=False,
)
@click.option("--name", prompt=False)
@click.option("--gm", help="Game Master username", prompt=False)
@click.option(
    "--players", help="Comma-separated list of player usernames (GitHub)", prompt=False
)
def init_game(root: str, name: str | None, gm: str | None, players: str | None):
    click.echo("what")
    player_usernames = players.split(",") if players else []

    app = get_app()
    app.init_game(
        #
        root_dir=root,
        name=(name or ""),
        gm_username=(gm or ""),
        player_usernames=player_usernames,
    )
