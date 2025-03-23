import os

class Config:
    """Configuration class for the Todoist MCP"""
    
    @staticmethod
    def get_api_token():
        """Get the Todoist API token from environment variables"""
        token = os.environ.get("TODOIST_API_TOKEN")
        if not token:
            raise ValueError("TODOIST_API_TOKEN environment variable not set")
        return token 