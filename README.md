# CipherTrust Manager MCP Server

This project implements an independently-developed CipherTrust MCP (Model Context Protocol) server that allows AI Assistants like Claude or Cursor to interact with CipherTrust Manager resources using the ksctl CLI.

## Table of Contents

- [Important Notice](#important-notice)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Testing](#testing)
- [Integration with AI Assistants](#integration-with-ai-assistants)
- [Environment Variables](#environment-variables)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Legal](#legal)
- [License](#license)

## Important Notice

This is an **independent, open-source project**. Please note:

- ⚠️ **Not officially supported** by Thales
- ✅ **Uses public APIs** and documented interfaces
- 🔧 **Independently maintained** 
- 📝 **Use at your own risk** - test thoroughly in your environment
- 💼 **No warranty** - see license for full terms

For official CipherTrust Manager support, please contact Thales directly.

## Features

The MCP server exposes a set of tools and endpoints for clients (such as Claude Desktop and Cursor) to interact with CipherTrust resources. Supported operations include:

- Key management
- CTE client management
- User management
- Connection management
- And more

**Benefits:**
- Unified interface for AI assistants to interact with CipherTrust Manager
- Support for key management, connection management, CTE client management, and more
- JSON-RPC communication over stdin/stdout
- Configurable via environment variables

## Prerequisites

- **Git**
- **Python 3.11 or higher**
- **uv** for dependency management
- **Access to a CipherTrust Manager instance**
- **Valid CipherTrust Manager credentials**

### Installing Git (Windows)

If you don't have Git installed on Windows, follow these steps:

- **Download and install Git for Windows**: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- **Or install via winget**:
  ```bash
  winget install --id Git.Git -e --source winget
  ```
- **Verify installation** - Open PowerShell and execute:
  ```bash
  git --version
  ```
  You should see the installed Git version.

## Installing Python and uv

### Method 1: Manual Installation

#### 1. Download Python
```powershell
# Open PowerShell as Administrator (optional)
cd $env:USERPROFILE\Downloads
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe" -OutFile "python-installer.exe"
```

#### 2. Run the Installer
```powershell
.\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
```

#### 3. Verify Installation
Open a new terminal and run:
```bash
python --version
pip --version
```

#### 4. Install uv
```bash
pip install uv
uv --version
```

#### 5. Clone the Repository
```bash
git clone https://github.com/sanyambassi/ciphertrust-manager-mcp-server.git
cd ciphertrust-manager-mcp-server
```

#### 6. Create a Virtual Environment and Install Dependencies
```bash
uv venv
.venv\Scripts\activate
uv pip install -e .
```

### Method 2: Using winget (Windows)

#### 1. Install Python with winget
```bash
winget install --id Python.Python.3.12 --source winget --accept-package-agreements --accept-source-agreements
```

#### 2. Close and Reopen PowerShell
This ensures Python is available in your PATH.

#### 3. Verify Installation
```bash
python --version
pip --version
```

#### 4. Install uv
```bash
pip install uv
uv --version
```

#### 5. Clone the Repository
```bash
git clone https://github.com/sanyambassi/ciphertrust-manager-mcp-server.git
cd ciphertrust-manager-mcp-server
```

#### 6. Create a Virtual Environment and Install Dependencies
```bash
uv venv
.venv\Scripts\activate
uv pip install -e .
```

## Configuration

### (Optional) Copy and Edit the Example Environment File

**Example `.env`:**
```bash
cp .env.example .env
# Edit .env with your CipherTrust Manager details
```

You can also set these as environment variables directly instead of using a `.env` file.

**Example `.env` content:**
```
CIPHERTRUST_URL=https://your-ciphertrust-manager.example.com
CIPHERTRUST_USER=admin
CIPHERTRUST_PASSWORD=your-password-here
CIPHERTRUST_NOSSLVERIFY=true
```

## Usage

**⚠️ Important:** Before starting, either the environment variable or .env should contain a valid CipherTrust Manager URL.

You have two main ways to run the CipherTrust MCP Server:

### Method 1: Direct Execution
```bash
uv run ciphertrust-mcp-server
```
This runs the `main()` function in `ciphertrust_mcp_server/__main__.py`.

### Method 2: Module Execution
```bash
uv run python -m ciphertrust_mcp_server.__main__
```

## Testing

This project includes comprehensive testing capabilities using the Model Context Protocol Inspector and Python unit tests.

### Quick Testing

```bash
# Manual JSON-RPC testing (direct stdin/stdout)
uv run ciphertrust-mcp-server
# Then send JSON-RPC commands (see TESTING.md for details)

# Interactive UI (Inspector 2.5+). Open the printed URL; it includes MCP_INSPECTOR_API_TOKEN.
npx @modelcontextprotocol/inspector uv run --no-sync ciphertrust-mcp-server

# Quick CLI testing
# Get tools
npx @modelcontextprotocol/inspector --cli --config tests/mcp_inspector_config.json --server ciphertrust-local --method tools/list --format json
# Get system information
npx @modelcontextprotocol/inspector --cli --config tests/mcp_inspector_config.json --server ciphertrust-local --method tools/call --tool-name system_information --tool-arg action=get --format json
# Get 2 keys
npx @modelcontextprotocol/inspector --cli --config tests/mcp_inspector_config.json --server ciphertrust-local --method tools/call --tool-name key_management --tool-arg action=list --tool-arg limit=2 --format json
```

### Available Testing Methods

- **🔧 Manual JSON-RPC Testing**: Direct stdin/stdout communication for debugging and development
- **🖥️ Interactive UI Testing**: Visual web interface for manual testing and debugging
- **⚡ CLI Automated Testing**: Command-line automation for CI/CD integration
- **🧪 Python Unit Tests**: Comprehensive unit testing for server components
- **🔗 Integration Tests**: End-to-end testing with real CipherTrust Manager instances

### NPM Scripts

```bash
npm run test:inspector:ui     # Open Inspector UI (uses project .env)
npm run test:inspector:cli    # List tools via Inspector CLI
npm run test:python          # Run Python unit tests
npm run test:full           # Run complete test suite
```

### Comprehensive Testing Guide

📖 **For detailed testing instructions, see [TESTING.md](docs/TESTING.md)**

🔧 **For example AI assistant prompts, see [EXAMPLE_PROMPTS.md](docs/EXAMPLE_PROMPTS.md)**

The testing guide covers:
- Complete setup and configuration
- Advanced testing scenarios


The example prompts include:
- Key management operations
- User and group management
- System and service management
- Cluster management
- License management
- CTE operations
- Crypto operations
- And more practical scenarios

## Integration with AI Assistants

### Using with Cursor

#### 1. Configure Cursor
- Go to **Settings > MCP Tools > Add Custom MCP**
- Add the following contents in the config file (e.g., `mcp.json`):

```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "Path to your project folder/ciphertrust-manager-mcp-server/.venv/bin/ciphertrust-mcp-server",
      "args": [],
      "env": {
        "CIPHERTRUST_URL": "https://your-ciphertrust.example.com",
        "CIPHERTRUST_USER": "admin",
        "CIPHERTRUST_PASSWORD": "your-password-here"
      }
    }
  }
}
```

On Windows, use the `.venv\Scripts\ciphertrust-mcp-server.exe` path and double backslashes:

```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "C:\\path\\to\\ciphertrust-manager-mcp-server\\.venv\\Scripts\\ciphertrust-mcp-server",
      "args": [],
      "env": {
        "CIPHERTRUST_URL": "https://your-ciphertrust.example.com",
        "CIPHERTRUST_USER": "admin",
        "CIPHERTRUST_PASSWORD": "your-password-here"
      }
    }
  }
}
```

#### 2. Apply Configuration
Disable and Re-enable the CipherTrust MCP server in Cursor to apply the changes.

### Using with Claude Desktop

#### 1. Locate or create the Claude Desktop config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Roaming\Claude\claude_desktop_config.json`

#### 2. Add or update the MCP server configuration:

**macOS/Linux Example:**
```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "/absolute/path/to/ciphertrust-manager-mcp-server/.venv/bin/ciphertrust-mcp-server",
      "env": {
        "CIPHERTRUST_URL": "https://your-ciphertrust.example.com",
        "CIPHERTRUST_USER": "admin",
        "CIPHERTRUST_PASSWORD": "your-password-here"
      }
    }
  }
}
```

**Windows Example:**
```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "C:\\absolute\\path\\to\\ciphertrust-manager-mcp-server\\.venv\\Scripts\\ciphertrust-mcp-server",
      "env": {
        "CIPHERTRUST_URL": "https://your-ciphertrust.example.com",
        "CIPHERTRUST_USER": "admin",
        "CIPHERTRUST_PASSWORD": "your-password-here"
      }
    }
  }
}
```

Adjust the path to match your actual project location and environment.

#### 3. Restart Claude Desktop
Restart Claude Desktop to apply the changes.

## Environment Variables

Set these in your shell or in a `.env` file in the project root:

| Variable Name | Description | Required/Default |
|---|---|---|
| `CIPHERTRUST_URL` | CipherTrust Manager URL (http/https) | Required |
| `CIPHERTRUST_USER` | CipherTrust Manager username | Required |
| `CIPHERTRUST_PASSWORD` | CipherTrust Manager password | Required |
| `CIPHERTRUST_NOSSLVERIFY` | Disable SSL verification (true/false) | `false` |
| `CIPHERTRUST_TIMEOUT` | Timeout for CipherTrust requests (seconds) | `30` |
| `CIPHERTRUST_DOMAIN` | Default CipherTrust domain | `root` |
| `CIPHERTRUST_AUTH_DOMAIN` | Authentication domain | `root` |
| `KSCTL_PATH` | Path to ksctl binary | `~/.ciphertrust-mcp/ksctl` |
| `KSCTL_CONFIG_PATH` | Path to ksctl config file | `~/.ksctl/config.yaml` |
| `LOG_LEVEL` | Logging level (DEBUG, INFO) | `INFO` |

**Example `.env` file:**
```bash
CIPHERTRUST_URL=https://your-ciphertrust.example.com
CIPHERTRUST_USER=admin
CIPHERTRUST_PASSWORD=yourpassword
CIPHERTRUST_NOSSLVERIFY=false
CIPHERTRUST_TIMEOUT=30
CIPHERTRUST_DOMAIN=root
CIPHERTRUST_AUTH_DOMAIN=root
KSCTL_PATH=
KSCTL_CONFIG_PATH=
LOG_LEVEL=INFO
```

## Troubleshooting

### Successful startup logs:

- The server is designed to be run as a subprocess by MCP clients (like Claude Desktop or Cursor) and communicates via JSON-RPC over stdin/stdout.
- You'll see log output like in the AI assistant's MCP log:

```
2025-06-16 02:22:30,462 - ciphertrust_mcp_server.server - INFO - Starting ciphertrust-manager v0.2.0
2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - Successfully connected to CipherTrust Manager
2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - MCP server ready and waiting for JSON-RPC messages on stdin...
```

### Dependencies

The `pyproject.toml` file includes these dependencies:
- `mcp>=2.1.1,<3`
- `pydantic>=2.12.0`
- `pydantic-settings>=2.0.0`
- `httpx>=0.27.0`
- `python-dotenv>=1.0.0`

If you encounter issues, ensure all dependencies are installed and up-to-date.

## Project Structure

```
ciphertrust-manager-mcp-server/
├── src
│   ├── ciphertrust_mcp_server/     # Main server code
├── tests/                      	# Testing configuration and unit tests
│   ├── mcp_inspector_config.json
│   ├── test_scenarios.json
│   ├── test_server.py
│   └── test_integration_simple.py
├── scripts/                    	# Testing and utility scripts
│   ├── test_with_inspector.bat
│   ├── test_with_inspector.sh
│   └── run_tests.py
├── docs/                      		# Additional documentation
│   ├── TESTING.md
│   ├── EXAMPLE_PROMPTS.md
│   └── TOOLS.md
├── README.md                   	# This file
├── pyproject.toml             		# Python dependencies
└── package.json               		# Node.js dependencies for testing
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. While this started as a personal project, contributions help make it better for everyone.

## Legal

### Trademark Notice
CipherTrust® and related trademarks are the property of Thales Group and its subsidiaries. This project is not affiliated with, endorsed by, or sponsored by Thales Group.

### No Warranty
This software is provided "as is" without warranty of any kind. Use at your own risk.

### Support
This is an independent project. For official CipherTrust Manager support, please contact Thales directly. For issues with this unofficial MCP server, please use the GitHub issue tracker.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---