"""OCI Keys operations for CCKM."""

from typing import Any, Dict


def get_key_operations() -> Dict[str, Any]:
    """Return schema and action requirements for OCI key operations."""
    return {
        "schema_properties": {
            "oci_keys_params": {
                "type": "object",
                "properties": {
                    # Basic key parameters
                    "key_name": {"type": "string", "description": "Name for the key"},
                    "oci_vault": {"type": "string", "description": "ID of the vault to create the key in"},
                    "oci_algorithm": {"type": "string", "description": "Algorithm of the key (AES, RSA, ECDSA)"},
                    "length": {"type": "integer", "description": "Length of the key"},
                    "protection_mode": {"type": "string", "description": "Protection mode (SOFTWARE, HSM)"},
                    "oci_compartment_id": {"type": "string", "description": "Compartment ID where the key will belong"},
                    
                    # Key attributes
                    "description": {"type": "string", "description": "Key description"},
                    "oci_curve": {"type": "string", "description": "Elliptic curve (NIST_P256, NIST_P384, NIST_P521)"},
                    
                    # Common parameters
                    "id": {"type": "string", "description": "Key ID"},
                    "oci_version_id": {"type": "string", "description": "Version ID for version operations"},
                    
                    # List parameters
                    "limit": {"type": "integer", "description": "Maximum number of results"},
                    "skip": {"type": "integer", "description": "Number of results to skip"},
                    "sort": {"type": "string", "description": "Sort field and order"},
                    
                    # JSON file parameters
                    "oci_keycreate_jsonfile": {"type": "string", "description": "OCI key create parameters in JSON file"},
                    "oci_defined_tags_jsonfile": {"type": "string", "description": "OCI defined tags in JSON file"},
                    "oci_freeform_tags_jsonfile": {"type": "string", "description": "OCI freeform tags in JSON file"},
                    "oci_keyaddversion_jsonfile": {"type": "string", "description": "OCI key add version parameters in JSON file"},
                    
                    # Schedule deletion
                    "days": {"type": "integer", "description": "Number of days for schedule deletion"},
                    
                    # Sync operations
                    "job_id": {"type": "string", "description": "Job ID for sync operations"},
                    "synchronize_all": {"type": "boolean", "description": "Synchronize all keys from all vaults"},
                    
                    # Metadata export
                    "file": {"type": "string", "description": "File path for metadata download"},
                    
                    # Auto rotation
                    "time_of_rotation": {"type": "string", "description": "Time of rotation in ISO 8601 format"},
                    "rotation_interval_days": {"type": "integer", "description": "Rotation interval in days"}
                }
            }
        },
        "action_requirements": {
            "keys_list": {"required": [], "optional": ["limit", "skip", "sort", "oci_compartment_id", "key_name", "oci_algorithm", "length", "protection_mode", "oci_curve", "oci_vault"]},
            "keys_get": {"required": ["id"], "optional": []},
            "keys_create": {"required": ["key_name", "oci_vault", "oci_algorithm", "length", "protection_mode", "oci_compartment_id"], "optional": ["description", "oci_curve", "oci_keycreate_jsonfile", "oci_defined_tags_jsonfile", "oci_freeform_tags_jsonfile"]},
            "keys_delete": {"required": ["id"], "optional": []},
            "keys_enable": {"required": ["id"], "optional": []},
            "keys_disable": {"required": ["id"], "optional": []},
            "keys_refresh": {"required": ["id"], "optional": []},
            "keys_restore": {"required": ["id"], "optional": []},
            "keys_schedule_deletion": {"required": ["id", "days"], "optional": []},
            "keys_cancel_deletion": {"required": ["id"], "optional": []},
            "keys_change_compartment": {"required": ["id", "oci_compartment_id"], "optional": []},
            "keys_enable_auto_rotation": {"required": ["id"], "optional": ["time_of_rotation", "rotation_interval_days"]},
            "keys_disable_auto_rotation": {"required": ["id"], "optional": []},
            "keys_delete_backup": {"required": ["id"], "optional": []},
            "keys_download_metadata": {"required": [], "optional": ["limit", "skip", "sort", "file", "oci_compartment_id", "oci_vault"]},
            "keys_add_version": {"required": ["id"], "optional": ["oci_keyaddversion_jsonfile"]},
            "keys_get_version": {"required": ["id", "oci_version_id"], "optional": []},
            "keys_list_version": {"required": ["id"], "optional": ["limit", "skip"]},
            "keys_schedule_deletion_version": {"required": ["id", "oci_version_id", "days"], "optional": []},
            "keys_cancel_schedule_deletion_version": {"required": ["id", "oci_version_id"], "optional": []},
            "keys_sync_jobs_start": {"required": [], "optional": ["oci_vault", "synchronize_all"]},
            "keys_sync_jobs_get": {"required": ["job_id"], "optional": []},
            "keys_sync_jobs_status": {"required": [], "optional": ["limit", "skip", "sort"]},
            "keys_sync_jobs_cancel": {"required": ["job_id"], "optional": []},
        }
    }


