"""CTE CSI StorageGroup management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# StorageGroup Parameter Models
class CTECSIStorageGroupCreateParams(BaseModel):
    """Parameters for creating a CSI StorageGroup."""
    storage_group_name: str = Field(..., description="Unique Name of CTE CSI StorageGroup")
    storage_class_name: str = Field(..., description="Unique Name of CTE CSI StorageClass")
    namespace_name: str = Field(..., description="Unique Name of CTE CSI Namespace")
    ctecsi_description: Optional[str] = Field(None, description="Description for CTE CSI resources")
    ctecsi_profile: Optional[str] = Field(None, description="Client Profile for CTE CSI resources")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create storage group in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupListParams(BaseModel):
    """Parameters for listing CSI StorageGroups."""
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    storage_group_name: Optional[str] = Field(None, description="Filter by StorageGroup name")
    storage_class_name: Optional[str] = Field(None, description="Filter by StorageClass name")
    namespace_name: Optional[str] = Field(None, description="Filter by Namespace name")
    sort: Optional[str] = Field(None, description="Sort field (prefix with - for descending)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list storage groups from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupGetParams(BaseModel):
    """Parameters for getting a CSI StorageGroup."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get storage group from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupDeleteParams(BaseModel):
    """Parameters for deleting a CSI StorageGroup."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete storage group from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupModifyParams(BaseModel):
    """Parameters for modifying a CSI StorageGroup."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    ctecsi_description: Optional[str] = Field(None, description="Description for CTE CSI resources")
    ctecsi_profile: Optional[str] = Field(None, description="Client Profile for CTE CSI resources")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify storage group in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Client Management Parameter Models
