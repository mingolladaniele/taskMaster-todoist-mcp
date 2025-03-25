# server.py
import sys
import os
from mcp.server.fastmcp import FastMCP

# Add src directory to path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our tools
from src.api.todoist_api import TodoistAPI

# Add debug logging
print(f"Starting MCP server from {__file__}", file=sys.stderr)
print(f"Python path: {sys.executable}", file=sys.stderr)
print(f"Current directory: {os.getcwd()}", file=sys.stderr)

# Create an MCP server
mcp = FastMCP("Todoist MCP")

# Initialize the Todoist API
api = TodoistAPI()

@mcp.tool()
def get_tasks_tool(
    filter_string: str,
    priority: int = None,
) -> list:
    """
    Fetch Todoist tasks
    
    This tool allows you to retrieve and filter tasks from Todoist using either
    simple predefined filters or Todoist's advanced filter syntax.
    
    Args:
        filter_string: English advanced Todoist filter query string for complex filtering
        priority: Priority level (1-4, where 1 is highest priority)
    
    Examples of filter_string:
        "Jan 3" - Tasks due on January 3rd
        "due before: May 5" - Tasks due before May 5th
        "due after: May 5" - Tasks due after May 5th
        "due before: +4 hours" - Tasks due within the next four hours and all overdue tasks
        "due before: next week" - Tasks due before the next week
        "due before: sat" - Tasks due in the current working week
        "(due: next week | due after: next week) & due before: 1 week after next week" - Tasks due next week
        "due before: first day" - Tasks due within the current calendar month
        "due: yesterday, today" - Tasks due yesterday and today
        "no date" - Tasks with no date or deadline
        "today & due before: today at 2pm" - Tasks due today before a specific time
        "overdue" - Tasks that are overdue
        "overdue & !no time, today & !no time" - Overdue tasks with assigned time, and today's tasks with time
        "#Inbox & no date, All & !#Inbox & !no date" - Inbox tasks without dates, followed by non-Inbox tasks with dates
        "5 days" or "next 5 days" - Tasks due within the next 5 days
        "recurring" - Tasks with a recurring date
        "!recurring" - Tasks that don't have a recurring date
        "no time & !recurring" - Tasks with a date but no time, which aren't recurring
    
    Returns:
        list: List of tasks matching the criteria
    """
    return api.get_tasks(
        filter_string=filter_string,
        priority=priority,
    )

@mcp.tool()
def create_task_tool(content: str, description: str = None, due_string: str = None, priority: int = 3) -> dict:
    """
    Create a new task in Todoist
    
    This tool creates a new task in Todoist with the given content and priority.

    Args:
        content: Task content. This value may contain markdown-formatted text and hyperlinks.
        description: A description for the task. This value may contain markdown-formatted text and hyperlinks.
        due_string: English human defined task due date (ex.: "next Monday", "Tomorrow"). Value is set using local (not UTC) time.
        priority: Task priority from 1 (normal) to 4 (urgent).
    
    Returns:
        dict: Return the response from the API call in JSON format.
    """
    return api.create_task(
        content=content,
        description=description,
        due_string=due_string,
        priority=priority
    )


# Start the server when this script is run directly
if __name__ == "__main__":
    print("Server initialized, starting now...", file=sys.stderr)
    mcp.run()