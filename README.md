# CipherTrust MCP Server

This project implements a CipherTrust MCP (Model Context Protocol) server that allows AI Assistants like Claude or Cursor to interact with CipherTrust Manager resources using the ksctl CLI.

---

## Overview

The MCP server exposes a set of tools and endpoints for clients (such as Claude Desktop and Cursor) to interact with CipherTrust resources. Supported operations include:
- Key management
- CTE client management
- User management
- Connection management
- And more

---

## Features

- Unified interface for AI assistants to interact with CipherTrust Manager
- Support for key management, connection management, CTE client management, and more
- JSON-RPC communication over stdin/stdout
- Configurable via environment variables

---

## Prerequisites

- **Python 3.11 or higher**
- [`uv`](https://github.com/astral-sh/uv) for dependency management
- Access to a CipherTrust Manager instance
- Valid CipherTrust Manager credentials

---

## Installation

You can install Python and `uv` using either the manual method or with `winget` (Windows only).

### Method 1: Manual Installation (Recommended for Fresh Systems)

1. **Download Python**
   ```powershell
   # Open PowerShell as Administrator (optional)
   cd $env:USERPROFILE\Downloads
   Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe" -OutFile "python-installer.exe"
   ```
2. **Run the Installer**
   ```powershell
   .\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
   ```
3. **Verify Installation**
   - Open a new terminal and run:
     ```powershell
     python --version
     pip --version
     ```
4. **Install uv**
   ```powershell
   pip install uv
   uv --version
   ```
5. **Clone the Repository**
   ```bash
   git clone https://github.com/sanyambassi/ciphertrust-manager-mcp-server.git
   cd ciphertrust-mcp-server
   ```
6. **Create a Virtual Environment and Install Dependencies**
   ```bash
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
   ```
7. **(Optional) Copy and Edit the Example Environment File**
   ```bash
   cp .env.example .env
   # Edit .env with your CipherTrust Manager details
   ```
   Example `.env`:
   ```env
   CIPHERTRUST_URL=https://your-ciphertrust-manager.example.com
   CIPHERTRUST_USER=admin
   CIPHERTRUST_PASSWORD=your-password-here
   ```
   *You can also set these as environment variables directly instead of using a `.env` file.*

---

### Method 2: Install Python and uv using winget (Windows Only)

1. **Install Python with winget**
   ```powershell
   winget install --id Python.Python.3.12 --source winget --accept-package-agreements --accept-source-agreements
   ```
2. **Close and Reopen PowerShell**
   - This ensures Python is available in your PATH.
3. **Verify Installation**
   ```powershell
   python --version
   pip --version
   ```
4. **Install uv**
   ```powershell
   pip install uv
   uv --version
   ```
5. **Clone the Repository**
   ```bash
   git clone https://github.com/sanyambassi/ciphertrust-manager-mcp-server.git
   cd ciphertrust-mcp-server
   ```
6. **Create a Virtual Environment and Install Dependencies**
   ```bash
   uv venv
   .venv\Scripts\activate
   uv pip install -e .
   ```
7. **(Optional) Copy and Edit the Example Environment File**
   ```bash
   cp .env.example .env
   # Edit .env with your CipherTrust Manager details
   ```
   Example `.env`:
   ```env
   CIPHERTRUST_URL=https://your-ciphertrust-manager.example.com
   CIPHERTRUST_USER=admin
   CIPHERTRUST_PASSWORD=your-password-here
   ```
   *You can also set these as environment variables directly instead of using a `.env` file.*

---

## 🚀 How to Start the Server

You have two main ways to run the CipherTrust MCP Server:

### 1. Using the CLI Script (Recommended)
```bash
uv run ciphertrust-mcp-server
```
This runs the `main()` function in `ciphertrust_mcp_server/__main__.py`.

### 2. Using Python Module Directly
```bash
uv run python -m ciphertrust_mcp_server.__main__
```

---

## 🛠️ Environment Variables

Set these in your shell or in a `.env` file in the project root:

| Variable Name             | Description                                         | Required/Default |
|--------------------------|-----------------------------------------------------|------------------|
| CIPHERTRUST_URL          | CipherTrust Manager URL (http/https)                | **Required**     |
| CIPHERTRUST_USER         | CipherTrust Manager username                        | **Required**     |
| CIPHERTRUST_PASSWORD     | CipherTrust Manager password                        | **Required**     |
| CIPHERTRUST_NOSSLVERIFY  | Disable SSL verification (`true`/`false`)           | `false`          |
| CIPHERTRUST_TIMEOUT      | Timeout for CipherTrust requests (seconds)          | `30`             |
| CIPHERTRUST_DOMAIN       | Default CipherTrust domain                          | `root`           |
| CIPHERTRUST_AUTH_DOMAIN  | Authentication domain                               | `root`           |
| KSCTL_DOWNLOAD_URL       | Custom ksctl download URL                           | auto-generated   |
| KSCTL_PATH               | Path to ksctl binary                                | `~/.ciphertrust-mcp/ksctl` |
| KSCTL_CONFIG_PATH        | Path to ksctl config file                           | `~/.ksctl/config.yaml` |
| MCP_SERVER_NAME          | Name for the MCP server                             | `ciphertrust-manager` |
| MCP_SERVER_VERSION       | Version string                                      | `0.1.0`          |
| LOG_LEVEL                | Logging level (`DEBUG`, `INFO`, etc.)               | `INFO`           |
| DEBUG_MODE               | Enable debug mode (`true`/`false`)                  | `false`          |

---

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

---

## 🧩 Integration with AI Assistants

- The server is designed to be run as a subprocess by MCP clients (like Claude Desktop or Cursor) and communicates via JSON-RPC over stdin/stdout.
- You'll see log output like in the AI assistant's MCP log:
  ```
  2025-06-16 02:22:30,462 - ciphertrust_mcp_server.server - INFO - Starting ciphertrust-manager v0.1.0
  2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - Successfully connected to CipherTrust Manager
  2025-06-16 02:22:30,838 - ciphertrust_mcp_server.server - INFO - MCP server ready and waiting for JSON-RPC messages on stdin...
  ```

---

## 🖥️ Using with Cursor

To use this server with Cursor:

1. **Configure Cursor**
   - Go to Settings > MCP Tools > Add Custom MCP
   - Add the following contents in the config file (e.g., `mcp.json`):
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
2. **Disable and Re-enable the CipherTrust MCP server** in Cursor to apply the changes.

---

## 📦 Reviewing Dependencies

The `pyproject.toml` file includes these dependencies:
- `mcp>=1.0.0`
- `pydantic>=2.0.0`
- `pydantic-settings>=2.0.0`
- `httpx>=0.27.0`
- `python-dotenv>=1.0.0`

If you encounter issues, ensure all dependencies are installed and up-to-date.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📝 License

This project is licensed under the MIT License. See the [`LICENSE`] (https://github.com/sanyambassi/ciphertrust-manager-mcp-server/blob/main/LICENSE) file for details.
