import requests
from datetime import datetime, timedelta
from ..config.config import Config

class TodoistAPI:
    """Wrapper for the Todoist REST API"""
    
    BASE_URL = "https://api.todoist.com/rest/v2"
    
    def __init__(self):
        self.token = Config.get_api_token()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
    
    def get_all_tasks(self):
        """Get all active tasks from Todoist"""
        url = f"{self.BASE_URL}/tasks"
        response = requests.get(url, headers=self.headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to get tasks: {response.status_code} - {response.text}")
    
    def get_today_tasks(self):
        """Get all tasks due today"""
        all_tasks = self.get_all_tasks()
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Filter tasks that are due today
        today_tasks = [
            task for task in all_tasks
            if task.get("due") and task["due"].get("date") == today
        ]
        
        return today_tasks
    
    def get_tasks_by_filter(self, filter_param=None):
        """Get tasks with optional filtering
        
        Arguments:
            filter_param: Optional filter parameter (e.g., "today", "overdue", etc.)
        """
        all_tasks = self.get_all_tasks()
        
        if not filter_param:
            return all_tasks
            
        today = datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        
        if filter_param == "today":
            return [
                task for task in all_tasks
                if task.get("due") and task["due"].get("date") == today
            ]
        elif filter_param == "overdue":
            return [
                task for task in all_tasks
                if task.get("due") and task["due"].get("date") < today
            ]
        else:
            # Return all tasks if filter not recognized
            return all_tasks 