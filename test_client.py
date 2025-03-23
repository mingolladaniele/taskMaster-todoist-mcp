#!/usr/bin/env python
# test_client.py
import asyncio
import os
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession

async def run_client():
    # Get the full path to the Python interpreter in the venv
    python_path = os.path.abspath(os.path.join(".venv", "Scripts", "python.exe"))
    server_path = os.path.abspath("server.py")
    
    # Connect to the local MCP server
    server_params = StdioServerParameters(
        command=python_path,
        args=[server_path],
        env=None,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()
            
            # List available tools
            tools_obj = await session.list_tools()
            print(f"Available tools: {tools_obj.tools}")
            
            # Test various filter options
            print("\nFetching tasks due tomorrow...")
            tomorrow_tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "tomorrow"})
            print(f"Tomorrow's tasks:\n{tomorrow_tasks}")
            
            print("\nFetching overdue tasks...")
            overdue_tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "overdue"})
            print(f"Overdue tasks:\n{overdue_tasks}")
            
            print("\nFetching tasks due in the next 7 days...")
            next7_tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "next_n_days:7"})
            print(f"Next 7 days tasks:\n{next7_tasks}")
            
            print("\nFetching tasks with advanced filter (no date)...")
            no_date_tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_string": "no date"})
            print(f"Tasks with no date:\n{no_date_tasks}")
            
            print("\nFetching high priority tasks...")
            high_priority_tasks = await session.call_tool("todoist_get_tasks", arguments={"priority": 1})
            print(f"High priority tasks:\n{high_priority_tasks}")
            
            print("MCP client test completed successfully!")

def main():
    asyncio.run(run_client())

if __name__ == "__main__":
    main() 