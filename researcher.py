from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.playground import Playground, serve_playground_app
import yaml

from dotenv import load_dotenv
load_dotenv()


prompt = yaml.safe_load(open("prompts/researcher.yaml"))
researcher = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="Researcher",
    tools=[TavilyTools()], 
    description=prompt["description"],
    instructions=prompt["instructions"]
)


app = Playground(agents=[researcher]).get_app()

if __name__ == "__main__":
    serve_playground_app("researcher:app", reload=True)
