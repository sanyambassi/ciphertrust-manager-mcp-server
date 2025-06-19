"""CTE Process Sets management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# CTE Process Set Parameter Models
class CTEProcessSetCreateParams(BaseModel):
    """Parameters for creating a CTE process set."""
    process_json: Optional[str] = Field(None, description="ProcessSet parameters in JSON format (string)")
    process_json_file: Optional[str] = Field(None, description="ProcessSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create process set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetListParams(BaseModel):
    """Parameters for listing CTE process sets."""
    limit: int = Field(10, description="Maximum number of process sets to return")
    skip: int = Field(0, description="Index of the first process set to return")
    process_set_name: Optional[str] = Field(None, description="Filter by process set name")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list process sets from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetGetParams(BaseModel):
    """Parameters for getting a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get process set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetDeleteParams(BaseModel):
    """Parameters for deleting a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete process set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetModifyParams(BaseModel):
    """Parameters for modifying a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    process_json: Optional[str] = Field(None, description="ProcessSet parameters in JSON format (string)")
    process_json_file: Optional[str] = Field(None, description="ProcessSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify process set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetAddProcessesParams(BaseModel):
    """Parameters for adding processes to a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    process_json_file: str = Field(..., description="ProcessSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add processes in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetDeleteProcessParams(BaseModel):
    """Parameters for deleting a process from a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    process_index_list: str = Field(..., description="Comma-separated list of process indices to delete")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete process from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetUpdateProcessParams(BaseModel):
    """Parameters for updating a process in a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    process_index: str = Field(..., description="Index of process in CTE ProcessSet")
    process_json_file: str = Field(..., description="ProcessSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to update process in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetListProcessesParams(BaseModel):
    """Parameters for listing processes in a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of processes to return")
    skip: int = Field(0, description="Index of the first process to return")
    search: Optional[str] = Field(None, description="Filter any resource")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list processes from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProcessSetListPoliciesParams(BaseModel):
    """Parameters for listing policies associated with a CTE process set."""
    process_set_identifier: str = Field(..., description="Identifier for CTE ProcessSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of policies to return")
    skip: int = Field(0, description="Index of the first policy to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list policies from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# CTE Process Set Management Tools
class CTEProcessSetManagementTool(BaseTool):
    """Manage CTE process sets (grouped)."""

    @property
    def name(self) -> str:
        return "cte_process_set_management"

    @property
    def description(self) -> str:
        return "Manage CTE process sets (create, list, get, delete, modify, add_processes, delete_process, update_process, list_processes, list_policies)"

    def get_schema(self) -> dict[str, Any]:
        return {
            "title": "CTEProcessSetManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["create", "list", "get", "delete", "modify", "add_processes", "delete_process", "update_process", "list_processes", "list_policies"],
                    "description": "Action to perform"
                },
                # Merge all params from the old tool classes
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if action == "create":
            params = CTEProcessSetCreateParams(**kwargs)
            if not params.process_json and not params.process_json_file:
                raise ValueError("Either process_json or process_json_file must be specified")
            args = ["cte", "process-sets", "create"]
            if params.process_json:
                args.extend(["--process-json", params.process_json])
            elif params.process_json_file:
                args.extend(["--process-json-file", params.process_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list":
            params = CTEProcessSetListParams(**kwargs)
            args = ["cte", "process-sets", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.process_set_name:
                args.extend(["--process-set-name", params.process_set_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = CTEProcessSetGetParams(**kwargs)
            args = ["cte", "process-sets", "get"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = CTEProcessSetDeleteParams(**kwargs)
            args = ["cte", "process-sets", "delete"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = CTEProcessSetModifyParams(**kwargs)
            if not params.process_json and not params.process_json_file:
                raise ValueError("Either process_json or process_json_file must be specified")
            args = ["cte", "process-sets", "modify"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            if params.process_json:
                args.extend(["--process-json", params.process_json])
            elif params.process_json_file:
                args.extend(["--process-json-file", params.process_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "add_processes":
            params = CTEProcessSetAddProcessesParams(**kwargs)
            args = ["cte", "process-sets", "add-processes"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            args.extend(["--process-json-file", params.process_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete_process":
            params = CTEProcessSetDeleteProcessParams(**kwargs)
            args = ["cte", "process-sets", "delete-process"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            args.extend(["--process-index-list", params.process_index_list])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "update_process":
            params = CTEProcessSetUpdateProcessParams(**kwargs)
            args = ["cte", "process-sets", "update-process"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            args.extend(["--process-index", params.process_index])
            args.extend(["--process-json-file", params.process_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_processes":
            params = CTEProcessSetListProcessesParams(**kwargs)
            args = ["cte", "process-sets", "list-processes"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.search:
                args.extend(["--search", params.search])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_policies":
            params = CTEProcessSetListPoliciesParams(**kwargs)
            args = ["cte", "process-sets", "list-policies"]
            args.extend(["--process-set-identifier", params.process_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")


# Export only the grouped tool
CTE_PROCESS_SET_TOOLS = [CTEProcessSetManagementTool]
