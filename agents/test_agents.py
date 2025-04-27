from config_loader import load_config, get_model_config
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent

config = load_config("config.json")
model_config = get_model_config(config, "gemini-1.5-pro")

# Initialize the ResearcherAgent
reseracher_agent = ResearcherAgent("Researcher", model_config)
writer = WriterAgent("Writer", model_config)
print("\n[Research Output]:\n")
result = reseracher_agent.run("Artificial Intelligence")
print(result)
print("\n[ResearcherAgent Test Completed]\n")
document = writer.run(result)
print("\n[Writer Output]:\n")
print(document)
print("\n[WriterAgent Test Completed]\n")