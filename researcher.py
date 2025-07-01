from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from dotenv import load_dotenv
load_dotenv()

researcher = Agent(
    name="Researcher",
    agent_id="researcher-agent",
    model=OpenAIChat(id="gpt-4.1-mini"),
    tools=[TavilyTools()],
    storage=SqliteStorage(
        table_name="researcher_sessions", 
        db_file="tmp/researcher.db", 
        auto_upgrade_schema=True
    ),
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
    """,
    add_history_to_messages=True,
    add_datetime_to_instructions=True,
    num_history_responses=5,
    markdown=True,
    show_tool_calls=True,
)

playground = Playground(
    agents=[researcher],
    name="Research Playground",
    description="Um playground para pesquisa avançada na internet",
    app_id="research-playground"
)
app = playground.get_app()

if __name__ == "__main__":
    playground.serve(app="researcher:app", reload=True, port=7777, host="localhost")