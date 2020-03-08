import click


from . import secrets


@click.group()
def cli():
    pass


@cli.command()
def login():
    secs = secrets.load_secrets()
    token = secs["github"]["access_token"]
    click.echo(f"Your access token is {len(token)} chars long.")

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
