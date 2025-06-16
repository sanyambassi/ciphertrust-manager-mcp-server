"""Template management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# Core CRUD Parameter Models
class TemplateListParams(BaseModel):
    """Parameters for listing templates."""
    limit: Optional[int] = Field(None, description="Maximum number of templates to return")
    skip: Optional[int] = Field(None, description="Offset at which to start the search")
    name: Optional[str] = Field(None, description="Filter by template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Filter by template ID")
    alg: Optional[str] = Field(None, description="Filter by algorithm (AES, TDES, HMAC-SHA1, etc.)")
    size: Optional[int] = Field(None, description="Filter by template size in bits")
    curve_id: Optional[str] = Field(None, description="Filter by elliptic curve ID")
    usage_mask: Optional[int] = Field(None, description="Filter by template usage mask")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list templates from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateCreateParams(BaseModel):
    """Parameters for creating a template."""
    name: str = Field(..., description="Template name (no special characters like <,> or \\)")
    alg: Optional[str] = Field(None, description="Template algorithm (AES, TDES, HMAC-SHA1, HMAC-SHA256, etc.)")
    size: Optional[int] = Field(None, description="Template size in bits")
    curve_id: Optional[str] = Field(None, description="Elliptic curve ID for EC templates")
    usage_mask: Optional[int] = Field(None, description="Template usage mask")
    ownerid: Optional[str] = Field(None, description="The user's ID")
    nodelete: bool = Field(False, description="Objects created using this template cannot be deleted")
    noexport: bool = Field(False, description="Objects created using this template cannot be exported")
    activation_date: Optional[str] = Field(None, description="Date/time the object becomes active")
    deactivation_date: Optional[str] = Field(None, description="Date/time the object becomes inactive")
    archive_date: Optional[str] = Field(None, description="Date/time the object becomes archived")
    process_start_date: Optional[str] = Field(None, description="Date/time when object may begin processing crypto operations")
    process_stop_date: Optional[str] = Field(None, description="Date/time after which object will not be used for crypto protection")
    jsonfile: Optional[str] = Field(None, description="JSON file with template parameters")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create template in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateGetParams(BaseModel):
    """Parameters for getting a template."""
    name: Optional[str] = Field(None, description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Template ID")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateDeleteParams(BaseModel):
    """Parameters for deleting a template."""
    name: Optional[str] = Field(None, description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Template ID")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateModifyParams(BaseModel):
    """Parameters for modifying a template."""
    name: str = Field(..., description="Template name, ID, URI, or alias")
    nodelete: Optional[bool] = Field(None, description="Objects created using this template cannot be deleted")
    noexport: Optional[bool] = Field(None, description="Objects created using this template cannot be exported")
    activation_date: Optional[str] = Field(None, description="Date/time the object becomes active")
    deactivation_date: Optional[str] = Field(None, description="Date/time the object becomes inactive")
    process_start_date: Optional[str] = Field(None, description="Date/time when object may begin processing crypto operations")
    process_stop_date: Optional[str] = Field(None, description="Date/time after which object will not be used for crypto protection")
    usage_mask: Optional[int] = Field(None, description="Template usage mask")
    jsonfile: Optional[str] = Field(None, description="JSON file with template modification parameters")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify template in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Tool Implementations - Core CRUD
class TemplateManagementTool(BaseTool):
    name = "template_management"
    description = "Template management operations (list, create, get, delete, modify)"

    def get_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["list", "create", "get", "delete", "modify"]},
                **TemplateListParams.model_json_schema()["properties"],
                **TemplateCreateParams.model_json_schema()["properties"],
                **TemplateGetParams.model_json_schema()["properties"],
                **TemplateDeleteParams.model_json_schema()["properties"],
                **TemplateModifyParams.model_json_schema()["properties"],
            },
            "required": ["action"],
        }

    async def execute(self, action: str, **kwargs: Any) -> Any:
        if action == "list":
            params = TemplateListParams(**kwargs)
            args = ["template", "list"]
            if params.limit is not None:
                args.extend(["--limit", str(params.limit)])
            if params.skip is not None:
                args.extend(["--skip", str(params.skip)])
            if params.name:
                args.extend(["--name", params.name])
            if params.id:
                args.extend(["--id", params.id])
            if params.alg:
                args.extend(["--alg", params.alg])
            if params.size is not None:
                args.extend(["--size", str(params.size)])
            if params.curve_id:
                args.extend(["--curve-id", params.curve_id])
            if params.usage_mask is not None:
                args.extend(["--usage-mask", str(params.usage_mask)])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "create":
            params = TemplateCreateParams(**kwargs)
            args = ["template", "create", "--name", params.name]
            if params.alg:
                args.extend(["--alg", params.alg])
            if params.size is not None:
                args.extend(["--size", str(params.size)])
            if params.curve_id:
                args.extend(["--curve-id", params.curve_id])
            if params.usage_mask is not None:
                args.extend(["--usage-mask", str(params.usage_mask)])
            if params.ownerid:
                args.extend(["--ownerid", params.ownerid])
            if params.nodelete:
                args.append("--nodelete")
            if params.noexport:
                args.append("--noexport")
            if params.activation_date:
                args.extend(["--activationdate", params.activation_date])
            if params.deactivation_date:
                args.extend(["--deactivationdate", params.deactivation_date])
            if params.archive_date:
                args.extend(["--archivedate", params.archive_date])
            if params.process_start_date:
                args.extend(["--processstartdate", params.process_start_date])
            if params.process_stop_date:
                args.extend(["--processstopdate", params.process_stop_date])
            if params.jsonfile:
                args.extend(["--jsonfile", params.jsonfile])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = TemplateGetParams(**kwargs)
            if not params.name and not params.id:
                raise ValueError("Either name or id must be specified")
            args = ["template", "get"]
            if params.name:
                args.extend(["--name", params.name])
            elif params.id:
                args.extend(["--id", params.id])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = TemplateDeleteParams(**kwargs)
            if not params.name and not params.id:
                raise ValueError("Either name or id must be specified")
            args = ["template", "delete"]
            if params.name:
                args.extend(["--name", params.name])
            elif params.id:
                args.extend(["--id", params.id])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = TemplateModifyParams(**kwargs)
            args = ["template", "modify", "--name", params.name]
            if params.nodelete is not None:
                args.extend(["--nodelete", "true" if params.nodelete else "false"])
            if params.noexport is not None:
                args.extend(["--noexport", "true" if params.noexport else "false"])
            if params.activation_date:
                args.extend(["--activationdate", params.activation_date])
            if params.deactivation_date:
                args.extend(["--deactivationdate", params.deactivation_date])
            if params.process_start_date:
                args.extend(["--processstartdate", params.process_start_date])
            if params.process_stop_date:
                args.extend(["--processstopdate", params.process_stop_date])
            if params.usage_mask is not None:
                args.extend(["--usage-mask", str(params.usage_mask)])
            if params.jsonfile:
                args.extend(["--jsonfile", params.jsonfile])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")

TEMPLATE_TOOLS = [TemplateManagementTool]
