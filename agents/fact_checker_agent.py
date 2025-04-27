from agent import Agent
import google.generativeai as genai
from db_manager import DatabaseManager

class FactCheckerAgent(Agent):
    def __init__(self, name, db_manager: DatabaseManager, model_config):
        super().__init__(name, db_manager, model_config)
        self.db_manager = db_manager
        self.model = model_config["model"]
        self.api_key = model_config["api_key"]
        self.db_manager.create_tables()

    def run(self, research_text, document_text):
        print(f"[{self.name}] Fact-checking research document ...")

        fact_check_results = self.check_facts(research_text, document_text)

        return fact_check_results

    def check_facts(self, research_text, document_text):
        previous_research = self.db_manager.get_context("research_text")
        previous_document = self.db_manager.get_context("document_text")

        if not previous_research:
            self.db_manager.save_context("research_text", research_text)
        if not previous_document:
            self.db_manager.save_context("document_text", document_text)

        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model)

        prompt = f"""You are a technical fact-checker. Carefully review the following technical document against the provided research findings.
Identify any factual inaccuracies, contradictions, or unverifiable claims in the document, and suggest corrections if needed.
Document:
{document_text}

Original Research:
{research_text}

Return your findings as a markdown list of issues and proposed corrections.
If everything looks fine, simply reply with: 'No issues found.'
"""

        response = model.generate_content(prompt)
        fact_check_text = response.candidates[0].content.parts[0].text

        self.db_manager.save_context("fact_check_text", fact_check_text)
        self.db_manager.log_interaction(self.name, "Fact-check", fact_check_text)

        return fact_check_text
