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
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
