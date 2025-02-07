import click
from backend.handler import start_components

@click.group()
def cli():
    """kriopy cli"""
    pass

@click.command()
@click.argument("start")
def cli(start):
    start_components()

if __name__ == '__main__':
    cli()