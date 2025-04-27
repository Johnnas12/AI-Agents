from config_loader import load_config, get_model_config
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent
from fact_checker_agent import FactCheckerAgent

config = load_config("config.json")
model_config = get_model_config(config, "gemini-1.5-pro")

# Initialize the ResearcherAgent
reseracher_agent = ResearcherAgent("Researcher", model_config)
writer = WriterAgent("Writer", model_config)
fact_checker = FactCheckerAgent("FactChecker", model_config)



print("\n[Research Output]:\n")
result = reseracher_agent.run("Artificial Intelligence in Healthcare")
print(result)
print("\n[ResearcherAgent Test Completed]\n")


document = writer.run(result)
print("\n[Writer Output]:\n")
print(document)
print("\n[WriterAgent Test Completed]\n")

max_round = 4
current_round = 1
fact_check_result = ""

while current_round <= max_round:
    print(f"\n--- Round {current_round} ---\n") 
    fact_check_result = fact_checker.run(result, document)
    print(f"\n[Fact-Checker Feedback]:\n{fact_check_result}")

    if "No issues found." in fact_check_result:
        print("\n✅ No issues found — final document is verified.")
        break
    
    document = writer.revise_document(document, fact_check_result)
    print(f"\n[Updated Document]:\n{document}")

    current_round += 1
if current_round > max_round:
    print("\n⚠️ Maximum rounds reached. Please review the document manually.")
writer.save_to_docx(document, "final_report.docx")



