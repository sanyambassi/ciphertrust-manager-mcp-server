"""Base classes for CipherTrust MCP tools with comprehensive domain support."""

from abc import ABC, abstractmethod
from typing import Any, TypeVar, Optional

from mcp.types import Tool
from pydantic import BaseModel

# Import the ksctl manager
try:
    from ..ksctl_cli_manager import KsctlManager, get_ksctl_manager
except ImportError:
    # If import fails, we'll handle it in __init__
    KsctlManager = None
    get_ksctl_manager = None

T = TypeVar("T", bound=BaseModel)


class BaseTool(ABC):
    """Base class for all CipherTrust MCP tools with domain support."""

    def __init__(self):
        if get_ksctl_manager:
            self.ksctl = get_ksctl_manager()  # type: ignore
        else:
            self.ksctl = None

    @property
    @abstractmethod
    def name(self) -> str:
        """Tool name."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Tool description."""
        pass

    @abstractmethod
    def get_schema(self) -> dict[str, Any]:
        """Get the JSON schema for tool parameters."""
        pass

    @abstractmethod
    async def execute(self, **kwargs: Any) -> Any:
        """Execute the tool with given parameters."""
        pass

    def execute_with_domain(self, args: list[str], domain: Optional[str] = None, auth_domain: Optional[str] = None) -> dict[str, Any]:
        """Execute ksctl command with optional domain override.
        
        This method allows executing commands in a specific domain without changing
        global settings. It temporarily modifies the command arguments to include
        domain parameters.
        
        Args:
            args: Base command arguments (e.g., ["users", "list"])
            domain: Optional domain override for this operation
            auth_domain: Optional auth domain override for this operation
            
        Returns:
            Command execution result
        """
        # Clone args to avoid modifying the original
        domain_args = args.copy()
        
        # Add domain parameters if specified
        if domain:
            domain_args.extend(["--domain", domain])
        if auth_domain:
            domain_args.extend(["--auth-domain", auth_domain])
        
        return self.ksctl.execute(domain_args)
    
    def execute_with_global_domain_override(self, args: list[str], domain: Optional[str], auth_domain: Optional[str]) -> dict[str, Any]:
        """Execute command with temporary global domain settings override.
        
        This method temporarily changes the global domain settings, executes the command,
        then restores the original settings. Use this when the command doesn't support
        --domain flags directly.
        
        Args:
            args: Base command arguments
            domain: Optional domain override
            auth_domain: Optional auth domain override
            
        Returns:
            Command execution result
        """
        from ..config import settings
        
        # Store original settings
        original_domain = settings.ciphertrust_domain
        original_auth_domain = settings.ciphertrust_auth_domain
        
        try:
            # Temporarily override settings
            if domain:
                settings.ciphertrust_domain = domain
            if auth_domain:
                settings.ciphertrust_auth_domain = auth_domain
            
            # Execute with overridden settings
            return self.ksctl.execute(args)
        
        finally:
            # Restore original settings
            settings.ciphertrust_domain = original_domain
            settings.ciphertrust_auth_domain = original_auth_domain

    # New helper methods for connection management tools
    def get_domain_auth_params(self) -> dict[str, Any]:
        """Get standard domain and auth-domain parameters."""
        return {
            "domain": {
                "type": "string",
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "default": None,
                "description": "The CipherTrust Manager Domain that the command will operate in",
                "title": "Domain"
            },
            "auth_domain": {
                "type": "string", 
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "default": None,
                "description": "The CipherTrust Manager Domain where the user is created",
                "title": "Auth Domain"
            }
        }

    def add_domain_auth_params(self, cmd: list[str], kwargs: dict[str, Any]) -> None:
        """Add domain and auth-domain parameters to command if specified."""
        if kwargs.get("domain"):
            cmd.extend(["--domain", kwargs["domain"]])
        if kwargs.get("auth_domain"):
            cmd.extend(["--auth-domain", kwargs["auth_domain"]])

    def execute_command(self, cmd: list[str]) -> str:
        """Execute a ksctl command and return the result."""
        try:
            # Use the ksctl manager
            result = self.ksctl.execute(cmd)
            
            # Return the data or stdout
            if result.get("data"):
                if isinstance(result["data"], str):
                    return result["data"]
                else:
                    import json
                    return json.dumps(result["data"], indent=2)
            else:
                return result.get("stdout", "")
                
        except Exception as e:
            return f"Error executing command: {str(e)}"

    def to_mcp_tool(self) -> Tool:
        """Convert to MCP Tool definition."""
        return Tool(
            name=self.name,
            description=self.description,
            inputSchema=self.get_schema(),
        )
