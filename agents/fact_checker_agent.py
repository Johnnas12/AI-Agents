from agent import Agent
import google.generativeai as genai

class FactCheckerAgent(Agent):
    def run(self, research_text, document_text):
        print(f"[{self.name}] Fact-checking research document ...")

        fact_check_results = self.check_facts(research_text, document_text)

        return fact_check_results
    
    def check_facts(self, research_text, document_text):
        genai.configure(api_key = self.api_key)
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
        return fact_check_text
    
