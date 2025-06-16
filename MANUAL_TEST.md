# Manual Test Guide: CipherTrust MCP Server (STDIO)

This guide will help you manually test your CipherTrust MCP Server, which communicates via JSON-RPC over stdin/stdout (not HTTP).

---

## 1. Start the MCP Server

Activate your virtual environment (if using one), then run:

```bash
.venv/bin/ciphertrust-mcp-server
```
- On Windows, use:
  ```
  .venv\Scripts\ciphertrust-mcp-server.exe
  # or
  .venv\Scripts\ciphertrust-mcp-server.bat
  ```
- Make sure you are in your project directory.

The server will wait for JSON-RPC messages on stdin.

---

## 2. Send a Test JSON-RPC Message

You can manually type or paste a JSON-RPC message into the terminal where the server is running. For example, paste this and press Enter:

```json
{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"0.1.0","capabilities":{},"clientInfo":{"name":"manual-test","version":"1.0"}},"id":1}
```

**Expected Result:**
- You should see a JSON response printed to stdout, containing server information and supported methods.

---

## 3. Test Grouped Tools (Modern Usage)

Most tools are now grouped and use the following pattern:

```json
{"jsonrpc":"2.0","method":"<grouped_tool_name>","params":{"action": "<action>", ...},"id":X}
```

### Example: List Users

```json
{"jsonrpc":"2.0","method":"user_management","params":{"action": "list"},"id":2}
```

### Example: List CTE Client Groups

```json
{"jsonrpc":"2.0","method":"ct_cte_clientgroup_management","params":{"action": "list"},"id":3}
```

### Example: System Info (if available as a grouped tool)

If system info is still available as a single method, you can use:
```json
{"jsonrpc":"2.0","method":"ct_system_info_get","params":{},"id":4}
```
Otherwise, check your tool list for the correct grouped method name.

**Expected Result:**
- The response should include the requested information (e.g., user list, client group list, or system info).

---

## 4. Tips for Manual Testing

- **Copy and paste** JSON-RPC messages into the terminal where the server is running.
- **Each message must be on a single line** and followed by Enter.
- **To exit** the server, press `Ctrl+C`.
- **Log output** is written to stderr and will appear in the terminal.

---

## 5. Troubleshooting

- **No response?**
  - Make sure you pressed Enter after pasting the JSON.
  - Check for errors in the terminal output.
- **Server not starting?**
  - Ensure your virtual environment is activated and dependencies are installed.
  - Run `python --version` to ensure you are using Python 3.11+.
- **Unexpected errors?**
  - Review the logs for error messages.
  - Ensure your `.env` file is present and correctly configured.

---

## 6. Next Steps

- Try other available tools (see `INTEGRATION_GUIDE.md` for a list).
- Integrate with Claude Desktop or other MCP clients for end-to-end testing.
- Report any issues or unexpected behavior.
