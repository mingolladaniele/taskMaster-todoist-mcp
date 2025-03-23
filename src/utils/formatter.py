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
            4: "🔴 P1",  # Urgent
            3: "🟠 P2",  # High
            2: "🔵 P3",  # Medium
            1: "⚪ P4"    # Low
        }
        priority = priority_map.get(task.get("priority"))
        
        # Format due date
        due_info = "⏱️ No due date"
        if due := task.get("due"):
            due_date = due.get("date", "")
            due_string = due.get("string", "")
            
            # Use due string if available, otherwise use the date
            if due_string:
                due_info = f"⏱️ {due_string}"
            else:
                due_info = f"⏱️ {due_date}"
                
            # Add time if available
            if due.get("datetime"):
                time_part = due.get("datetime", "").split("T")[1][:5]  # Get HH:MM part
                due_info += f" at {time_part}"
                
            # Mark recurring tasks
            if due.get("is_recurring"):
                due_info += " (recurring)"
        
        # Format project
        project_info = f"📁 Project: {task.get('project_id', 'N/A')}"
        
        # Format labels
        labels = task.get("labels", [])
        labels_info = ""
        if labels:
            labels_info = f"🏷️ {', '.join(labels)}"
        
        # Format task with all available information
        formatted_task = f"{priority} | {content} | {due_info}"
        
        # Add additional info on a new line if available
        additional_info = []
        if labels_info:
            additional_info.append(labels_info)
        if task.get("description"):
            description = task.get("description", "")
            if len(description) > 50:
                description = description[:47] + "..."
            additional_info.append(f"📝 {description}")
            
        if additional_info:
            formatted_task += f"\n    {' | '.join(additional_info)}"
        
        # Add task ID at the end for reference
        formatted_task += f" (ID: {task_id})"
        
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