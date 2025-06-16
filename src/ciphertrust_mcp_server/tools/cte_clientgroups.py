"""CTE Client Groups management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional, List

from pydantic import BaseModel, Field

from .base import BaseTool


# Client Group Parameter Models
class CTEClientGroupCreateParams(BaseModel):
    """Parameters for creating a CTE client group."""
    client_group_name: str = Field(..., description="Name of CTE ClientGroup")
    client_group_description: Optional[str] = Field(None, description="Descriptive string for CTE ClientGroup")
    client_group_password: Optional[str] = Field(None, description="Password for CTE ClientGroup")
    password_creation_method: str = Field("GENERATE", description="Method to create password: GENERATE or MANUAL")
    cluster_type: str = Field("NON-CLUSTER", description="Cluster Type: NON-CLUSTER or HDFS")
    comm_enabled: bool = Field(False, description="Toggle CTE client Communication parameter")
    cte_profile_identifier: Optional[str] = Field(None, description="CTE profile identifier")
    cte_domain: Optional[str] = Field(None, description="CTE Domain Identifier")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create client group in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupListParams(BaseModel):
    """Parameters for listing CTE client groups."""
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    client_group_name: Optional[str] = Field(None, description="Filter by client group name")
    cluster_type: Optional[str] = Field(None, description="Filter by cluster type: NON-CLUSTER or HDFS")
    enable_domain_sharing: bool = Field(False, description="Enable/Disable domain sharing for resource")
    fetch_current_domain_resources_only: bool = Field(False, description="Filter resources belonging to current domain only")
    native_domain: Optional[str] = Field(None, description="Filter by native domain (comma-separated list)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list client groups from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupGetParams(BaseModel):
    """Parameters for getting a CTE client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get client group from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupDeleteParams(BaseModel):
    """Parameters for deleting a CTE client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete client group from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupModifyParams(BaseModel):
    """Parameters for modifying a CTE client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    client_group_description: Optional[str] = Field(None, description="Descriptive string for CTE ClientGroup")
    client_group_password: Optional[str] = Field(None, description="Password for CTE ClientGroup")
    password_creation_method: Optional[str] = Field(None, description="Method to create password: GENERATE or MANUAL")
    comm_enabled: Optional[bool] = Field(None, description="Toggle CTE client Communication parameter")
    cte_client_locked: Optional[bool] = Field(None, description="Toggle CTE client Lock Status")
    system_locked: Optional[bool] = Field(None, description="Toggle System Lock Status")
    cte_profile_identifier: Optional[str] = Field(None, description="CTE profile identifier")
    enable_domain_sharing: Optional[bool] = Field(None, description="Enable/Disable domain sharing for resource")
    shared_domain_list: Optional[str] = Field(None, description='List of domains to share with (JSON array string)')
    capabilities: Optional[str] = Field(None, description="Capabilities")
    enabled_capabilities: Optional[str] = Field(None, description="Enabled Capabilities")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify client group in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Client Management Parameter Models
class CTEClientGroupAddClientsParams(BaseModel):
    """Parameters for adding clients to a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    cte_client_list: str = Field(..., description="Comma-separated list of CTE client identifiers")
    inherit_attributes: bool = Field(False, description="Inherit attributes from client group")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupRemoveClientParams(BaseModel):
    """Parameters for removing a client from a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupListClientsParams(BaseModel):
    """Parameters for listing clients in a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    cte_client_name: Optional[str] = Field(None, description="Filter by CTE Client name")
    limit: int = Field(10, description="Maximum number of resources to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list clients from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupGetClientParams(BaseModel):
    """Parameters for getting a client in a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get client from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# GuardPoint Management Parameter Models
