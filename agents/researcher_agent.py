from agent import Agent
import google.generativeai as genai

class ResearcherAgent(Agent):
    def run(self, topic):
        print(f"[{self.name}], Researching topic: {topic}") 
        research_results = self.perform_research(topic)
        return research_results

        
    def perform_research(self, topic):
        # This is where the actual research would be performed.
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model)

        prompt = f"Research and provide a concise technical overview about: {topic}"
        response = model.generate_content(prompt)
        research_text = response.candidates[0].content.parts[0].text

        return research_text