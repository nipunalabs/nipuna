from yaml import safe_load, dump
import os

class YAMLHandler:
    def __init__(self):
        pass

    def read_yaml_configs(self, project_name):
        yaml_config_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"utils/samples/sample.yaml")

        open_yaml = open(yaml_config_file, "r")
        parse_yaml = safe_load(open_yaml)
        parse_yaml['project_name'] = project_name
        return parse_yaml
    
    def generate_assets(self, project_name):
        yaml_payload = self.read_yaml_configs(project_name)

        try:
            project_path = os.path.join(os.getcwd(), project_name)
            print(project_path)
            if not os.path.exists(project_path):
                os.mkdir(project_path)
                os.chdir(project_path)
                with open('{}.yaml'.format(project_name), 'w') as file:
                    dump(yaml_payload, file)
        except:
            print("Please pass valid project name in config")
        return "Generated Protect Utils"
    