# 🔬 Agno Deep Research - Alternativa OpenSource ao Deep Research

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)
![Agno](https://img.shields.io/badge/agno-v1.5.10+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Sobre o Projeto

**Agno Deep Research** é uma alternativa **100% gratuita e open-source** ao Deep Research da OpenAI. Este agente inteligente utiliza o framework **Agno** para realizar pesquisas profundas na internet e gerar relatórios estruturados com fontes verificadas.

### ✨ Principais Características:

- 🔍 **Pesquisa Inteligente**: Utiliza Tavily para buscar informações atualizadas na web
- 📊 **Relatórios Estruturados**: Gera relatórios em markdown com fontes e referências
- 💾 **Memória Persistente**: Salva histórico de conversas e aprende com interações
- 🎮 **Interface Flexível**: Use via playground web, interface local ou terminal
- ⚡ **Rápido e Eficiente**: Respostas em segundos com qualidade profissional
- 🔧 **Totalmente Customizável**: Adapte o prompt e comportamento às suas necessidades

## 🛠️ Tecnologias Utilizadas

- **[Agno](https://agno.com)**: Framework para criação de agentes IA
- **[Tavily](https://tavily.com)**: API de pesquisa web inteligente
- **OpenAI GPT-4o-mini**: Modelo de linguagem para análise e síntese
- **SQLite**: Armazenamento local de sessões e histórico
- **FastAPI**: Backend para a API do agente
- **React**: Interface web (Agent UI)

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.12+
- Node.js 18+ (para interface web)
- Conta na [OpenAI](https://platform.openai.com/api-keys) (API Key)
- Conta na [Tavily](https://app.tavily.com/sign-up) (API Key gratuita)

### 1. Clone o Repositório

```bash
git clone https://github.com/rtadewald/Agno-Deep-Research.git
cd agno-deep-research
```

### 2. Instale o UV (Gerenciador de Dependências)

```bash
pip install uv
```

### 3. Instale as Dependências

```bash
uv sync
```

### 4. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# OpenAI API Key (obrigatória)
OPENAI_API_KEY=sk-sua-chave-da-openai-aqui

# Tavily API Key (obrigatória)
TAVILY_API_KEY=tvly-sua-chave-da-tavily-aqui
```

**Como obter as chaves:**
- **OpenAI**: Acesse [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Tavily**: Acesse [app.tavily.com/sign-up](https://app.tavily.com/sign-up) (gratuito)

## 🎮 Como Usar

### Opção 1: 🌐 Playground Web (Recomendado)

1. **Inicie o servidor:**
```bash
uv run researcher.py
```

2. **Configure um túnel público** (necessário para conectar ao playground online):

**Com ngrok** (recomendado):
```bash
# Baixe ngrok em: https://ngrok.com/download
ngrok http 8000
```

**Com Cloudflare Tunnel:**
```bash
# Instale cloudflared e execute:
cloudflared tunnel --url http://localhost:8000
```

3. **Acesse o playground** usando a URL gerada pelo túnel:
   - Copie a URL HTTPS (ex: `https://abc123.ngrok-free.app`)
   - Acesse: `https://app.agno.com/playground?endpoint=SUA_URL_AQUI`

### Opção 2: 💻 Interface Local

1. **Inicie o servidor do agente:**
```bash
uv run researcher.py
```

2. **Em outro terminal, inicie a Agent UI:**
```bash
cd agent-ui

npm i

npm run dev
```

3. **Acesse:** http://localhost:3000

### Opção 3: 🖥️ Terminal

Para testes rápidos ou integração em scripts:

```python
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

researcher = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[TavilyTools()],
    instructions="Pesquise na web e forneça um relatório detalhado com fontes."
)

# Use o agente
researcher.print_response("Pesquise sobre inteligência artificial em 2024")
```

## 📝 Exemplos de Uso

### Pesquisa Rápida
```
Faça uma pesquisa rápida sobre blockchain e criptomoedas
```

### Pesquisa Profunda
```
Quero uma pesquisa profunda sobre mudanças climáticas. 
Foque em: impactos ambientais, políticas públicas e soluções tecnológicas.
```

### Análise de Mercado
```
Pesquise sobre o mercado de carros elétricos no Brasil em 2024.
Inclua dados de vendas, principais players e perspectivas futuras.
```

## 📊 Estrutura do Projeto

```
agno-deep-research/
├── researcher.py          # Arquivo principal do agente
├── pyproject.toml         # Configurações do projeto Python
├── uv.lock               # Lock file das dependências
├── .env                  # Variáveis de ambiente (criar)
├── tmp/                  # Banco de dados SQLite (auto-criado)
├── agent-ui/             # Interface web React
└── README.md             # Este arquivo
```


## 📚 Quer Aprender Mais?

### 🎓 [Trilha Aplicações IA com Python - Asimov Academy](https://asimov.academy/trilha-aplicacoes-ia-com-python/)

Aprenda a criar aplicações completas de IA:

- 🤖 **Fundamentos de IA**: Conceitos essenciais e teoría
- 🐍 **Python Avançado**: Programação profissional
- 🔧 **Frameworks Modernos**: Agno, LangChain, Streamlit
- 📊 **Projetos Práticos**: Do básico ao avançado
- 🚀 **Deploy em Produção**: AWS, Docker, APIs

**Por que nossa trilha?**
- ✅ Conteúdo sempre atualizado
- ✅ Projetos reais de mercado
- ✅ Mentoria personalizada
- ✅ Certificado reconhecido
- ✅ Comunidade ativa no Discord

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🙏 Agradecimentos

- [Agno](https://agno.com) - Framework excepcional para agentes IA
- [Tavily](https://tavily.com) - API de pesquisa web inteligente
- [OpenAI](https://openai.com) - Modelos de linguagem GPT
- Comunidade Python e open-source

---

⭐ **Se este projeto foi útil, considere dar uma estrela no GitHub!**

📧 **Dúvidas?** Abra uma [issue](https://github.com/seu-usuario/agno-deep-research/issues) ou entre em contato!

🔗 **Links Úteis:**
- [Documentação do Agno](https://docs.agno.com)
- [Documentação da Tavily](https://docs.tavily.com)
- [OpenAI API Reference](https://platform.openai.com/docs)
