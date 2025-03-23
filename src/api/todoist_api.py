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
    
    def get_tasks(self, filter_string=None, project_id=None, label=None, limit=None):
        """Get tasks with flexible filtering options using Todoist's native filtering
        
        Args:
            filter_string: Todoist filter query string (e.g., "today", "overdue", 
                           "date: Jan 3", "date before: May 5", etc.)
            project_id: Optional project ID to filter tasks
            label: Optional label to filter tasks
            limit: Optional limit on number of results returned
            
        Returns:
            List of filtered task objects
        """
        url = f"{self.BASE_URL}/tasks"
        
        # Add API parameters for supported filters
        params = {}
        if filter_string:
            params["filter"] = filter_string
        if project_id:
            params["project_id"] = project_id
        if label:
            params["label"] = label
        
        # Make the API request with filters
        response = requests.get(url, headers=self.headers, params=params)
        
        if response.status_code != 200:
            raise Exception(f"Failed to get tasks: {response.status_code} - {response.text}")
        
        tasks = response.json()
        
        # Apply limit if specified
        if limit and isinstance(limit, int) and limit > 0:
            tasks = tasks[:limit]
                
        return tasks
    
    def get_tasks_by_filter(self, filter_param=None, priority=None, project_id=None, label=None, limit=None):
        """Get tasks with common predefined filters
        
        Args:
            filter_param: Predefined filter option ("today", "tomorrow", "overdue", 
                         "next_n_days:<n>")
            priority: Optional priority filter (1-4)
            project_id: Optional project ID to filter tasks
            label: Optional label to filter tasks
            limit: Optional limit on number of results returned
            
        Returns:
            List of filtered task objects
        """
        # Map our simple filter options to Todoist filter syntax
        filter_string = None
        
        if filter_param:
            if filter_param == "today":
                filter_string = "today"
            elif filter_param == "tomorrow":
                filter_string = "tomorrow"
            elif filter_param == "overdue":
                filter_string = "overdue"
            elif filter_param.startswith("next_n_days:"):
                try:
                    days = int(filter_param.split(":")[1])
                    filter_string = f"date: {days} days"
                except (ValueError, IndexError):
                    # Default to 7 days if there's an issue parsing
                    filter_string = "date: 7 days"
        
        # Get tasks with the filter string
        if filter_string:
            tasks = self.get_tasks(filter_string=filter_string, project_id=project_id, label=label)
        else:
            tasks = self.get_tasks(project_id=project_id, label=label)
        
        # Apply priority filter if specified (client-side filtering)
        if priority:
            tasks = [task for task in tasks if task.get("priority") == priority]
        
        # Apply limit if specified
        if limit and isinstance(limit, int) and limit > 0:
            tasks = tasks[:limit]
                
        return tasks 