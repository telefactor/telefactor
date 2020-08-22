import typing as t

from tfr import data_utils, game_store

from .base import cli, click
from .io_utils import echo_info


@cli.command("init")
@click.option("--name", prompt=True)
@click.option("--players")
@click.option(
    "--path",
    default="./game.yaml",
    type=click.Path(exists=False, dir_okay=False, readable=True),
    prompt=True
)
def init_game(name: str, players: t.List[str], path: str):
    id = data_utils.name_to_id(name)

    player_names = players.split(',')
    if len(player_names) < 1:
        while player_name := click.prompt("Add player:") is not "":
            player_names.append(player_name)

    echo_info("Add players")

    game = game_store.Game(
        name=name, id=id, gm=None, players=player, apps=[], repositories=[]
    )
    game_store.save("./game.yaml", game)


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
