from config_loader import load_config, get_model_config
from researcher_agent import ResearcherAgent
from writer_agent import WriterAgent
from fact_checker_agent import FactCheckerAgent
from db_manager import DatabaseManager

db_manager = DatabaseManager('agents_memory.db')
config = load_config("config.json")
model_config = get_model_config(config, "gemini-1.5-pro")

# Initialize the ResearcherAgent
reseracher_agent = ResearcherAgent("Researcher", db_manager, model_config)
writer = WriterAgent("Writer", db_manager, model_config)
fact_checker = FactCheckerAgent("FactChecker", db_manager, model_config)

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


stored_research = db_manager.get_context("research_text")
stored_document = db_manager.get_context("document_text")
stored_fact_check = db_manager.get_context("fact_check_text")

print("\n📌 Stored Research Text:\n", stored_research)
print("\n📌 Stored Document Text:\n", stored_document)
print("\n📌 Stored Fact-Check Result:\n", stored_fact_check)


while True:
    user_input = input("\n👤 You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting session.")
        break

    if "previously" in user_input.lower() and "talking about" in user_input.lower():
        # Retrieve stored context from DB
        stored_research = db_manager.get_context("research_text")
        stored_document = db_manager.get_context("document_text")
        stored_fact_check = db_manager.get_context("fact_check_text")

        if stored_research:
            print("\n📝 Previously, we were discussing a research topic on:")
            print(f"➡️ {stored_research[:300]}...")  
            print("\n📝 The drafted document was about:")
            print(f"➡️ {stored_document[:300]}...")

            print("\n📝 Fact-checker's last feedback was:")
            print(f"➡️ {stored_fact_check[:300]}...")

        else:
            print("\n⚠️ No previous conversation context found.")

    else:
        print("🤖 Sorry, I can only recall the last discussion if you ask 'previously what we were talking about'. Type 'exit' to quit.")