"""Complete Optimized CTE Management Tool for CipherTrust Manager with AI Assistant Optimization."""

from typing import Any, Optional, Dict, List
from pydantic import BaseModel, Field
from .base import BaseTool

# JSON Structure Documentation
JSON_EXAMPLES = {
    "user_set": {
        "description": "User set structure for defining users and groups",
        "example": {
            "name": "AdminUsers",
            "description": "Administrative users set",
            "users": [
                {
                    "uname": "admin",
                    "uid": 1000,
                    "gname": "admingroup",
                    "gid": 1000,
                    "os_domain": "CORPORATE"  # For Windows domain users
                },
                {
                    "uname": "user1",
                    "uid": 1001,
                    "gname": "users",
                    "gid": 100
                }
            ]
        }
    },
    "process_set": {
        "description": "Process set structure for defining allowed processes",
        "example": {
            "name": "TrustedProcesses",
            "description": "Trusted application processes",
            "processes": [
                {
                    "signature": "AppSignatureSet",
                    "directory": "/usr/bin",
                    "file": "app.exe"
                },
                {
                    "signature": "SystemSignatureSet",
                    "directory": "/bin",
                    "file": "*"  # All files in directory
                }
            ]
        }
    },
    "resource_set": {
        "description": "Resource set structure for defining protected resources",
        "example": {
            "name": "SensitiveData",
            "description": "Sensitive data directories",
            "resources": [
                {
                    "directory": "/data/sensitive",
                    "file": "*",
                    "include_subfolders": True,
                    "hdfs": False
                },
                {
                    "directory": "/data/reports",
                    "file": "*.pdf",
                    "include_subfolders": False,
                    "hdfs": False
                }
            ]
        }
    },
    "security_rules": {
        "description": "Security rules for policy",
        "example": [
            {
                "effect": "permit,audit",  # Multiple effects comma-separated
                "action": "read",
                "partial_match": False,
                "user_set_id": "AdminUsers",
                "process_set_id": "TrustedProcesses",
                "resource_set_id": "SensitiveData",
                "exclude_user_set": False,
                "exclude_process_set": False,
                "exclude_resource_set": False
            }
        ]
    },
    "key_rules": {
        "description": "Key rules for encryption/decryption",
        "example": [
            {
                "key_id": "DataEncryptionKey",
                "key_type": "name",
                "resource_set_id": "SensitiveData"
            }
        ]
    },
    "ldt_rules": {
        "description": "LDT (Live Data Transformation) rules",
        "example": [
            {
                "resource_set_id": "DataToTransform",
                "current_key": {
                    "key_id": "clear_key",
                    "key_type": "name",
                    "key_usage": "ONLINE"
                },
                "transformation_key": {
                    "key_id": "NewEncryptionKey",
                    "key_type": "name",
                    "key_usage": "ONLINE"
                }
            }
        ]
    },
    "cache_settings": {
        "description": "Cache configuration for CTE profile",
        "example": {
            "max_files": 1000,
            "max_space": 500000  # in KB
        }
    },
    "logger_settings": {
        "description": "Logger configuration (applies to all logger types)",
        "example": {
            "duplicates": "SUPPRESS",  # ALLOW or SUPPRESS
            "threshold": "INFO",  # DEBUG, INFO, WARN, ERROR, FATAL
            "file_enabled": True,
            "syslog_enabled": False,
            "upload_enabled": True
        }
    },
    "syslog_settings": {
        "description": "Syslog configuration for CTE profile",
        "example": {
            "local": False,
            "servers": [
                {
                    "message_format": "RFC5424",  # CEF, LEEF, RFC5424, PLAIN
                    "name": "syslog.company.com",
                    "protocol": "TCP"  # TCP or UDP
                }
            ],
            "syslog_threshold": "WARN"
        }
    }
}

