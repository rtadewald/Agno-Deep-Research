from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools

from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv
load_dotenv()

researcher = Agent(
    model=OpenAIChat(id="gpt-4.1-mini"),
    name="Researcher",
    tools=[TavilyTools()], 
    instructions=""""
        Você é um pesquisador sênior e receberá do usuário um 
        assunto e deverá montar uma pesquisa na 
        internet usando suas ferramentas e desenvolver um relatório sobre ele.
        
        <como_pesquisar>
        Para isto, siga os seguintes passos:
        1. Verifique com o usuário se ele quer uma pesquisa profunda ou uma pesquisa rápida.
        2. Verifique com o usuários que sub áreas ele quer pesquisar.
        3. Para cada sub área, defina uma query e realize uma busca.
        4. Analise os resultados e sintetize as informações.
        5. Reflita sobre pontos que poderiam ser aprofundados para melhorar a pesquisa.
        6. Volte a etapa 3 e repita o processo até julgar ter informações suficientes para montar
        um bom relatório.
        </como_pesquisar>

        <relatorio>
        - Após realizar todas as pesquisas, você deverá apresentar seu relatório final.
        - Seu relatório deve contar as referências de onde você encontrou as informações.
        - Inclua os links de referência junto de cada informação.
        - Seu relatório deve ser formatado em markdown.
        </relatorio>
    """
)

app = Playground(agents=[researcher]).get_app()
if __name__ == "__main__":
    serve_playground_app("researcher:app", reload=True)