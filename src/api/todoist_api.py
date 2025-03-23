import requests
from ..config.config import Config
from ..utils.formatter import TaskFormatter

class TodoistAPI:
    """Wrapper for the Todoist REST API"""
    
    BASE_URL = "https://api.todoist.com/rest/v2"
    
    def __init__(self):
        self.token = Config.get_api_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def get_tasks(self, filter_string: str, priority: int = None) -> list:
        """Get tasks with flexible filtering options using Todoist's native filtering
        
        Args:
            filter_string: Todoist filter query string (e.g., "today", "overdue", 
                           "p1", "p1 & today", etc.)
            
        Returns:
            List of filtered task objects
        """
        url = f"{self.BASE_URL}/tasks"
        
        # Add API parameters for supported filters
        params = {}
        if filter_string:
            params["filter"] = filter_string
        
        # Make the API request with filters
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code != 200:
            raise Exception(f"Failed to get tasks: {response.status_code} - {response.text}")
        
        tasks = response.json()

        if priority:
            tasks = [task for task in tasks if task.get("priority") == priority]
        
        # Format the tasks for display
        formatted_tasks = TaskFormatter.format_task_list(tasks)
                
        return formatted_tasks