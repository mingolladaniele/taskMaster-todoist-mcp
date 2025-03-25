import requests
from ..config.config import Config
from ..utils.formatter import TaskFormatter

class TodoistAPI:
    """Wrapper for the Todoist REST API"""
    
    BASE_URL = "https://api.todoist.com/rest/v2"
    BASE_TASK_URL = f"{BASE_URL}/tasks"
    
    def __init__(self):
        self.token = Config.get_api_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def get_tasks(self, filter: str, priority: int = None) -> list:
        """Get tasks with flexible filtering options using Todoist's native filtering
        
        Args:
            filter: Todoist filter query string (e.g., "today", "overdue", 
                           "p1", "p1 & today", etc.)
            
        Returns:
            List of filtered task objects
        """
        url = self.BASE_TASK_URL
        
        # Add API parameters for supported filters
        params = {}
        if filter:
            params["filter"] = filter
        
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
        
    def create_task(self, content: str, description: str = None, due_string: str = None, priority: int = 1) -> dict:
        """Creates a new task in Todoist
        
        Args:
            content: Task content. This value may contain markdown-formatted text and hyperlinks.
            description: A description for the task. This value may contain markdown-formatted text and hyperlinks.
            due_string: Human defined task due date (ex.: "next Monday", "Tomorrow"). Value is set using local (not UTC) time.
            priority: Task priority from 1 (normal) to 4 (urgent).
            
        Returns:
            The created task object
        """
        url = self.BASE_TASK_URL
        
        task_data = {
            "content": content,
            "description": description,
            "due_string": due_string,
            "priority": priority
        }
        
        response = requests.post(url, headers=self.headers, json=task_data)
        
        if response.status_code != 200:
            raise Exception(f"Failed to create task: {response.status_code} - {response.text}")
        
        return response.json()
        
    def close_task(self, task_id: str) -> dict:
        """Closes (completes) a single task in Todoist by its ID
        
        Args:
            task_id s: The ID of the task to close
            
        Returns:
            dict: The API response confirming completion
        """
        url = f"{self.BASE_TASK_URL}/{task_id}/close"
        
        # Make the API request to close the task
        response = requests.post(url, headers=self.headers)
        
        if response.status_code != 204:
            raise Exception(f"Failed to close task: {response.status_code} - {response.text}")
        
        return {"success": True, "task_id": task_id}