"""Template management tools for CipherTrust Manager with built-in domain support."""

import json
from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# Core CRUD Parameter Models
class TemplateListParams(BaseModel):
    """Parameters for listing templates."""
    limit: Optional[int] = Field(None, description="Maximum number of templates to return")
    skip: Optional[int] = Field(None, description="Offset at which to start the search")
    name: Optional[str] = Field(None, description="Filter by template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    labels_query: Optional[str] = Field(None, description="Filter by label selector expressions")
    created_after: Optional[str] = Field(None, description="Time after which the template is created")
    created_before: Optional[str] = Field(None, description="Time before which the template is created")
    meta_contains: Optional[str] = Field(None, description="Search for Meta Data in Template")
    key_attributes_contains: Optional[str] = Field(None, description="Search for Key Attributes in Template")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list templates from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateCreateParams(BaseModel):
    """Parameters for creating a template."""
    name: str = Field(..., description="Template name (no special characters like <,> or \\)")
    desc: Optional[str] = Field(None, description="Template description")
    labels: Optional[str] = Field(None, description="Comma-separated key=value labels")
    meta: Optional[str] = Field(None, description="Meta information in JSON format")
    key_attributes: Optional[str] = Field(None, description="Key attributes in JSON format")
    template_jsonfile: Optional[str] = Field(None, description="Template information passed in JSON format via a file")
    
    # Individual key attribute parameters (for easier use)
    algorithm: Optional[str] = Field(None, description="Template algorithm (AES, RSA, EC, etc.)")
    size: Optional[int] = Field(None, description="Template size in bits")
    curve_id: Optional[str] = Field(None, description="Elliptic curve ID for EC templates")
    usage_mask: Optional[int] = Field(None, description="Template usage mask")
    undeletable: Optional[bool] = Field(None, description="Template cannot be deleted")
    unexportable: Optional[bool] = Field(None, description="Template cannot be exported")
    activation_date: Optional[str] = Field(None, description="Date/time the object becomes active")
    archive_date: Optional[str] = Field(None, description="Date/time the object becomes archived")
    deactivation_date: Optional[str] = Field(None, description="Date/time the object becomes inactive")
    process_start_date: Optional[str] = Field(None, description="Date/time when object may begin processing crypto operations")
    process_stop_date: Optional[str] = Field(None, description="Date/time after which object will not be used for crypto protection")
    
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create template in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateGetParams(BaseModel):
    """Parameters for getting a template."""
    name: str = Field(..., description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateDeleteParams(BaseModel):
    """Parameters for deleting a template."""
    name: str = Field(..., description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateModifyParams(BaseModel):
    """Parameters for modifying a template."""
    name: str = Field(..., description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    desc: Optional[str] = Field(None, description="Template description")
    labels: Optional[str] = Field(None, description="Comma-separated key=value labels")
    meta: Optional[str] = Field(None, description="Meta information in JSON format")
    key_attributes: Optional[str] = Field(None, description="Key attributes in JSON format")
    template_jsonfile: Optional[str] = Field(None, description="Template information passed in JSON format via a file")
    
    # Individual key attribute parameters (for easier use)
    algorithm: Optional[str] = Field(None, description="Template algorithm")
    size: Optional[int] = Field(None, description="Template size in bits")
    curve_id: Optional[str] = Field(None, description="Elliptic curve ID for EC templates")
    usage_mask: Optional[int] = Field(None, description="Template usage mask")
    undeletable: Optional[bool] = Field(None, description="Template cannot be deleted")
    unexportable: Optional[bool] = Field(None, description="Template cannot be exported")
    
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
                # List parameters
                "limit": {"anyOf": [{"type": "integer"}, {"type": "number"}, {"type": "null"}], "description": "Maximum number of templates to return"},
                "skip": {"anyOf": [{"type": "integer"}, {"type": "number"}, {"type": "null"}], "description": "Offset at which to start the search"},
                "name": {"type": "string", "description": "Template name, ID, URI, or alias"},
                "id": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Template ID"},
                "labels_query": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Filter by label selector expressions"},
                "created_after": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Time after which the template is created"},
                "created_before": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Time before which the template is created"},
                "meta_contains": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Search for Meta Data in Template"},
                "key_attributes_contains": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Search for Key Attributes in Template"},
                
                # Create/Update parameters
                "desc": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Template description"},
                "labels": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Comma-separated key=value labels"},
                "meta": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Meta information in JSON format"},
                "key_attributes": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Key attributes in JSON format"},
                "template_jsonfile": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Template information passed in JSON format via a file"},
                
                # Individual key attribute parameters
                "algorithm": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Template algorithm (AES, RSA, EC, etc.)"},
                "size": {"anyOf": [{"type": "integer"}, {"type": "number"}, {"type": "null"}], "description": "Template size in bits"},
                "curve_id": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Elliptic curve ID for EC templates"},
                "usage_mask": {"anyOf": [{"type": "integer"}, {"type": "number"}, {"type": "null"}], "description": "Template usage mask"},
                "undeletable": {"anyOf": [{"type": "boolean"}, {"type": "null"}], "description": "Template cannot be deleted"},
                "unexportable": {"anyOf": [{"type": "boolean"}, {"type": "null"}], "description": "Template cannot be exported"},
                "activation_date": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Date/time the object becomes active"},
                "archive_date": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Date/time the object becomes archived"},
                "deactivation_date": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Date/time the object becomes inactive"},
                "process_start_date": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Date/time when object may begin processing crypto operations"},
                "process_stop_date": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Date/time after which object will not be used for crypto protection"},
                "ownerid": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "The user's ID"},
                "nodelete": {"anyOf": [{"type": "boolean"}, {"type": "null"}], "description": "Objects created using this template cannot be deleted"},
                "noexport": {"anyOf": [{"type": "boolean"}, {"type": "null"}], "description": "Objects created using this template cannot be exported"},
                
                # Domain parameters
                "domain": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Domain to operate in"},
                "auth_domain": {"anyOf": [{"type": "string"}, {"type": "null"}], "description": "Authentication domain"},
            },
            "required": ["action"],
            "allOf": [
                {
                    "if": {"properties": {"action": {"enum": ["create"]}}},
                    "then": {"required": ["action", "name"]}
                },
                {
                    "if": {"properties": {"action": {"enum": ["get", "delete", "modify"]}}},
                    "then": {"required": ["action", "name"]}
                }
            ]
        }

    def _build_key_attributes_from_params(self, **kwargs) -> Optional[str]:
        """Build key_attributes JSON from individual parameters."""
        key_attrs = {}
        
        # Map individual parameters to key_attributes
        if kwargs.get('algorithm'):
            key_attrs['algorithm'] = kwargs['algorithm']
        if kwargs.get('size') is not None:
            key_attrs['size'] = kwargs['size']
        if kwargs.get('curve_id'):
            key_attrs['curveid'] = kwargs['curve_id']  # Note: API uses 'curveid'
        if kwargs.get('usage_mask') is not None:
            key_attrs['usageMask'] = kwargs['usage_mask']
        if kwargs.get('undeletable') is not None:
            key_attrs['undeletable'] = kwargs['undeletable']
        if kwargs.get('unexportable') is not None:
            key_attrs['unexportable'] = kwargs['unexportable']
        if kwargs.get('activation_date'):
            key_attrs['activationDate'] = kwargs['activation_date']
        if kwargs.get('archive_date'):
            key_attrs['archiveDate'] = kwargs['archive_date']
        if kwargs.get('deactivation_date'):
            key_attrs['deactivationDate'] = kwargs['deactivation_date']
        if kwargs.get('process_start_date'):
            key_attrs['processStartDate'] = kwargs['process_start_date']
        if kwargs.get('process_stop_date'):
            key_attrs['processStopDate'] = kwargs['process_stop_date']  # Fixed: use processStopDate instead of protectStopDate
            
        return json.dumps(key_attrs) if key_attrs else None

    async def execute(self, action: str, **kwargs: Any) -> Any:
        try:
            if action == "list":
                params = TemplateListParams(**kwargs)
                args = ["templates", "list"]
                
                if params.limit is not None:
                    args.extend(["--limit", str(params.limit)])
                if params.skip is not None:
                    args.extend(["--skip", str(params.skip)])
                if params.name:
                    args.extend(["--name", params.name])
                if params.id:
                    args.extend(["--id", params.id])
                if params.labels_query:
                    args.extend(["--labels-query", params.labels_query])
                if params.created_after:
                    args.extend(["--created_after", params.created_after])
                if params.created_before:
                    args.extend(["--created_before", params.created_before])
                if params.meta_contains:
                    args.extend(["--meta_contains", params.meta_contains])
                if params.key_attributes_contains:
                    args.extend(["--key_attributes_contains", params.key_attributes_contains])
                    
                result = self.execute_with_domain(args, params.domain, params.auth_domain)
                return result.get("data", result.get("stdout", ""))
                
            elif action == "create":
                params = TemplateCreateParams(**kwargs)
                args = ["templates", "create", "--name", params.name]
                
                if params.desc:
                    args.extend(["--desc", params.desc])
                if params.labels:
                    args.extend(["--labels", params.labels])
                if params.meta:
                    args.extend(["--meta", params.meta])
                
                # Use provided key_attributes or build from individual parameters
                key_attributes = params.key_attributes
                if not key_attributes:
                    key_attributes = self._build_key_attributes_from_params(**kwargs)
                
                if key_attributes:
                    args.extend(["--key_attributes", key_attributes])
                    
                if params.template_jsonfile:
                    args.extend(["--template_jsonfile", params.template_jsonfile])
                    
                result = self.execute_with_domain(args, params.domain, params.auth_domain)
                return result.get("data", result.get("stdout", ""))
                
            elif action == "get":
                params = TemplateGetParams(**kwargs)
                args = ["templates", "get", "--name", params.name]
                
                if params.id:
                    args.extend(["--id", params.id])
                    
                result = self.execute_with_domain(args, params.domain, params.auth_domain)
                return result.get("data", result.get("stdout", ""))
                
            elif action == "delete":
                params = TemplateDeleteParams(**kwargs)
                args = ["templates", "delete", "--name", params.name]
                
                if params.id:
                    args.extend(["--id", params.id])
                    
                result = self.execute_with_domain(args, params.domain, params.auth_domain)
                return result.get("data", result.get("stdout", ""))
                
            elif action == "modify":
                params = TemplateModifyParams(**kwargs)
                args = ["templates", "modify", "--name", params.name]
                
                if params.id:
                    args.extend(["--id", params.id])
                if params.desc:
                    args.extend(["--desc", params.desc])
                if params.labels:
                    args.extend(["--labels", params.labels])
                if params.meta:
                    args.extend(["--meta", params.meta])
                
                # Use provided key_attributes or build from individual parameters
                key_attributes = params.key_attributes
                if not key_attributes:
                    key_attributes = self._build_key_attributes_from_params(**kwargs)
                
                if key_attributes:
                    args.extend(["--key_attributes", key_attributes])
                    
                if params.template_jsonfile:
                    args.extend(["--template_jsonfile", params.template_jsonfile])
                    
                result = self.execute_with_domain(args, params.domain, params.auth_domain)
                return result.get("data", result.get("stdout", ""))
                
            else:
                raise ValueError(f"Unknown action: {action}")
                
        except Exception as e:
            # Enhanced error handling
            error_msg = str(e)
            if "validation error" in error_msg.lower():
                raise ValueError(f"Parameter validation error: {error_msg}")
            elif "command not found" in error_msg.lower():
                raise ValueError(f"CipherTrust Manager command error: {error_msg}")
            elif "authentication" in error_msg.lower():
                raise ValueError(f"Authentication error: {error_msg}")
            else:
                raise ValueError(f"Template operation failed: {error_msg}")


# Helper functions for building key_attributes JSON
def build_key_attributes_json(**attributes) -> str:
    """
    Build key_attributes JSON string for template creation.
    
    Valid attributes according to ksctl documentation:
    - activationDate: string
    - algorithm: string
    - objectType: string
    - archiveDate: string
    - curveid: string
    - deactivationDate: string
    - meta: {"ownerId": string}
    - processStartDate: string
    - protectStopDate: string
    - size: integer
    - undeletable: boolean
    - unexportable: boolean
    - usageMask: integer
    - format: string
    - xts: boolean
    - state: string
    - description: string
    """
    # Filter out None values
    filtered_attributes = {k: v for k, v in attributes.items() if v is not None}
    
    # Validate known attributes
    valid_attrs = {
        'activationDate', 'algorithm', 'objectType', 'archiveDate', 'curveid',
        'deactivationDate', 'meta', 'processStartDate', 'protectStopDate',
        'size', 'undeletable', 'unexportable', 'usageMask', 'format',
        'xts', 'state', 'description'
    }
    
    unknown_attrs = set(filtered_attributes.keys()) - valid_attrs
    if unknown_attrs:
        raise ValueError(f"Unknown key attributes: {unknown_attrs}")
    
    return json.dumps(filtered_attributes)


def build_meta_json(**meta_data) -> str:
    """Build meta JSON string for template creation."""
    return json.dumps(meta_data)


# Usage examples
def get_template_examples():
    """Get template usage examples."""
    return {
        "create_basic_template_with_individual_params": {
            "action": "create",
            "name": "aes_256_template",
            "desc": "AES 256-bit encryption template",
            "algorithm": "AES",
            "size": 256,
            "usage_mask": 12,  # Encrypt + Decrypt
            "undeletable": False,
            "unexportable": False
        },
        "create_basic_template_with_json": {
            "action": "create",
            "name": "aes_256_template",
            "desc": "AES 256-bit encryption template",
            "key_attributes": build_key_attributes_json(
                algorithm="AES",
                size=256,
                usageMask=12,  # Encrypt + Decrypt
                undeletable=False,
                unexportable=False
            )
        },
        "create_rsa_template": {
            "action": "create", 
            "name": "rsa_2048_template",
            "desc": "RSA 2048-bit signing template",
            "algorithm": "RSA",
            "size": 2048,
            "usage_mask": 8,  # Sign
            "undeletable": True,
            "labels": "key_type=rsa,purpose=signing"
        },
        "create_ec_template": {
            "action": "create",
            "name": "ec_p256_template", 
            "desc": "EC P-256 template",
            "algorithm": "EC",
            "curve_id": "secp256r1",
            "usage_mask": 8  # Sign
        },
        "list_templates": {
            "action": "list",
            "limit": 20
        },
        "list_with_filter": {
            "action": "list",
            "labels_query": "key_type=rsa",
            "limit": 10
        },
        "get_template": {
            "action": "get",
            "name": "aes_256_template"
        },
        "update_template": {
            "action": "modify",
            "name": "aes_256_template",
            "desc": "Updated AES 256-bit encryption template",
            "labels": "key_type=aes,purpose=encryption,updated=true"
        },
        "delete_template": {
            "action": "delete",
            "name": "aes_256_template"
        }
    }


TEMPLATE_TOOLS = [TemplateManagementTool]