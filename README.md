# Todoist MCP

A Model Context Protocol (MCP) server implementation for Todoist integration. This server allows Claude and other AI assistants to interact with your Todoist tasks via MCP.

## Features

- **Get Today's Tasks**: Fetch and display all tasks due today
- **Flexible Task Filtering**: Filter tasks using simple predefined filters or Todoist's advanced filter syntax
  - Filter by due date: today, tomorrow, overdue, or next X days
  - Filter by priority levels (1-4)
  - Filter by project ID or label
  - Apply advanced Todoist filter queries
- **Rich Task Formatting**: Each task displays priority, due date, and other relevant information

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- Todoist account and API token

### Setup

1. Clone this repository:
```bash
git clone <repository-url>
cd todoist-mcp
```

2. Install dependencies with Poetry:
```bash
poetry install
```

3. Set your Todoist API token as an environment variable:
```bash
# Linux/macOS
export TODOIST_API_TOKEN="your-api-token-here"

# Windows
set TODOIST_API_TOKEN="your-api-token-here"
```

You can find your Todoist API token in Todoist settings → Integrations → Developer.

## Usage

### Running the server

```bash
poetry run python server.py
```

### Testing the client

To test the server functionality:

```bash
poetry run python test_client.py
```

### MCP Tools

#### `todoist_get_today_tasks`

Retrieves all tasks that are due today.

**Example usage:**
```python
tasks = await session.call_tool("todoist_get_today_tasks", arguments={})
```

#### `todoist_get_tasks`

Retrieves tasks with powerful filtering options.

**Parameters:**
- `filter_param`: Simple predefined filter ("today", "tomorrow", "overdue", "next_n_days:X")
- `filter_string`: Advanced Todoist filter query string for complex filtering
- `priority`: Priority level (1-4, where 4 is highest)
- `project_id`: Project ID to filter by project
- `label`: Label name to filter tasks
- `limit`: Maximum number of tasks to return

**Example usage:**
```python
# Get tasks due tomorrow
tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "tomorrow"})

# Get overdue tasks
tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "overdue"})

# Get tasks due in the next 7 days
tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_param": "next_n_days:7"})

# Get tasks with no due date
tasks = await session.call_tool("todoist_get_tasks", arguments={"filter_string": "no date"})

# Get high priority tasks
tasks = await session.call_tool("todoist_get_tasks", arguments={"priority": 4})
```

### Using with Claude Desktop

To use with Claude Desktop, add the server config:

- On macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "todoist": {
      "command": "path/to/python",
      "args": ["path/to/todoist-mcp/server.py"],
      "env": {
        "TODOIST_API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

## Advanced Filtering

The `todoist_get_tasks` tool supports Todoist's powerful filtering syntax through the `filter_string` parameter. Here are some examples:

- `"today"` - Tasks due today
- `"overdue"` - Overdue tasks
- `"date: Jan 3"` - Tasks due on January 3rd
- `"date before: May 5"` - Tasks due before May 5th
- `"date after: May 5"` - Tasks due after May 5th
- `"date: 7 days"` - Tasks due in the next 7 days
- `"no date"` - Tasks with no due date
- `"date before: next week"` - Tasks due before next week
- `"date before: sat"` - Tasks dated in the current working week

## Development

The codebase is organized into modules:

- `api/`: API wrapper for Todoist
- `config/`: Configuration and settings
- `tools/`: MCP tools implementation
- `utils/`: Utility functions and helpers

## Contribution

Contributions are welcome! Feel free to submit pull requests or open issues.

## License

MIT License 