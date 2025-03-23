import pytest

from tfr import game_store


class DescribeNormer:
    @pytest.fixture
    def game(self):
        gm = {"name": "George Masterson", "username": "gm-gm"}
        pj = {"name": "Paul Jorts", "username": "pj-pj"}
        dj = {"name": "Dan Jager", "username": "dj-dj"}

        killbot = {"name": "Killbot", "id": "id-killbot"}

        return game_store.normer(
            data={
                "name": "dat-game-doh",
                "id": "eye dee",
                "gm": gm,
                "players": [gm, pj, dj],
                "apps": [killbot],
            }
        )

    def it_constructs_game(self, game):
        assert isinstance(game, game_store.Game)

    def it_assigns_nested_values(self, game):
        for field, typ in (
            ("gm", game_store.User),
            ("players", list),
            ("apps", list),
        ):
            assert isinstance(getattr(game, field), typ)
