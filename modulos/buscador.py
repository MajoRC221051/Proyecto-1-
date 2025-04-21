import os
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.tools.tavily_search import TavilySearchResults

class BuscadorWeb:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-4")
        self.tavily_tool = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"))
        self.agent = initialize_agent(
            [
                Tool(
                    name="Tavily",
                    func=self.tavily_tool.run,
                    description="Herramienta de búsqueda Tavily"
                )
            ],
            self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )

    def buscar(self, tema):
        return self.agent.run(f"Busca información actualizada sobre: {tema}")