class CTEClientGroupCreateGuardPointParams(BaseModel):
    """Parameters for creating a guardpoint on a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    guard_path_list: str = Field(..., description="Comma-separated list of paths to guard")
    guard_point_type: str = Field(..., description="Type: directory_auto, directory_manual, ransomware_protection, etc.")
    cte_policy_identifier: Optional[str] = Field(None, description="Identifier for CTE Policy")
    guard_enabled: bool = Field(True, description="Whether guard is enabled or not")
    auto_mount_enabled: bool = Field(False, description="Flag for automount (Standard or LDT policy)")
    cifs_enabled: bool = Field(False, description="Flag for CIFS enable")
    early_access: bool = Field(False, description="Early access (secure start) on Windows clients")
    preserve_sparse_regions: bool = Field(True, description="Preserve sparse file regions (LDT clients only)")
    mfa_enabled: bool = Field(False, description="Enable MFA at guard point level")
    intelligent_protection: bool = Field(False, description="Enable intelligent protection (classification policies only)")
    is_idt_capable_device: bool = Field(False, description="Whether device is IDT capable")
    network_share_credentials_identifier: Optional[str] = Field(None, description="Identifier of CIFS credentials")
    disk_name: Optional[str] = Field(None, description="Name of disk for Oracle ASM disk group")
    disk_group_name: Optional[str] = Field(None, description="Name of Oracle ASM disk group")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create guardpoint in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupListGuardPointsParams(BaseModel):
    """Parameters for listing guardpoints on a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    guard_path: Optional[str] = Field(None, description="Filter by guard path")
    guard_point_type: Optional[str] = Field(None, description="Filter by guardpoint type")
    guard_enabled: Optional[bool] = Field(None, description="Filter by guard enabled status")
    cte_policy_identifier: Optional[str] = Field(None, description="Filter by CTE Policy identifier")
    cte_policy_name: Optional[str] = Field(None, description="Filter by CTE Policy name")
    mfa_enabled: Optional[bool] = Field(None, description="Filter by MFA enabled status")
    sort: Optional[str] = Field(None, description="Sort field (prefix with - for descending)")
    fetch_current_domain_resources_only: bool = Field(False, description="Filter resources belonging to current domain only")
    native_domain: Optional[str] = Field(None, description="Filter by native domain (comma-separated list)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list guardpoints from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupGetGuardPointParams(BaseModel):
    """Parameters for getting a guardpoint on a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get guardpoint from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupModifyGuardPointParams(BaseModel):
    """Parameters for modifying a guardpoint on a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    guard_enabled: Optional[bool] = Field(None, description="Whether guard is enabled or not")
    mfa_enabled: Optional[bool] = Field(None, description="Enable MFA at guard point level")
    network_share_credentials_identifier: Optional[str] = Field(None, description="Identifier of CIFS credentials")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify guardpoint in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupUnguardGuardPointParams(BaseModel):
    """Parameters for unguarding a guardpoint from a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to unguard guardpoint from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupUnguardBulkGuardPointsParams(BaseModel):
    """Parameters for unguarding multiple guardpoints from a client group."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    guard_point_identifier_list: str = Field(..., description="Comma-separated list of GuardPoint identifiers")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to unguard guardpoints from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Special Operations Parameter Models
class CTEClientGroupModifyPasswordParams(BaseModel):
    """Parameters for modifying client group password."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    client_group_password: str = Field(..., description="New password for CTE ClientGroup")
    password_creation_method: str = Field("MANUAL", description="Method to create password: GENERATE or MANUAL")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify password in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupModifyAuthBinariesParams(BaseModel):
    """Parameters for modifying authorized binaries."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    auth_bin_json: Optional[str] = Field(None, description="Authorized binary parameters in JSON format")
    auth_bin_json_file: Optional[str] = Field(None, description="File containing authorized binary parameters in JSON")
    re_sign: bool = Field(False, description="Whether authorized binaries should be re-signed")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify auth binaries in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupSendLDTPauseParams(BaseModel):
    """Parameters for sending LDT pause/resume request."""
    client_group_identifier: str = Field(..., description="Identifier of CTE ClientGroup (UUID, URI or Name)")
    ldt_pause: bool = Field(..., description="True to pause LDT, False to resume")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to send LDT pause in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGroupManagementTool(BaseTool):
    """Grouped tool for all CTE client group management operations (with action parameter)."""

    @property
    def name(self) -> str:
        return "ct_cte_clientgroup_management"

    @property
    def description(self) -> str:
        return "Manage CTE client groups, clients, guardpoints, and special operations (grouped tool with action parameter)"

    def get_schema(self) -> dict[str, Any]:
        # Return a schema with an 'action' parameter and all possible parameter models
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": [
                    "create", "list", "get", "delete", "modify",
                    "add_clients", "remove_client", "list_clients", "get_client",
                    "create_guardpoint", "list_guardpoints", "get_guardpoint", "modify_guardpoint",
                    "unguard_guardpoint", "unguard_bulk_guardpoints",
                    "modify_password", "modify_auth_binaries", "send_ldt_pause"
                ]},
                # Add all parameter schemas under their action names
                "create": CTEClientGroupCreateParams.model_json_schema(),
                "list": CTEClientGroupListParams.model_json_schema(),
                "get": CTEClientGroupGetParams.model_json_schema(),
                "delete": CTEClientGroupDeleteParams.model_json_schema(),
                "modify": CTEClientGroupModifyParams.model_json_schema(),
                "add_clients": CTEClientGroupAddClientsParams.model_json_schema(),
                "remove_client": CTEClientGroupRemoveClientParams.model_json_schema(),
                "list_clients": CTEClientGroupListClientsParams.model_json_schema(),
                "get_client": CTEClientGroupGetClientParams.model_json_schema(),
                "create_guardpoint": CTEClientGroupCreateGuardPointParams.model_json_schema(),
                "list_guardpoints": CTEClientGroupListGuardPointsParams.model_json_schema(),
                "get_guardpoint": CTEClientGroupGetGuardPointParams.model_json_schema(),
                "modify_guardpoint": CTEClientGroupModifyGuardPointParams.model_json_schema(),
                "unguard_guardpoint": CTEClientGroupUnguardGuardPointParams.model_json_schema(),
                "unguard_bulk_guardpoints": CTEClientGroupUnguardBulkGuardPointsParams.model_json_schema(),
                "modify_password": CTEClientGroupModifyPasswordParams.model_json_schema(),
                "modify_auth_binaries": CTEClientGroupModifyAuthBinariesParams.model_json_schema(),
                "send_ldt_pause": CTEClientGroupSendLDTPauseParams.model_json_schema(),
            },
            "required": ["action"],
            "additionalProperties": True,
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if not action:
            raise ValueError("Missing required 'action' parameter")

        # Core Client Group Management
        if action == "create":
            params = CTEClientGroupCreateParams(**kwargs)
            args = ["cte", "client-groups", "create"]
            args.extend(["--client-group-name", params.client_group_name])
            if params.client_group_description:
                args.extend(["--client-group-description", params.client_group_description])
            if params.client_group_password:
                args.extend(["--client-group-password", params.client_group_password])
            if params.password_creation_method:
                args.extend(["--password-creation-method", params.password_creation_method])
            if params.cluster_type:
                args.extend(["--cluster-type", params.cluster_type])
            if params.comm_enabled:
                args.append("--comm-enabled")
            if params.cte_profile_identifier:
                args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.cte_domain:
                args.extend(["--cte-domain", params.cte_domain])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list":
            params = CTEClientGroupListParams(**kwargs)
            args = ["cte", "client-groups", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.client_group_name:
                args.extend(["--client-group-name", params.client_group_name])
            if params.cluster_type:
                args.extend(["--cluster-type", params.cluster_type])
            if params.enable_domain_sharing:
                args.append("--enable-domain-sharing")
            if params.fetch_current_domain_resources_only:
                args.append("--fetch-current-domain-resources-only")
            if params.native_domain:
                args.extend(["--native-domain", params.native_domain])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get":
            params = CTEClientGroupGetParams(**kwargs)
            args = ["cte", "client-groups", "get", "--client-group-identifier", params.client_group_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "delete":
            params = CTEClientGroupDeleteParams(**kwargs)
            args = ["cte", "client-groups", "delete", "--client-group-identifier", params.client_group_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "modify":
            params = CTEClientGroupModifyParams(**kwargs)
            args = ["cte", "client-groups", "modify", "--client-group-identifier", params.client_group_identifier]
            if params.client_group_description:
                args.extend(["--client-group-description", params.client_group_description])
            if params.client_group_password:
                args.extend(["--client-group-password", params.client_group_password])
            if params.password_creation_method:
                args.extend(["--password-creation-method", params.password_creation_method])
            if params.comm_enabled is not None:
                args.append("--comm-enabled" if params.comm_enabled else "--no-comm-enabled")
            if params.cte_client_locked is not None:
                args.append("--cte-client-locked" if params.cte_client_locked else "--no-cte-client-locked")
            if params.system_locked is not None:
                args.append("--system-locked" if params.system_locked else "--no-system-locked")
            if params.cte_profile_identifier:
                args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.enable_domain_sharing is not None:
                args.append("--enable-domain-sharing" if params.enable_domain_sharing else "--no-enable-domain-sharing")
            if params.shared_domain_list:
                args.extend(["--shared-domain-list", params.shared_domain_list])
            if params.capabilities:
                args.extend(["--capabilities", params.capabilities])
            if params.enabled_capabilities:
                args.extend(["--enabled-capabilities", params.enabled_capabilities])
            return self.execute_with_domain(args, params.domain, params.auth_domain)

        # Client Management
        elif action == "add_clients":
            params = CTEClientGroupAddClientsParams(**kwargs)
            args = ["cte", "client-groups", "add-clients", "--client-group-identifier", params.client_group_identifier, "--cte-client-list", params.cte_client_list]
            if params.inherit_attributes:
                args.append("--inherit-attributes")
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "remove_client":
            params = CTEClientGroupRemoveClientParams(**kwargs)
            args = ["cte", "client-groups", "remove-client", "--client-group-identifier", params.client_group_identifier, "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list_clients":
            params = CTEClientGroupListClientsParams(**kwargs)
            args = ["cte", "client-groups", "list-clients", "--client-group-identifier", params.client_group_identifier, "--limit", str(params.limit)]
            if params.cte_client_name:
                args.extend(["--cte-client-name", params.cte_client_name])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get_client":
            params = CTEClientGroupGetClientParams(**kwargs)
            args = ["cte", "client-groups", "get-client", "--client-group-identifier", params.client_group_identifier, "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)

        # GuardPoint Management
        elif action == "create_guardpoint":
            params = CTEClientGroupCreateGuardPointParams(**kwargs)
            args = ["cte", "client-groups", "create-guardpoints", "--client-group-identifier", params.client_group_identifier, "--guard-path-list", params.guard_path_list, "--guard-point-type", params.guard_point_type]
            if params.cte_policy_identifier:
                args.extend(["--cte-policy-identifier", params.cte_policy_identifier])
            if not params.guard_enabled:
                args.append("--no-guard-enabled")
            if params.auto_mount_enabled:
                args.append("--auto-mount-enabled")
            if params.cifs_enabled:
                args.append("--cifs-enabled")
            if params.early_access:
                args.append("--early-access")
            if not params.preserve_sparse_regions:
                args.append("--no-preserve-sparse-regions")
            if params.mfa_enabled:
                args.append("--mfa-enabled")
            if params.intelligent_protection:
                args.append("--intelligent-protection")
            if params.is_idt_capable_device:
                args.append("--is-idt-capable-device")
            if params.network_share_credentials_identifier:
                args.extend(["--network-share-credentials-identifier", params.network_share_credentials_identifier])
            if params.disk_name:
                args.extend(["--disk-name", params.disk_name])
            if params.disk_group_name:
                args.extend(["--disk-group-name", params.disk_group_name])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "list_guardpoints":
            params = CTEClientGroupListGuardPointsParams(**kwargs)
            args = ["cte", "client-groups", "list-guardpoints", "--client-group-identifier", params.client_group_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.guard_path:
                args.extend(["--guard-path", params.guard_path])
            if params.guard_point_type:
                args.extend(["--guard-point-type", params.guard_point_type])
            if params.guard_enabled is not None:
                args.append("--guard-enabled" if params.guard_enabled else "--no-guard-enabled")
            if params.cte_policy_identifier:
                args.extend(["--cte-policy-identifier", params.cte_policy_identifier])
            if params.cte_policy_name:
                args.extend(["--cte-policy-name", params.cte_policy_name])
            if params.mfa_enabled is not None:
                args.append("--mfa-enabled" if params.mfa_enabled else "--no-mfa-enabled")
            if params.sort:
                args.extend(["--sort", params.sort])
            if params.fetch_current_domain_resources_only:
                args.append("--fetch-current-domain-resources-only")
            if params.native_domain:
                args.extend(["--native-domain", params.native_domain])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "get_guardpoint":
            params = CTEClientGroupGetGuardPointParams(**kwargs)
            args = ["cte", "client-groups", "get-guardpoint", "--client-group-identifier", params.client_group_identifier, "--guard-point-identifier", params.guard_point_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "modify_guardpoint":
            params = CTEClientGroupModifyGuardPointParams(**kwargs)
            args = ["cte", "client-groups", "modify-guardpoints", "--client-group-identifier", params.client_group_identifier, "--guard-point-identifier", params.guard_point_identifier]
            if params.guard_enabled is not None:
                args.append("--guard-enabled" if params.guard_enabled else "--no-guard-enabled")
            if params.mfa_enabled is not None:
                args.append("--mfa-enabled" if params.mfa_enabled else "--no-mfa-enabled")
            if params.network_share_credentials_identifier:
                args.extend(["--network-share-credentials-identifier", params.network_share_credentials_identifier])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "unguard_guardpoint":
            params = CTEClientGroupUnguardGuardPointParams(**kwargs)
            args = ["cte", "client-groups", "unguard-guardpoints", "--client-group-identifier", params.client_group_identifier, "--guard-point-identifier", params.guard_point_identifier]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "unguard_bulk_guardpoints":
            params = CTEClientGroupUnguardBulkGuardPointsParams(**kwargs)
            args = ["cte", "client-groups", "unguard-bulk-guardpoints", "--client-group-identifier", params.client_group_identifier, "--guard-point-identifier-list", params.guard_point_identifier_list]
            return self.execute_with_domain(args, params.domain, params.auth_domain)

        # Special Operations
        elif action == "modify_password":
            params = CTEClientGroupModifyPasswordParams(**kwargs)
            args = ["cte", "client-groups", "modify-password", "--client-group-identifier", params.client_group_identifier, "--client-group-password", params.client_group_password, "--password-creation-method", params.password_creation_method]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "modify_auth_binaries":
            params = CTEClientGroupModifyAuthBinariesParams(**kwargs)
            if not params.auth_bin_json and not params.auth_bin_json_file:
                raise ValueError("Either auth_bin_json or auth_bin_json_file must be specified")
            args = ["cte", "client-groups", "modify-auth-binaries", "--client-group-identifier", params.client_group_identifier]
            if params.auth_bin_json:
                args.extend(["--auth-bin-json", params.auth_bin_json])
            elif params.auth_bin_json_file:
                args.extend(["--auth-bin-json-file", params.auth_bin_json_file])
            if params.re_sign:
                args.extend(["--re-sign", "true"])
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        elif action == "send_ldt_pause":
            params = CTEClientGroupSendLDTPauseParams(**kwargs)
            args = ["cte", "client-groups", "send-ldt-pause", "--client-group-identifier", params.client_group_identifier, "--ldt-pause", "true" if params.ldt_pause else "false"]
            return self.execute_with_domain(args, params.domain, params.auth_domain)
        else:
            raise ValueError(f"Unknown action: {action}")


# Export only the grouped tool
CTE_CLIENTGROUP_TOOLS = [CTEClientGroupManagementTool]
