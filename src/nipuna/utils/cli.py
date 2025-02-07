import click
from components.API_handler import start_components

@click.group()
def cli():
    """kriopy cli"""
    pass

@click.command()
@click.argument("start")
def cli(start):
    start_components()