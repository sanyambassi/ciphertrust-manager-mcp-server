"""Secrets management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# Core CRUD Parameter Models
class SecretListParams(BaseModel):
    """Parameters for listing secrets."""
    limit: int = Field(10, description="Maximum number of secrets to return")
    skip: int = Field(0, description="Offset at which to start the search")
    name: Optional[str] = Field(None, description="Filter by secret name, ID or URI")
    object_type: Optional[str] = Field(None, description="Filter by object type (Secret Data or Opaque Object)")
    secretversion: Optional[int] = Field(None, description="Filter by secret version")
    sha1_fingerprint: Optional[str] = Field(None, description="Filter by SHA1 fingerprint (supports wildcards)")
    sha256_fingerprint: Optional[str] = Field(None, description="Filter by SHA256 fingerprint (supports wildcards)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list secrets from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretCreateParams(BaseModel):
    """Parameters for creating a secret."""
    name: str = Field(..., description="Name of the secret.")
    description: Optional[str] = Field(None, description="Description of the secret.")
    type: str = Field(..., description="Type of the secret. Can be 'password', 'text', or 'file'.")
    value: Optional[str] = Field(None, description="Value of the secret.")
    # Domain support
    domain: Optional[str] = Field(None, description="The domain where the action/operation will be performed.")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretGetParams(BaseModel):
    """Parameters for getting a secret."""
    id: str = Field(..., description="ID of the secret to retrieve.")
    file: Optional[str] = Field(None, description="File path to save the secret to.")
    # Domain support
    domain: Optional[str] = Field(None, description="The domain where the action/operation will be performed.")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretDeleteParams(BaseModel):
    """Parameters for deleting a secret."""
    id: str = Field(..., description="ID of the secret to delete.")
    # Domain support
    domain: Optional[str] = Field(None, description="The domain where the action/operation will be performed.")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretModifyParams(BaseModel):
    """Parameters for modifying a secret."""
    id: str = Field(..., description="ID of the secret to update.")
    name: Optional[str] = Field(None, description="New name for the secret.")
    # Domain support
    domain: Optional[str] = Field(None, description="The domain where the action/operation will be performed.")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


# Advanced Parameter Models
class SecretExportParams(BaseModel):
    """Parameters for exporting a secret."""
    name: str = Field(..., description="Secret name, ID or URI")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to export secret from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretDestroyParams(BaseModel):
    """Parameters for destroying a secret's material."""
    name: str = Field(..., description="Secret name, ID or URI")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to destroy secret in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretVersionParams(BaseModel):
    """Parameters for creating a new version of a secret."""
    name: str = Field(..., description="Secret name, ID or URI")
    material: Optional[str] = Field(None, description="Secret material data for new version")
    id_size: Optional[int] = Field(None, description="Size of ID for the managed object")
    include_material: bool = Field(False, description="Include secret bytes in the response")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to version secret in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretListVersionParams(BaseModel):
    """Parameters for listing secret versions."""
    name: str = Field(..., description="Secret name, ID or URI")
    limit: int = Field(10, description="Maximum number of versions to return")
    skip: int = Field(0, description="Offset at which to start the search")
    secretfields: Optional[str] = Field(None, description="Comma separated fields ('meta', 'links') to include")
    secretlinktype: Optional[str] = Field(None, description="Filter by link types (supports wildcards)")
    secretstate: Optional[str] = Field(None, description="Filter by state (Pre-Active, Active, Deactivated, etc.)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list versions from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="The domain where the user is created. Defaults to 'root' if not specified.")


class SecretsManagementTool(BaseTool):
    name = "secrets_management"
    description = "Secret management operations (list, create, get, delete, modify, export, destroy, version, list_version)"

    def get_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": [
                    "list", "create", "get", "delete", "modify", "export", "destroy", "version", "list_version"
                ]},
                **SecretListParams.model_json_schema()["properties"],
                **SecretCreateParams.model_json_schema()["properties"],
                **SecretGetParams.model_json_schema()["properties"],
                **SecretDeleteParams.model_json_schema()["properties"],
                **SecretModifyParams.model_json_schema()["properties"],
                **SecretExportParams.model_json_schema()["properties"],
                **SecretDestroyParams.model_json_schema()["properties"],
                **SecretVersionParams.model_json_schema()["properties"],
                **SecretListVersionParams.model_json_schema()["properties"],
            },
            "required": ["action"],
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if action == "list":
            params = SecretListParams(**kwargs)
            args = ["secrets", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.name:
                args.extend(["--name", params.name])
            if params.object_type:
                args.extend(["--object-type", params.object_type])
            if params.secretversion is not None:
                args.extend(["--secretversion", str(params.secretversion)])
            if params.sha1_fingerprint:
                args.extend(["--sha1-fingerprint", params.sha1_fingerprint])
            if params.sha256_fingerprint:
                args.extend(["--sha256-fingerprint", params.sha256_fingerprint])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "create":
            params = SecretCreateParams(**kwargs)
            args = ["secrets", "create"]
            if params.name:
                args.extend(["--name", params.name])
            if params.autoname:
                args.append("--autoname")
            args.extend(["--data-type", params.data_type])
            if params.material:
                args.extend(["--material", params.material])
            if params.id_size is not None:
                args.extend(["--id-size", str(params.id_size)])
            if params.include_material:
                args.append("--includematerial")
            if params.jsonfile:
                args.extend(["--jsonfile", params.jsonfile])
            if params.nodelete:
                args.append("--nodelete")
            if params.noexport:
                args.append("--noexport")
            if params.ownerid:
                args.extend(["--ownerid", params.ownerid])
            if params.passwordconfig:
                args.extend(["--passwordconfig", params.passwordconfig])
            if params.ret:
                args.append("--ret")
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = SecretGetParams(**kwargs)
            args = ["secrets", "get", "--name", params.name]
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = SecretDeleteParams(**kwargs)
            args = ["secrets", "delete", "--name", params.name]
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = SecretModifyParams(**kwargs)
            args = ["secrets", "modify", "--name", params.name]
            if params.jsonfile:
                args.extend(["--jsonfile", params.jsonfile])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "export":
            params = SecretExportParams(**kwargs)
            args = ["secrets", "export", "--name", params.name]
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "destroy":
            params = SecretDestroyParams(**kwargs)
            args = ["secrets", "destroy", "--name", params.name]
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "version":
            params = SecretVersionParams(**kwargs)
            args = ["secrets", "version", "--name", params.name]
            if params.material:
                args.extend(["--material", params.material])
            if params.id_size is not None:
                args.extend(["--id-size", str(params.id_size)])
            if params.include_material:
                args.append("--includematerial")
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list_version":
            params = SecretListVersionParams(**kwargs)
            args = ["secrets", "listversion", "--name", params.name]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.secretfields:
                args.extend(["--secretfields", params.secretfields])
            if params.secretlinktype:
                args.extend(["--secretlinktype", params.secretlinktype])
            if params.secretstate:
                args.extend(["--secretstate", params.secretstate])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")

SECRET_TOOLS = [SecretsManagementTool]
