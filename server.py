# server.py
import sys
import os
from mcp.server.fastmcp import FastMCP

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our tools
from src.tools import get_tasks

# Add debug logging
print(f"Starting MCP server from {__file__}", file=sys.stderr)
print(f"Python path: {sys.executable}", file=sys.stderr)
print(f"Current directory: {os.getcwd()}", file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Todoist MCP")

@mcp.tool()
def todoist_get_tasks(
    filter_param: str = None,
    filter_string: str = None,
    priority: int = None,
    project_id: str = None,
    label: str = None,
    limit: int = None
) -> list:
    """
    Fetch Todoist tasks with powerful filtering options
    
    This tool allows you to retrieve and filter tasks from Todoist using either
    simple predefined filters or Todoist's advanced filter syntax.
    
    Args:
        filter_param: Simple filter option ("today", "tomorrow", "overdue", "next_n_days:X")
        filter_string: Advanced Todoist filter query string for complex filtering
                      (e.g., "date: Jan 3", "date before: May 5", "overdue")
        priority: Priority level (1-4, where 1 is highest priority)
        project_id: Project ID to filter by project
        label: Label name to filter tasks
        limit: Maximum number of tasks to return
    
    Examples of filter_string:
        "today" - Tasks due today
        "overdue" - Overdue tasks
        "date: Jan 3" - Tasks due on January 3rd
        "date before: May 5" - Tasks due before May 5th
        "date after: May 5" - Tasks due after May 5th
        "date: 7 days" - Tasks due in the next 7 days
        "no date" - Tasks with no due date
    
    Returns:
        list: List of tasks matching the criteria
    """
    return get_tasks(
        filter_param=filter_param,
        filter_string=filter_string,
        priority=priority,
        project_id=project_id,
        label=label,
        limit=limit
    )


# Start the server when this script is run directly
if __name__ == "__main__":
    print("Server initialized, starting now...", file=sys.stderr)
    mcp.run()