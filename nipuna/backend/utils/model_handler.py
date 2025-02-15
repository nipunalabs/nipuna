
from ollama import chat, Client
from .config_handler import YAMLHandler

class ModelHandler:
    def __init__(self, project_name: str, file_path: str):
        self.project_name = project_name
        self.file_path = file_path
        # self.handler = YAMLHandler(project_name=self.project_name)
        # self.configs = self.handler.read_yaml_configs(self.file_path)

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
    
    def trigger_model(self,configs, workflow_configs):
        # workflow_configs = self.configs['WORKFLOW']
        # print(workflow_configs[0])
        
        config_model = workflow_configs[0].keys()
        model_from_config = workflow_configs[0][list(config_model)[0]]
        print(configs[model_from_config])


        if "image_path" not in configs[model_from_config]:
            task, client, model_name,role = configs[model_from_config].values()
            workflow_task_type, prompt,type = workflow_configs[0]
        else:
            task, client, model_name,role, image_path = configs[model_from_config].values()
            workflow_task_type, prompt, type = workflow_configs[0]


        model_dict = self.model_init(model_name=model_name)
        model = model_dict[client]

        if task == 'chat':
            model_resp = model.chat_with_model(role=role, content=prompt)
            model_resp
        elif task == 'image_analsis':
            model_resp = model.analyze_image(model=model_name, content=prompt, role=role, image_path=image_path)
        return model_resp

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
    
    def analyze_image(self, model: str, content: str, role: str, image_path: str):
        print("Generating response...")
        response = chat(
            model= model,
            messages=[
                {
                'role': role,
                'content': content,
                'images': [image_path],
                }
            ],
            )
        return response