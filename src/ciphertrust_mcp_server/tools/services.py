"""Services management tools for CipherTrust Manager."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


class ServiceStatusParams(BaseModel):
    """Parameters for getting service status."""
    service_names: Optional[str] = Field(None, description="Specific service name (e.g., nae-kmip, web)")
    overall_status: bool = Field(False, description="Return overall status of all services")


class ServiceRestartParams(BaseModel):
    """Parameters for restarting services."""
    service_names: Optional[str] = Field(None, description="Specific service name to restart (e.g., nae-kmip, web)")
    yes: bool = Field(True, description="Automatically respond yes to all prompts")
    delay: int = Field(5, description="Delay in seconds before restart")


class ServiceResetParams(BaseModel):
    """Parameters for resetting services."""
    delay: int = Field(5, description="Delay in seconds before reset")


class ServiceManagementTool(BaseTool):
    name = "service_management"
    description = "Service management operations (status, restart, reset)"

    def get_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["status", "restart", "reset"]},
                **ServiceStatusParams.model_json_schema()["properties"],
                **ServiceRestartParams.model_json_schema()["properties"],
                **ServiceResetParams.model_json_schema()["properties"],
            },
            "required": ["action"],
        }

    async def execute(self, action: str, **kwargs: Any) -> Any:
        if action == "status":
            params = ServiceStatusParams(**kwargs)
            args = ["services", "status"]
            if params.overall_status:
                args.append("--overall-status")
            elif params.service_names:
                args.extend(["--service-names", params.service_names])
            result = self.ksctl.execute(args)
            return result.get("data", result.get("stdout", ""))
        elif action == "restart":
            params = ServiceRestartParams(**kwargs)
            args = ["services", "restart"]
            if params.service_names:
                args.extend(["--service-names", params.service_names])
            if params.yes:
                args.append("--yes")
            args.extend(["--delay", str(params.delay)])
            result = self.ksctl.execute(args)
            return result.get("data", result.get("stdout", ""))
        elif action == "reset":
            params = ServiceResetParams(**kwargs)
            warning = (
                "WARNING: This operation will perform a full reset of CipherTrust Manager "
                "and WIPE ALL DATA. This action cannot be undone."
            )
            args = ["services", "reset"]
            args.extend(["--delay", str(params.delay)])
            result = self.ksctl.execute(args)
            if isinstance(result, dict):
                result["warning"] = warning
            return result
        else:
            raise ValueError(f"Unknown action: {action}")

SERVICE_MGMT_TOOLS = [ServiceManagementTool]
