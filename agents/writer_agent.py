from agent import Agent
import google.generativeai as genai

class WriterAgent(Agent):
    def run(self, research_text):
        print(f"[{self.name}] Drafting technical report ...")

        document = self.draft_report(research_text)
        return document
    
    def draft_report(self, research_text):

        genai.configure(api_key = self.api_key)
        prompt = f"""You are a technical writer. Using the following research text, organize it into a clear, properly structured, polished technical report in markdown format. Include a title, table of contents, headings, and a conclusion.
        Research Text:
        {research_text}
        """
        model = genai.GenerativeModel(self.model)  
        response = model.generate_content(prompt)

        report_text = response.candidates[0].content.parts[0].text
        return report_text