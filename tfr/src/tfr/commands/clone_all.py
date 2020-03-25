from .base import game, click
from .io_utils import echo, echo_info, definition_list


@game.command()
@click.pass_obj
def clone_all(app):
    echo("app.game_path.")
