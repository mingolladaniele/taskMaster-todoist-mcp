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

            # Basic filter tests
            print("\nFetching tasks due today...")
            today_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "today"}
            )
            print(f"Today's tasks:\n{today_tasks}")

            print("\nFetching tasks due tomorrow...")
            tomorrow_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "tomorrow"}
            )
            print(f"Tomorrow's tasks:\n{tomorrow_tasks}")

            print("\nFetching overdue tasks...")
            overdue_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "od"}
            )
            print(f"Overdue tasks:\n{overdue_tasks}")

            # Week filters
            print("\nFetching tasks for this week...")
            this_week_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "due before: sat"}
            )
            print(f"This week's tasks:\n{this_week_tasks}")

            print("\nFetching tasks for next week...")
            next_week_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "next week"}
            )
            print(f"Next week's tasks:\n{next_week_tasks}")

            # Next N days filter
            print("\nFetching tasks due in the next 7 days...")
            next7_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "next 7 days"}
            )
            print(f"Next 7 days tasks:\n{next7_tasks}")

            # Priority filters

            print("\nFetching high priority (P1) tasks due this week...")
            p1_this_week = await session.call_tool(
                "get_tasks_tool",
                arguments={"filter_string": "p1 & (today | next 7 days)"},
            )
            print(f"P1 tasks this week:\n{p1_this_week}")

            print("\nFetching tasks for this month...")
            this_month_tasks = await session.call_tool(
                "get_tasks_tool", arguments={"filter_string": "next 30 days"}
            )
            print(f"This month's tasks:\n{this_month_tasks}")

            print("MCP client test completed successfully!")


def main():
    asyncio.run(run_client())


if __name__ == "__main__":
    main()
