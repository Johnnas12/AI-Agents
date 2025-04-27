from config_loader import load_config, get_model_config
from researcher_agent import ResearcherAgent

config = load_config("config.json")
model_config = get_model_config(config, "gemini-1.5-pro")

# Initialize the ResearcherAgent
reseracher_agent = ResearcherAgent("Researcher", model_config)

# test the run method
result = reseracher_agent.run("Artificial Intelligence")
print(result)
