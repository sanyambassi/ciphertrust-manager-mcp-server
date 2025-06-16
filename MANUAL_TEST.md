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

## 3. Try These Common Tool Examples

Copy and paste each of these JSON-RPC messages (one at a time) into the running server terminal. Each will test a different grouped tool.

### a) Get System Information
```json
{"jsonrpc":"2.0","method":"system_information_management","params":{"action": "get"},"id":2}
```

### b) List Users
```json
{"jsonrpc":"2.0","method":"user_management","params":{"action": "list"},"id":3}
```

### c) List CTE Client Groups
```json
{"jsonrpc":"2.0","method":"ct_cte_clientgroup_management","params":{"action": "list"},"id":4}
```

### d) List Keys
```json
{"jsonrpc":"2.0","method":"key_management","params":{"action": "list"},"id":5}
```

**Expected Result:**
- Each request should return a JSON response with the relevant information (system info, user list, client group list, or key list).

---

## 4. Tool Reference

For a full, up-to-date list of available tools and their JSON-RPC method names, see [TOOLS.md](./TOOLS.md).

- TOOLS.md lists every grouped tool, its method name, and a short description.
- Use these method names in your JSON-RPC requests for manual testing or integration.

---

## 5. Tips for Manual Testing

- **Copy and paste** JSON-RPC messages into the terminal where the server is running.
- **Each message must be on a single line** and followed by Enter.
- **To exit** the server, press `Ctrl+C`.
- **Log output** is written to stderr and will appear in the terminal.

---

## 6. Troubleshooting

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

## 7. Next Steps

- Try more grouped tool actions by changing the `