"""CTE Resource Sets management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# CTE Resource Set Parameter Models
class CTEResourceSetCreateParams(BaseModel):
    """Parameters for creating a CTE resource set."""
    resource_json: Optional[str] = Field(None, description="ResourceSet parameters in JSON format (string)")
    resource_json_file: Optional[str] = Field(None, description="ResourceSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create resource set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetListParams(BaseModel):
    """Parameters for listing CTE resource sets."""
    limit: int = Field(10, description="Maximum number of resource sets to return")
    skip: int = Field(0, description="Index of the first resource set to return")
    resource_set_name: Optional[str] = Field(None, description="Filter by resource set name")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list resource sets from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetGetParams(BaseModel):
    """Parameters for getting a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get resource set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetDeleteParams(BaseModel):
    """Parameters for deleting a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete resource set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetModifyParams(BaseModel):
    """Parameters for modifying a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    resource_json: Optional[str] = Field(None, description="ResourceSet parameters in JSON format (string)")
    resource_json_file: Optional[str] = Field(None, description="ResourceSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify resource set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetAddResourcesParams(BaseModel):
    """Parameters for adding resources to a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    resource_json_file: str = Field(..., description="ResourceSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add resources in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetDeleteResourceParams(BaseModel):
    """Parameters for deleting a resource from a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    resource_index_list: str = Field(..., description="Comma-separated list of resource indices to delete")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete resource from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetUpdateResourceParams(BaseModel):
    """Parameters for updating a resource in a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    resource_index: str = Field(..., description="Index of resource in CTE ResourceSet")
    resource_json_file: str = Field(..., description="ResourceSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to update resource in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetListResourcesParams(BaseModel):
    """Parameters for listing resources in a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    search: Optional[str] = Field(None, description="Filter any resource")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list resources from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEResourceSetListPoliciesParams(BaseModel):
    """Parameters for listing policies associated with a CTE resource set."""
    resource_set_identifier: str = Field(..., description="Identifier for CTE ResourceSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of policies to return")
    skip: int = Field(0, description="Index of the first policy to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list policies from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# CTE Resource Set Management Tools
class CTEResourceSetManagementTool(BaseTool):
    """Manage CTE resource sets (grouped)."""

    @property
    def name(self) -> str:
        return "cte_resource_set_management"

    @property
    def description(self) -> str:
        return "Manage CTE resource sets (create, list, get, delete, modify, add_resources, delete_resource, update_resource, list_resources, list_policies)"

    def get_schema(self) -> dict[str, Any]:
        return {
            "title": "CTEResourceSetManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["create", "list", "get", "delete", "modify", "add_resources", "delete_resource", "update_resource", "list_resources", "list_policies"],
                    "description": "Action to perform"
                },
                # Merge all params from the old tool classes
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if action == "create":
            params = CTEResourceSetCreateParams(**kwargs)
            if not params.resource_json and not params.resource_json_file:
                raise ValueError("Either resource_json or resource_json_file must be specified")
            args = ["cte", "resource-sets", "create"]
            if params.resource_json:
                args.extend(["--resource-json", params.resource_json])
            elif params.resource_json_file:
                args.extend(["--resource-json-file", params.resource_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list":
            params = CTEResourceSetListParams(**kwargs)
            args = ["cte", "resource-sets", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.resource_set_name:
                args.extend(["--resource-set-name", params.resource_set_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = CTEResourceSetGetParams(**kwargs)
            args = ["cte", "resource-sets", "get"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = CTEResourceSetDeleteParams(**kwargs)
            args = ["cte", "resource-sets", "delete"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = CTEResourceSetModifyParams(**kwargs)
            if not params.resource_json and not params.resource_json_file:
                raise ValueError("Either resource_json or resource_json_file must be specified")
            args = ["cte", "resource-sets", "modify"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            if params.resource_json:
                args.extend(["--resource-json", params.resource_json])
            elif params.resource_json_file:
                args.extend(["--resource-json-file", params.resource_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "add_resources":
            params = CTEResourceSetAddResourcesParams(**kwargs)
            args = ["cte", "resource-sets", "add-resources"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            args.extend(["--resource-json-file", params.resource_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete_resource":
            params = CTEResourceSetDeleteResourceParams(**kwargs)
            args = ["cte", "resource-sets", "delete-resource"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            args.extend(["--resource-index-list", params.resource_index_list])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "update_resource":
            params = CTEResourceSetUpdateResourceParams(**kwargs)
            args = ["cte", "resource-sets", "update-resource"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            args.extend(["--resource-index", params.resource_index])
            args.extend(["--resource-json-file", params.resource_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_resources":
            params = CTEResourceSetListResourcesParams(**kwargs)
            args = ["cte", "resource-sets", "list-resources"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.search:
                args.extend(["--search", params.search])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_policies":
            params = CTEResourceSetListPoliciesParams(**kwargs)
            args = ["cte", "resource-sets", "list-policies"]
            args.extend(["--resource-set-identifier", params.resource_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")


# Export only the grouped tool
CTE_RESOURCE_SET_TOOLS = [CTEResourceSetManagementTool]
