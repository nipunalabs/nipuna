import json
import click
import ast
from ..backend.api.api_handler import start_components
from ..backend.utils.config_handler import YAMLHandler
from ..backend.utils.model_handler import ModelHandler
from ..workflow.chaining import WorkflowChaining
@click.group()
def nipuna():
    """Nipuna cli"""
    pass

@nipuna.command()
def start():
    start_components()

@nipuna.command()
@click.argument("workflow_name")
def create(workflow_name):
    config_handler = YAMLHandler(project_name=workflow_name)
    config_handler.generate_assets()

@nipuna.command()
@click.argument("start")
@click.option("--file_path")
def start(start, file_path):
    chains = WorkflowChaining(project_name=start, file_path=file_path)
    print(chains.chain())
    # model = ModelHandler(project_name=start, file_path=file_path)
    # model.trigger_model()



if __name__ == '__main__':
    nipuna()
