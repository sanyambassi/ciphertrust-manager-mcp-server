# CipherTrust MCP Server Integration Guide

Your CipherTrust MCP Server is now ready for use! Here's how to integrate it with various MCP clients.

## Claude Desktop Integration

### macOS

1. Open (or create) the Claude Desktop configuration file:
   ```bash
   nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
2. Add or update the CipherTrust server configuration (adjust the path as needed):
   ```json
   {
     "mcpServers": {
       "ciphertrust": {
         "command": "/absolute/path/to/.venv/bin/ciphertrust-mcp-server"
       }
     }
   }
   ```
   - Replace `/absolute/path/to/` with the actual path to your project directory.
   - If you use a virtual environment, make sure the path points to the executable inside `.venv/bin/`.
3. Restart Claude Desktop.

### Windows

1. Open (or create) the Claude Desktop configuration file:
   ```
   notepad %APPDATA%\Claude\claude_desktop_config.json
   ```
2. Add or update the CipherTrust server configuration (adjust the path as needed):
   ```json
   {
     "mcpServers": {
       "ciphertrust": {
         "command": "C:\\absolute\\path\\to\\.venv\\Scripts\\ciphertrust-mcp-server.exe"
       }
     }
   }
   ```
   - If you are using a virtual environment, the executable may be `.bat` or `.ps1` (e.g., `ciphertrust-mcp-server.bat`).
   - Make sure the path is absolute and points to the correct script in your virtual environment.
3. Restart Claude Desktop.

### Linux

1. Open (or create) the Claude Desktop configuration file:
   ```bash
   nano ~/.config/Claude/claude_desktop_config.json
   ```
2. Add or update the CipherTrust server configuration (adjust the path as needed):
   ```json
   {
     "mcpServers": {
       "ciphertrust": {
         "command": "/absolute/path/to/.venv/bin/ciphertrust-mcp-server"
       }
     }
   }
   ```
   - Replace `/absolute/path/to/` with the actual path to your project directory.
   - If you use a virtual environment, make sure the path points to the executable inside `.venv/bin/`.
3. Restart Claude Desktop.

**Note:**
- The config file may not exist by default; you may need to create it.
- The `"command"` path must be absolute and executable.
- If you use environment variables, see the section below.

## Environment Variables

If you need to pass environment variables to the server in the Claude config, add them under the `"env"` key:

```json
{
  "mcpServers": {
    "ciphertrust": {
      "command": "/absolute/path/to/.venv/bin/ciphertrust-mcp-server",
      "env": {
        "CIPHERTRUST_URL": "https://your-server.com",
        "CIPHERTRUST_USER": "your-username",
        "CIPHERTRUST_PASSWORD": "your-password"
      }
    }
  }
}
```
- You can set any required environment variables this way.
- For production, consider using a `.env` file and not committing secrets.

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

*For a full list of available tools, see the server logs or documentation.*

## Example Usage in Claude

Once integrated, you can ask Claude things like:

- "Use the CipherTrust tools to show me the system information"
- "List all users in CipherTrust Manager"
- "Create a new user named 'testuser' with email test@example.com"
- "Generate a JWT token for authentication"

## Troubleshooting

### If Claude doesn't see the tools:

1. **Check Claude's logs:**
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%APPDATA%\Claude\logs\`
   - Linux: `~/.config/Claude/logs/`
2. **Verify the server runs correctly:**
   ```bash
   /absolute/path/to/.venv/bin/ciphertrust-mcp-server
   ```
   Then paste:
   ```json
   {"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"0.1.0","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}
   ```
   You should see a JSON response.
3. **Check permissions on the executable:**
   ```bash
   ls -la /absolute/path/to/.venv/bin/ciphertrust-mcp-server
   chmod +x /absolute/path/to/.venv/bin/ciphertrust-mcp-server  # if needed
   ```
4. **Check that your virtual environment is activated and dependencies are installed.**

## Security Notes

- The server uses the credentials from your `.env` file or environment variables.
- Logs are written to stderr and do not contain passwords.
- All communication with CipherTrust Manager uses your configured SSL settings.
- Consider using JWT tokens instead of passwords for production use.
- Do not commit secrets to version control. Use a `.env.example` for sharing config structure.

## Next Steps

1. Add more CipherTrust tools as needed
2. Implement resource providers for policies, keys, etc.
3. Add support for more ksctl commands
4. Create custom prompts for common CipherTrust workflows
