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
            tools = await session.list_tools()
            print(f"Available tools: {tools}")
            
            # Call the add tool
            result = await session.call_tool("add", arguments={"a": 5, "b": 7})
            print(f"5 + 7 = {result}")
            
            # Get a greeting
            name = "Daniele"
            content, mime_type = await session.read_resource(f"greeting://{name}")
            print(f"Greeting: {content} (mime type: {mime_type})")
            
            print("MCP client test completed successfully!")

def main():
    asyncio.run(run_client())

if __name__ == "__main__":
    main() 