"""CTE Profiles management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional

from pydantic import BaseModel, Field

from .base import BaseTool


# CTE Profile Parameter Models
class CTEProfileCreateParams(BaseModel):
    """Parameters for creating a CTE profile."""
    cte_profile_name: str = Field(..., description="Name of the CTE profile")
    cte_profile_description: Optional[str] = Field(None, description="Description of the CTE profile")
    
    # Cache settings
    cache_settings_json: Optional[str] = Field(None, description="Cache settings in JSON format")
    cache_settings_json_file: Optional[str] = Field(None, description="Cache settings JSON file path")
    
    # Basic settings
    concise_logging: Optional[bool] = Field(None, description="Whether to allow concise logging")
    connect_timeout: Optional[int] = Field(None, description="Connect timeout in seconds (5-150)")
    metadata_scan_interval: Optional[int] = Field(None, description="Time interval in seconds to scan files under guard point (default: 600)")
    partial_config_enable: Optional[bool] = Field(None, description="Enable CM to send partial config to agents")
    server_response_rate: Optional[int] = Field(None, description="Percentage value of successful API calls (0-100)")
    
    # Logger settings
    duplicate_settings_json: Optional[str] = Field(None, description="Duplicate settings in JSON format")
    duplicate_settings_json_file: Optional[str] = Field(None, description="Duplicate settings JSON file path")
    file_settings_json: Optional[str] = Field(None, description="File settings configuration in JSON format")
    file_settings_json_file: Optional[str] = Field(None, description="File settings JSON file path")
    management_service_logger_json: Optional[str] = Field(None, description="Management service logger config in JSON format")
    management_service_logger_json_file: Optional[str] = Field(None, description="Management service logger JSON file path")
    policy_evaluation_logger_json: Optional[str] = Field(None, description="Policy evaluation logger config in JSON format")
    policy_evaluation_logger_json_file: Optional[str] = Field(None, description="Policy evaluation logger JSON file path")
    security_admin_logger_json: Optional[str] = Field(None, description="Security admin logger config in JSON format")
    security_admin_logger_json_file: Optional[str] = Field(None, description="Security admin logger JSON file path")
    system_admin_logger_json: Optional[str] = Field(None, description="System admin logger config in JSON format")
    system_admin_logger_json_file: Optional[str] = Field(None, description="System admin logger JSON file path")
    
    # LDT QoS settings
    ldt_qos_cap_cpu_allocation: Optional[bool] = Field(None, description="LDT QOS cap CPU allocation")
    ldt_qos_cpu_percent: Optional[int] = Field(None, description="LDT QOS CPU percent (0-100)")
    ldt_qos_schedule: Optional[str] = Field(None, description="LDT QOS schedule (WEEKENDS, WEEKNIGHTS, ANY_TIME, CUSTOM, CUSTOM_WITH_OVERWRITE)")
    ldt_qos_status_check_rate: Optional[int] = Field(None, description="Frequency to update LDT status (600-86400 seconds)")
    qos_rekey_option: Optional[str] = Field(None, description="LDT QoS Rekey Option (RekeyRate or CPU)")
    qos_rekey_rate: Optional[int] = Field(None, description="LDT QoS Rekey rate in MB/s")
    qos_schedules_json: Optional[str] = Field(None, description="QOS schedules in JSON format")
    qos_schedules_json_file: Optional[str] = Field(None, description="QOS schedules JSON file path")
    
    # MFA settings
    mfa_exempt_user_set_id: Optional[str] = Field(None, description="User set identifier exempted from MFA")
    oidc_connection_id: Optional[str] = Field(None, description="OIDC connection identifier for MFA")
    
    # Ransomware protection settings
    rwp_operation: Optional[str] = Field(None, description="Ransomware protection operation (permit, deny, disable)")
    rwp_process_set: Optional[str] = Field(None, description="ID of process set to be whitelisted")
    
    # Server and upload settings
    server_settings_json: Optional[str] = Field(None, description="Server configuration of cluster nodes in JSON format")
    server_settings_json_file: Optional[str] = Field(None, description="Server configuration JSON file path")
    syslog_settings_json: Optional[str] = Field(None, description="Syslog settings in JSON format")
    syslog_settings_json_file: Optional[str] = Field(None, description="Syslog settings JSON file path")
    upload_settings_json: Optional[str] = Field(None, description="Upload settings in JSON format")
    upload_settings_json_file: Optional[str] = Field(None, description="Upload settings JSON file path")
    
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create profile in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProfileListParams(BaseModel):
    """Parameters for listing CTE profiles."""
    limit: int = Field(10, description="Maximum number of profiles to return")
    skip: int = Field(0, description="Index of the first profile to return")
    cte_profile_name: Optional[str] = Field(None, description="Filter by profile name")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list profiles from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProfileGetParams(BaseModel):
    """Parameters for getting a CTE profile."""
    cte_profile_identifier: str = Field(..., description="Identifier of CTE profile (UUID, URI or Name)")
    cte_profile_name: Optional[str] = Field(None, description="CTE profile name (alternative identifier)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get profile from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProfileDeleteParams(BaseModel):
    """Parameters for deleting a CTE profile."""
    cte_profile_identifier: str = Field(..., description="Identifier of CTE profile (UUID, URI or Name)")
    cte_profile_name: Optional[str] = Field(None, description="CTE profile name (alternative identifier)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete profile from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProfileModifyParams(BaseModel):
    """Parameters for modifying a CTE profile."""
    cte_profile_identifier: str = Field(..., description="Identifier of CTE profile (UUID, URI or Name)")
    cte_profile_description: Optional[str] = Field(None, description="Updated description of the CTE profile")
    
    # Cache settings
    cache_settings_json: Optional[str] = Field(None, description="Cache settings in JSON format")
    cache_settings_json_file: Optional[str] = Field(None, description="Cache settings JSON file path")
    
    # Basic settings
    concise_logging: Optional[bool] = Field(None, description="Whether to allow concise logging")
    connect_timeout: Optional[int] = Field(None, description="Connect timeout in seconds (5-150)")
    metadata_scan_interval: Optional[int] = Field(None, description="Time interval in seconds to scan files under guard point")
    partial_config_enable: Optional[bool] = Field(None, description="Enable CM to send partial config to agents")
    server_response_rate: Optional[int] = Field(None, description="Percentage value of successful API calls (0-100)")
    
    # Logger settings
    duplicate_settings_json: Optional[str] = Field(None, description="Duplicate settings in JSON format")
    duplicate_settings_json_file: Optional[str] = Field(None, description="Duplicate settings JSON file path")
    file_settings_json: Optional[str] = Field(None, description="File settings configuration in JSON format")
    file_settings_json_file: Optional[str] = Field(None, description="File settings JSON file path")
    management_service_logger_json: Optional[str] = Field(None, description="Management service logger config in JSON format")
    management_service_logger_json_file: Optional[str] = Field(None, description="Management service logger JSON file path")
    policy_evaluation_logger_json: Optional[str] = Field(None, description="Policy evaluation logger config in JSON format")
    policy_evaluation_logger_json_file: Optional[str] = Field(None, description="Policy evaluation logger JSON file path")
    security_admin_logger_json: Optional[str] = Field(None, description="Security admin logger config in JSON format")
    security_admin_logger_json_file: Optional[str] = Field(None, description="Security admin logger JSON file path")
    system_admin_logger_json: Optional[str] = Field(None, description="System admin logger config in JSON format")
    system_admin_logger_json_file: Optional[str] = Field(None, description="System admin logger JSON file path")
    
    # LDT QoS settings
    ldt_qos_cap_cpu_allocation: Optional[bool] = Field(None, description="LDT QOS cap CPU allocation")
    ldt_qos_cpu_percent: Optional[int] = Field(None, description="LDT QOS CPU percent (0-100)")
    ldt_qos_schedule: Optional[str] = Field(None, description="LDT QOS schedule (WEEKENDS, WEEKNIGHTS, ANY_TIME, CUSTOM, CUSTOM_WITH_OVERWRITE)")
    ldt_qos_status_check_rate: Optional[int] = Field(None, description="Frequency to update LDT status (600-86400 seconds)")
    qos_rekey_option: Optional[str] = Field(None, description="LDT QoS Rekey Option (RekeyRate or CPU)")
    qos_rekey_rate: Optional[int] = Field(None, description="LDT QoS Rekey rate in MB/s")
    qos_schedules_json: Optional[str] = Field(None, description="QOS schedules in JSON format")
    qos_schedules_json_file: Optional[str] = Field(None, description="QOS schedules JSON file path")
    
    # MFA settings
    mfa_exempt_user_set_id: Optional[str] = Field(None, description="User set identifier exempted from MFA")
    oidc_connection_id: Optional[str] = Field(None, description="OIDC connection identifier for MFA")
    
    # Ransomware protection settings
    rwp_operation: Optional[str] = Field(None, description="Ransomware protection operation (permit, deny, disable)")
    rwp_process_set: Optional[str] = Field(None, description="ID of process set to be whitelisted")
    
    # Server and upload settings
    server_settings_json: Optional[str] = Field(None, description="Server configuration of cluster nodes in JSON format")
    server_settings_json_file: Optional[str] = Field(None, description="Server configuration JSON file path")
    syslog_settings_json: Optional[str] = Field(None, description="Syslog settings in JSON format")
    syslog_settings_json_file: Optional[str] = Field(None, description="Syslog settings JSON file path")
    upload_settings_json: Optional[str] = Field(None, description="Upload settings in JSON format")
    upload_settings_json_file: Optional[str] = Field(None, description="Upload settings JSON file path")
    
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify profile in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEProfileDeleteServerParams(BaseModel):
    """Parameters for deleting a CTE profile syslog server."""
    cte_profile_identifier: str = Field(..., description="Identifier of CTE profile (UUID, URI or Name)")
    syslog_server_name: str = Field(..., description="Identifier for CTE profile syslog server (Hostname or IP)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete server from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# CTE Profile Management Tools
class CTEProfileManagementTool(BaseTool):
    """Manage CTE profiles (grouped)."""

    @property
    def name(self) -> str:
        return "cte_profile_management"

    @property
    def description(self) -> str:
        return "Manage CTE profiles (create, list, get, delete, modify, delete_server)"

    def get_schema(self) -> dict[str, Any]:
        return {
            "title": "CTEProfileManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["create", "list", "get", "delete", "modify", "delete_server"],
                    "description": "Action to perform"
                },
                # Merge all params from the old tool classes
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        if action == "create":
            params = CTEProfileCreateParams(**kwargs)
            args = ["cte", "profiles", "create"]
            args.extend(["--cte-profile-name", params.cte_profile_name])
            if params.cte_profile_description:
                args.extend(["--cte-profile-description", params.cte_profile_description])
            if params.cache_settings_json:
                args.extend(["--cache-settings-json", params.cache_settings_json])
            if params.cache_settings_json_file:
                args.extend(["--cache-settings-json-file", params.cache_settings_json_file])
            if params.concise_logging is not None:
                if params.concise_logging:
                    args.append("--concise-logging")
            if params.connect_timeout is not None:
                args.extend(["--connect-timeout", str(params.connect_timeout)])
            if params.metadata_scan_interval is not None:
                args.extend(["--metadata-scan-interval", str(params.metadata_scan_interval)])
            if params.partial_config_enable is not None:
                if params.partial_config_enable:
                    args.append("--partial-config-enable")
            if params.server_response_rate is not None:
                args.extend(["--server-response-rate", str(params.server_response_rate)])
            if params.duplicate_settings_json:
                args.extend(["--duplicate-settings-json", params.duplicate_settings_json])
            if params.duplicate_settings_json_file:
                args.extend(["--duplicate-settings-json-file", params.duplicate_settings_json_file])
            if params.file_settings_json:
                args.extend(["--file-settings-json", params.file_settings_json])
            if params.file_settings_json_file:
                args.extend(["--file-settings-json-file", params.file_settings_json_file])
            if params.management_service_logger_json:
                args.extend(["--management-service-logger-json", params.management_service_logger_json])
            if params.management_service_logger_json_file:
                args.extend(["--management-service-logger-json-file", params.management_service_logger_json_file])
            if params.policy_evaluation_logger_json:
                args.extend(["--policy-evaluation-logger-json", params.policy_evaluation_logger_json])
            if params.policy_evaluation_logger_json_file:
                args.extend(["--policy-evaluation-logger-json-file", params.policy_evaluation_logger_json_file])
            if params.security_admin_logger_json:
                args.extend(["--security-admin-logger-json", params.security_admin_logger_json])
            if params.security_admin_logger_json_file:
                args.extend(["--security-admin-logger-json-file", params.security_admin_logger_json_file])
            if params.system_admin_logger_json:
                args.extend(["--system-admin-logger-json", params.system_admin_logger_json])
            if params.system_admin_logger_json_file:
                args.extend(["--system-admin-logger-json-file", params.system_admin_logger_json_file])
            if params.ldt_qos_cap_cpu_allocation is not None:
                if params.ldt_qos_cap_cpu_allocation:
                    args.append("--ldt-qos-cap-cpu-allocation")
            if params.ldt_qos_cpu_percent is not None:
                args.extend(["--ldt-qos-cpu-percent", str(params.ldt_qos_cpu_percent)])
            if params.ldt_qos_schedule:
                args.extend(["--ldt-qos-schedule", params.ldt_qos_schedule])
            if params.ldt_qos_status_check_rate is not None:
                args.extend(["--ldt-qos-status-check-rate", str(params.ldt_qos_status_check_rate)])
            if params.qos_rekey_option:
                args.extend(["--qos-rekey-option", params.qos_rekey_option])
            if params.qos_rekey_rate is not None:
                args.extend(["--qos-rekey-rate", str(params.qos_rekey_rate)])
            if params.qos_schedules_json:
                args.extend(["--qos-schedules-json", params.qos_schedules_json])
            if params.qos_schedules_json_file:
                args.extend(["--qos-schedules-json-file", params.qos_schedules_json_file])
            if params.mfa_exempt_user_set_id:
                args.extend(["--mfa-exempt-user-set-id", params.mfa_exempt_user_set_id])
            if params.oidc_connection_id:
                args.extend(["--oidc-connection-id", params.oidc_connection_id])
            if params.rwp_operation:
                args.extend(["--rwp-operation", params.rwp_operation])
            if params.rwp_process_set:
                args.extend(["--rwp-process-set", params.rwp_process_set])
            if params.server_settings_json:
                args.extend(["--server-settings-json", params.server_settings_json])
            if params.server_settings_json_file:
                args.extend(["--server-settings-json-file", params.server_settings_json_file])
            if params.syslog_settings_json:
                args.extend(["--syslog-settings-json", params.syslog_settings_json])
            if params.syslog_settings_json_file:
                args.extend(["--syslog-settings-json-file", params.syslog_settings_json_file])
            if params.upload_settings_json:
                args.extend(["--upload-settings-json", params.upload_settings_json])
            if params.upload_settings_json_file:
                args.extend(["--upload-settings-json-file", params.upload_settings_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "list":
            params = CTEProfileListParams(**kwargs)
            args = ["cte", "profiles", "list"]
            args.extend(["--limit", str(params.limit)])
            args.extend(["--skip", str(params.skip)])
            if params.cte_profile_name:
                args.extend(["--cte-profile-name", params.cte_profile_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "get":
            params = CTEProfileGetParams(**kwargs)
            args = ["cte", "profiles", "get"]
            args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.cte_profile_name:
                args.extend(["--cte-profile-name", params.cte_profile_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete":
            params = CTEProfileDeleteParams(**kwargs)
            args = ["cte", "profiles", "delete"]
            args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.cte_profile_name:
                args.extend(["--cte-profile-name", params.cte_profile_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "modify":
            params = CTEProfileModifyParams(**kwargs)
            args = ["cte", "profiles", "modify"]
            args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            if params.cte_profile_description:
                args.extend(["--cte-profile-description", params.cte_profile_description])
            if params.cache_settings_json:
                args.extend(["--cache-settings-json", params.cache_settings_json])
            if params.cache_settings_json_file:
                args.extend(["--cache-settings-json-file", params.cache_settings_json_file])
            if params.concise_logging is not None:
                if params.concise_logging:
                    args.append("--concise-logging")
            if params.connect_timeout is not None:
                args.extend(["--connect-timeout", str(params.connect_timeout)])
            if params.metadata_scan_interval is not None:
                args.extend(["--metadata-scan-interval", str(params.metadata_scan_interval)])
            if params.partial_config_enable is not None:
                if params.partial_config_enable:
                    args.append("--partial-config-enable")
            if params.server_response_rate is not None:
                args.extend(["--server-response-rate", str(params.server_response_rate)])
            if params.duplicate_settings_json:
                args.extend(["--duplicate-settings-json", params.duplicate_settings_json])
            if params.duplicate_settings_json_file:
                args.extend(["--duplicate-settings-json-file", params.duplicate_settings_json_file])
            if params.file_settings_json:
                args.extend(["--file-settings-json", params.file_settings_json])
            if params.file_settings_json_file:
                args.extend(["--file-settings-json-file", params.file_settings_json_file])
            if params.management_service_logger_json:
                args.extend(["--management-service-logger-json", params.management_service_logger_json])
            if params.management_service_logger_json_file:
                args.extend(["--management-service-logger-json-file", params.management_service_logger_json_file])
            if params.policy_evaluation_logger_json:
                args.extend(["--policy-evaluation-logger-json", params.policy_evaluation_logger_json])
            if params.policy_evaluation_logger_json_file:
                args.extend(["--policy-evaluation-logger-json-file", params.policy_evaluation_logger_json_file])
            if params.security_admin_logger_json:
                args.extend(["--security-admin-logger-json", params.security_admin_logger_json])
            if params.security_admin_logger_json_file:
                args.extend(["--security-admin-logger-json-file", params.security_admin_logger_json_file])
            if params.system_admin_logger_json:
                args.extend(["--system-admin-logger-json", params.system_admin_logger_json])
            if params.system_admin_logger_json_file:
                args.extend(["--system-admin-logger-json-file", params.system_admin_logger_json_file])
            if params.ldt_qos_cap_cpu_allocation is not None:
                if params.ldt_qos_cap_cpu_allocation:
                    args.append("--ldt-qos-cap-cpu-allocation")
            if params.ldt_qos_cpu_percent is not None:
                args.extend(["--ldt-qos-cpu-percent", str(params.ldt_qos_cpu_percent)])
            if params.ldt_qos_schedule:
                args.extend(["--ldt-qos-schedule", params.ldt_qos_schedule])
            if params.ldt_qos_status_check_rate is not None:
                args.extend(["--ldt-qos-status-check-rate", str(params.ldt_qos_status_check_rate)])
            if params.qos_rekey_option:
                args.extend(["--qos-rekey-option", params.qos_rekey_option])
            if params.qos_rekey_rate is not None:
                args.extend(["--qos-rekey-rate", str(params.qos_rekey_rate)])
            if params.qos_schedules_json:
                args.extend(["--qos-schedules-json", params.qos_schedules_json])
            if params.qos_schedules_json_file:
                args.extend(["--qos-schedules-json-file", params.qos_schedules_json_file])
            if params.mfa_exempt_user_set_id:
                args.extend(["--mfa-exempt-user-set-id", params.mfa_exempt_user_set_id])
            if params.oidc_connection_id:
                args.extend(["--oidc-connection-id", params.oidc_connection_id])
            if params.rwp_operation:
                args.extend(["--rwp-operation", params.rwp_operation])
            if params.rwp_process_set:
                args.extend(["--rwp-process-set", params.rwp_process_set])
            if params.server_settings_json:
                args.extend(["--server-settings-json", params.server_settings_json])
            if params.server_settings_json_file:
                args.extend(["--server-settings-json-file", params.server_settings_json_file])
            if params.syslog_settings_json:
                args.extend(["--syslog-settings-json", params.syslog_settings_json])
            if params.syslog_settings_json_file:
                args.extend(["--syslog-settings-json-file", params.syslog_settings_json_file])
            if params.upload_settings_json:
                args.extend(["--upload-settings-json", params.upload_settings_json])
            if params.upload_settings_json_file:
                args.extend(["--upload-settings-json-file", params.upload_settings_json_file])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        elif action == "delete_server":
            params = CTEProfileDeleteServerParams(**kwargs)
            args = ["cte", "profiles", "delete-server"]
            args.extend(["--cte-profile-identifier", params.cte_profile_identifier])
            args.extend(["--syslog-server-name", params.syslog_server_name])
            result = self.execute_with_domain(args, params.domain, params.auth_domain)
            return result.get("data", result.get("stdout", ""))
        else:
            raise ValueError(f"Unknown action: {action}")

# Export only the grouped tool
CTE_PROFILE_TOOLS = [CTEProfileManagementTool]
