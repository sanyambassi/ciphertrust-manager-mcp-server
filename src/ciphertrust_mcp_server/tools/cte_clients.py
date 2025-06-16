"""CTE Clients management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional, List, Literal

from pydantic import BaseModel, Field

from .base import BaseTool


# Client Parameter Models
class CTEClientCreateParams(BaseModel):
    """Parameters for creating a CTE client."""
    cte_client_name: str = Field(..., description="Name for CTE Client")
    client_password: Optional[str] = Field(None, description="Client password")
    password_creation_method: str = Field("GENERATE", description="Method to create password: GENERATE or MANUAL")
    comm_enabled: bool = Field(False, description="Toggle CTE client Communication parameter")
    reg_allowed: bool = Field(False, description="Toggle CTE Client Registration Allow parameter")
    cte_client_type: Optional[str] = Field(None, description="Type of CTE Client: FS, CSI or CTE-U")
    cte_profile_identifier: Optional[str] = Field(None, description="CTE profile identifier")
    description: Optional[str] = Field(None, description="Description for the CTE client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create client in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientListParams(BaseModel):
    """Parameters for listing CTE clients."""
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    cte_client_name: Optional[str] = Field(None, description="Filter by CTE Client name")
    cte_client_type: Optional[str] = Field(None, description="Filter by type: FS, CSI or CTE-U")
    client_os_type: Optional[str] = Field(None, description="Operating System Type: Windows, Linux, FreeBSD")
    client_status: Optional[str] = Field(None, description="Health Status: HEALTHY, ERROR, WARNING, UNREGISTERED")
    client_version: Optional[str] = Field(None, description="Client Version")
    client_mfa_enabled: bool = Field(False, description="Filter MFA enabled clients")
    num_errors: Optional[int] = Field(None, description="Filter by number of errors")
    num_gp_errors: Optional[int] = Field(None, description="Filter by number of GuardPoint errors")
    num_warnings: Optional[int] = Field(None, description="Filter by number of warnings")
    assigned_with_ldt_group_comm_service: bool = Field(False, description="Filter by LDT group service assignment")
    enable_domain_sharing: bool = Field(False, description="Enable/Disable domain sharing for resource")
    fetch_current_domain_resources_only: bool = Field(False, description="Filter resources belonging to current domain only")
    native_domain: Optional[str] = Field(None, description="Filter by native domain (comma-separated list)")
    filter_protection_mode: Optional[str] = Field(None, description="Filter by protection mode: CTE or RWP")
    cte_namespace_name: Optional[str] = Field(None, description="Filter CSI client by namespace (comma-separated)")
    cte_node_name: Optional[str] = Field(None, description="Filter CSI client by node name (comma-separated)")
    cte_storage_group_name: Optional[str] = Field(None, description="Filter CSI client by storage group (comma-separated)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list clients from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGetParams(BaseModel):
    """Parameters for getting a CTE client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get client from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientDeleteParams(BaseModel):
    """Parameters for deleting a CTE client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client (UUID, URI or Name)")
    del_client: bool = Field(True, description="Identifies that client delete is triggered")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete client from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientBulkDeleteParams(BaseModel):
    """Parameters for bulk deleting CTE clients."""
    client_identifier_list: Optional[str] = Field(None, description="Comma-separated list of client identifiers")
    del_client: bool = Field(True, description="Identifies that client delete is triggered")
    delete_stale_clients: bool = Field(False, description="Option for cleaning up stale clients")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete clients from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientModifyParams(BaseModel):
    """Parameters for modifying a CTE client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client (UUID, URI or Name)")
    client_password: Optional[str] = Field(None, description="Client password")
    password_creation_method: Optional[str] = Field(None, description="Method to create password: GENERATE or MANUAL")
    comm_enabled: Optional[bool] = Field(None, description="Toggle CTE client Communication parameter")
    reg_allowed: Optional[bool] = Field(None, description="Toggle CTE Client Registration Allow parameter")
    cte_client_locked: Optional[bool] = Field(None, description="Toggle CTE client Lock Status")
    system_locked: Optional[bool] = Field(None, description="Toggle System Lock Status")
    cte_profile_identifier: Optional[str] = Field(None, description="CTE profile identifier")
    host_name: Optional[str] = Field(None, description="HostName of CTE Client")
    client_mfa_enabled: Optional[bool] = Field(None, description="Enable MFA at client level")
    lgcs_access_only: Optional[bool] = Field(None, description="Whether client can be added to LDT communication group")
    max_num_cache_log: Optional[int] = Field(None, description="Maximum number of logs to cache")
    max_space_cache_log: Optional[int] = Field(None, description="Maximum space for cached logs")
    rekey_rate: Optional[int] = Field(None, description="Rekey rate")
    protection_mode: Optional[str] = Field(None, description="Protection mode: CTE RWP")
    enable_domain_sharing: Optional[bool] = Field(None, description="Enable/Disable domain sharing for resource")
    shared_domain_list: Optional[str] = Field(None, description='List of domains to share with (JSON array string)')
    capabilities: Optional[str] = Field(None, description="Capabilities")
    enabled_capabilities: Optional[str] = Field(None, description="Enabled capabilities")
    dynamic_parameters: Optional[str] = Field(None, description="CTE Dynamic Parameters in JSON format")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify client in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Enrollment Parameter Models
