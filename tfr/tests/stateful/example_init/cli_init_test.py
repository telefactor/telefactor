from click.testing import CliRunner

from tfr import commands


class DescribeCliInit:
    # @pytest.fixture
    # def game(self):

    # with runner.isolated_filesystem():

    def it_inits(self):
        runner = CliRunner()
        result = runner.invoke(commands.init_game, [])
        print(result.output)
        assert result.exit_code == 0
        assert result.output == "Hello World!\n"
