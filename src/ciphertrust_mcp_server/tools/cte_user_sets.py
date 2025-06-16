"""CTE User Sets management tools for CipherTrust Manager with built-in domain support.

User Set JSON Structure:
{
    "name": "string",
    "description": "string",
    "users": [
        {
            "uname": "string",       // Username only, no domain
            "uid": integer,          // Optional user ID
            "gname": "string",       // Optional group name
            "gid": integer,          // Optional group ID
            "os_domain": "string"    // Domain name for Windows users (e.g., "DOMAIN" or "domain.local")
        }
    ]
}

Example for Windows domain users:
- For DOMAIN\\username: use uname="username", os_domain="DOMAIN"
- For user@domain.local: use uname="user", os_domain="domain.local"
"""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# CTE User Set Parameter Models
class CTEUserSetCreateParams(BaseModel):
    """Parameters for creating a CTE user set."""
    user_json: Optional[str] = Field(None, description="UserSet parameters in JSON format (string)")
    user_json_file: Optional[str] = Field(None, description="UserSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create user set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetListParams(BaseModel):
    """Parameters for listing CTE user sets."""
    limit: int = Field(10, description="Maximum number of user sets to return")
    skip: int = Field(0, description="Index of the first user set to return")
    user_set_name: Optional[str] = Field(None, description="Filter by user set name")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list user sets from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetGetParams(BaseModel):
    """Parameters for getting a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get user set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetDeleteParams(BaseModel):
    """Parameters for deleting a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete user set from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetModifyParams(BaseModel):
    """Parameters for modifying a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    user_json: Optional[str] = Field(None, description="UserSet parameters in JSON format (string)")
    user_json_file: Optional[str] = Field(None, description="UserSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify user set in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetAddUsersParams(BaseModel):
    """Parameters for adding users to a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    user_json_file: str = Field(..., description="UserSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add users in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetDeleteUserParams(BaseModel):
    """Parameters for deleting a user from a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    user_index_list: str = Field(..., description="Comma-separated list of user indices to delete")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete user from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetUpdateUserParams(BaseModel):
    """Parameters for updating a user in a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    user_index: str = Field(..., description="Index of user in CTE UserSet")
    user_json_file: str = Field(..., description="UserSet parameters in JSON format (file)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to update user in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetListUsersParams(BaseModel):
    """Parameters for listing users in a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of users to return")
    skip: int = Field(0, description="Index of the first user to return")
    search: Optional[str] = Field(None, description="Filter any resource")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list users from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEUserSetListPoliciesParams(BaseModel):
    """Parameters for listing policies associated with a CTE user set."""
    user_set_identifier: str = Field(..., description="Identifier for CTE UserSet (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of policies to return")
    skip: int = Field(0, description="Index of the first policy to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list policies from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# CTE User Set Management Tools
class CTEUserSetManagementTool(BaseTool):
    """Manage CTE user sets (grouped)."""

    @property
    def name(self) -> str:
        return "cte_user_set_management"

    @property
    def description(self) -> str:
        return "Manage CTE user sets (create, list, get, delete, modify, add_users, delete_user, update_user, list_users, list_policies)"

    def get_schema(self) -> dict[str, Any]:
        return {
            "title": "CTEUserSetManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["create", "list", "get", "delete", "modify", "add_users", "delete_user", "update_user", "list_users", "list_policies"],
                    "description": "Action to perform"
                },
                # Merge all params from the old tool classes
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if action == "create":
            params = CTEUserSetCreateParams(**kwargs)
            if not params.user_json and not params.user_json_file:
                raise ValueError("Either user_json or user_json_file must be specified")
            args = ["cte", "user-sets", "create"]
            if params.user_json:
                args.extend(["--user-json", params.user_json])
            elif params.user_json_file:
                args.extend(["--user-json-file", params.user_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list":
            params = CTEUserSetListParams(**kwargs)
            args = ["cte", "user-sets", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.user_set_name:
                args.extend(["--user-set-name", params.user_set_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = CTEUserSetGetParams(**kwargs)
            args = ["cte", "user-sets", "get"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = CTEUserSetDeleteParams(**kwargs)
            args = ["cte", "user-sets", "delete"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = CTEUserSetModifyParams(**kwargs)
            if not params.user_json and not params.user_json_file:
                raise ValueError("Either user_json or user_json_file must be specified")
            args = ["cte", "user-sets", "modify"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            if params.user_json:
                args.extend(["--user-json", params.user_json])
            elif params.user_json_file:
                args.extend(["--user-json-file", params.user_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "add_users":
            params = CTEUserSetAddUsersParams(**kwargs)
            args = ["cte", "user-sets", "add-users"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            args.extend(["--user-json-file", params.user_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete_user":
            params = CTEUserSetDeleteUserParams(**kwargs)
            args = ["cte", "user-sets", "delete-user"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            args.extend(["--user-index-list", params.user_index_list])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "update_user":
            params = CTEUserSetUpdateUserParams(**kwargs)
            args = ["cte", "user-sets", "update-user"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            args.extend(["--user-index", params.user_index])
            args.extend(["--user-json-file", params.user_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_users":
            params = CTEUserSetListUsersParams(**kwargs)
            args = ["cte", "user-sets", "list-users"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.search:
                args.extend(["--search", params.search])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_policies":
            params = CTEUserSetListPoliciesParams(**kwargs)
            args = ["cte", "user-sets", "list-policies"]
            args.extend(["--user-set-identifier", params.user_set_identifier])
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")


# Export only the grouped tool
CTE_USER_SET_TOOLS = [CTEUserSetManagementTool]
