import click

from .secrets import load_secrets


@click.group()
def cli():
    pass


@cli.command()
def login():
    secrets = load_secrets()
    token_len = len(secrets.github.access_token)
    click.echo(f"Your access token is {token_len} chars long.")


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option(
    "--name", prompt="Your name", help="The person to greet.",
)
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo("Hello %s!" % name)


if __name__ == "__main__":
    cli()
