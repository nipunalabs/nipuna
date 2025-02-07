from yaml import safe_load, dump
import os

class YAMLHandler:
    def __init__(self):
        pass

    def read_yaml_configs(self, path):

        open_yaml = open(path, "r")
        parse_yaml = safe_load(open_yaml)
        return parse_yaml
    
    def generate_assets(self, path):
        yaml_payload = self.read_yaml_configs(path)
        project_name = yaml_payload['project_name']
        try:
            project_path = os.path.join(os.getcwd(), project_name)
            print(project_path)
            if not os.path.exists(project_path):
                os.mkdir(project_path)
        except:
            print("Please pass valid project name in config")
        return yaml_payload