class CTECSIStorageGroupAddClientsParams(BaseModel):
    """Parameters for adding clients to a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    csi_client_list: str = Field(..., description="Comma-separated list of CSI client identifiers")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupRemoveClientParams(BaseModel):
    """Parameters for removing a client from a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    csi_client_identifier: str = Field(..., description="Identifier for CSI Client (name or UUID)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupListClientsParams(BaseModel):
    """Parameters for listing clients in a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    csi_client_id: Optional[str] = Field(None, description="Filter by CSI Client UUID")
    csi_client_name: Optional[str] = Field(None, description="Filter by CSI Client name")
    sort: Optional[str] = Field(None, description="Sort field (prefix with - for descending)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list clients from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupGetClientParams(BaseModel):
    """Parameters for getting a client in a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    csi_client_identifier: str = Field(..., description="Identifier for CSI Client (name or UUID)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get client from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# GuardPolicy Management Parameter Models
class CTECSIStorageGroupAddGuardPolicyParams(BaseModel):
    """Parameters for adding guard policies to a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    csi_policy_list: str = Field(..., description="Comma-separated list of CSI policy identifiers")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupRemoveGuardPolicyParams(BaseModel):
    """Parameters for removing a guard policy from a storage group."""
    guard_policy_id: str = Field(..., description="UUID of GuardPolicy")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupListGuardPolicyParams(BaseModel):
    """Parameters for listing guard policies in a storage group."""
    storage_group_identifier: str = Field(..., description="Unique Identifier of CTE CSI StorageGroup (name or UUID)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    csi_policy_id: Optional[str] = Field(None, description="Filter by CSI Policy UUID")
    csi_policy_name: Optional[str] = Field(None, description="Filter by CSI Policy name")
    guard_policy_enabled: Optional[bool] = Field(None, description="Filter by enabled state of GuardPolicy")
    guard_policy_state: Optional[str] = Field(None, description="Filter by state of GuardPolicy")
    sort: Optional[str] = Field(None, description="Sort field (prefix with - for descending)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list policies from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupGetGuardPolicyParams(BaseModel):
    """Parameters for getting a guard policy in a storage group."""
    guard_policy_id: str = Field(..., description="UUID of GuardPolicy")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get policy from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupModifyGuardPolicyParams(BaseModel):
    """Parameters for modifying a guard policy in a storage group."""
    guard_policy_id: str = Field(..., description="UUID of GuardPolicy")
    guard_policy_enabled: bool = Field(..., description="Enable/Disable GuardPolicy")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify policy in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTECSIStorageGroupManagementTool(BaseTool):
    """Grouped tool for all CTE CSI StorageGroup management operations (with action parameter)."""

    @property
    def name(self) -> str:
        return "cte_csi_storagegroup_management"

    @property
    def description(self) -> str:
        return "Manage CTE CSI StorageGroups, clients, and guard policies (grouped tool with action parameter)"

    def get_schema(self) -> dict[str, Any]:
        # Return a schema with an 'action' parameter and all possible parameter models
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": [
                    "create", "list", "get", "delete", "modify",
                    "add_clients", "remove_client", "list_clients", "get_client",
                    "add_guardpolicy", "remove_guardpolicy", "list_guardpolicy", "get_guardpolicy", "modify_guardpolicy"
                ]},
                # Add all parameter schemas under their action names
                "create": CTECSIStorageGroupCreateParams.model_json_schema(),
                "list": CTECSIStorageGroupListParams.model_json_schema(),
                "get": CTECSIStorageGroupGetParams.model_json_schema(),
                "delete": CTECSIStorageGroupDeleteParams.model_json_schema(),
                "modify": CTECSIStorageGroupModifyParams.model_json_schema(),
                "add_clients": CTECSIStorageGroupAddClientsParams.model_json_schema(),
                "remove_client": CTECSIStorageGroupRemoveClientParams.model_json_schema(),
                "list_clients": CTECSIStorageGroupListClientsParams.model_json_schema(),
                "get_client": CTECSIStorageGroupGetClientParams.model_json_schema(),
                "add_guardpolicy": CTECSIStorageGroupAddGuardPolicyParams.model_json_schema(),
                "remove_guardpolicy": CTECSIStorageGroupRemoveGuardPolicyParams.model_json_schema(),
                "list_guardpolicy": CTECSIStorageGroupListGuardPolicyParams.model_json_schema(),
                "get_guardpolicy": CTECSIStorageGroupGetGuardPolicyParams.model_json_schema(),
                "modify_guardpolicy": CTECSIStorageGroupModifyGuardPolicyParams.model_json_schema(),
            },
            "required": ["action"],
            "additionalProperties": True,
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if not action:
            raise ValueError("Missing required 'action' parameter")

        # Core StorageGroup Management
        if action == "create":
            params = CTECSIStorageGroupCreateParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "create"]
            args.extend(["--storage-group-name", params.storage_group_name])
            args.extend(["--storage-class-name", params.storage_class_name])
            args.extend(["--namespace-name", params.namespace_name])
            if params.ctecsi_description:
                args.extend(["--ctecsi-description", params.ctecsi_description])
            if params.ctecsi_profile:
                args.extend(["--ctecsi-profile", params.ctecsi_profile])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list":
            params = CTECSIStorageGroupListParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.storage_group_name:
                args.extend(["--storage-group-name", params.storage_group_name])
            if params.storage_class_name:
                args.extend(["--storage-class-name", params.storage_class_name])
            if params.namespace_name:
                args.extend(["--namespace-name", params.namespace_name])
            if params.sort:
                args.extend(["--sort", params.sort])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get":
            params = CTECSIStorageGroupGetParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "get", "--storage-group-identifier", params.storage_group_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "delete":
            params = CTECSIStorageGroupDeleteParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "delete", "--storage-group-identifier", params.storage_group_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "modify":
            params = CTECSIStorageGroupModifyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "modify", "--storage-group-identifier", params.storage_group_identifier]
            if params.ctecsi_description is not None:
                args.extend(["--ctecsi-description", params.ctecsi_description])
            if params.ctecsi_profile:
                args.extend(["--ctecsi-profile", params.ctecsi_profile])
            return self.execute_with_domain(args, params.domain, params.auth_domain)

        # Client Management
        elif action == "add_clients":
            params = CTECSIStorageGroupAddClientsParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "add-clients", "--storage-group-identifier", params.storage_group_identifier, "--csi-client-list", params.csi_client_list]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "remove_client":
            params = CTECSIStorageGroupRemoveClientParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "remove-client", "--storage-group-identifier", params.storage_group_identifier, "--csi-client-identifier", params.csi_client_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list_clients":
            params = CTECSIStorageGroupListClientsParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "list-clients", "--storage-group-identifier", params.storage_group_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.csi_client_id:
                args.extend(["--csi-client-id", params.csi_client_id])
            if params.csi_client_name:
                args.extend(["--csi-client-name", params.csi_client_name])
            if params.sort:
                args.extend(["--sort", params.sort])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get_client":
            params = CTECSIStorageGroupGetClientParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "get-client", "--storage-group-identifier", params.storage_group_identifier, "--csi-client-identifier", params.csi_client_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)

        # GuardPolicy Management
        elif action == "add_guardpolicy":
            params = CTECSIStorageGroupAddGuardPolicyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "add-guardpolicy", "--storage-group-identifier", params.storage_group_identifier, "--csi-policy-list", params.csi_policy_list]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "remove_guardpolicy":
            params = CTECSIStorageGroupRemoveGuardPolicyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "remove-guardpolicy", "--guard-policy-id", params.guard_policy_id]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list_guardpolicy":
            params = CTECSIStorageGroupListGuardPolicyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "list-guardpolicy", "--storage-group-identifier", params.storage_group_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.csi_policy_id:
                args.extend(["--csi-policy-id", params.csi_policy_id])
            if params.csi_policy_name:
                args.extend(["--csi-policy-name", params.csi_policy_name])
            if params.guard_policy_enabled is not None:
                args.append("--guard-policy-enabled" if params.guard_policy_enabled else "--no-guard-policy-enabled")
            if params.guard_policy_state:
                args.extend(["--guard-policy-state", params.guard_policy_state])
            if params.sort:
                args.extend(["--sort", params.sort])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get_guardpolicy":
            params = CTECSIStorageGroupGetGuardPolicyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "get-guardpolicy", "--guard-policy-id", params.guard_policy_id]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "modify_guardpolicy":
            params = CTECSIStorageGroupModifyGuardPolicyParams(**kwargs)
            args = ["cte", "csi", "k8s-storage-group", "modify-guardpolicy", "--guard-policy-id", params.guard_policy_id]
            args.append("--guard-policy-enabled" if params.guard_policy_enabled else "--no-guard-policy-enabled")
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        else:
            raise ValueError(f"Unknown action: {action}")


# Export only the grouped tool
CTE_CSI_STORAGEGROUP_TOOLS = [CTECSIStorageGroupManagementTool]
