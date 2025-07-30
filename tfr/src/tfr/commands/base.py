import click
from tfr.app import get_app


@click.group()
@click.pass_context
def cli(ctx, secrets_path):
    tfr = get_app()
    ctx.obj = tfr


if __name__ == "__main__":
    cli()
