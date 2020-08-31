from tfr import game_store
from tfr.io_utils import echo_info

from .base import cli, click


@cli.command("init")
@click.option(
    "--path",
    default="./tfr.yaml",
    type=click.Path(exists=False, dir_okay=False, readable=True),
    prompt=True,
)
@click.option("--name", prompt=True)
@click.option("--players", help="Comma-separated list of player usernames (GitHub)", prompt=True)
@click.option("--gm", help="Game master username", prompt=True)
def init_game(path: str, name: str, players: str, gm: str):
    gm_user = game_store.User(username=gm, name=gm)
    # Create user objects from unique player ids.
    player_users = [
        game_store.User(username=username, name=username)
        for username in set(n for n in players.split(",") if len(n))
    ]

    game = game_store.Game(
        name=name,
        gm=gm_user,
        players=player_users,
        apps=[],
        repositories=[]
    )
    game_store.save(path, game)
    echo_info("New game at", path)
