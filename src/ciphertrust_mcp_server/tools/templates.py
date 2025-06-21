"""Template management tools for CipherTrust Manager with built-in domain support.

This module provides comprehensive template management capabilities for CipherTrust Manager,
including creating, listing, getting, updating, and deleting templates. It supports individual
parameter specification for easy key attribute configuration as well as advanced JSON-based
configurations for complex scenarios.

Key Features:
- Full CRUD operations for templates (Create, Read, Update, Delete)
- Domain and authentication domain support for multi-tenant environments
- Individual parameter support for easy key attribute specification
- JSON-based key_attributes for advanced configurations
- Automatic template ID lookup by name for user-friendly operations
- Comprehensive error handling and validation
- Support for all CipherTrust Manager template types (AES, RSA, EC, etc.)

Smart Template Modification:
The tool automatically handles template identification for modify operations:
- Users can specify 'id' for direct template identification (fastest)
- Users can specify 'template_name' for name-based identification (user-friendly)
- The tool automatically performs ID lookup when template name is provided

All operations support domain-specific execution, making it suitable for enterprise
multi-tenant CipherTrust Manager deployments.
"""

import json
from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# Core CRUD Parameter Models
class TemplateListParams(BaseModel):
    """Parameters for listing templates.
    
    Supports filtering by name, labels, creation dates, and metadata. Includes pagination
    controls and search capabilities. All operations support domain-specific execution.
    """
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
    """Parameters for creating a template.
    
    Supports creation of templates with key attributes, metadata, and labels.
    Can accept either individual key attribute parameters or a complete JSON
    specification. All operations support domain-specific execution.
    """
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
    """Parameters for getting a template.
    
    Retrieves detailed information about a specific template by name, ID, URI, or alias.
    Supports domain-specific execution for multi-tenant environments.
    """
    name: str = Field(..., description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateDeleteParams(BaseModel):
    """Parameters for deleting a template.
    
    Deletes a template by name, ID, URI, or alias. Includes safety checks
    and domain-specific execution for secure template management.
    """
    name: str = Field(..., description="Template name, ID, URI, or alias")
    id: Optional[str] = Field(None, description="Specify the type of identifier (name, id, uri, alias)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete template from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class TemplateModifyParams(BaseModel):
    """Parameters for modifying a template.
    
    Updates template properties including name, description, key attributes, and metadata.
    Supports both direct ID specification and automatic ID lookup by template name.
    Template identification can be done via either 'id' (direct) or 'template_name' (lookup).
    All operations support domain-specific execution.
    """
    id: Optional[str] = Field(None, description="Template ID for modification (if known)")
    template_name: Optional[str] = Field(None, description="Template name to identify which template to modify")
    name: Optional[str] = Field(None, description="New name for the template")
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
    """Manage templates in CipherTrust Manager.
    
    This tool provides comprehensive template management capabilities including:
    - Basic template operations (list, create, get, delete, modify)
    - Key attribute management with individual parameters or JSON specification
    - Automatic template ID lookup by name for user-friendly operations
    - Domain and authentication domain support for multi-tenant environments
    
    All operations support domain-specific execution and include proper error handling
    and response formatting.
    """

    @property
    def name(self) -> str:
        return "template_management"

    @property
    def description(self) -> str:
        return "Template management operations (list, create, get, delete, modify)"

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
            "allOf": [
                {
                    "if": {"properties": {"action": {"enum": ["create"]}}},
                    "then": {"required": ["action", "name"]}
                },
                {
                    "if": {"properties": {"action": {"enum": ["get", "delete"]}}},
                    "then": {"required": ["action", "name"]}
                },
                {
                    "if": {"properties": {"action": {"enum": ["modify"]}}},
                    "then": {
                        "anyOf": [
                            {"required": ["action", "id"]},
                            {"required": ["action", "template_name"]}
                        ]
                    }
                }
            ]
        }

    def _build_key_attributes_from_params(self, **kwargs) -> Optional[str]:
        """
        Build key_attributes JSON from individual parameters.
        
        This method converts individual key attribute parameters into a JSON string
        that can be used with the ksctl --key_attributes parameter.
        
        Args:
            **kwargs: Individual key attribute parameters
            
        Returns:
            JSON string of key attributes or None if no attributes specified
            
        Raises:
            ValueError: If size value cannot be converted to integer
        """
        key_attrs = {}
        
        # Map individual parameters to key_attributes
        if kwargs.get('algorithm'):
            key_attrs['algorithm'] = kwargs['algorithm']
        if kwargs.get('size') is not None:
            # Ensure size is an integer
            size_val = kwargs['size']
            if isinstance(size_val, (int, float)):
                key_attrs['size'] = int(size_val)
            else:
                try:
                    key_attrs['size'] = int(size_val)
                except (ValueError, TypeError):
                    raise ValueError(f"Invalid size value: {size_val}. Size must be an integer.")
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

    async def _find_template_id_by_name(self, template_name: str, domain: Optional[str] = None, auth_domain: Optional[str] = None) -> str:
        """
        Find template ID by name using template list operation.
        
        Args:
            template_name: Name of the template to find
            domain: Domain to search in
            auth_domain: Authentication domain
            
        Returns:
            Template ID if found
            
        Raises:
            ValueError: If template not found or multiple templates found
        """
        try:
            # Search for template by name
            args = ["templates", "list", "--name", template_name]
            result = self.execute_with_domain(args, domain, auth_domain)
            
            # Parse the result to extract template data
            data = result.get("data", result.get("stdout", ""))
            if isinstance(data, str):
                try:
                    import json
                    data = json.loads(data)
                except (json.JSONDecodeError, ValueError):
                    raise ValueError(f"Failed to parse template list response")
            
            # Handle different response formats
            templates = []
            if isinstance(data, list):
                templates = data
            elif isinstance(data, dict):
                if "templates" in data:
                    templates = data["templates"]
                elif "data" in data:
                    templates = data["data"]
                else:
                    # Single template response
                    templates = [data]
            
            if not templates:
                raise ValueError(f"Template '{template_name}' not found")
                
            # Filter templates by exact name match
            matching_templates = [t for t in templates if t.get("name") == template_name]
            
            if not matching_templates:
                raise ValueError(f"Template '{template_name}' not found")
            elif len(matching_templates) > 1:
                raise ValueError(f"Multiple templates found with name '{template_name}'. Please use template ID instead.")
            
            template_id = matching_templates[0].get("id")
            if not template_id:
                raise ValueError(f"Template '{template_name}' found but has no ID")
                
            return template_id
            
        except Exception as e:
            if "not found" in str(e) or "Multiple templates" in str(e):
                raise e
            else:
                raise ValueError(f"Failed to find template '{template_name}': {str(e)}")

    async def execute(self, action: str, **kwargs: Any) -> Any:
        """
        Execute a template management operation.
        
        Args:
            action: The operation to perform (list, create, get, delete, modify)
            **kwargs: Operation-specific parameters
            
        Returns:
            Operation result data
            
        Raises:
            ValueError: For validation errors, authentication issues, or operation failures
        """
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
                    # FIXED: Use underscore instead of hyphen for correct ksctl syntax
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
                
                # Determine template ID - either provided directly or lookup by name
                template_id = params.id
                if not template_id and params.template_name:
                    # Look up template ID by name
                    template_id = await self._find_template_id_by_name(
                        params.template_name, 
                        params.domain, 
                        params.auth_domain
                    )
                elif not template_id and not params.template_name:
                    raise ValueError("Either 'id' or 'template_name' must be provided for template modification")
                
                # FIXED: Use 'update' command and require ID for identification
                args = ["templates", "update", "--id", template_id]
                
                # Optional parameters to update the template
                if params.name:
                    args.extend(["--name", params.name])
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
                    # FIXED: Use underscore instead of hyphen for correct ksctl syntax
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
    
    This helper function creates a properly formatted JSON string for use with
    the --key_attributes parameter in ksctl commands.
    
    Valid attributes according to ksctl documentation:
    - activationDate: string - Date/time the object becomes active
    - algorithm: string - Encryption algorithm (AES, RSA, EC, etc.)
    - objectType: string - Type of cryptographic object
    - archiveDate: string - Date/time the object becomes archived
    - curveid: string - Elliptic curve identifier for EC keys
    - deactivationDate: string - Date/time the object becomes inactive
    - meta: {"ownerId": string} - Metadata with owner information
    - processStartDate: string - Date/time when object may begin processing
    - protectStopDate: string - Date/time after which object won't be used for protection
    - size: integer - Key size in bits (128, 192, 256 for AES; 1024, 2048, 4096 for RSA)
    - undeletable: boolean - Whether the template cannot be deleted
    - unexportable: boolean - Whether the template cannot be exported
    - usageMask: integer - Bitmask defining allowed operations
    - format: string - Key format specification
    - xts: boolean - Whether to use XTS mode for AES
    - state: string - Initial state of objects created from template
    - description: string - Human-readable description
    
    Args:
        **attributes: Key-value pairs of template attributes
        
    Returns:
        JSON string representation of the attributes
        
    Raises:
        ValueError: If unknown attributes are provided
        
    Example:
        >>> build_key_attributes_json(algorithm="AES", size=256, undeletable=True)
        '{"algorithm": "AES", "size": 256, "undeletable": true}'
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
    """
    Build meta JSON string for template creation.
    
    This helper function creates a properly formatted JSON string for use with
    the --meta parameter in ksctl commands.
    
    Args:
        **meta_data: Key-value pairs of metadata
        
    Returns:
        JSON string representation of the metadata
        
    Example:
        >>> build_meta_json(ownerId="user123", department="security")
        '{"ownerId": "user123", "department": "security"}'
    """
    return json.dumps(meta_data)


# Usage examples
def get_template_examples():
    """
    Get template usage examples.
    
    This function provides comprehensive examples of how to use the template
    management tool for various scenarios.
    
    Returns:
        Dictionary containing example usage patterns for all template operations
    """
    return {
        "create_basic_template_with_individual_params": {
            "description": "Create a basic AES template using individual parameters",
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
            "description": "Create a basic AES template using key_attributes JSON",
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
            "description": "Create an RSA template for signing operations",
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
            "description": "Create an Elliptic Curve template",
            "action": "create",
            "name": "ec_p256_template", 
            "desc": "EC P-256 template",
            "algorithm": "EC",
            "curve_id": "secp256r1",
            "usage_mask": 8  # Sign
        },
        "list_templates": {
            "description": "List all templates with pagination",
            "action": "list",
            "limit": 20
        },
        "list_with_filter": {
            "description": "List templates with label-based filtering",
            "action": "list",
            "labels_query": "key_type=rsa",
            "limit": 10
        },
        "get_template": {
            "description": "Retrieve a specific template by name",
            "action": "get",
            "name": "aes_256_template"
        },
        "update_template_name": {
            "description": "Update template name using ID",
            "action": "modify",
            "id": "ece51cf0-bbf9-47ad-9d28-f2d82707cccc",
            "name": "newname"
        },
        "update_template_description": {
            "description": "Update template description using ID",
            "action": "modify",
            "id": "ece51cf0-bbf9-47ad-9d28-f2d82707cccc",
            "desc": "Updated AES 256-bit encryption template"
        },
        "update_template_by_name": {
            "description": "Update template description using template name (tool will auto-lookup ID)",
            "action": "modify",
            "template_name": "temp_aes",
            "desc": "Updated description via template name"
        },
        "update_template_name_by_template_name": {
            "description": "Update template name using template name for lookup",
            "action": "modify",
            "template_name": "old_template_name",
            "name": "new_template_name"
        },
        "update_template_key_attributes": {
            "description": "Update template key attributes using ID",
            "action": "modify",
            "id": "ece51cf0-bbf9-47ad-9d28-f2d82707cccc",
            "key_attributes": build_key_attributes_json(
                algorithm="AES",
                size=128,  # Changed from 256 to 128
                description="AES 128-bit template"
            )
        },
        "delete_template": {
            "description": "Delete a template by name",
            "action": "delete",
            "name": "aes_256_template"
        }
    }


# Export the tools
TEMPLATE_TOOLS = [TemplateManagementTool]