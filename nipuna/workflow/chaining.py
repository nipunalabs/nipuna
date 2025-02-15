from ..backend.utils.model_handler import ModelHandler
from ..backend.utils.config_handler import YAMLHandler

class WorkflowChaining:
    def __init__(self, project_name, file_path):
        self.project_name = project_name
        self.file_path = file_path

    def workflow_config(self):
        handler = YAMLHandler(project_name=self.project_name)
        configs = handler.read_yaml_configs(self.file_path)
        return configs
    
    def chain(self):
        configs = self.workflow_config()
        model_handler = ModelHandler(project_name=self.project_name, file_path=self.file_path)
        response = model_handler.trigger_model(configs, configs['WORKFLOW'])
        return response

