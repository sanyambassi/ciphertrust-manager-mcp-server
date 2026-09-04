"""Main MCP server implementation for CipherTrust Manager."""

import json
import logging
from typing import Any

from mcp.server import Server, ServerRequestContext
from mcp.server.stdio import stdio_server
from mcp.types import (
    CallToolRequestParams,
    CallToolResult,
    GetPromptRequestParams,
    GetPromptResult,
    ListPromptsResult,
    ListResourcesResult,
    ListToolsResult,
    PaginatedRequestParams,
    TextContent,
)

from .config import settings
from .ksctl_cli_manager import get_ksctl_manager
from .tools import ALL_TOOLS

logger = logging.getLogger(__name__)


def _is_closed_stdio(exc: BaseException) -> bool:
    if isinstance(exc, (BrokenPipeError, ConnectionResetError)):
        return True
    return isinstance(exc, ValueError) and "closed file" in str(exc).lower()


class CipherTrustMCPServer:
    """MCP Server for CipherTrust Manager."""

    def __init__(self):
        self.tools: dict[str, Any] = {}
        self._setup_tools()
        self.server = Server(
            settings.mcp_server_name,
            version=settings.mcp_server_version,
            on_list_tools=self._handle_list_tools,
            on_call_tool=self._handle_call_tool,
            on_list_resources=self._handle_list_resources,
            on_list_prompts=self._handle_list_prompts,
            on_get_prompt=self._handle_get_prompt,
        )

    def _setup_tools(self) -> None:
        """Initialize all available tools."""
        logger.info(f"Starting tool registration. Total tools to register: {len(ALL_TOOLS)}")

        for tool_class in ALL_TOOLS:
            logger.info(f"Found tool class: {tool_class.__name__}")

        for tool_class in ALL_TOOLS:
            try:
                logger.info(f"Initializing tool: {tool_class.__name__}")
                tool = tool_class()
                self.tools[tool.name] = tool
                logger.info(f"Successfully registered tool: {tool.name}")
            except Exception as e:
                logger.error(f"Failed to register tool {tool_class.__name__}: {str(e)}", exc_info=True)

        logger.info(f"Tool registration complete. Registered {len(self.tools)} tools")
        logger.info(f"Available tools: {list(self.tools.keys())}")

    async def _handle_list_tools(
        self,
        ctx: ServerRequestContext,
        params: PaginatedRequestParams | None,
    ) -> ListToolsResult:
        """List all available tools."""
        return ListToolsResult(tools=[tool.to_mcp_tool() for tool in self.tools.values()])

    async def _handle_call_tool(
        self,
        ctx: ServerRequestContext,
        params: CallToolRequestParams,
    ) -> CallToolResult:
        """Handle tool execution."""
        name = params.name
        arguments = params.arguments or {}
        if name not in self.tools:
            return CallToolResult(
                content=[TextContent(type="text", text=f"Unknown tool: {name}")],
                is_error=True,
            )

        try:
            result = await self.tools[name].execute(**arguments)
            text = json.dumps(result, indent=2) if isinstance(result, (dict, list)) else str(result)
            return CallToolResult(content=[TextContent(type="text", text=text)])
        except Exception as e:
            logger.error(f"Tool execution failed: {e}")
            return CallToolResult(
                content=[TextContent(type="text", text=f"Tool execution failed: {e}")],
                is_error=True,
            )

    async def _handle_list_resources(
        self,
        ctx: ServerRequestContext,
        params: PaginatedRequestParams | None,
    ) -> ListResourcesResult:
        """List available resources."""
        return ListResourcesResult(resources=[])

    async def _handle_list_prompts(
        self,
        ctx: ServerRequestContext,
        params: PaginatedRequestParams | None,
    ) -> ListPromptsResult:
        """List available prompts."""
        return ListPromptsResult(prompts=[])

    async def _handle_get_prompt(
        self,
        ctx: ServerRequestContext,
        params: GetPromptRequestParams,
    ) -> GetPromptResult:
        """Handle get prompt requests."""
        raise ValueError(f"Unknown prompt: {params.name}")

    async def run(self) -> None:
        """Run the MCP server over stdio."""
        logger.info(f"Starting {settings.mcp_server_name} v{settings.mcp_server_version}")

        try:
            ksctl = get_ksctl_manager()
            if ksctl.test_connection():
                logger.info("Successfully connected to CipherTrust Manager")
            else:
                logger.warning("Failed to connect to CipherTrust Manager")
        except Exception as e:
            logger.error(f"Error testing connection: {e}")

        logger.info("MCP server ready and waiting for JSON-RPC messages on stdin...")

        try:
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(
                    read_stream,
                    write_stream,
                    self.server.create_initialization_options(),
                )
        except Exception as e:
            if _is_closed_stdio(e):
                logger.info("MCP client closed the stdio connection")
                return
            raise
