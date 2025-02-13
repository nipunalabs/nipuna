import click
from .backend.api_handler import start_components
from .backend.utils.config_handler import YAMLHandler

@click.group()
def nipuna():
    """Nipuna cli"""
    pass

@nipuna.command()
def start():
    start_components()

@nipuna.command()
@click.argument("project_name")
def create(project_name):
    print(project_name)
    config_handler = YAMLHandler()
    config_handler.generate_assets(project_name=project_name)

if __name__ == '__main__':
    nipuna()
