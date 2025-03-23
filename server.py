# server.py
import sys
import os
from mcp.server.fastmcp import FastMCP

# Add debug logging
print(f"Starting MCP server from {__file__}", file=sys.stderr)
print(f"Python path: {sys.executable}", file=sys.stderr)
print(f"Current directory: {os.getcwd()}", file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} + {b}", file=sys.stderr)
    return a + b


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print(f"Getting greeting for {name}", file=sys.stderr)
    return f"Hello, {name}!"


# Start the server when this script is run directly
if __name__ == "__main__":
    print("Server initialized, starting now...", file=sys.stderr)
    mcp.run()