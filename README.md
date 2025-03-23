# Todoist MCP

A Model Context Protocol (MCP) server implementation for Todoist integration. This server allows Claude and other AI assistants to interact with your Todoist tasks via MCP.

## Features

- **Get Today's Tasks**: Fetch and display all tasks due today

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