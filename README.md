# CipherTrust MCP Server

This project implements a CipherTrust MCP (Model Context Protocol) server that allows AI Assistants like Claude or Cursor to interact with CipherTrust manager resources using the ksctl CLI.

## Overview

The MCP server exposes a set of tools and endpoints that allow clients (such as Claude Desktop and Cursor) to interact with CipherTrust resources. It supports various operations including key management, CTE client management, user management, and more.

## Features

- Unified interface for AI assistants to interact with CipherTrust maanger
- Support for key management, connection management, CTE client management and more
- JSON-RPC communication over stdin/stdout
- Configurable via environment variables

## Prerequisites

- Python 3.11 or higher
- [uv](https://github.com/astral-sh/uv) for dependency management
- Access to a CipherTrust Manager instance
- Valid CipherTrust Manager credentials

## Installation

### Method 1: Manual Installation (Recommended for fresh systems)

**Step 1: Download Python**

```powershell
# Open PowerShell as Administrator (optional but recommended)
# Navigate to your Downloads folder
cd $env:USERPROFILE\Downloads

# Download Python installer using PowerShell
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe" -OutFile "python-installer.exe"
```

**Step 2: Run the installer**

```powershell
# Run the installer with important flags
.\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
```

**Step 3: Verify installation**

```powershell
# Refresh your PATH environment variable
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# In a new terminal, check Python installation
python --version

# Check pip version
pip --version
```

**Step 4: Install uv**:
   - Open PowerShell and run:
     ```powershell
     pip install uv
     ```
   - Verify the installation:
     ```powershell
     uv --version
     ```

**Step 5: Clone the repository**:
   ```bash
   git clone https://github.com/sanyambassi/ciphertrust-manager-mcp-server.git
   cd ciphertrust-mcp-server
   ```

**Step 6: Create a virtual environment and install dependencies using uv**:
   ```bash
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
   ```

**Step 7: Copy the example environment file and configure it. Skip this and the next step to directly use environment vairables in the mcp server configuration**:
   ```bash
   cp .env.example .env
   ```

**Step 8: Edit `.env` with your CipherTrust Manager details**:
   ```env
   CIPHERTRUST_URL=https://your-ciphertrust-manager.example.com
   CIPHERTRUST_USER=admin
   CIPHERTRUST_PASSWORD=your-password-here
   ```

## 🚀 How to Start the Server

You have **two main entrypoints** for running the CipherTrust MCP Server:

### 1. Using the CLI Script (Recommended)
If you installed the package (editable or otherwise), you can use the CLI entrypoint defined in your `pyproject.toml`:
```bash
uv run ciphertrust-mcp-server
```
This will invoke the `main()` function in `ciphertrust_mcp_server/__main__.py`.

### 2. Using Python Module Directly
You can also run the server as a module:
```bash
uv run python -m ciphertrust_mcp_server.__main__
```

## 🛠️ Environment Variables

You can configure the server using environment variables (set them in your shell or in a `.env` file in the project root):

| Variable Name                | Description                                                      | Default/Required         |
|------------------------------|------------------------------------------------------------------|--------------------------|
| `CIPHERTRUST_URL`            | CipherTrust Manager URL (must start with http/https)             | **Required**             |
| `CIPHERTRUST_USER`           | CipherTrust Manager username                                     | **Required**             |
| `CIPHERTRUST_PASSWORD`       | CipherTrust Manager password                                     | **Required**             |
| `CIPHERTRUST_NOSSLVERIFY`    | Disable SSL verification (`true`/`false`)                        | `false`                  |
| `CIPHERTRUST_TIMEOUT`        | Timeout for CipherTrust requests (seconds)                       | `30`                     |
| `CIPHERTRUST_DOMAIN`         | Default CipherTrust domain                                       | `root`                   |
| `CIPHERTRUST_AUTH_DOMAIN`    | Authentication domain                                            | `root`                   |
| `KSCTL_DOWNLOAD_URL`         | Custom ksctl download URL                                        | auto-generated           |
| `KSCTL_PATH`                 | Path to ksctl binary                                             | `~/.ciphertrust-mcp/ksctl`|
| `KSCTL_CONFIG_PATH`          | Path to ksctl config file                                        | `~/.ksctl/config.yaml`   |
| `MCP_SERVER_NAME`            | Name for the MCP server                                          | `ciphertrust-manager`    |
| `MCP_SERVER_VERSION`         | Version string                                                   | `0.1.0`                  |
| `LOG_LEVEL`                  | Logging level (`DEBUG`, `INFO`, etc.)                            | `INFO`                   |
| `DEBUG_MODE`                 | Enable debug mode (`true`/`false`)                               | `false`                  |

## 📝 Example `.env` File

```env
CIPHERTRUST_URL=https://your-ciphertrust.example.com
CIPHERTRUST_USER=admin
CIPHERTRUST_PASSWORD=yourpassword
CIPHERTRUST_NOSSLVERIFY=false
CIPHERTRUST_TIMEOUT=30
CIPHERTRUST_DOMAIN=root
CIPHERTRUST_AUTH_DOMAIN=root
KSCTL_DOWNLOAD_URL=
KSCTL_PATH=
KSCTL_CONFIG_PATH=
MCP_SERVER_NAME=ciphertrust-manager
MCP_SERVER_VERSION=0.1.0
LOG_LEVEL=INFO
DEBUG_MODE=false
```

## 🧩 Integration

- The server is designed to be run as a subprocess by MCP clients (like Claude Desktop or Cursor) and communicates via JSON-RPC over stdin/stdout.
- You'll see log output like in the AI assistants MCP log:
  ```
  2025-06-16 02:22:30,462 - ciphertrust_mcp_server.server - INFO - Starting ciphertrust-manager v0.1.0
  2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - Successfully connected to CipherTrust Manager
  2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - MCP server ready and waiting for JSON-RPC messages on stdin...
  ```

### Using with Cursor

To use this server with Cursor, you need to configure Cursor to run the server as a subprocess. Here's how:

1. **Configure Cursor** to use this `mcp.json` file. In Cursor, go to Settings > MCP Tools > Add Custom MCP and add the following contents in the config file:
   ```json
   {
     "mcpServers": {
       "ciphertrust": {
         "command": "uv",
         "args": ["run", "ciphertrust-mcp-server"],
         "env": {
           "CIPHERTRUST_URL": "https://your-ciphertrust-manager.example.com",
           "CIPHERTRUST_USER": "admin",
           "CIPHERTRUST_PASSWORD": "your-password-here"
         }
       }
     }
   }
   ```

2. **Disable and Re-enable the ciphertrust mcp server** to apply the changes.

### Reviewing Dependencies

The `pyproject.toml` file includes the following dependencies:
- `mcp>=1.0.0`
- `pydantic>=2.0.0`
- `pydantic-settings>=2.0.0`
- `httpx>=0.27.0`
- `python-dotenv>=1.0.0`

These dependencies are necessary for the server to function correctly. If you encounter any issues, ensure that all dependencies are installed and up-to-date.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