class CTEClientEnrollParams(BaseModel):
    """Parameters for enrolling a CTE client."""
    cte_client_name: str = Field(..., description="Name for CTE Client")
    client_reg_identifier: str = Field(..., description="Client Registration ID for CTE Client")
    host_name: str = Field(..., description="HostName of CTE Client")
    client_os_type: str = Field(..., description="Operating System Type: Windows, Linux, FreeBSD")
    agent_type: Optional[str] = Field(None, description="Agent Type on CTE Client")
    agent_version: Optional[str] = Field(None, description="Agent Version")
    agent_build_identifier: Optional[int] = Field(None, description="Build Id of Agent")
    comm_version_min: Optional[int] = Field(None, description="Minimum communication version")
    comm_version_max: Optional[int] = Field(None, description="Maximum communication version")
    curr_time: Optional[int] = Field(None, description="Current Time on Agent")
    description: Optional[str] = Field(None, description="Description")
    enable_cloud: bool = Field(False, description="Enable Cloud")
    enable_docker: bool = Field(False, description="Enable Docker")
    enable_es: bool = Field(False, description="Enable ES")
    enable_fs: bool = Field(False, description="Enable FS")
    enable_ldt: bool = Field(False, description="Enable LDT")
    enable_rwp: bool = Field(False, description="Enable Ransomware Protection")
    features: Optional[str] = Field(None, description="Features")
    install_directory: Optional[str] = Field(None, description="Install Directory")
    lgcs_access_only: bool = Field(False, description="Whether client can be added to LDT communication group")
    os_kernel: Optional[str] = Field(None, description="Specific CTE Linux Kernel Flavour")
    os_sub_type: Optional[str] = Field(None, description="Specific Flavour of Operating system")
    secfs_key: Optional[str] = Field(None, description="SecFs Key")
    server_hostname: Optional[str] = Field(None, description="Hostname or IP of Key Server")
    silo_name: Optional[str] = Field(None, description="Silo Name")
    client_group: Optional[str] = Field(None, description="Client Group")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to enroll client in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientUnenrollParams(BaseModel):
    """Parameters for unenrolling a CTE client."""
    cte_client_name: str = Field(..., description="Name for CTE Client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to unenroll client from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# GuardPoint Management Parameter Models
class CTEClientCreateGuardPointParams(BaseModel):
    """Parameters for creating a guardpoint on a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client (UUID, URI or Name)")
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


class CTEClientCreateGuardPointCSVParams(BaseModel):
    """Parameters for creating guardpoints from CSV file."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client (UUID, URI or Name)")
    guard_path_csv_file: str = Field(..., description="GuardPath list passed in CSV format via a file")
    guard_point_type: str = Field(..., description="Type: directory_auto, directory_manual, ransomware_protection, etc.")
    cte_policy_identifier: Optional[str] = Field(None, description="Identifier for CTE Policy")
    guard_enabled: bool = Field(True, description="Whether guard is enabled or not")
    auto_mount_enabled: bool = Field(False, description="Flag for automount (Standard or LDT policy)")
    cifs_enabled: bool = Field(False, description="Flag for CIFS enable")
    early_access: bool = Field(False, description="Early access (secure start) on Windows clients")
    preserve_sparse_regions: bool = Field(True, description="Preserve sparse file regions (LDT clients only)")
    is_idt_capable_device: bool = Field(False, description="Whether device is IDT capable")
    network_share_credentials_identifier: Optional[str] = Field(None, description="Identifier of CIFS credentials")
    disk_name: Optional[str] = Field(None, description="Name of disk for Oracle ASM disk group")
    disk_group_name: Optional[str] = Field(None, description="Name of Oracle ASM disk group")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create guardpoints in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientListGuardPointsParams(BaseModel):
    """Parameters for listing guardpoints on a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    guard_path: Optional[str] = Field(None, description="Filter by guard path")
    guard_point_type: Optional[str] = Field(None, description="Filter by guardpoint type")
    guard_point_state: Optional[str] = Field(None, description="Filter by state: ACTIVE or INACTIVE")
    guard_enabled: Optional[bool] = Field(None, description="Filter by guard enabled status")
    cte_policy_identifier: Optional[str] = Field(None, description="Filter by CTE Policy identifier")
    cte_policy_name: Optional[str] = Field(None, description="Filter by CTE Policy name")
    client_group_identifier: Optional[str] = Field(None, description="Filter by Client Group identifier")
    client_group_name: Optional[str] = Field(None, description="Filter by Client Group name")
    mfa_enabled: Optional[bool] = Field(None, description="Filter by MFA enabled status")
    pending_operation: Optional[str] = Field(None, description="Filter by pending operation: DELETE")
    sort: Optional[str] = Field(None, description="Sort field (prefix with - for descending)")
    fetch_current_domain_resources_only: bool = Field(False, description="Filter resources belonging to current domain only")
    native_domain: Optional[str] = Field(None, description="Filter by native domain (comma-separated list)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list guardpoints from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGetGuardPointParams(BaseModel):
    """Parameters for getting a guardpoint on a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get guardpoint from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientModifyGuardPointParams(BaseModel):
    """Parameters for modifying a guardpoint on a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    guard_enabled: Optional[bool] = Field(None, description="Whether guard is enabled or not")
    mfa_enabled: Optional[bool] = Field(None, description="Enable MFA at guard point level")
    network_share_credentials_identifier: Optional[str] = Field(None, description="Identifier of CIFS credentials")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify guardpoint in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientModifyEarlyAccessParams(BaseModel):
    """Parameters for modifying early access on a guardpoint."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    early_access: bool = Field(..., description="Early access (secure start) on Windows clients")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify early access in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientPreserveSparseRegionOffParams(BaseModel):
    """Parameters for turning off preserve sparse regions."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientUnguardGuardPointParams(BaseModel):
    """Parameters for unguarding a guardpoint from a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier: str = Field(..., description="Identifier for CTE GuardPoint")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to unguard guardpoint from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientUnguardBulkGuardPointsParams(BaseModel):
    """Parameters for unguarding multiple guardpoints from a client."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    guard_point_identifier_list: str = Field(..., description="Comma-separated list of GuardPoint identifiers")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to unguard guardpoints from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Agent Info Management Parameter Models
class CTEClientAgentInfoParams(BaseModel):
    """Parameters for agent info operations."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientClearAgentInfoParams(BaseModel):
    """Parameters for clearing agent info."""
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to clear agent info in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Special Operations Parameter Models
class CTEClientGetClientGroupsParams(BaseModel):
    """Parameters for getting client groups."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get client groups from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientModifyPasswordParams(BaseModel):
    """Parameters for modifying client password."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    client_password: str = Field(..., description="New client password")
    password_creation_method: str = Field("MANUAL", description="Method to create password: GENERATE or MANUAL")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify password in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientModifyAuthBinariesParams(BaseModel):
    """Parameters for modifying authorized binaries."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    auth_bin_json: Optional[str] = Field(None, description="Authorized binary parameters in JSON format")
    auth_bin_json_file: Optional[str] = Field(None, description="File containing authorized binary parameters in JSON")
    re_sign: bool = Field(False, description="Whether authorized binaries should be re-signed")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify auth binaries in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientSendLDTPauseParams(BaseModel):
    """Parameters for sending LDT pause/resume request."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    ldt_pause: bool = Field(..., description="True to pause LDT, False to resume")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to send LDT pause in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientQueryCapabilitiesParams(BaseModel):
    """Parameters for querying client capabilities."""
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to query capabilities in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientQueryStatusUpdateParams(BaseModel):
    """Parameters for querying status update."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to query status in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientGetChallengeResponseParams(BaseModel):
    """Parameters for getting challenge response."""
    cte_client_identifier: str = Field(..., description="Identifier for CTE Client")
    challenge: str = Field(..., description="Challenge string generated on CTE client")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get challenge response from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Compatibility Matrix Parameter Models
class CTEClientGetCompatibilityMatrixParams(BaseModel):
    """Parameters for getting compatibility matrix."""
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get matrix from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientUploadCompatibilityMatrixParams(BaseModel):
    """Parameters for uploading compatibility matrix."""
    kernel_json_file: str = Field(..., description="Kernel compatibility matrix JSON file location")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to upload matrix to (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientDeleteCompatibilityMatrixParams(BaseModel):
    """Parameters for deleting compatibility matrix."""
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete matrix from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEClientManagementTool(BaseTool):
    """Manage CTE clients and related operations (grouped)."""

    @property
    def name(self) -> str:
        return "cte_client_management"

    @property
    def description(self) -> str:
        return "Manage CTE clients and related operations (create, list, get, delete, modify, enroll, guardpoints, agent info, etc.)"

    def get_schema(self) -> dict[str, Any]:
        return {
            "title": "CTEClientManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": [
                        "create", "list", "get", "delete", "bulk_delete", "modify", "enroll", "unenroll",
                        "create_guardpoint", "create_guardpoint_csv", "list_guardpoints", "get_guardpoint", "modify_guardpoint",
                        "modify_early_access", "preserve_sparse_region_off", "unguard_guardpoint", "unguard_bulk_guardpoints",
                        "check_agent_info", "clear_agent_info", "download_agent_info", "get_agent_info", "get_client_groups",
                        "modify_password", "modify_auth_binaries", "send_ldt_pause", "query_capabilities", "query_status_update",
                        "get_challenge_response", "get_compatibility_matrix", "upload_compatibility_matrix", "delete_compatibility_matrix"
                    ],
                    "description": "Action to perform"
                },
                **CTEClientCreateParams.model_json_schema()["properties"],
                **CTEClientListParams.model_json_schema()["properties"],
                **CTEClientGetParams.model_json_schema()["properties"],
                **CTEClientDeleteParams.model_json_schema()["properties"],
                **CTEClientBulkDeleteParams.model_json_schema()["properties"],
                **CTEClientModifyParams.model_json_schema()["properties"],
                **CTEClientEnrollParams.model_json_schema()["properties"],
                **CTEClientUnenrollParams.model_json_schema()["properties"],
                **CTEClientCreateGuardPointParams.model_json_schema()["properties"],
                **CTEClientCreateGuardPointCSVParams.model_json_schema()["properties"],
                **CTEClientListGuardPointsParams.model_json_schema()["properties"],
                **CTEClientGetGuardPointParams.model_json_schema()["properties"],
                **CTEClientModifyGuardPointParams.model_json_schema()["properties"],
                **CTEClientModifyEarlyAccessParams.model_json_schema()["properties"],
                **CTEClientPreserveSparseRegionOffParams.model_json_schema()["properties"],
                **CTEClientUnguardGuardPointParams.model_json_schema()["properties"],
                **CTEClientUnguardBulkGuardPointsParams.model_json_schema()["properties"],
                **CTEClientAgentInfoParams.model_json_schema()["properties"],
                **CTEClientClearAgentInfoParams.model_json_schema()["properties"],
                **CTEClientGetClientGroupsParams.model_json_schema()["properties"],
                **CTEClientModifyPasswordParams.model_json_schema()["properties"],
                **CTEClientModifyAuthBinariesParams.model_json_schema()["properties"],
                **CTEClientSendLDTPauseParams.model_json_schema()["properties"],
                **CTEClientQueryCapabilitiesParams.model_json_schema()["properties"],
                **CTEClientQueryStatusUpdateParams.model_json_schema()["properties"],
                **CTEClientGetChallengeResponseParams.model_json_schema()["properties"],
                **CTEClientGetCompatibilityMatrixParams.model_json_schema()["properties"],
                **CTEClientUploadCompatibilityMatrixParams.model_json_schema()["properties"],
                **CTEClientDeleteCompatibilityMatrixParams.model_json_schema()["properties"],
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        
        if action == "create":
            params = CTEClientCreateParams(**kwargs)
            cmd = ["cte", "client", "create", "--cte-client-name", params.cte_client_name]
            if params.client_password:
                cmd.extend(["--client-password", params.client_password])
            if params.password_creation_method != "GENERATE":
                cmd.extend(["--password-creation-method", params.password_creation_method])
            if params.comm_enabled:
                cmd.append("--comm-enabled")
            if params.reg_allowed:
                cmd.append("--reg-allowed")
            if params.cte_client_type:
                cmd.extend(["--cte-client-type", params.cte_client_type])
            if params.cte_profile_identifier:
                cmd.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.description:
                cmd.extend(["--description", params.description])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "list":
            params = CTEClientListParams(**kwargs)
            cmd = ["cte", "client", "list"]
            cmd.extend(["--limit", str(params.limit)])
            cmd.extend(["--skip", str(params.skip)])
            if params.cte_client_name:
                cmd.extend(["--cte-client-name", params.cte_client_name])
            if params.cte_client_type:
                cmd.extend(["--cte-client-type", params.cte_client_type])
            if params.client_os_type:
                cmd.extend(["--client-os-type", params.client_os_type])
            if params.client_status:
                cmd.extend(["--client-status", params.client_status])
            if params.client_version:
                cmd.extend(["--client-version", params.client_version])
            if params.client_mfa_enabled:
                cmd.append("--client-mfa-enabled")
            if params.num_errors is not None:
                cmd.extend(["--num-errors", str(params.num_errors)])
            if params.num_gp_errors is not None:
                cmd.extend(["--num-gp-errors", str(params.num_gp_errors)])
            if params.num_warnings is not None:
                cmd.extend(["--num-warnings", str(params.num_warnings)])
            if params.assigned_with_ldt_group_comm_service:
                cmd.append("--assigned-with-ldt-group-comm-service")
            if params.enable_domain_sharing:
                cmd.append("--enable-domain-sharing")
            if params.fetch_current_domain_resources_only:
                cmd.append("--fetch-current-domain-resources-only")
            if params.native_domain:
                cmd.extend(["--native-domain", params.native_domain])
            if params.filter_protection_mode:
                cmd.extend(["--filter-protection-mode", params.filter_protection_mode])
            if params.cte_namespace_name:
                cmd.extend(["--cte-namespace-name", params.cte_namespace_name])
            if params.cte_node_name:
                cmd.extend(["--cte-node-name", params.cte_node_name])
            if params.cte_storage_group_name:
                cmd.extend(["--cte-storage-group-name", params.cte_storage_group_name])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get":
            params = CTEClientGetParams(**kwargs)
            cmd = ["cte", "client", "get", "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "delete":
            params = CTEClientDeleteParams(**kwargs)
            cmd = ["cte", "client", "delete", "--cte-client-identifier", params.cte_client_identifier]
            if params.del_client:
                cmd.append("--del-client")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "bulk_delete":
            params = CTEClientBulkDeleteParams(**kwargs)
            cmd = ["cte", "client", "bulk-delete"]
            if params.client_identifier_list:
                cmd.extend(["--client-identifier-list", params.client_identifier_list])
            if params.del_client:
                cmd.append("--del-client")
            if params.delete_stale_clients:
                cmd.append("--delete-stale-clients")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "modify":
            params = CTEClientModifyParams(**kwargs)
            cmd = ["cte", "client", "modify", "--cte-client-identifier", params.cte_client_identifier]
            if params.client_password:
                cmd.extend(["--client-password", params.client_password])
            if params.password_creation_method:
                cmd.extend(["--password-creation-method", params.password_creation_method])
            if params.comm_enabled is not None:
                cmd.append("--comm-enabled" if params.comm_enabled else "--no-comm-enabled")
            if params.reg_allowed is not None:
                cmd.append("--reg-allowed" if params.reg_allowed else "--no-reg-allowed")
            if params.cte_client_locked is not None:
                cmd.append("--cte-client-locked" if params.cte_client_locked else "--no-cte-client-locked")
            if params.system_locked is not None:
                cmd.append("--system-locked" if params.system_locked else "--no-system-locked")
            if params.cte_profile_identifier:
                cmd.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.host_name:
                cmd.extend(["--host-name", params.host_name])
            if params.client_mfa_enabled is not None:
                cmd.append("--client-mfa-enabled" if params.client_mfa_enabled else "--no-client-mfa-enabled")
            if params.lgcs_access_only is not None:
                cmd.append("--lgcs-access-only" if params.lgcs_access_only else "--no-lgcs-access-only")
            if params.max_num_cache_log is not None:
                cmd.extend(["--max-num-cache-log", str(params.max_num_cache_log)])
            if params.max_space_cache_log is not None:
                cmd.extend(["--max-space-cache-log", str(params.max_space_cache_log)])
            if params.rekey_rate is not None:
                cmd.extend(["--rekey-rate", str(params.rekey_rate)])
            if params.protection_mode:
                cmd.extend(["--protection-mode", params.protection_mode])
            if params.enable_domain_sharing is not None:
                cmd.append("--enable-domain-sharing" if params.enable_domain_sharing else "--no-enable-domain-sharing")
            if params.shared_domain_list:
                cmd.extend(["--shared-domain-list", params.shared_domain_list])
            if params.capabilities:
                cmd.extend(["--capabilities", params.capabilities])
            if params.enabled_capabilities:
                cmd.extend(["--enabled-capabilities", params.enabled_capabilities])
            if params.dynamic_parameters:
                cmd.extend(["--dynamic-parameters", params.dynamic_parameters])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "enroll":
            params = CTEClientEnrollParams(**kwargs)
            cmd = ["cte", "client", "enroll", "--cte-client-name", params.cte_client_name,
                  "--client-reg-identifier", params.client_reg_identifier,
                  "--host-name", params.host_name,
                  "--client-os-type", params.client_os_type]
            if params.agent_type:
                cmd.extend(["--agent-type", params.agent_type])
            if params.agent_version:
                cmd.extend(["--agent-version", params.agent_version])
            if params.agent_build_identifier is not None:
                cmd.extend(["--agent-build-identifier", str(params.agent_build_identifier)])
            if params.comm_version_min is not None:
                cmd.extend(["--comm-version-min", str(params.comm_version_min)])
            if params.comm_version_max is not None:
                cmd.extend(["--comm-version-max", str(params.comm_version_max)])
            if params.curr_time is not None:
                cmd.extend(["--curr-time", str(params.curr_time)])
            if params.description:
                cmd.extend(["--description", params.description])
            if params.enable_cloud:
                cmd.append("--enable-cloud")
            if params.enable_docker:
                cmd.append("--enable-docker")
            if params.enable_es:
                cmd.append("--enable-es")
            if params.enable_fs:
                cmd.append("--enable-fs")
            if params.enable_ldt:
                cmd.append("--enable-ldt")
            if params.enable_rwp:
                cmd.append("--enable-rwp")
            if params.features:
                cmd.extend(["--features", params.features])
            if params.install_directory:
                cmd.extend(["--install-directory", params.install_directory])
            if params.lgcs_access_only:
                cmd.append("--lgcs-access-only")
            if params.os_kernel:
                cmd.extend(["--os-kernel", params.os_kernel])
            if params.os_sub_type:
                cmd.extend(["--os-sub-type", params.os_sub_type])
            if params.secfs_key:
                cmd.extend(["--secfs-key", params.secfs_key])
            if params.server_hostname:
                cmd.extend(["--server-hostname", params.server_hostname])
            if params.silo_name:
                cmd.extend(["--silo-name", params.silo_name])
            if params.client_group:
                cmd.extend(["--client-group", params.client_group])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "unenroll":
            params = CTEClientUnenrollParams(**kwargs)
            cmd = ["cte", "client", "unenroll", "--cte-client-name", params.cte_client_name]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "create_guardpoint":
            params = CTEClientCreateGuardPointParams(**kwargs)
            cmd = ["cte", "client", "create-guardpoint", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-path-list", params.guard_path_list,
                  "--guard-point-type", params.guard_point_type]
            if params.cte_policy_identifier:
                cmd.extend(["--cte-policy-identifier", params.cte_policy_identifier])
            if not params.guard_enabled:
                cmd.append("--no-guard-enabled")
            if params.auto_mount_enabled:
                cmd.append("--auto-mount-enabled")
            if params.cifs_enabled:
                cmd.append("--cifs-enabled")
            if params.early_access:
                cmd.append("--early-access")
            if not params.preserve_sparse_regions:
                cmd.append("--no-preserve-sparse-regions")
            if params.mfa_enabled:
                cmd.append("--mfa-enabled")
            if params.intelligent_protection:
                cmd.append("--intelligent-protection")
            if params.is_idt_capable_device:
                cmd.append("--is-idt-capable-device")
            if params.network_share_credentials_identifier:
                cmd.extend(["--network-share-credentials-identifier", params.network_share_credentials_identifier])
            if params.disk_name:
                cmd.extend(["--disk-name", params.disk_name])
            if params.disk_group_name:
                cmd.extend(["--disk-group-name", params.disk_group_name])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "create_guardpoint_csv":
            params = CTEClientCreateGuardPointCSVParams(**kwargs)
            cmd = ["cte", "client", "create-guardpoint-csv", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-path-csv-file", params.guard_path_csv_file,
                  "--guard-point-type", params.guard_point_type]
            if params.cte_policy_identifier:
                cmd.extend(["--cte-policy-identifier", params.cte_policy_identifier])
            if not params.guard_enabled:
                cmd.append("--no-guard-enabled")
            if params.auto_mount_enabled:
                cmd.append("--auto-mount-enabled")
            if params.cifs_enabled:
                cmd.append("--cifs-enabled")
            if params.early_access:
                cmd.append("--early-access")
            if not params.preserve_sparse_regions:
                cmd.append("--no-preserve-sparse-regions")
            if params.is_idt_capable_device:
                cmd.append("--is-idt-capable-device")
            if params.network_share_credentials_identifier:
                cmd.extend(["--network-share-credentials-identifier", params.network_share_credentials_identifier])
            if params.disk_name:
                cmd.extend(["--disk-name", params.disk_name])
            if params.disk_group_name:
                cmd.extend(["--disk-group-name", params.disk_group_name])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "list_guardpoints":
            params = CTEClientListGuardPointsParams(**kwargs)
            cmd = ["cte", "client", "list-guardpoints", "--cte-client-identifier", params.cte_client_identifier]
            cmd.extend(["--limit", str(params.limit)])
            cmd.extend(["--skip", str(params.skip)])
            if params.guard_path:
                cmd.extend(["--guard-path", params.guard_path])
            if params.guard_point_type:
                cmd.extend(["--guard-point-type", params.guard_point_type])
            if params.guard_point_state:
                cmd.extend(["--guard-point-state", params.guard_point_state])
            if params.guard_enabled is not None:
                cmd.append("--guard-enabled" if params.guard_enabled else "--no-guard-enabled")
            if params.cte_policy_identifier:
                cmd.extend(["--cte-policy-identifier", params.cte_policy_identifier])
            if params.cte_policy_name:
                cmd.extend(["--cte-policy-name", params.cte_policy_name])
            if params.client_group_identifier:
                cmd.extend(["--client-group-identifier", params.client_group_identifier])
            if params.client_group_name:
                cmd.extend(["--client-group-name", params.client_group_name])
            if params.mfa_enabled is not None:
                cmd.append("--mfa-enabled" if params.mfa_enabled else "--no-mfa-enabled")
            if params.pending_operation:
                cmd.extend(["--pending-operation", params.pending_operation])
            if params.sort:
                cmd.extend(["--sort", params.sort])
            if params.fetch_current_domain_resources_only:
                cmd.append("--fetch-current-domain-resources-only")
            if params.native_domain:
                cmd.extend(["--native-domain", params.native_domain])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get_guardpoint":
            params = CTEClientGetGuardPointParams(**kwargs)
            cmd = ["cte", "client", "get-guardpoint", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier", params.guard_point_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "modify_guardpoint":
            params = CTEClientModifyGuardPointParams(**kwargs)
            cmd = ["cte", "client", "modify-guardpoint", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier", params.guard_point_identifier]
            if params.guard_enabled is not None:
                cmd.append("--guard-enabled" if params.guard_enabled else "--no-guard-enabled")
            if params.mfa_enabled is not None:
                cmd.append("--mfa-enabled" if params.mfa_enabled else "--no-mfa-enabled")
            if params.network_share_credentials_identifier:
                cmd.extend(["--network-share-credentials-identifier", params.network_share_credentials_identifier])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "modify_early_access":
            params = CTEClientModifyEarlyAccessParams(**kwargs)
            cmd = ["cte", "client", "modify-early-access", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier", params.guard_point_identifier]
            cmd.append("--early-access" if params.early_access else "--no-early-access")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "preserve_sparse_region_off":
            params = CTEClientPreserveSparseRegionOffParams(**kwargs)
            cmd = ["cte", "client", "preserve-sparse-region-off", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier", params.guard_point_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "unguard_guardpoint":
            params = CTEClientUnguardGuardPointParams(**kwargs)
            cmd = ["cte", "client", "unguard-guardpoint", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier", params.guard_point_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "unguard_bulk_guardpoints":
            params = CTEClientUnguardBulkGuardPointsParams(**kwargs)
            cmd = ["cte", "client", "unguard-bulk-guardpoints", "--cte-client-identifier", params.cte_client_identifier,
                  "--guard-point-identifier-list", params.guard_point_identifier_list]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "check_agent_info":
            params = CTEClientAgentInfoParams(**kwargs)
            cmd = ["cte", "client", "check-agent-info", "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "clear_agent_info":
            params = CTEClientClearAgentInfoParams(**kwargs)
            cmd = ["cte", "client", "clear-agent-info"]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "download_agent_info":
            params = CTEClientAgentInfoParams(**kwargs)
            cmd = ["cte", "client", "download-agent-info", "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get_agent_info":
            params = CTEClientAgentInfoParams(**kwargs)
            cmd = ["cte", "client", "get-agent-info", "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get_client_groups":
            params = CTEClientGetClientGroupsParams(**kwargs)
            cmd = ["cte", "client", "get-client-groups", "--cte-client-identifier", params.cte_client_identifier]
            cmd.extend(["--limit", str(params.limit)])
            cmd.extend(["--skip", str(params.skip)])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "modify_password":
            params = CTEClientModifyPasswordParams(**kwargs)
            cmd = ["cte", "client", "modify-password", "--cte-client-identifier", params.cte_client_identifier,
                  "--client-password", params.client_password]
            if params.password_creation_method != "MANUAL":
                cmd.extend(["--password-creation-method", params.password_creation_method])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "modify_auth_binaries":
            params = CTEClientModifyAuthBinariesParams(**kwargs)
            cmd = ["cte", "client", "modify-auth-binaries", "--cte-client-identifier", params.cte_client_identifier]
            if params.auth_bin_json:
                cmd.extend(["--auth-bin-json", params.auth_bin_json])
            if params.auth_bin_json_file:
                cmd.extend(["--auth-bin-json-file", params.auth_bin_json_file])
            if params.re_sign:
                cmd.append("--re-sign")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "send_ldt_pause":
            params = CTEClientSendLDTPauseParams(**kwargs)
            cmd = ["cte", "client", "send-ldt-pause", "--cte-client-identifier", params.cte_client_identifier]
            cmd.append("--ldt-pause" if params.ldt_pause else "--no-ldt-pause")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "query_capabilities":
            params = CTEClientQueryCapabilitiesParams(**kwargs)
            cmd = ["cte", "client", "query-capabilities"]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "query_status_update":
            params = CTEClientQueryStatusUpdateParams(**kwargs)
            cmd = ["cte", "client", "query-status-update", "--cte-client-identifier", params.cte_client_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get_challenge_response":
            params = CTEClientGetChallengeResponseParams(**kwargs)
            cmd = ["cte", "client", "get-challenge-response", "--cte-client-identifier", params.cte_client_identifier,
                  "--challenge", params.challenge]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "get_compatibility_matrix":
            params = CTEClientGetCompatibilityMatrixParams(**kwargs)
            cmd = ["cte", "client", "get-compatibility-matrix"]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "upload_compatibility_matrix":
            params = CTEClientUploadCompatibilityMatrixParams(**kwargs)
            cmd = ["cte", "client", "upload-compatibility-matrix", "--kernel-json-file", params.kernel_json_file]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        elif action == "delete_compatibility_matrix":
            params = CTEClientDeleteCompatibilityMatrixParams(**kwargs)
            cmd = ["cte", "client", "delete-compatibility-matrix"]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
            
        else:
            raise ValueError(f"Unknown action: {action}")

CTE_CLIENT_TOOLS = [CTEClientManagementTool]
