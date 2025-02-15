
from ollama import chat, Client
from .config_handler import YAMLHandler

class ModelHandler:
    def __init__(self, project_name: str, file_path: str):
        self.project_name = project_name
        self.file_path = file_path
        self.handler = YAMLHandler(project_name=self.project_name)
        self.configs = self.handler.read_yaml_configs(self.file_path)

    def model_init(self, model_name: str):
        # print(self.configs.keys())
        model_dict = {"ollama": OllamaHandler(model_name=model_name)}
        return model_dict
        
        # client, model_name,client_type, system = self.configs['custom_ollama'].values()
        # model_dict = {"ollama": OllamaHandler(model_name=model_name)}
        
        # model = model_dict[client]
        # model_ref = model.connect(client_type=client_type, system=system)
        # print(model_ref)
        # return model_ref
    
    def chat(self):
        workflow_configs = self.configs['WORKFLOW']
        client, model_name,role, content = self.configs[workflow_configs['model']].values()
        model_dict = self.model_init(model_name=model_name)
        model = model_dict[client]
        model_resp = model.chat_with_model(role=role, content=content)
        print(model_resp)

class OllamaHandler:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def connect_custom(self, client_type: str, system: str, enable_streaming: bool = False,port: str = 11434):
        model_client = Client(host='https://localhost:{}'.format(port))
        model_ref = model_client.create(
            model = client_type,
            from_=self.model_name,
            system=system,
            stream=enable_streaming
        )
        return model_ref
    
    def chat_with_model(self, content: str, role: str):
        print("Generating response...")
        messages = [
            {
                'role': role,
                'content': content
            }
        ]

        chat_resp = chat(model=self.model_name, messages=messages)
        return chat_resp