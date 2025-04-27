class Agent:
    def __init__(self, name, db_manager, model_config):
        self.name = name
        self.db_manager = db_manager
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
from db_manager import DatabaseManager
config = load_config()
db_manager = DatabaseManager('agent_memory.db')
model_config = get_model_config(config, "gemini-1.5-flash")
agent = Agent("Researcher Agents", db_manager, model_config)
print(agent)
