# server.py
import sys
import os
from mcp.server.fastmcp import FastMCP

# Import our tools
from src.tools.get_today_tasks import get_today_tasks

# Add debug logging
print(f"Starting MCP server from {__file__}", file=sys.stderr)
print(f"Python path: {sys.executable}", file=sys.stderr)
print(f"Current directory: {os.getcwd()}", file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Todoist MCP")

# Add our Todoist get tasks tool
@mcp.tool()
def todoist_get_today_tasks() -> str:
    """
    Fetch all tasks due today from Todoist
    
    This tool will connect to your Todoist account and retrieve all tasks
    that are due today. It requires a valid Todoist API token set in the
    TODOIST_API_TOKEN environment variable.
    
    Returns:
        A formatted list of today's tasks
    """
    return get_today_tasks()


# Start the server when this script is run directly
if __name__ == "__main__":
    print("Server initialized, starting now...", file=sys.stderr)
    mcp.run()