from tfr import data_utils, game_store
from tfr.io_utils import echo_info

from .base import cli, click


@cli.command("init")
@click.option("--name", prompt=True)
@click.option("--players", help="Comma-separated list of player names", prompt=True)
@click.option(
    "--path",
    default="./game.yaml",
    type=click.Path(exists=False, dir_okay=False, readable=True),
    prompt=True,
)
@click.option("--apps", help="Comma-separated list of player names", prompt=True)
def init_game(name: str, players: str, path: str):
    id = data_utils.name_to_id(name)

    player_names = [n for n in players.split(",") if len(n)]

    game = game_store.Game(
        name=name, id=id, gm=None, players=player_names, apps=[], repositories=[]
    )
    game_store.save(path, game)
    echo_info("New game at", path)


# @game.command("init")
# def init_game():
#     # steps = Steps(["Name your game", "Add players"])
#     echo_info("Name your game")
#     name = click.prompt("name")
#     id = data_utils.name_to_id(name)

#     echo_info("Add players")
#     name = click.prompt("name")

#     game = game_store.Game(
#         name=name, id=id, gm=None, players=[], apps=[], repositories=[]
#     )
#     game_store.save("./game.yaml", game)
