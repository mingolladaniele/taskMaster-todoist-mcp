from ..api.todoist_api import TodoistAPI
from ..utils.formatter import TaskFormatter

def get_tasks(filter_param=None, filter_string=None, priority=None, project_id=None, label=None, limit=None) -> list:
    """
    Fetch tasks from Todoist with flexible filtering options
    
    Args:
        filter_param: Predefined simple filter ("today", "tomorrow", "overdue", "next_n_days:X")
        filter_string: Direct Todoist filter query string for advanced filtering
        priority: Priority level (1-4, where 1 is highest priority)
        project_id: Project ID to filter by project
        label: Label name to filter tasks
        limit: Maximum number of tasks to return
    
    Returns:
        list: List of tasks matching the criteria
    """
    try:
        # Initialize the Todoist API
        api = TodoistAPI()
        
        # Use filter_string directly if provided, otherwise use predefined filter_param
        if filter_string:
            tasks = api.get_tasks(
                filter_string=filter_string,
                project_id=project_id,
                label=label,
                limit=limit
            )
            
            # Apply priority filter if specified (client-side filtering)
            if priority:
                tasks = [task for task in tasks if task.get("priority") == priority]
        else:
            # Use the predefined filters
            tasks = api.get_tasks_by_filter(
                filter_param=filter_param,
                priority=priority,
                project_id=project_id,
                label=label,
                limit=limit
            )
        
        # Format the tasks for display
        formatted_tasks = TaskFormatter.format_task_list(tasks)
        
        return formatted_tasks
    
    except Exception as e:
        return f"Error fetching tasks: {str(e)}"