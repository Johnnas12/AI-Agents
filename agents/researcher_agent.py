from agent import Agent


class ResearcherAgent(Agent):
    def run(self, topic):
        print(f"[{self.name}], Researching topic: {topic}") 

        # Simple simulation of research
        research_results = self.perform_research(topic)
        return research_results

        
    def perform_research(self, topic):
        # mock research results to be returned
        mock_results =  f"Gathered research on {topic}: \n" 
        return mock_results