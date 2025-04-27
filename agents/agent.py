class Agent:
    def __init__(self, name, model_config):
        self.name = name
        self.model = model_config['model']
        self.api_key = model_config['api_key']
        self.api_type = model_config['api_type']

    def run(self, input_text):
        raise NotImplementedError("Each Agent must implement its own run() method.")


    def __str__(self):
        return f"{self.name} (Model: {self.model})"


#  Testing Examples if everything is working!
from agent import Agent
from  config_loader  import load_config, get_model_config
config = load_config()
model_config = get_model_config(config, "gemini-1.5-flash")
agent = Agent("Researcher Agents", model_config)
print(agent)
