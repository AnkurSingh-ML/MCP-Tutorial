from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "math" : {
            "command" : "python",
            "args" : ["mathserver.py"],
            "transport" : "stdio"
        },
        "weather" : {
            "url" : "http://127.0.0.1:8000/mcp",
            "transport" : "streamable_http"
        }
    })

    tools = await client.get_tools()

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke({"messages" : [{"role": "user", "content": "What is (3+5) x 5?"},]})

    if "messages" in math_response:
        for convo in math_response["messages"]:
            convo.pretty_print()

    weather_response = await agent.ainvoke({"messages" : [{"role": "user", "content": "What is the weather in California?"},]})

    if "messages" in weather_response:
        for convo in weather_response["messages"]:
            convo.pretty_print()

asyncio.run(main())