class CTEManagementTool(BaseTool):
    """Optimized CTE Management Tool with improved AI assistant usability.
    
    This tool combines all CTE (CipherTrust Transparent Encryption) operations into a single 
    interface while maintaining clear parameter requirements and examples for each action.
    
    Key Features:
    - Unified interface for all CTE operations
    - Comprehensive JSON examples for complex structures
    - Clear parameter documentation
    - Support for policies, user/process/resource sets, clients, profiles, and more
    
    Common Workflows:
    1. Create sets (users, processes, resources) → Create policy with rules → Create client → Apply guardpoints
    2. Create profile → Create client with profile → Create policy → Apply guardpoints
    3. Create client group → Add clients → Create group guardpoints (applies to all clients)
    """
    @property
    def name(self) -> str:
        return "cte_management"

    @property
    def description(self) -> str:
        return (
            "CTE (CipherTrust Transparent Encryption) management operations. "
            "Supports policies, user sets, process sets, resource sets, clients, profiles, and CSI storage groups. "
            "Each action has specific required and optional parameters - see action_requirements in schema for details."
        )

    def get_schema(self) -> dict[str, Any]:
        """Optimized schema with action-specific parameter guidance."""
        schema = {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": [
                        # POLICY OPERATIONS (Most Common)
                        "policy_create", "policy_list", "policy_get", "policy_delete", "policy_modify",
                        "policy_add_security_rule", "policy_delete_security_rule", "policy_get_security_rule",
                        "policy_list_security_rules", "policy_modify_security_rule",
                        "policy_add_key_rule", "policy_delete_key_rule", "policy_get_key_rule",
                        "policy_list_key_rules", "policy_modify_key_rule",
                        "policy_add_ldt_rule", "policy_delete_ldt_rule", "policy_get_ldt_rule",
                        "policy_list_ldt_rules", "policy_modify_ldt_rule",
                        
                        # USER SET OPERATIONS  
                        "user_set_create", "user_set_list", "user_set_get", "user_set_delete", "user_set_modify",
                        "user_set_add_users", "user_set_delete_user", "user_set_update_user",
                        "user_set_list_users", "user_set_list_policies",
                        
                        # PROCESS SET OPERATIONS
                        "process_set_create", "process_set_list", "process_set_get", "process_set_delete", "process_set_modify",
                        "process_set_add_processes", "process_set_delete_process", "process_set_update_process",
                        "process_set_list_processes", "process_set_list_policies",
                        
                        # RESOURCE SET OPERATIONS
                        "resource_set_create", "resource_set_list", "resource_set_get", "resource_set_delete", "resource_set_modify",
                        "resource_set_add_resources", "resource_set_delete_resource", "resource_set_update_resource",
                        "resource_set_list_resources", "resource_set_list_policies",
                        
                        # CLIENT OPERATIONS
                        "client_create", "client_list", "client_get", "client_delete", "client_modify",
                        "client_create_guardpoint", "client_list_guardpoints", "client_get_guardpoint",
                        "client_modify_guardpoint", "client_unguard_guardpoint",
                        
                        # CLIENT GROUP OPERATIONS
                        "client_group_create", "client_group_list", "client_group_get", "client_group_delete", "client_group_modify",
                        
                        # PROFILE OPERATIONS
                        "profile_create", "profile_list", "profile_get", "profile_delete", "profile_modify",
                        
                        # CSI STORAGE GROUP OPERATIONS
                        "csi_storage_group_create", "csi_storage_group_list", "csi_storage_group_get", 
                        "csi_storage_group_delete", "csi_storage_group_modify"
                    ],
                    "description": "The CTE operation to perform. Choose based on what you want to accomplish."
                },
                
                # COMMON PARAMETERS (used across multiple actions)
                "domain": {
                    "type": "string", 
                    "description": "Domain context (optional, defaults to current domain)"
                },
                "auth_domain": {
                    "type": "string",
                    "description": "Authentication domain (optional, defaults to current auth domain)" 
                },
                "limit": {
                    "type": "integer",
                    "default": 10,
                    "description": "Maximum results to return (for list operations)"
                },
                "skip": {
                    "type": "integer", 
                    "default": 0,
                    "description": "Number of results to skip (for pagination)"
                },
                "description": {
                    "type": "string",
                    "description": "Description for the resource being created/modified"
                },
                
                # POLICY-SPECIFIC PARAMETERS
                "cte_policy_name": {
                    "type": "string",
                    "description": "Name of the CTE policy (required for policy_create)"
                },
                "cte_policy_identifier": {
                    "type": "string", 
                    "description": "Policy identifier: name, ID, or URI (required for policy operations)"
                },
                "policy_type": {
                    "type": "string",
                    "enum": ["Standard", "Cloud_Object_Storage", "LDT", "IDT", "CSI"],
                    "description": "Type of policy (required for policy_create)"
                },
                "never_deny": {
                    "type": "boolean",
                    "default": False,
                    "description": "Always permit operations in policy (for policies)"
                },
                
                # SECURITY RULE PARAMETERS
                "effect": {
                    "type": "string", 
                    "description": "Rule effect: permit, deny, audit, applykey (comma-separated for multiple effects)"
                },
                "action_type": {
                    "type": "string",
                    "description": "Action type: read, write, all_ops, key_op (for security rules)"
                },
                "security_rule_identifier": {
                    "type": "string",
                    "description": "Security rule identifier for rule operations"
                },
                "exclude_user_set": {
                    "type": "boolean",
                    "default": False,
                    "description": "Exclude the user set from the policy"
                },
                "exclude_process_set": {
                    "type": "boolean", 
                    "default": False,
                    "description": "Exclude the process set from the policy"
                },
                "exclude_resource_set": {
                    "type": "boolean",
                    "default": False,
                    "description": "Exclude the resource set from the policy"
                },
                "order_number": {
                    "type": "integer",
                    "description": "Order number for rule ordering"
                },
                
                # KEY RULE PARAMETERS
                "key_identifier": {
                    "type": "string",
                    "description": "Key identifier: name, id, slug, alias, uri, uuid, muid, key_id, or 'clear_key'"
                },
                "key_type": {
                    "type": "string",
                    "description": "Key type: name, id, slug, alias, uri, uuid, muid, or key_id"
                },
                "key_rule_identifier": {
                    "type": "string",
                    "description": "Key rule identifier for rule operations"
                },
                
                # LDT RULE PARAMETERS
                "current_key_json_file": {
                    "type": "string",
                    "description": "Path to JSON file with current key parameters (required for LDT rules)"
                },
                "transform_key_json_file": {
                    "type": "string", 
                    "description": "Path to JSON file with transformation key parameters (required for LDT rules)"
                },
                "ldt_rule_identifier": {
                    "type": "string",
                    "description": "LDT rule identifier for rule operations"
                },
                "is_exclusion_rule": {
                    "type": "boolean",
                    "default": False,
                    "description": "Whether LDT rule is exclusion rule"
                },
                
                # SET IDENTIFIERS
                "user_set_identifier": {
                    "type": "string",
                    "description": "User set identifier (name, ID, or URI)"
                },
                "process_set_identifier": {
                    "type": "string", 
                    "description": "Process set identifier (name, ID, or URI)"
                },
                "resource_set_identifier": {
                    "type": "string",
                    "description": "Resource set identifier (name, ID, or URI)"
                },
                "user_set_name": {
                    "type": "string",
                    "description": "User set name for filtering"
                },
                "process_set_name": {
                    "type": "string",
                    "description": "Process set name for filtering"
                },
                "resource_set_name": {
                    "type": "string",
                    "description": "Resource set name for filtering"
                },
                
                # USER/PROCESS/RESOURCE MANAGEMENT
                "user_index": {
                    "type": "string",
                    "description": "Index of user in user set"
                },
                "user_index_list": {
                    "type": "string",
                    "description": "Comma-separated list of user indices"
                },
                "process_index": {
                    "type": "string",
                    "description": "Index of process in process set"
                },
                "process_index_list": {
                    "type": "string",
                    "description": "Comma-separated list of process indices"
                },
                "resource_index": {
                    "type": "string",
                    "description": "Index of resource in resource set"
                },
                "resource_index_list": {
                    "type": "string",
                    "description": "Comma-separated list of resource indices"
                },
                
                # CLIENT PARAMETERS
                "cte_client_name": {
                    "type": "string",
                    "description": "Name for the CTE client (required for client_create)"
                },
                "cte_client_identifier": {
                    "type": "string",
                    "description": "Client identifier: name, ID, or URI (required for client operations)"
                },
                "client_password": {
                    "type": "string",
                    "description": "Client password (optional, will be generated if not provided)"
                },
                "password_creation_method": {
                    "type": "string",
                    "enum": ["GENERATE", "MANUAL"],
                    "default": "GENERATE",
                    "description": "Method to create password"
                },
                "comm_enabled": {
                    "type": "boolean",
                    "default": False,
                    "description": "Enable communication for the client"
                },
                "reg_allowed": {
                    "type": "boolean", 
                    "default": False,
                    "description": "Allow client registration"
                },
                "cte_client_type": {
                    "type": "string",
                    "enum": ["FS", "CSI", "CTE-U"],
                    "description": "Type of CTE client"
                },
                "cte_profile_identifier": {
                    "type": "string",
                    "description": "CTE profile identifier to assign to client"
                },
                "cte_client_locked": {
                    "type": "boolean",
                    "description": "Lock status of CTE client"
                },
                "system_locked": {
                    "type": "boolean",
                    "description": "System lock status"
                },
                "host_name": {
                    "type": "string",
                    "description": "Hostname of CTE client"
                },
                "client_mfa_enabled": {
                    "type": "boolean",
                    "description": "Enable MFA at client level"
                },
                
                # GUARDPOINT PARAMETERS
                "guard_path_list": {
                    "type": "string",
                    "description": "Comma-separated list of paths to guard (required for client_create_guardpoint)"
                },
                "guard_point_type": {
                    "type": "string",
                    "description": "Guardpoint type: directory_auto, directory_manual, etc. (required for client_create_guardpoint)"
                },
                "guard_point_identifier": {
                    "type": "string",
                    "description": "Guardpoint identifier for guardpoint operations"
                },
                "guard_enabled": {
                    "type": "boolean",
                    "default": True,
                    "description": "Whether guard is enabled"
                },
                "auto_mount_enabled": {
                    "type": "boolean",
                    "default": False,
                    "description": "Enable automount"
                },
                "cifs_enabled": {
                    "type": "boolean",
                    "default": False,
                    "description": "Enable CIFS"
                },
                "early_access": {
                    "type": "boolean",
                    "default": False,
                    "description": "Early access (secure start) on Windows clients"
                },
                "preserve_sparse_regions": {
                    "type": "boolean",
                    "default": True,
                    "description": "Preserve sparse file regions (LDT clients)"
                },
                "mfa_enabled": {
                    "type": "boolean",
                    "default": False,
                    "description": "Enable MFA at guard point level"
                },
                "intelligent_protection": {
                    "type": "boolean",
                    "default": False,
                    "description": "Enable intelligent protection"
                },
                "is_idt_capable_device": {
                    "type": "boolean", 
                    "default": False,
                    "description": "Whether device is IDT capable"
                },
                
                # CLIENT GROUP PARAMETERS
                "client_group_name": {
                    "type": "string",
                    "description": "Name of CTE client group"
                },
                "client_group_identifier": {
                    "type": "string",
                    "description": "Client group identifier"
                },
                "client_group_description": {
                    "type": "string",
                    "description": "Description for CTE client group"
                },
                "client_group_password": {
                    "type": "string",
                    "description": "Password for CTE client group"
                },
                "cluster_type": {
                    "type": "string",
                    "enum": ["NON-CLUSTER", "HDFS"],
                    "default": "NON-CLUSTER",
                    "description": "Cluster type"
                },
                
                # PROFILE PARAMETERS
                "cte_profile_name": {
                    "type": "string",
                    "description": "Name of the CTE profile"
                },
                "cte_profile_description": {
                    "type": "string",
                    "description": "Description of the CTE profile"
                },
                "concise_logging": {
                    "type": "boolean",
                    "description": "Whether to allow concise logging"
                },
                "connect_timeout": {
                    "type": "integer",
                    "description": "Connect timeout in seconds (5-150)"
                },
                "metadata_scan_interval": {
                    "type": "integer",
                    "description": "Time interval in seconds to scan files under guard point"
                },
                "partial_config_enable": {
                    "type": "boolean",
                    "description": "Enable CM to send partial config to agents"
                },
                "server_response_rate": {
                    "type": "integer",
                    "description": "Percentage value of successful API calls (0-100)"
                },
                
                # CSI STORAGE GROUP PARAMETERS
                "storage_group_name": {
                    "type": "string",
                    "description": "Name of CSI storage group"
                },
                "storage_group_identifier": {
                    "type": "string",
                    "description": "CSI storage group identifier"
                },
                "storage_class_name": {
                    "type": "string",
                    "description": "Name of storage class"
                },
                "namespace_name": {
                    "type": "string",
                    "description": "Name of namespace"
                },
                "ctecsi_description": {
                    "type": "string",
                    "description": "Description for CTE CSI resources"
                },
                "ctecsi_profile": {
                    "type": "string",
                    "description": "Client profile for CTE CSI resources"
                },
                
                # JSON FILE PARAMETERS (for complex configurations)
                "user_json": {
                    "type": "string",
                    "description": "User set configuration in JSON format"
                },
                "user_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing user set configuration"
                },
                "process_json": {
                    "type": "string",
                    "description": "Process set configuration in JSON format"
                },
                "process_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing process set configuration"
                },
                "resource_json": {
                    "type": "string", 
                    "description": "Resource set configuration in JSON format"
                },
                "resource_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing resource set configuration"
                },
                
                # RULE JSON PARAMETERS
                "security_rules_json": {
                    "type": "string",
                    "description": "Security rules in JSON format (for policy_create)"
                },
                "security_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing security rules (for policy_create)"
                },
                "key_rules_json": {
                    "type": "string",
                    "description": "Key rules in JSON format (for policy_create)"
                },
                "key_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing key rules (for policy_create)"
                },
                "ldt_rules_json": {
                    "type": "string",
                    "description": "LDT rules in JSON format (for policy_create)"
                },
                "ldt_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing LDT rules (for policy_create)"
                },
                "data_tx_rules_json": {
                    "type": "string",
                    "description": "Data transformation rules in JSON format (for policy_create)"
                },
                "data_tx_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing data transformation rules (for policy_create)"
                },
                "idt_rules_json": {
                    "type": "string",
                    "description": "IDT rules in JSON format (for policy_create)"
                },
                "idt_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing IDT rules (for policy_create)"
                },
                "signature_rules_json": {
                    "type": "string",
                    "description": "Signature rules in JSON format (for policy_create)"
                },
                "signature_rules_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing signature rules (for policy_create)"
                },
                "restrict_update_json": {
                    "type": "string",
                    "description": "Restrict update parameters in JSON format"
                },
                "restrict_update_json_file": {
                    "type": "string",
                    "description": "Path to JSON file containing restrict update parameters"
                },
                
                # SEARCH AND FILTERING
                "search": {
                    "type": "string",
                    "description": "Search filter for list operations"
                },
                "sort": {
                    "type": "string",
                    "description": "Sort field (prefix with - for descending)"
                }
            },
            "required": ["action"],
            "additionalProperties": False,
            
            # ACTION-SPECIFIC REQUIREMENTS AND EXAMPLES
            "action_requirements": {
                "policy_create": {
                    "required": ["cte_policy_name", "policy_type"],
                    "optional": ["description", "never_deny", "security_rules_json", "key_rules_json", "domain", "auth_domain"],
                    "example": {
                        "action": "policy_create",
                        "cte_policy_name": "MyDataPolicy", 
                        "policy_type": "Standard",
                        "description": "Policy for sensitive data protection"
                    }
                },
                "policy_list": {
                    "required": [],
                    "optional": ["limit", "skip", "cte_policy_name", "policy_type", "domain", "auth_domain"],
                    "example": {
                        "action": "policy_list",
                        "limit": 20
                    }
                },
                "policy_get": {
                    "required": ["cte_policy_identifier"],
                    "optional": ["domain", "auth_domain"],
                    "example": {
                        "action": "policy_get",
                        "cte_policy_identifier": "MyDataPolicy"
                    }
                },
                "policy_add_security_rule": {
                    "required": ["cte_policy_identifier", "effect"],
                    "optional": ["action_type", "user_set_identifier", "process_set_identifier", "resource_set_identifier", "exclude_user_set", "exclude_process_set", "exclude_resource_set", "domain", "auth_domain"],
                    "example": {
                        "action": "policy_add_security_rule",
                        "cte_policy_identifier": "MyDataPolicy",
                        "effect": "permit",
                        "action_type": "read",
                        "user_set_identifier": "AdminUsers"
                    }
                },
                "policy_add_key_rule": {
                    "required": ["cte_policy_identifier", "key_identifier"],
                    "optional": ["key_type", "resource_set_identifier", "domain", "auth_domain"],
                    "example": {
                        "action": "policy_add_key_rule", 
                        "cte_policy_identifier": "MyDataPolicy",
                        "key_identifier": "DataEncryptionKey",
                        "key_type": "name"
                    }
                },
                "user_set_create": {
                    "required": [],
                    "optional": ["user_json", "user_json_file", "domain", "auth_domain"],
                    "example": {
                        "action": "user_set_create",
                        "user_json": "{\"name\": \"USet01\", \"description\": \"User set for Administrator in thales.com domain\", \"users\": [{\"uname\": \"Administrator\", \"os_domain\": \"thales.com\"}]}"
                    }
                },
                "client_create": {
                    "required": ["cte_client_name"],
                    "optional": ["client_password", "password_creation_method", "comm_enabled", "reg_allowed", "cte_client_type", "cte_profile_identifier", "description", "domain", "auth_domain"],
                    "example": {
                        "action": "client_create",
                        "cte_client_name": "WebServer01",
                        "comm_enabled": True,
                        "reg_allowed": True
                    }
                },
                "client_create_guardpoint": {
                    "required": ["cte_client_identifier", "guard_path_list", "guard_point_type"],
                    "optional": ["cte_policy_identifier", "guard_enabled", "auto_mount_enabled", "cifs_enabled", "early_access", "preserve_sparse_regions", "mfa_enabled", "intelligent_protection", "is_idt_capable_device", "domain", "auth_domain"],
                    "example": {
                        "action": "client_create_guardpoint",
                        "cte_client_identifier": "WebServer01", 
                        "guard_path_list": "/data/sensitive,/logs/audit",
                        "guard_point_type": "directory_auto",
                        "cte_policy_identifier": "MyDataPolicy"
                    }
                }
            }
        }
        return schema

    async def execute(self, action: str, **kwargs: Any) -> Any:
        """Execute CTE operation with enhanced validation and guidance."""
        # Validate action-specific requirements
        if not self._validate_action_params(action, kwargs):
            schema = self.get_schema()
            requirements = schema.get("action_requirements", {}).get(action, {})
            required_params = requirements.get("required", [])
            example = requirements.get("example", {})
            json_structure = requirements.get("json_structure")
            error_info = {
                "error": f"Missing required parameters for action '{action}'",
                "required": required_params,
                "example": example
            }
            if json_structure:
                error_info["json_structure"] = json_structure
            return error_info
        
        # Route to appropriate operation with clear error handling
        try:
            if action.startswith("policy_"):
                return await self._execute_policy_operation(action, **kwargs)
            elif action.startswith("user_set_"):
                return await self._execute_user_set_operation(action, **kwargs)
            elif action.startswith("process_set_"):
                return await self._execute_process_set_operation(action, **kwargs)
            elif action.startswith("resource_set_"):
                return await self._execute_resource_set_operation(action, **kwargs)
            elif action.startswith("client_group_"):
                return await self._execute_client_group_operation(action, **kwargs)
            elif action.startswith("client_"):
                return await self._execute_client_operation(action, **kwargs)
            elif action.startswith("profile_"):
                return await self._execute_profile_operation(action, **kwargs)
            elif action.startswith("csi_storage_group_"):
                return await self._execute_csi_operation(action, **kwargs)
            else:
                return {"error": f"Unknown action: {action}"}
                
        except Exception as e:
            return {"error": f"Failed to execute {action}: {str(e)}"}

    def _validate_action_params(self, action: str, params: dict) -> bool:
        """Validate that required parameters are present for the action."""
        schema = self.get_schema()
        requirements = schema.get("action_requirements", {}).get(action, {})
        required_params = requirements.get("required", [])

        # Special case for user_set_create: allow either user_json or user_json_file
        if action == "user_set_create":
            if not (params.get("user_json") or params.get("user_json_file")):
                return False
            return True

        for param in required_params:
            if param not in params or params[param] is None:
                return False
        return True

    # ==================================================================================
    # POLICY OPERATIONS
    # ==================================================================================

    async def _execute_policy_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute policy-related operations."""
        
        if action == "policy_create":
            return self._policy_create(**kwargs)
        elif action == "policy_list":
            return self._policy_list(**kwargs) 
        elif action == "policy_get":
            return self._policy_get(**kwargs)
        elif action == "policy_delete":
            return self._policy_delete(**kwargs)
        elif action == "policy_modify":
            return self._policy_modify(**kwargs)
        elif action == "policy_add_security_rule":
            return self._policy_add_security_rule(**kwargs)
        elif action == "policy_delete_security_rule":
            return self._policy_delete_security_rule(**kwargs)
        elif action == "policy_get_security_rule":
            return self._policy_get_security_rule(**kwargs)
        elif action == "policy_list_security_rules":
            return self._policy_list_security_rules(**kwargs)
        elif action == "policy_modify_security_rule":
            return self._policy_modify_security_rule(**kwargs)
        elif action == "policy_add_key_rule":
            return self._policy_add_key_rule(**kwargs)
        elif action == "policy_delete_key_rule":
            return self._policy_delete_key_rule(**kwargs)
        elif action == "policy_get_key_rule":
            return self._policy_get_key_rule(**kwargs)
        elif action == "policy_list_key_rules":
            return self._policy_list_key_rules(**kwargs)
        elif action == "policy_modify_key_rule":
            return self._policy_modify_key_rule(**kwargs)
        elif action == "policy_add_ldt_rule":
            return self._policy_add_ldt_rule(**kwargs)
        elif action == "policy_delete_ldt_rule":
            return self._policy_delete_ldt_rule(**kwargs)
        elif action == "policy_get_ldt_rule":
            return self._policy_get_ldt_rule(**kwargs)
        elif action == "policy_list_ldt_rules":
            return self._policy_list_ldt_rules(**kwargs)
        elif action == "policy_modify_ldt_rule":
            return self._policy_modify_ldt_rule(**kwargs)
        else:
            return {"error": f"Unknown policy action: {action}"}

    def _policy_create(self, **kwargs):
        """Create a CTE policy."""
        args = ["cte", "policies", "create"]
        
        # Required parameters
        args.extend(["--cte-policy-name", kwargs["cte_policy_name"]])
        args.extend(["--policy-type", kwargs["policy_type"]])
        
        # Optional parameters
        if kwargs.get("description"):
            args.extend(["--description", kwargs["description"]])
        if kwargs.get("never_deny", False):
            args.append("--never-deny")
        
        # Rule JSON parameters
        if kwargs.get("security_rules_json"):
            args.extend(["--security-rules-json", kwargs["security_rules_json"]])
        elif kwargs.get("security_rules_json_file"):
            args.extend(["--security-rules-json-file", kwargs["security_rules_json_file"]])
            
        if kwargs.get("key_rules_json"):
            args.extend(["--key-rules-json", kwargs["key_rules_json"]])
        elif kwargs.get("key_rules_json_file"):
            args.extend(["--key-rules-json-file", kwargs["key_rules_json_file"]])
            
        if kwargs.get("data_tx_rules_json"):
            args.extend(["--data-tx-rules-json", kwargs["data_tx_rules_json"]])
        elif kwargs.get("data_tx_rules_json_file"):
            args.extend(["--data-tx-rules-json-file", kwargs["data_tx_rules_json_file"]])
            
        if kwargs.get("ldt_rules_json"):
            args.extend(["--ldt-rules-json", kwargs["ldt_rules_json"]])
        elif kwargs.get("ldt_rules_json_file"):
            args.extend(["--ldt-rules-json-file", kwargs["ldt_rules_json_file"]])
            
        if kwargs.get("idt_rules_json"):
            args.extend(["--idt-rules-json", kwargs["idt_rules_json"]])
        elif kwargs.get("idt_rules_json_file"):
            args.extend(["--idt-rules-json-file", kwargs["idt_rules_json_file"]])
            
        if kwargs.get("signature_rules_json"):
            args.extend(["--signature-rules-json", kwargs["signature_rules_json"]])
        elif kwargs.get("signature_rules_json_file"):
            args.extend(["--signature-rules-json-file", kwargs["signature_rules_json_file"]])
            
        if kwargs.get("restrict_update_json"):
            args.extend(["--restrict-update-json", kwargs["restrict_update_json"]])
        elif kwargs.get("restrict_update_json_file"):
            args.extend(["--restrict-update-json-file", kwargs["restrict_update_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_list(self, **kwargs):
        """List CTE policies."""
        args = ["cte", "policies", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("cte_policy_name"):
            args.extend(["--cte-policy-name", kwargs["cte_policy_name"]])
        if kwargs.get("policy_type"):
            args.extend(["--policy-type", kwargs["policy_type"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_get(self, **kwargs):
        """Get a specific CTE policy."""
        args = ["cte", "policies", "get"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_delete(self, **kwargs):
        """Delete a CTE policy."""
        args = ["cte", "policies", "delete"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_modify(self, **kwargs):
        """Modify a CTE policy."""
        args = ["cte", "policies", "modify"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        
        if kwargs.get("description") is not None:
            args.extend(["--description", kwargs["description"]])
        if kwargs.get("never_deny") is not None:
            args.append("--never-deny" if kwargs["never_deny"] else "--no-never-deny")
        
        if kwargs.get("restrict_update_json"):
            args.extend(["--restrict-update-json", kwargs["restrict_update_json"]])
        elif kwargs.get("restrict_update_json_file"):
            args.extend(["--restrict-update-json-file", kwargs["restrict_update_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_add_security_rule(self, **kwargs):
        """Add a security rule to a policy."""
        args = ["cte", "policies", "add-security-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--effect", kwargs["effect"]])
        
        if kwargs.get("action_type"):
            args.extend(["--action", kwargs["action_type"]])  # Note: CLI uses --action
        if kwargs.get("user_set_identifier"):
            args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        if kwargs.get("process_set_identifier"):
            args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        if kwargs.get("exclude_user_set"):
            args.append("--exclude-user-set")
        if kwargs.get("exclude_process_set"):
            args.append("--exclude-process-set")
        if kwargs.get("exclude_resource_set"):
            args.append("--exclude-resource-set")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_delete_security_rule(self, **kwargs):
        """Delete a security rule from a policy."""
        args = ["cte", "policies", "delete-security-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--security-rule-identifier", kwargs["security_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_get_security_rule(self, **kwargs):
        """Get a security rule from a policy."""
        args = ["cte", "policies", "get-security-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--security-rule-identifier", kwargs["security_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_list_security_rules(self, **kwargs):
        """List security rules in a policy."""
        args = ["cte", "policies", "list-security-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("action_type"):
            args.extend(["--action", kwargs["action_type"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_modify_security_rule(self, **kwargs):
        """Modify a security rule in a policy."""
        args = ["cte", "policies", "modify-security-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--security-rule-identifier", kwargs["security_rule_identifier"]])
        
        if kwargs.get("effect"):
            args.extend(["--effect", kwargs["effect"]])
        if kwargs.get("action_type"):
            args.extend(["--action", kwargs["action_type"]])
        if kwargs.get("order_number") is not None:
            args.extend(["--order-number", str(kwargs["order_number"])])
        if kwargs.get("user_set_identifier"):
            args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        if kwargs.get("process_set_identifier"):
            args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        if kwargs.get("exclude_user_set") is not None:
            args.append("--exclude-user-set" if kwargs["exclude_user_set"] else "--no-exclude-user-set")
        if kwargs.get("exclude_process_set") is not None:
            args.append("--exclude-process-set" if kwargs["exclude_process_set"] else "--no-exclude-process-set")
        if kwargs.get("exclude_resource_set") is not None:
            args.append("--exclude-resource-set" if kwargs["exclude_resource_set"] else "--no-exclude-resource-set")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_add_key_rule(self, **kwargs):
        """Add a key rule to a policy."""
        args = ["cte", "policies", "add-key-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--key-identifier", kwargs["key_identifier"]])
        
        if kwargs.get("key_type"):
            args.extend(["--key-type", kwargs["key_type"]])
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_delete_key_rule(self, **kwargs):
        """Delete a key rule from a policy."""
        args = ["cte", "policies", "delete-key-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--key-rule-identifier", kwargs["key_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_get_key_rule(self, **kwargs):
        """Get a key rule from a policy."""
        args = ["cte", "policies", "get-key-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--key-rule-identifier", kwargs["key_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_list_key_rules(self, **kwargs):
        """List key rules in a policy."""
        args = ["cte", "policies", "list-key-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_modify_key_rule(self, **kwargs):
        """Modify a key rule in a policy."""
        args = ["cte", "policies", "modify-key-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--key-rule-identifier", kwargs["key_rule_identifier"]])
        
        if kwargs.get("key_identifier"):
            args.extend(["--key-identifier", kwargs["key_identifier"]])
        if kwargs.get("key_type"):
            args.extend(["--key-type", kwargs["key_type"]])
        if kwargs.get("order_number") is not None:
            args.extend(["--order-number", str(kwargs["order_number"])])
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_add_ldt_rule(self, **kwargs):
        """Add an LDT rule to a policy."""
        args = ["cte", "policies", "add-ldt-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--current-key-json-file", kwargs["current_key_json_file"]])
        args.extend(["--transform-key-json-file", kwargs["transform_key_json_file"]])
        
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        if kwargs.get("is_exclusion_rule"):
            args.append("--is-exclusion-rule")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_delete_ldt_rule(self, **kwargs):
        """Delete an LDT rule from a policy."""
        args = ["cte", "policies", "delete-ldt-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--ldt-rule-identifier", kwargs["ldt_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_get_ldt_rule(self, **kwargs):
        """Get an LDT rule from a policy."""
        args = ["cte", "policies", "get-ldt-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--ldt-rule-identifier", kwargs["ldt_rule_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_list_ldt_rules(self, **kwargs):
        """List LDT rules in a policy."""
        args = ["cte", "policies", "list-ldt-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _policy_modify_ldt_rule(self, **kwargs):
        """Modify an LDT rule in a policy."""
        args = ["cte", "policies", "modify-ldt-rules"]
        args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        args.extend(["--ldt-rule-identifier", kwargs["ldt_rule_identifier"]])
        
        if kwargs.get("current_key_json_file"):
            args.extend(["--current-key-json-file", kwargs["current_key_json_file"]])
        if kwargs.get("transform_key_json_file"):
            args.extend(["--transform-key-json-file", kwargs["transform_key_json_file"]])
        if kwargs.get("order_number") is not None:
            args.extend(["--order-number", str(kwargs["order_number"])])
        if kwargs.get("resource_set_identifier"):
            args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        if kwargs.get("is_exclusion_rule") is not None:
            args.append("--is-exclusion-rule" if kwargs["is_exclusion_rule"] else "--no-is-exclusion-rule")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # USER SET OPERATIONS
    # ==================================================================================

    async def _execute_user_set_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute user set operations."""
        
        if action == "user_set_create":
            return self._user_set_create(**kwargs)
        elif action == "user_set_list":
            return self._user_set_list(**kwargs)
        elif action == "user_set_get":
            return self._user_set_get(**kwargs)
        elif action == "user_set_delete":
            return self._user_set_delete(**kwargs)
        elif action == "user_set_modify":
            return self._user_set_modify(**kwargs)
        elif action == "user_set_add_users":
            return self._user_set_add_users(**kwargs)
        elif action == "user_set_delete_user":
            return self._user_set_delete_user(**kwargs)
        elif action == "user_set_update_user":
            return self._user_set_update_user(**kwargs)
        elif action == "user_set_list_users":
            return self._user_set_list_users(**kwargs)
        elif action == "user_set_list_policies":
            return self._user_set_list_policies(**kwargs)
        else:
            return {"error": f"Unknown user set action: {action}"}

    def _user_set_create(self, **kwargs):
        """Create a CTE user set."""
        args = ["cte", "user-sets", "create"]
        
        if kwargs.get("user_json"):
            args.extend(["--user-json", kwargs["user_json"]])
        elif kwargs.get("user_json_file"):
            args.extend(["--user-json-file", kwargs["user_json_file"]])
        else:
            return {"error": "Either user_json or user_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_list(self, **kwargs):
        """List CTE user sets."""
        args = ["cte", "user-sets", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("user_set_name"):
            args.extend(["--user-set-name", kwargs["user_set_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_get(self, **kwargs):
        """Get a CTE user set."""
        args = ["cte", "user-sets", "get"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_delete(self, **kwargs):
        """Delete a CTE user set."""
        args = ["cte", "user-sets", "delete"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_modify(self, **kwargs):
        """Modify a CTE user set."""
        args = ["cte", "user-sets", "modify"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        
        if kwargs.get("user_json"):
            args.extend(["--user-json", kwargs["user_json"]])
        elif kwargs.get("user_json_file"):
            args.extend(["--user-json-file", kwargs["user_json_file"]])
        else:
            return {"error": "Either user_json or user_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_add_users(self, **kwargs):
        """Add users to a CTE user set."""
        args = ["cte", "user-sets", "add-users"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        args.extend(["--user-json-file", kwargs["user_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_delete_user(self, **kwargs):
        """Delete a user from a CTE user set."""
        args = ["cte", "user-sets", "delete-user"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        args.extend(["--user-index-list", kwargs["user_index_list"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_update_user(self, **kwargs):
        """Update a user in a CTE user set."""
        args = ["cte", "user-sets", "update-user"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        args.extend(["--user-index", kwargs["user_index"]])
        args.extend(["--user-json-file", kwargs["user_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_list_users(self, **kwargs):
        """List users in a CTE user set."""
        args = ["cte", "user-sets", "list-users"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("search"):
            args.extend(["--search", kwargs["search"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _user_set_list_policies(self, **kwargs):
        """List policies associated with a CTE user set."""
        args = ["cte", "user-sets", "list-policies"]
        args.extend(["--user-set-identifier", kwargs["user_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # PROCESS SET OPERATIONS
    # ==================================================================================

    async def _execute_process_set_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute process set operations."""
        
        if action == "process_set_create":
            return self._process_set_create(**kwargs)
        elif action == "process_set_list":
            return self._process_set_list(**kwargs)
        elif action == "process_set_get":
            return self._process_set_get(**kwargs)
        elif action == "process_set_delete":
            return self._process_set_delete(**kwargs)
        elif action == "process_set_modify":
            return self._process_set_modify(**kwargs)
        elif action == "process_set_add_processes":
            return self._process_set_add_processes(**kwargs)
        elif action == "process_set_delete_process":
            return self._process_set_delete_process(**kwargs)
        elif action == "process_set_update_process":
            return self._process_set_update_process(**kwargs)
        elif action == "process_set_list_processes":
            return self._process_set_list_processes(**kwargs)
        elif action == "process_set_list_policies":
            return self._process_set_list_policies(**kwargs)
        else:
            return {"error": f"Unknown process set action: {action}"}

    def _process_set_create(self, **kwargs):
        """Create a CTE process set."""
        args = ["cte", "process-sets", "create"]
        
        if kwargs.get("process_json"):
            args.extend(["--process-json", kwargs["process_json"]])
        elif kwargs.get("process_json_file"):
            args.extend(["--process-json-file", kwargs["process_json_file"]])
        else:
            return {"error": "Either process_json or process_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_list(self, **kwargs):
        """List CTE process sets."""
        args = ["cte", "process-sets", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("process_set_name"):
            args.extend(["--process-set-name", kwargs["process_set_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_get(self, **kwargs):
        """Get a CTE process set."""
        args = ["cte", "process-sets", "get"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_delete(self, **kwargs):
        """Delete a CTE process set."""
        args = ["cte", "process-sets", "delete"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_modify(self, **kwargs):
        """Modify a CTE process set."""
        args = ["cte", "process-sets", "modify"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        
        if kwargs.get("process_json"):
            args.extend(["--process-json", kwargs["process_json"]])
        elif kwargs.get("process_json_file"):
            args.extend(["--process-json-file", kwargs["process_json_file"]])
        else:
            return {"error": "Either process_json or process_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_add_processes(self, **kwargs):
        """Add processes to a CTE process set."""
        args = ["cte", "process-sets", "add-processes"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        args.extend(["--process-json-file", kwargs["process_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_delete_process(self, **kwargs):
        """Delete a process from a CTE process set."""
        args = ["cte", "process-sets", "delete-process"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        args.extend(["--process-index-list", kwargs["process_index_list"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_update_process(self, **kwargs):
        """Update a process in a CTE process set."""
        args = ["cte", "process-sets", "update-process"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        args.extend(["--process-index", kwargs["process_index"]])
        args.extend(["--process-json-file", kwargs["process_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_list_processes(self, **kwargs):
        """List processes in a CTE process set."""
        args = ["cte", "process-sets", "list-processes"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("search"):
            args.extend(["--search", kwargs["search"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _process_set_list_policies(self, **kwargs):
        """List policies associated with a CTE process set."""
        args = ["cte", "process-sets", "list-policies"]
        args.extend(["--process-set-identifier", kwargs["process_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # RESOURCE SET OPERATIONS
    # ==================================================================================

    async def _execute_resource_set_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute resource set operations."""
        
        if action == "resource_set_create":
            return self._resource_set_create(**kwargs)
        elif action == "resource_set_list":
            return self._resource_set_list(**kwargs)
        elif action == "resource_set_get":
            return self._resource_set_get(**kwargs)
        elif action == "resource_set_delete":
            return self._resource_set_delete(**kwargs)
        elif action == "resource_set_modify":
            return self._resource_set_modify(**kwargs)
        elif action == "resource_set_add_resources":
            return self._resource_set_add_resources(**kwargs)
        elif action == "resource_set_delete_resource":
            return self._resource_set_delete_resource(**kwargs)
        elif action == "resource_set_update_resource":
            return self._resource_set_update_resource(**kwargs)
        elif action == "resource_set_list_resources":
            return self._resource_set_list_resources(**kwargs)
        elif action == "resource_set_list_policies":
            return self._resource_set_list_policies(**kwargs)
        else:
            return {"error": f"Unknown resource set action: {action}"}

    def _resource_set_create(self, **kwargs):
        """Create a CTE resource set."""
        args = ["cte", "resource-sets", "create"]
        
        if kwargs.get("resource_json"):
            args.extend(["--resource-json", kwargs["resource_json"]])
        elif kwargs.get("resource_json_file"):
            args.extend(["--resource-json-file", kwargs["resource_json_file"]])
        else:
            return {"error": "Either resource_json or resource_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_list(self, **kwargs):
        """List CTE resource sets."""
        args = ["cte", "resource-sets", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("resource_set_name"):
            args.extend(["--resource-set-name", kwargs["resource_set_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_get(self, **kwargs):
        """Get a CTE resource set."""
        args = ["cte", "resource-sets", "get"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_delete(self, **kwargs):
        """Delete a CTE resource set."""
        args = ["cte", "resource-sets", "delete"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_modify(self, **kwargs):
        """Modify a CTE resource set."""
        args = ["cte", "resource-sets", "modify"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        
        if kwargs.get("resource_json"):
            args.extend(["--resource-json", kwargs["resource_json"]])
        elif kwargs.get("resource_json_file"):
            args.extend(["--resource-json-file", kwargs["resource_json_file"]])
        else:
            return {"error": "Either resource_json or resource_json_file must be specified"}
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_add_resources(self, **kwargs):
        """Add resources to a CTE resource set."""
        args = ["cte", "resource-sets", "add-resources"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        args.extend(["--resource-json-file", kwargs["resource_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_delete_resource(self, **kwargs):
        """Delete a resource from a CTE resource set."""
        args = ["cte", "resource-sets", "delete-resource"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        args.extend(["--resource-index-list", kwargs["resource_index_list"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_update_resource(self, **kwargs):
        """Update a resource in a CTE resource set."""
        args = ["cte", "resource-sets", "update-resource"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        args.extend(["--resource-index", kwargs["resource_index"]])
        args.extend(["--resource-json-file", kwargs["resource_json_file"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_list_resources(self, **kwargs):
        """List resources in a CTE resource set."""
        args = ["cte", "resource-sets", "list-resources"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("search"):
            args.extend(["--search", kwargs["search"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _resource_set_list_policies(self, **kwargs):
        """List policies associated with a CTE resource set."""
        args = ["cte", "resource-sets", "list-policies"]
        args.extend(["--resource-set-identifier", kwargs["resource_set_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # CLIENT OPERATIONS
    # ==================================================================================

    async def _execute_client_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute client operations."""
        
        if action == "client_create":
            return self._client_create(**kwargs)
        elif action == "client_list":
            return self._client_list(**kwargs)
        elif action == "client_get":
            return self._client_get(**kwargs)
        elif action == "client_delete":
            return self._client_delete(**kwargs)
        elif action == "client_modify":
            return self._client_modify(**kwargs)
        elif action == "client_create_guardpoint":
            return self._client_create_guardpoint(**kwargs)
        elif action == "client_list_guardpoints":
            return self._client_list_guardpoints(**kwargs)
        elif action == "client_get_guardpoint":
            return self._client_get_guardpoint(**kwargs)
        elif action == "client_modify_guardpoint":
            return self._client_modify_guardpoint(**kwargs)
        elif action == "client_unguard_guardpoint":
            return self._client_unguard_guardpoint(**kwargs)
        else:
            return {"error": f"Unknown client action: {action}"}

    def _client_create(self, **kwargs):
        """Create a CTE client."""
        args = ["cte", "clients", "create"]
        args.extend(["--cte-client-name", kwargs["cte_client_name"]])
        
        if kwargs.get("client_password"):
            args.extend(["--client-password", kwargs["client_password"]])
        if kwargs.get("password_creation_method", "GENERATE") != "GENERATE":
            args.extend(["--password-creation-method", kwargs["password_creation_method"]])
        if kwargs.get("comm_enabled"):
            args.append("--comm-enabled")
        if kwargs.get("reg_allowed"):
            args.append("--reg-allowed")
        if kwargs.get("cte_client_type"):
            args.extend(["--cte-client-type", kwargs["cte_client_type"]])
        if kwargs.get("cte_profile_identifier"):
            args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        if kwargs.get("description"):
            args.extend(["--description", kwargs["description"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_list(self, **kwargs):
        """List CTE clients."""
        args = ["cte", "clients", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("cte_client_name"):
            args.extend(["--cte-client-name", kwargs["cte_client_name"]])
        if kwargs.get("cte_client_type"):
            args.extend(["--cte-client-type", kwargs["cte_client_type"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_get(self, **kwargs):
        """Get a CTE client."""
        args = ["cte", "clients", "get"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_delete(self, **kwargs):
        """Delete a CTE client."""
        args = ["cte", "clients", "delete"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.append("--del-client")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_modify(self, **kwargs):
        """Modify a CTE client."""
        args = ["cte", "clients", "modify"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        
        if kwargs.get("client_password"):
            args.extend(["--client-password", kwargs["client_password"]])
        if kwargs.get("password_creation_method"):
            args.extend(["--password-creation-method", kwargs["password_creation_method"]])
        if kwargs.get("comm_enabled") is not None:
            args.append("--comm-enabled" if kwargs["comm_enabled"] else "--no-comm-enabled")
        if kwargs.get("reg_allowed") is not None:
            args.append("--reg-allowed" if kwargs["reg_allowed"] else "--no-reg-allowed")
        if kwargs.get("cte_client_locked") is not None:
            args.append("--cte-client-locked" if kwargs["cte_client_locked"] else "--no-cte-client-locked")
        if kwargs.get("system_locked") is not None:
            args.append("--system-locked" if kwargs["system_locked"] else "--no-system-locked")
        if kwargs.get("cte_profile_identifier"):
            args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        if kwargs.get("host_name"):
            args.extend(["--host-name", kwargs["host_name"]])
        if kwargs.get("client_mfa_enabled") is not None:
            args.append("--client-mfa-enabled" if kwargs["client_mfa_enabled"] else "--no-client-mfa-enabled")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_create_guardpoint(self, **kwargs):
        """Create a guardpoint on a CTE client."""
        args = ["cte", "clients", "create-guardpoints"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.extend(["--guard-path-list", kwargs["guard_path_list"]])
        args.extend(["--guard-point-type", kwargs["guard_point_type"]])
        
        if kwargs.get("cte_policy_identifier"):
            args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        if not kwargs.get("guard_enabled", True):
            args.append("--no-guard-enabled")
        if kwargs.get("auto_mount_enabled"):
            args.append("--auto-mount-enabled")
        if kwargs.get("cifs_enabled"):
            args.append("--cifs-enabled")
        if kwargs.get("early_access"):
            args.append("--early-access")
        if not kwargs.get("preserve_sparse_regions", True):
            args.append("--no-preserve-sparse-regions")
        if kwargs.get("mfa_enabled"):
            args.append("--mfa-enabled")
        if kwargs.get("intelligent_protection"):
            args.append("--intelligent-protection")
        if kwargs.get("is_idt_capable_device"):
            args.append("--is-idt-capable-device")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_list_guardpoints(self, **kwargs):
        """List guardpoints on a CTE client."""
        args = ["cte", "clients", "list-guardpoints"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("cte_policy_identifier"):
            args.extend(["--cte-policy-identifier", kwargs["cte_policy_identifier"]])
        if kwargs.get("sort"):
            args.extend(["--sort", kwargs["sort"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_get_guardpoint(self, **kwargs):
        """Get a guardpoint on a CTE client."""
        args = ["cte", "clients", "get-guardpoints"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.extend(["--guard-point-identifier", kwargs["guard_point_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_modify_guardpoint(self, **kwargs):
        """Modify a guardpoint on a CTE client."""
        args = ["cte", "clients", "modify-guardpoints"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.extend(["--guard-point-identifier", kwargs["guard_point_identifier"]])
        
        if kwargs.get("guard_enabled") is not None:
            args.append("--guard-enabled" if kwargs["guard_enabled"] else "--no-guard-enabled")
        if kwargs.get("mfa_enabled") is not None:
            args.append("--mfa-enabled" if kwargs["mfa_enabled"] else "--no-mfa-enabled")
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_unguard_guardpoint(self, **kwargs):
        """Unguard a guardpoint from a CTE client."""
        args = ["cte", "clients", "unguard-guardpoints"]
        args.extend(["--cte-client-identifier", kwargs["cte_client_identifier"]])
        args.extend(["--guard-point-identifier", kwargs["guard_point_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # CLIENT GROUP OPERATIONS
    # ==================================================================================

    async def _execute_client_group_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute client group operations."""
        
        if action == "client_group_create":
            return self._client_group_create(**kwargs)
        elif action == "client_group_list":
            return self._client_group_list(**kwargs)
        elif action == "client_group_get":
            return self._client_group_get(**kwargs)
        elif action == "client_group_delete":
            return self._client_group_delete(**kwargs)
        elif action == "client_group_modify":
            return self._client_group_modify(**kwargs)
        else:
            return {"error": f"Unknown client group action: {action}"}

    def _client_group_create(self, **kwargs):
        """Create a CTE client group."""
        args = ["cte", "client-groups", "create"]
        args.extend(["--client-group-name", kwargs["client_group_name"]])
        args.extend(["--cluster-type", kwargs.get("cluster_type", "NON-CLUSTER")])

        if kwargs.get("client_group_description"):
            args.extend(["--client-group-description", kwargs["client_group_description"]])
        if kwargs.get("client_group_password"):
            args.extend(["--client-group-password", kwargs["client_group_password"]])
        if kwargs.get("password_creation_method", "GENERATE") != "GENERATE":
            args.extend(["--password-creation-method", kwargs["password_creation_method"]])
        if kwargs.get("comm_enabled"):
            args.append("--comm-enabled")
        if kwargs.get("cte_profile_identifier"):
            args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_group_list(self, **kwargs):
        """List CTE client groups."""
        args = ["cte", "client-groups", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("client_group_name"):
            args.extend(["--client-group-name", kwargs["client_group_name"]])
        if kwargs.get("cluster_type"):
            args.extend(["--cluster-type", kwargs["cluster_type"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_group_get(self, **kwargs):
        """Get a CTE client group."""
        args = ["cte", "client-groups", "get"]
        args.extend(["--client-group-identifier", kwargs["client_group_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_group_delete(self, **kwargs):
        """Delete a CTE client group."""
        args = ["cte", "client-groups", "delete"]
        args.extend(["--client-group-identifier", kwargs["client_group_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _client_group_modify(self, **kwargs):
        """Modify a CTE client group."""
        args = ["cte", "client-groups", "modify"]
        args.extend(["--client-group-identifier", kwargs["client_group_identifier"]])
        
        if kwargs.get("client_group_description") is not None:
            args.extend(["--client-group-description", kwargs["client_group_description"]])
        if kwargs.get("client_group_password"):
            args.extend(["--client-group-password", kwargs["client_group_password"]])
        if kwargs.get("password_creation_method"):
            args.extend(["--password-creation-method", kwargs["password_creation_method"]])
        if kwargs.get("comm_enabled") is not None:
            args.append("--comm-enabled" if kwargs["comm_enabled"] else "--no-comm-enabled")
        if kwargs.get("cte_client_locked") is not None:
            args.append("--cte-client-locked" if kwargs["cte_client_locked"] else "--no-cte-client-locked")
        if kwargs.get("system_locked") is not None:
            args.append("--system-locked" if kwargs["system_locked"] else "--no-system-locked")
        if kwargs.get("cte_profile_identifier"):
            args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # PROFILE OPERATIONS
    # ==================================================================================

    async def _execute_profile_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute profile operations."""
        
        if action == "profile_create":
            return self._profile_create(**kwargs)
        elif action == "profile_list":
            return self._profile_list(**kwargs)
        elif action == "profile_get":
            return self._profile_get(**kwargs)
        elif action == "profile_delete":
            return self._profile_delete(**kwargs)
        elif action == "profile_modify":
            return self._profile_modify(**kwargs)
        else:
            return {"error": f"Unknown profile action: {action}"}

    def _profile_create(self, **kwargs):
        """Create a CTE profile."""
        args = ["cte", "profiles", "create"]
        args.extend(["--cte-profile-name", kwargs["cte_profile_name"]])
        
        if kwargs.get("cte_profile_description"):
            args.extend(["--cte-profile-description", kwargs["cte_profile_description"]])
        if kwargs.get("concise_logging") is not None:
            if kwargs["concise_logging"]:
                args.append("--concise-logging")
        if kwargs.get("connect_timeout") is not None:
            args.extend(["--connect-timeout", str(kwargs["connect_timeout"])])
        if kwargs.get("metadata_scan_interval") is not None:
            args.extend(["--metadata-scan-interval", str(kwargs["metadata_scan_interval"])])
        if kwargs.get("partial_config_enable") is not None:
            if kwargs["partial_config_enable"]:
                args.append("--partial-config-enable")
        if kwargs.get("server_response_rate") is not None:
            args.extend(["--server-response-rate", str(kwargs["server_response_rate"])])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _profile_list(self, **kwargs):
        """List CTE profiles."""
        args = ["cte", "profiles", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("cte_profile_name"):
            args.extend(["--cte-profile-name", kwargs["cte_profile_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _profile_get(self, **kwargs):
        """Get a CTE profile."""
        args = ["cte", "profiles", "get"]
        args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        
        if kwargs.get("cte_profile_name"):
            args.extend(["--cte-profile-name", kwargs["cte_profile_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _profile_delete(self, **kwargs):
        """Delete a CTE profile."""
        args = ["cte", "profiles", "delete"]
        args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        
        if kwargs.get("cte_profile_name"):
            args.extend(["--cte-profile-name", kwargs["cte_profile_name"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _profile_modify(self, **kwargs):
        """Modify a CTE profile."""
        args = ["cte", "profiles", "modify"]
        args.extend(["--cte-profile-identifier", kwargs["cte_profile_identifier"]])
        
        if kwargs.get("cte_profile_description"):
            args.extend(["--cte-profile-description", kwargs["cte_profile_description"]])
        if kwargs.get("concise_logging") is not None:
            if kwargs["concise_logging"]:
                args.append("--concise-logging")
        if kwargs.get("connect_timeout") is not None:
            args.extend(["--connect-timeout", str(kwargs["connect_timeout"])])
        if kwargs.get("metadata_scan_interval") is not None:
            args.extend(["--metadata-scan-interval", str(kwargs["metadata_scan_interval"])])
        if kwargs.get("partial_config_enable") is not None:
            if kwargs["partial_config_enable"]:
                args.append("--partial-config-enable")
        if kwargs.get("server_response_rate") is not None:
            args.extend(["--server-response-rate", str(kwargs["server_response_rate"])])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    # ==================================================================================
    # CSI STORAGE GROUP OPERATIONS
    # ==================================================================================

    async def _execute_csi_operation(self, action: str, **kwargs: Any) -> Any:
        """Execute CSI storage group operations."""
        
        if action == "csi_storage_group_create":
            return self._csi_storage_group_create(**kwargs)
        elif action == "csi_storage_group_list":
            return self._csi_storage_group_list(**kwargs)
        elif action == "csi_storage_group_get":
            return self._csi_storage_group_get(**kwargs)
        elif action == "csi_storage_group_delete":
            return self._csi_storage_group_delete(**kwargs)
        elif action == "csi_storage_group_modify":
            return self._csi_storage_group_modify(**kwargs)
        else:
            return {"error": f"Unknown CSI storage group action: {action}"}

    def _csi_storage_group_create(self, **kwargs):
        """Create a CSI StorageGroup."""
        args = ["cte", "csi", "k8s-storage-group", "create"]
        args.extend(["--storage-group-name", kwargs["storage_group_name"]])
        args.extend(["--storage-class-name", kwargs["storage_class_name"]])
        args.extend(["--namespace-name", kwargs["namespace_name"]])
        
        if kwargs.get("ctecsi_description"):
            args.extend(["--ctecsi-description", kwargs["ctecsi_description"]])
        if kwargs.get("ctecsi_profile"):
            args.extend(["--ctecsi-profile", kwargs["ctecsi_profile"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _csi_storage_group_list(self, **kwargs):
        """List CSI StorageGroups."""
        args = ["cte", "csi", "k8s-storage-group", "list"]
        args.extend(["--limit", str(kwargs.get("limit", 10))])
        args.extend(["--skip", str(kwargs.get("skip", 0))])
        
        if kwargs.get("storage_group_name"):
            args.extend(["--storage-group-name", kwargs["storage_group_name"]])
        if kwargs.get("storage_class_name"):
            args.extend(["--storage-class-name", kwargs["storage_class_name"]])
        if kwargs.get("namespace_name"):
            args.extend(["--namespace-name", kwargs["namespace_name"]])
        if kwargs.get("sort"):
            args.extend(["--sort", kwargs["sort"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _csi_storage_group_get(self, **kwargs):
        """Get a CSI StorageGroup."""
        args = ["cte", "csi", "k8s-storage-group", "get"]
        args.extend(["--storage-group-identifier", kwargs["storage_group_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _csi_storage_group_delete(self, **kwargs):
        """Delete a CSI StorageGroup."""
        args = ["cte", "csi", "k8s-storage-group", "delete"]
        args.extend(["--storage-group-identifier", kwargs["storage_group_identifier"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))

    def _csi_storage_group_modify(self, **kwargs):
        """Modify a CSI StorageGroup."""
        args = ["cte", "csi", "k8s-storage-group", "modify"]
        args.extend(["--storage-group-identifier", kwargs["storage_group_identifier"]])
        
        if kwargs.get("ctecsi_description") is not None:
            args.extend(["--ctecsi-description", kwargs["ctecsi_description"]])
        if kwargs.get("ctecsi_profile"):
            args.extend(["--ctecsi-profile", kwargs["ctecsi_profile"]])
        
        result = self.execute_with_domain(args, kwargs.get("domain"), kwargs.get("auth_domain"))
        return result.get("data", result.get("stdout", ""))


# Export the optimized tool
CTE_TOOLS = [CTEManagementTool]