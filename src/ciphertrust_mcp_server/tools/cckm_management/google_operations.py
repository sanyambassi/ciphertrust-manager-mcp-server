"""Google Cloud operations for CCKM."""

from typing import Any, Dict, List
from .base import CCKMOperations
from .constants import (
    GOOGLE_PARAMETERS, GOOGLE_KEYRING_PARAMETERS, GOOGLE_LOCATION_PARAMETERS,
    GOOGLE_PROJECT_PARAMETERS, GOOGLE_REPORTS_PARAMETERS, CLOUD_OPERATIONS
)


class GoogleOperations(CCKMOperations):
    """Google Cloud key operations for CCKM."""
    
    def get_operations(self) -> List[str]:
        """Return list of supported Google Cloud operations."""
        return CLOUD_OPERATIONS["google"]
    
    def get_schema_properties(self) -> Dict[str, Any]:
        """Return schema properties for Google Cloud operations."""
        return {
            "google_params": {
                "type": "object",
                "properties": {
                    **GOOGLE_PARAMETERS,
                    **GOOGLE_KEYRING_PARAMETERS,
                    **GOOGLE_LOCATION_PARAMETERS,
                    **GOOGLE_PROJECT_PARAMETERS,
                    **GOOGLE_REPORTS_PARAMETERS,
                    # Additional parameters
                    "backup_data": {"type": "string", "description": "Backup data for restore operations"},
                    "keyring": {"type": "string", "description": "Key ring name"},
                    "file_path": {"type": "string", "description": "File path for download operations"},
                    "job_id": {"type": "string", "description": "Job ID for operations"}
                },
                "description": "Google Cloud-specific parameters"
            }
        }
    
    def get_action_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Return action-specific parameter requirements for Google Cloud."""
        return {
            "list": {
                "required": [],
                "optional": ["project_id", "location", "key_ring", "limit", "skip", "domain", "auth_domain"]
            },
            "get": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "create": {
                "required": ["alias", "project_id", "location", "key_ring"],
                "optional": ["protection_level", "algorithm", "purpose", "domain", "auth_domain"]
            },
            "update": {
                "required": ["id"],
                "optional": ["alias", "description", "enabled", "tags", "domain", "auth_domain"]
            },
            "delete": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "enable": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "disable": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "rotate": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "destroy": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "restore": {
                "required": ["backup_data"],
                "optional": ["domain", "auth_domain"]
            },
            # Additional key operations
            "add_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "cancel_schedule_destroy": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "disable_auto_rotation": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "disable_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "download_metadata": {
                "required": [],
                "optional": ["project_id", "location", "keyring", "limit", "skip", "file_path", "domain", "auth_domain"]
            },
            "download_public_key": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "enable_auto_rotation": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "enable_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "get_update_all_versions_status": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "get_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "list_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "policy": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "re_import": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "refresh": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "refresh_version": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "schedule_destroy": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "upload_key": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "update_all_versions_jobs": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            # Key synchronization operations
            "keys_sync_jobs_start": {
                "required": ["project_id"],
                "optional": ["domain", "auth_domain"]
            },
            "keys_sync_jobs_get": {
                "required": ["job_id"],
                "optional": ["domain", "auth_domain"]
            },
            "keys_sync_jobs_status": {
                "required": [],
                "optional": ["domain", "auth_domain"]
            },
            "keys_sync_jobs_cancel": {
                "required": ["job_id"],
                "optional": ["domain", "auth_domain"]
            },
            # Key ring operations
            "keyrings_list": {
                "required": [],
                "optional": ["project_id", "location", "limit", "skip", "domain", "auth_domain"]
            },
            "keyrings_get": {
                "required": ["keyring_id"],
                "optional": ["domain", "auth_domain"]
            },
            "keyrings_create": {
                "required": ["keyring_name", "project_id", "location"],
                "optional": ["domain", "auth_domain"]
            },
            "keyrings_delete": {
                "required": ["keyring_id"],
                "optional": ["domain", "auth_domain"]
            },
            "keyrings_update_acls": {
                "required": ["keyring_id", "acls"],
                "optional": ["domain", "auth_domain"]
            },
            # Location operations
            "locations_get_locations": {
                "required": [],
                "optional": ["domain", "auth_domain"]
            },
            # Project operations
            "projects_list": {
                "required": [],
                "optional": ["limit", "skip", "domain", "auth_domain"]
            },
            "projects_get": {
                "required": ["project_id"],
                "optional": ["domain", "auth_domain"]
            },
            "projects_add": {
                "required": ["project_id"],
                "optional": ["project_name", "domain", "auth_domain"]
            },
            "projects_update": {
                "required": ["project_id"],
                "optional": ["project_name", "domain", "auth_domain"]
            },
            "projects_delete": {
                "required": ["project_id"],
                "optional": ["domain", "auth_domain"]
            },
            "projects_get_project": {
                "required": [],
                "optional": ["domain", "auth_domain"]
            },
            "projects_update_acls": {
                "required": ["project_id", "acls"],
                "optional": ["domain", "auth_domain"]
            },
            # Reports operations
            "reports_list": {
                "required": [],
                "optional": ["limit", "skip", "domain", "auth_domain"]
            },
            "reports_get": {
                "required": ["job_id"],
                "optional": ["domain", "auth_domain"]
            },
            "reports_generate": {
                "required": ["report_type"],
                "optional": ["report_format", "filters", "domain", "auth_domain"]
            },
            "reports_download": {
                "required": ["job_id", "file_path"],
                "optional": ["domain", "auth_domain"]
            },
            "reports_delete": {
                "required": ["job_id"],
                "optional": ["domain", "auth_domain"]
            },
            "reports_get_report": {
                "required": [],
                "optional": ["report_type", "filters", "limit", "skip", "domain", "auth_domain"]
            }
        }
    
    async def execute_operation(self, action: str, params: Dict[str, Any]) -> Any:
        """Execute Google Cloud operation."""
        google_params = params.get("google_params", {})
        
        # Build base command
        cmd = ["cckm", "google", "keys"]
        
        # Add action-specific command
        if action == "list":
            cmd.append("list")
            if google_params.get("project_id"):
                cmd.extend(["--project-id", google_params["project_id"]])
            if google_params.get("location"):
                cmd.extend(["--location", google_params["location"]])
            if google_params.get("key_ring"):
                cmd.extend(["--key-ring", google_params["key_ring"]])
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
                
        elif action == "get":
            cmd.extend(["get", "--id", google_params["id"]])
            
        elif action == "create":
            cmd.extend(["create", 
                       "--alias", google_params["alias"],
                       "--project-id", google_params["project_id"],
                       "--location", google_params["location"],
                       "--key-ring", google_params["key_ring"]])
            if google_params.get("protection_level"):
                cmd.extend(["--protection-level", google_params["protection_level"]])
            if google_params.get("algorithm"):
                cmd.extend(["--algorithm", google_params["algorithm"]])
            if google_params.get("purpose"):
                cmd.extend(["--purpose", google_params["purpose"]])
                
        elif action == "update":
            cmd.extend(["update", "--id", google_params["id"]])
            if google_params.get("alias"):
                cmd.extend(["--alias", google_params["alias"]])
            if google_params.get("description"):
                cmd.extend(["--description", google_params["description"]])
            if google_params.get("enabled") is not None:
                cmd.extend(["--enabled", "yes" if google_params["enabled"] else "no"])
            if google_params.get("tags"):
                cmd.extend(["--tags", str(google_params["tags"])])
                
        elif action == "delete":
            cmd.extend(["delete", "--id", google_params["id"]])
            
        elif action == "enable":
            cmd.extend(["enable", "--id", google_params["id"]])
            
        elif action == "disable":
            cmd.extend(["disable", "--id", google_params["id"]])
            
        elif action == "rotate":
            cmd.extend(["rotate", "--id", google_params["id"]])
            
        elif action == "destroy":
            cmd.extend(["destroy", "--id", google_params["id"]])
            
        elif action == "restore":
            cmd.extend(["restore", "--backup-data", google_params["backup_data"]])
            
        # Additional key operations
        elif action == "add_version":
            cmd.extend(["add-version", "--id", google_params["id"]])
            
        elif action == "cancel_schedule_destroy":
            cmd.extend(["cancel-schedule-destroy", "--id", google_params["id"]])
            
        elif action == "disable_auto_rotation":
            cmd.extend(["disable-auto-rotation", "--id", google_params["id"]])
            
        elif action == "disable_version":
            cmd.extend(["disable-version", "--id", google_params["id"]])
            
        elif action == "download_metadata":
            cmd = ["cckm", "google", "keys", "download-metadata"]
            if google_params.get("project_id"):
                cmd.extend(["--project-id", google_params["project_id"]])
            if google_params.get("location"):
                cmd.extend(["--location", google_params["location"]])
            if google_params.get("keyring"):
                cmd.extend(["--keyring", google_params["keyring"]])
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
            if google_params.get("file_path"):
                cmd.extend(["--file-path", google_params["file_path"]])
                
        elif action == "download_public_key":
            cmd.extend(["download-public-key", "--id", google_params["id"]])
            
        elif action == "enable_auto_rotation":
            cmd.extend(["enable-auto-rotation", "--id", google_params["id"]])
            
        elif action == "enable_version":
            cmd.extend(["enable-version", "--id", google_params["id"]])
            
        elif action == "get_update_all_versions_status":
            cmd.extend(["get-update-all-versions-status", "--id", google_params["id"]])
            
        elif action == "get_version":
            cmd.extend(["get-version", "--id", google_params["id"]])
            
        elif action == "list_version":
            cmd.extend(["list-version", "--id", google_params["id"]])
            
        elif action == "policy":
            cmd.extend(["policy", "--id", google_params["id"]])
            
        elif action == "re_import":
            cmd.extend(["re-import", "--id", google_params["id"]])
            
        elif action == "refresh":
            cmd.extend(["refresh", "--id", google_params["id"]])
            
        elif action == "refresh_version":
            cmd.extend(["refresh-version", "--id", google_params["id"]])
            
        elif action == "schedule_destroy":
            cmd.extend(["schedule-destroy", "--id", google_params["id"]])
            
        elif action == "upload_key":
            cmd.extend(["upload-key", "--id", google_params["id"]])
            
        elif action == "update_all_versions_jobs":
            cmd.extend(["update-all-versions-jobs", "--id", google_params["id"]])
            
        # Key synchronization operations
        elif action == "keys_sync_jobs_start":
            cmd = ["cckm", "google", "keys", "synchronization-jobs", "start", "--project-id", google_params["project_id"]]
            
        elif action == "keys_sync_jobs_get":
            cmd = ["cckm", "google", "keys", "synchronization-jobs", "get", "--id", google_params["job_id"]]
            
        elif action == "keys_sync_jobs_status":
            cmd = ["cckm", "google", "keys", "synchronization-jobs", "status"]
            
        elif action == "keys_sync_jobs_cancel":
            cmd = ["cckm", "google", "keys", "synchronization-jobs", "cancel", "--id", google_params["job_id"]]
            
        # Key ring operations
        elif action == "keyrings_list":
            cmd = ["cckm", "google", "key-rings", "list"]
            if google_params.get("project_id"):
                cmd.extend(["--project-id", google_params["project_id"]])
            if google_params.get("location"):
                cmd.extend(["--location", google_params["location"]])
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
                
        elif action == "keyrings_get":
            cmd = ["cckm", "google", "key-rings", "get", "--id", google_params["keyring_id"]]
            
        elif action == "keyrings_create":
            cmd = ["cckm", "google", "key-rings", "create", "--keyring-name", google_params["keyring_name"], "--project-id", google_params["project_id"], "--location", google_params["location"]]
            
        elif action == "keyrings_delete":
            cmd = ["cckm", "google", "key-rings", "delete", "--id", google_params["keyring_id"]]
            
        elif action == "keyrings_update_acls":
            cmd = ["cckm", "google", "key-rings", "update-acls", "--id", google_params["keyring_id"], "--acls", str(google_params["acls"])]
            
        # Location operations
        elif action == "locations_get_locations":
            cmd = ["cckm", "google", "locations", "get-locations"]
            
        # Project operations
        elif action == "projects_list":
            cmd = ["cckm", "google", "projects", "list"]
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
                
        elif action == "projects_get":
            cmd = ["cckm", "google", "projects", "get", "--id", google_params["project_id"]]
            
        elif action == "projects_add":
            cmd = ["cckm", "google", "projects", "add", "--project-id", google_params["project_id"]]
            if google_params.get("project_name"):
                cmd.extend(["--project-name", google_params["project_name"]])
                
        elif action == "projects_update":
            cmd = ["cckm", "google", "projects", "update", "--id", google_params["project_id"]]
            if google_params.get("project_name"):
                cmd.extend(["--project-name", google_params["project_name"]])
                
        elif action == "projects_delete":
            cmd = ["cckm", "google", "projects", "delete", "--id", google_params["project_id"]]
            
        elif action == "projects_get_project":
            cmd = ["cckm", "google", "projects", "get-project"]
            
        elif action == "projects_update_acls":
            cmd = ["cckm", "google", "projects", "update-acls", "--id", google_params["project_id"], "--acls", str(google_params["acls"])]
            
        # Reports operations
        elif action == "reports_list":
            cmd = ["cckm", "google", "reports", "list"]
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
                
        elif action == "reports_get":
            cmd = ["cckm", "google", "reports", "get", "--id", google_params["job_id"]]
            
        elif action == "reports_generate":
            cmd = ["cckm", "google", "reports", "generate-report", "--report-type", google_params["report_type"]]
            if google_params.get("report_format"):
                cmd.extend(["--report-format", google_params["report_format"]])
            if google_params.get("filters"):
                cmd.extend(["--filters", str(google_params["filters"])])
                
        elif action == "reports_download":
            cmd = ["cckm", "google", "reports", "download", "--id", google_params["job_id"], "--file-path", google_params["file_path"]]
            
        elif action == "reports_delete":
            cmd = ["cckm", "google", "reports", "delete", "--id", google_params["job_id"]]
            
        elif action == "reports_get_report":
            cmd = ["cckm", "google", "reports", "get-report"]
            if google_params.get("report_type"):
                cmd.extend(["--report-type", google_params["report_type"]])
            if google_params.get("filters"):
                cmd.extend(["--filters", str(google_params["filters"])])
            if google_params.get("limit"):
                cmd.extend(["--limit", str(google_params["limit"])])
            if google_params.get("skip"):
                cmd.extend(["--skip", str(google_params["skip"])])
                
        else:
            raise ValueError(f"Unsupported Google Cloud action: {action}")
        
        # Execute command
        # Pass domain parameters to execute_command
        result = self.execute_command(cmd, params.get("domain"), params.get("auth_domain"))
        return result.get("data", result.get("stdout", "")) 