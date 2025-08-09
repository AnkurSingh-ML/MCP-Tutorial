from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the Weather information for a specific location.
    """
    return "It's always Sunny in " + location

if __name__ == "__main__":
    mcp.run(transport="streamable-http")