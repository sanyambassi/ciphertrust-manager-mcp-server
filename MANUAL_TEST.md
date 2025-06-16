# Manual Testing of CipherTrust MCP Server

The MCP server communicates via JSON-RPC over stdin/stdout. When you run `ciphertrust-mcp-server`, it's waiting for JSON-RPC messages.

## Manual Test

You can manually test the server by typing JSON-RPC messages:

1. Start the server:
```bash
ciphertrust-mcp-server
```

2. In the same terminal, type this initialize request and press Enter:
```json
{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"0.1.0","capabilities":{},"clientInfo":{"name":"manual-test","version":"1.0"}},"id":1}
```

3. You should see a response like:
```json
{"jsonrpc": "2.0", "result": {"protocolVersion": "0.1.0", "capabilities": {"tools": {}}, "serverInfo": {"name": "ciphertrust-manager", "version": "0.1.0"}}, "id": 1}
```

4. Send the initialized notification:
```json
{"jsonrpc":"2.0","method":"notifications/initialized"}
```

5. List available tools:
```json
{"jsonrpc":"2.0","method":"tools/list","params":{},"id":2}
```

6. Call a tool (e.g., system info):
```json
{"jsonrpc":"2.0","method":"tools/call","params":{"name":"ct_system_info_get","arguments":{}},"id":3}
```

7. Press Ctrl+C to exit.

## Understanding MCP Server Behavior

- The server runs continuously, waiting for JSON-RPC messages on stdin
- It sends responses on stdout
- Log messages go to stderr (so they don't interfere with JSON-RPC)
- This is designed for programmatic communication with MCP clients

## Using with MCP Clients

MCP clients (like Claude Desktop) will handle this communication automatically. You just need to configure them to run the server command.
