# CipherTrust MCP Server Integration Guide

Your CipherTrust MCP Server is now ready for use! Here's how to integrate it with various MCP clients.

## Claude Desktop Integration

### macOS

1. Open Claude Desktop configuration:
```bash
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. Add the CipherTrust server configuration:
```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "/mcp_servers/v1/ciphertrust-mcp-server/.venv/bin/ciphertrust-mcp-server"
    }
  }
}
```

3. Restart Claude Desktop

### Windows

1. Open Claude Desktop configuration:
```
notepad %APPDATA%\Claude\claude_desktop_config.json
```

2. Add the CipherTrust server configuration:
```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "C:\\mcp_servers\\v1\\ciphertrust-mcp-server\\.venv\\Scripts\\ciphertrust-mcp-server.exe"
    }
  }
}
```

3. Restart Claude Desktop

### Linux

1. Open Claude Desktop configuration:
```bash
nano ~/.config/Claude/claude_desktop_config.json
```

2. Add the CipherTrust server configuration (your current setup):
```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "/mcp_servers/v1/ciphertrust-mcp-server/.venv/bin/ciphertrust-mcp-server"
    }
  }
}
```

3. Restart Claude Desktop

## Available Tools in Claude

Once configured, you can use these tools in Claude:

### System Management
- **ct_system_info_get**: Get CipherTrust Manager system information
- **ct_system_info_set**: Set the system's friendly name

### Token Management
- **ct_token_create**: Create JWT/refresh tokens
- **ct_token_list**: List tokens with filtering
- **ct_token_get**: Get token details
- **ct_token_delete**: Delete a token
- **ct_token_revoke**: Revoke a token

### User Management
- **ct_user_create**: Create new users
- **ct_user_list**: List users with filtering
- **ct_user_get**: Get user details
- **ct_user_delete**: Delete users
- **ct_user_modify**: Modify user settings

## Example Usage in Claude

Once integrated, you can ask Claude things like:

- "Use the CipherTrust tools to show me the system information"
- "List all users in CipherTrust Manager"
- "Create a new user named 'testuser' with email test@example.com"
- "Generate a JWT token for authentication"

## Troubleshooting

### If Claude doesn't see the tools:

1. Check Claude's logs:
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%APPDATA%\Claude\logs\`
   - Linux: `~/.config/Claude/logs/`

2. Verify the server runs correctly:
```bash
/mcp_servers/v1/ciphertrust-mcp-server/.venv/bin/ciphertrust-mcp-server
```
Then paste: `{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"0.1.0","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}`

3. Check permissions on the executable:
```bash
ls -la /mcp_servers/v1/ciphertrust-mcp-server/.venv/bin/ciphertrust-mcp-server
```

### Environment Variables

If you need to pass environment variables to the server in Claude config:

```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "/mcp_servers/v1/ciphertrust-mcp-server/.venv/bin/ciphertrust-mcp-server",
      "env": {
        "CIPHERTRUST_URL": "https://your-server.com",
        "CIPHERTRUST_USER": "different-user"
      }
    }
  }
}
```

## Security Notes

- The server uses the credentials from your `.env` file
- Logs are written to stderr and don't contain passwords
- All communication with CipherTrust Manager uses your configured SSL settings
- Consider using JWT tokens instead of passwords for production use

## Next Steps

1. Add more CipherTrust tools as needed
2. Implement resource providers for policies, keys, etc.
3. Add support for more ksctl commands
4. Create custom prompts for common CipherTrust workflows
