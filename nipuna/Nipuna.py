import typing
import os
from .backend.utils.config_handler import YAMLHandler
from .backend.utils.data_handler import DataHandler

class Nipuna():
    def __init__(self):
        self.yamlHandler = YAMLHandler()
        self.dataHandler = DataHandler()

    def init_inline(self):
        print("reading inline")

    def init_yaml(self, path: str):
        package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        yaml_path = os.path.join(package_dir, path)
        self.yamlHandler.generate_assets(yaml_path)

