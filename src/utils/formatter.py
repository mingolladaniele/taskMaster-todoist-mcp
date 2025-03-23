class TaskFormatter:
    """Utility to format Todoist tasks for display"""
    
    @staticmethod
    def format_task(task):
        """Format a single task for display
        
        Arguments:
            task: A task object from the Todoist API
            
        Returns:
            str: Formatted task string
        """
        task_id = task.get("id", "N/A")
        content = task.get("content", "")
        
        # Format priority (4 is highest, 1 is lowest in Todoist)
        priority_map = {
            4: "Urgent",
            3: "High",
            2: "Medium",
            1: "Low"
        }
        priority = priority_map.get(task.get("priority", 1), "Low")
        
        # Format due date
        due_info = ""
        if due := task.get("due"):
            due_date = due.get("date", "")
            due_string = due.get("string", "")
            due_info = f" | Due: {due_string} ({due_date})"
        
        # Format project
        project_info = f" | Project ID: {task.get('project_id', 'N/A')}"
        
        # Format labels
        labels = task.get("labels", [])
        labels_info = ""
        if labels:
            labels_info = f" | Labels: {', '.join(labels)}"
        
        # Format task with all available information
        formatted_task = f"[{priority}] {content}{due_info}{project_info}{labels_info} (ID: {task_id})"
        
        return formatted_task
    
    @staticmethod
    def format_task_list(tasks):
        """Format a list of tasks for display
        
        Arguments:
            tasks: A list of task objects from the Todoist API
            
        Returns:
            str: Formatted task list string
        """
        if not tasks:
            return "No tasks found."
        
        formatted_tasks = []
        for i, task in enumerate(tasks, 1):
            formatted_task = TaskFormatter.format_task(task)
            formatted_tasks.append(f"{i}. {formatted_task}")
        
        return "\n".join(formatted_tasks) 