def build_key_command(action: str, oci_params: Dict[str, Any]) -> list:
    """Build the ksctl command for a given OCI key operation."""
    cmd = ["cckm", "oci", "keys"]
    
    # Extract the base operation name (remove 'keys_' prefix)
    base_action = action.replace("keys_", "")
    
    # Simple actions that only need --id parameter
    simple_actions = ["get", "delete", "enable", "disable", "refresh", "restore", "cancel_deletion", "disable_auto_rotation", "delete_backup"]
    
    if base_action in simple_actions:
        cmd.extend([base_action.replace("_", "-"), "--id", oci_params["id"]])
        return cmd
    
    if base_action == "list":
        cmd.append("list")
        if "limit" in oci_params:
            cmd.extend(["--limit", str(oci_params["limit"])])
        if "skip" in oci_params:
            cmd.extend(["--skip", str(oci_params["skip"])])
        if "sort" in oci_params:
            cmd.extend(["--sort", oci_params["sort"]])
        if "oci_compartment_id" in oci_params:
            cmd.extend(["--oci-compartment-id", oci_params["oci_compartment_id"]])
        if "key_name" in oci_params:
            cmd.extend(["--key-name", oci_params["key_name"]])
        if "oci_algorithm" in oci_params:
            cmd.extend(["--oci-algorithm", oci_params["oci_algorithm"]])
        if "length" in oci_params:
            cmd.extend(["--length", str(oci_params["length"])])
        if "protection_mode" in oci_params:
            cmd.extend(["--protection-mode", oci_params["protection_mode"]])
        if "oci_curve" in oci_params:
            cmd.extend(["--oci-curve", oci_params["oci_curve"]])
        if "oci_vault" in oci_params:
            cmd.extend(["--oci-vault", oci_params["oci_vault"]])
            
    elif base_action == "create":
        cmd.append("create")
        # Required parameters
        cmd.extend(["--key-name", oci_params["key_name"]])
        cmd.extend(["--oci-vault", oci_params["oci_vault"]])
        cmd.extend(["--oci-algorithm", oci_params["oci_algorithm"]])
        cmd.extend(["--length", str(oci_params["length"])])
        cmd.extend(["--protection-mode", oci_params["protection_mode"]])
        cmd.extend(["--oci-compartment-id", oci_params["oci_compartment_id"]])
        
        # Optional parameters
        if "description" in oci_params:
            cmd.extend(["--description", oci_params["description"]])
        if "oci_curve" in oci_params:
            cmd.extend(["--oci-curve", oci_params["oci_curve"]])
        if "oci_keycreate_jsonfile" in oci_params:
            cmd.extend(["--oci-keycreate-jsonfile", oci_params["oci_keycreate_jsonfile"]])
        if "oci_defined_tags_jsonfile" in oci_params:
            cmd.extend(["--oci-defined-tags-jsonfile", oci_params["oci_defined_tags_jsonfile"]])
        if "oci_freeform_tags_jsonfile" in oci_params:
            cmd.extend(["--oci-freeform-tags-jsonfile", oci_params["oci_freeform_tags_jsonfile"]])
            
    elif base_action == "schedule_deletion":
        cmd.extend(["schedule-deletion", "--id", oci_params["id"], "--days", str(oci_params["days"])])
        
    elif base_action == "change_compartment":
        cmd.extend(["change-compartment", "--id", oci_params["id"], "--oci-compartment-id", oci_params["oci_compartment_id"]])
        
    elif base_action == "enable_auto_rotation":
        cmd.extend(["enable-auto-rotation", "--id", oci_params["id"]])
        if "time_of_rotation" in oci_params:
            cmd.extend(["--time-of-rotation", oci_params["time_of_rotation"]])
        if "rotation_interval_days" in oci_params:
            cmd.extend(["--rotation-interval-days", str(oci_params["rotation_interval_days"])])
            
    elif base_action == "download_metadata":
        cmd.extend(["download-metadata"])
        if "limit" in oci_params:
            cmd.extend(["--limit", str(oci_params["limit"])])
        if "skip" in oci_params:
            cmd.extend(["--skip", str(oci_params["skip"])])
        if "sort" in oci_params:
            cmd.extend(["--sort", oci_params["sort"]])
        if "file" in oci_params:
            cmd.extend(["--file", oci_params["file"]])
        if "oci_compartment_id" in oci_params:
            cmd.extend(["--oci-compartment-id", oci_params["oci_compartment_id"]])
        if "oci_vault" in oci_params:
            cmd.extend(["--oci-vault", oci_params["oci_vault"]])
            
    elif base_action == "add_version":
        cmd.extend(["add-version", "--id", oci_params["id"]])
        if "oci_keyaddversion_jsonfile" in oci_params:
            cmd.extend(["--oci-keyaddversion-jsonfile", oci_params["oci_keyaddversion_jsonfile"]])
            
    elif base_action == "get_version":
        cmd.extend(["get-version", "--id", oci_params["id"], "--oci-version-id", oci_params["oci_version_id"]])
        
    elif base_action == "list_version":
        cmd.extend(["list-version", "--id", oci_params["id"]])
        if "limit" in oci_params:
            cmd.extend(["--limit", str(oci_params["limit"])])
        if "skip" in oci_params:
            cmd.extend(["--skip", str(oci_params["skip"])])
            
    elif base_action == "schedule_deletion_version":
        cmd.extend(["schedule-deletion-version", "--id", oci_params["id"], "--oci-version-id", oci_params["oci_version_id"], "--days", str(oci_params["days"])])
        
    elif base_action == "cancel_schedule_deletion_version":
        cmd.extend(["cancel-schedule-deletion-version", "--id", oci_params["id"], "--oci-version-id", oci_params["oci_version_id"]])
        
    elif base_action == "sync_jobs_start":
        cmd.extend(["synchronization-jobs", "start"])
        if "oci_vault" in oci_params:
            cmd.extend(["--oci-vault", oci_params["oci_vault"]])
        if "synchronize_all" in oci_params and oci_params["synchronize_all"]:
            cmd.append("--synchronize-all")
            
    elif base_action == "sync_jobs_get":
        cmd.extend(["synchronization-jobs", "get", "--id", oci_params["job_id"]])
        
    elif base_action == "sync_jobs_status":
        cmd.extend(["synchronization-jobs", "status"])
        if "limit" in oci_params:
            cmd.extend(["--limit", str(oci_params["limit"])])
        if "skip" in oci_params:
            cmd.extend(["--skip", str(oci_params["skip"])])
        if "sort" in oci_params:
            cmd.extend(["--sort", oci_params["sort"]])
            
    elif base_action == "sync_jobs_cancel":
        cmd.extend(["synchronization-jobs", "cancel", "--id", oci_params["job_id"]])
        
    else:
        raise ValueError(f"Unsupported OCI keys action: {action}")
    
    return cmd 