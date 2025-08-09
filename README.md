# 🧠 MCP with LangChain

This project demonstrates how to integrate **Model Context Protocol (MCP)** with [LangChain](https://www.langchain.com/) to enable AI models to interact with custom tools, data sources, and workflows.

With MCP, you can define **tools** that your LLM can call dynamically — LangChain acts as the orchestration layer to handle these tool calls and combine them with LLM reasoning.

---

## 📌 Features

- **MCP Server** for exposing custom tools via MCP
- **LangChain Agent** that uses these tools to process queries
- Example integration with `TavilySearch` and a `human_assistance` tool
- Designed to be extended with more MCP-compliant tools

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo>.git](https://github.com/AnkurSingh-ML/MCP-Tutorial.git)
cd MCP-Tutorial
```
## 2. Create Virtual Environment
Install UV Package Manager. <br>
Create a Virtual Environment.<br>
Activate the Virtual Environment.<br>
Install the dependencies.<br>
```bash
pip install uv
uv venv
.venv\Scripts\activate  # On Windows
source .venv/bin/activate  # On Mac/Linux
uv pip -r requirements.txt
```
### 3. Create .env file with Groq API Key
```bash
GROQ_API_KEY="your_groq_api_key_here"
```
### 4. Start the MCP Servers in different Terminals
```bash
python mathserver.py
python weatherapi.py
```
### 5. Start the MCP Client
```bash
python client.py
```
