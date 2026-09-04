"""Main entry point for CipherTrust MCP Server."""

import asyncio
import logging
import sys

from .config import settings
from .server import CipherTrustMCPServer


def setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(sys.stderr)],
    )
    if not settings.debug_mode:
        logging.getLogger("httpx").setLevel(logging.WARNING)


async def async_main() -> None:
    """Async main function."""
    setup_logging()
    
    server = CipherTrustMCPServer()
    await server.run()


def _is_closed_stdio(exc: BaseException) -> bool:
    if isinstance(exc, (BrokenPipeError, ConnectionResetError, KeyboardInterrupt)):
        return True
    return isinstance(exc, ValueError) and "closed file" in str(exc).lower()


def main() -> None:
    """Main entry point."""
    try:
        asyncio.run(async_main())
    except Exception as e:
        if _is_closed_stdio(e):
            return
        logging.error(f"Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
