# 🚀 TaskMaster: Todoist MCP for Cursor AI

A Model Context Protocol (MCP) server implementation for Todoist integration, specifically developed for Cursor AI. This server allows Cursor AI assistants to interact with your Todoist tasks directly from your coding environment.

## Demo Video
[![TaskMaster Demo](https://img.youtube.com/vi/RM-AaSpTqYI/0.jpg)](https://www.youtube.com/watch?v=RM-AaSpTqYI)
*Watch the TaskMaster demo on YouTube*

## Features

- **Flexible Task Filtering**: Filter tasks using Todoist's powerful filter syntax
  - Filter by due date: today, tomorrow, overdue
  - Filter by priority levels (1-4, where 1 is highest)
  - Filter using complex query combinations
- **Rich Task Formatting**: Each task displays priority, due date, and other relevant information with clear icons
- **Cursor AI Integration**: Seamlessly use Todoist within your Cursor AI coding environment

## Installation

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)
- Todoist account and API token

### Setup

1. Clone this repository:
```bash
git clone https://github.com/mingolladaniele/todoist-mcp.git
cd todoist-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
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
python server.py
```

### MCP Tool

The server provides the following MCP tool:

#### `get_tasks_tool`

Retrieves tasks with powerful filtering options.

**Parameters:**
- `filter_string`: Advanced Todoist filter query string for complex filtering
- `priority`: Optional priority level (1-4, where 1 is highest priority)

**Example filter strings:**
- `"today"` - Tasks due today
- `"overdue"` - Overdue tasks
- `"Jan 3"` - Tasks due on January 3rd
- `"due before: May 5"` - Tasks due before May 5th
- `"due after: May 5"` - Tasks due after May 5th
- `"due before: +4 hours"` - Tasks due within the next four hours and all overdue tasks
- `"no date"` - Tasks with no due date
- `"5 days"` or `"next 5 days"` - Tasks due in the next 5 days
- `"recurring"` - Tasks with a recurring date

## Setting up with Cursor AI

To use with Cursor AI, create or edit the MCP configuration file:

**Windows**: `C:\Users\<username>\.cursor\mcp.json`

```json
{
  "mcpServers": {
    "todoist-mcp": {
      "command": "C:/Users/<username>/path/to/todoist-mcp/.venv/Scripts/python.exe",
      "args": [
        "C:/Users/<username>/path/to/todoist-mcp/server.py"
      ],
      "env": {
        "TODOIST_API_TOKEN": "your-api-token-here"
      }
    }
  }
}
```

Replace `<username>` and paths with your actual username and the correct paths to your installation.

**Once you do that, go to Cursor Settings  → MCP and check that the server is correctly running (green dot).**

## Project Structure

The codebase is organized into modules:

- `api/`: API wrapper for Todoist
- `config/`: Configuration and settings
- `utils/`: Utility functions and helpers including task formatting

## Roadmap

Here are the features planned for future releases:

- **Task Creation**: Add new tasks to your Todoist directly from Cursor AI
- **Task Completion**: Mark tasks as complete without switching context
- **Task Deletion**: Remove tasks that are no longer needed
- **Smart Task Balancing**: AI-powered task rebalancing based on:
  - Project priority
  - Time commitments
  - Due dates
  - Current workload
- **Project Management**: Create and manage Todoist projects
- **Labels and Filters**: Add custom labels and create saved filters

## License

MIT License