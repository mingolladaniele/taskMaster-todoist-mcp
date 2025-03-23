from ..api.todoist_api import TodoistAPI
from ..utils.formatter import TaskFormatter

def get_today_tasks():
    """
    Fetch all tasks due today from Todoist
    
    Returns:
        str: Formatted list of tasks due today
    """
    try:
        # Initialize the Todoist API
        api = TodoistAPI()
        
        # Get tasks due today
        today_tasks = api.get_today_tasks()
        
        # Format the tasks for display
        formatted_tasks = TaskFormatter.format_task_list(today_tasks)
        
        return formatted_tasks
    
    except Exception as e:
        return f"Error fetching today's tasks: {str(e)}" 