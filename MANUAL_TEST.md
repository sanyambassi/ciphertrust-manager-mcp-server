# Manual Test Guide: CipherTrust MCP Server

This guide will help you manually test your CipherTrust MCP Server to ensure it is working as expected.

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

---

## 2. Send a Test JSON-RPC Request

You can use `curl`, `httpie`, or any HTTP client to send a request. Here's how to do it with `curl`:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"0.1.0","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}' \
  http://localhost:PORT/
```
- Replace `PORT` with the port your server is running on (default is usually 8000 or as configured).

**Expected Result:**
- You should receive a JSON response with server information and supported methods.

---

## 3. Test a Tool (e.g., System Info)

Send a request to get system info:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  --data '{"jsonrpc":"2.0","method":"ct_system_info_get","params":{},"id":2}' \
  http://localhost:PORT/
```

**Expected Result:**
- The response should include CipherTrust Manager system information (e.g., version, name, etc.).

---

## 4. Check Logs

- The server logs output to the terminal (stderr).
- Look for errors or stack traces if something fails.

---

## 5. Troubleshooting

- **Server not starting?**
  - Check that your virtual environment is activated and dependencies are installed.
  - Run `python --version` to ensure you are using Python 3.11+.
- **No response or connection refused?**
  - Make sure the server is running and listening on the correct port.
  - Check firewall or security group settings if running on a remote server.
- **Unexpected errors?**
  - Review the logs for error messages.
  - Ensure your `.env` file is present and correctly configured.

---

## 6. Next Steps

- Try other available tools (see `INTEGRATION_GUIDE.md` for a list).
- Integrate with Claude Desktop or other MCP clients for end-to-end testing.
- Report any issues or unexpected behavior.
