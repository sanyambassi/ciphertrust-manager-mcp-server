"""OCI connection operations for Connection Management."""

from typing import Any, Dict, List
from .base import ConnectionOperations
from .constants import OCI_PARAMETERS, CONNECTION_OPERATIONS


class OCIOperations(ConnectionOperations):
    """OCI connection operations for Connection Management."""
    
    def get_operations(self) -> List[str]:
        """Return list of supported OCI operations."""
        return CONNECTION_OPERATIONS["oci"]
    
    def get_schema_properties(self) -> Dict[str, Any]:
        """Return schema properties for OCI operations."""
        return {
            "oci_params": {
                "type": "object",
                "properties": OCI_PARAMETERS,
                "description": "OCI-specific parameters"
            }
        }
    
    def get_action_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Return action-specific parameter requirements for OCI."""
        return {
            "create": {
                "required": ["name"],
                "optional": ["tenancy_ocid", "user_ocid", "fingerprint", "private_key", "region", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
            },
            "list": {
                "required": [],
                "optional": ["name", "cloudname", "category", "products", "limit", "skip", "fields", "labels_query", "lastconnectionafter", "lastconnectionbefore", "lastconnectionok", "domain", "auth_domain"]
            },
            "get": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            },
            "delete": {
                "required": ["id"],
                "optional": ["force", "domain", "auth_domain"]
            },
            "modify": {
                "required": ["id"],
                "optional": ["name", "tenancy_ocid", "user_ocid", "fingerprint", "private_key", "region", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
            },
            "test": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            }
        }
    
    async def execute_operation(self, action: str, params: Dict[str, Any]) -> Any:
        """Execute OCI connection operation."""
        oci_params = params.get("oci_params", {})
        
        # Build base command
        cmd = ["connectionmgmt", "oci", action]
        
        # Add action-specific parameters
        if action == "create":
            if oci_params.get("name"):
                cmd.extend(["--name", oci_params["name"]])
            if oci_params.get("tenancy_ocid"):
                cmd.extend(["--tenancy-ocid", oci_params["tenancy_ocid"]])
            if oci_params.get("user_ocid"):
                cmd.extend(["--user-ocid", oci_params["user_ocid"]])
            if oci_params.get("fingerprint"):
                cmd.extend(["--fingerprint", oci_params["fingerprint"]])
            if oci_params.get("private_key"):
                cmd.extend(["--private-key", oci_params["private_key"]])
            if oci_params.get("region"):
                cmd.extend(["--region", oci_params["region"]])
            if oci_params.get("products"):
                cmd.extend(["--products", oci_params["products"]])
            if oci_params.get("description"):
                cmd.extend(["--description", oci_params["description"]])
            if oci_params.get("meta"):
                cmd.extend(["--meta", oci_params["meta"]])
            if oci_params.get("labels"):
                cmd.extend(["--labels", oci_params["labels"]])
            if oci_params.get("json_file"):
                cmd.extend(["--json-file", oci_params["json_file"]])
                
        elif action == "list":
            if oci_params.get("name"):
                cmd.extend(["--name", oci_params["name"]])
            if oci_params.get("cloudname"):
                cmd.extend(["--cloudname", oci_params["cloudname"]])
            if oci_params.get("category"):
                cmd.extend(["--category", oci_params["category"]])
            if oci_params.get("products"):
                cmd.extend(["--products", oci_params["products"]])
            if oci_params.get("limit"):
                cmd.extend(["--limit", str(oci_params["limit"])])
            if oci_params.get("skip"):
                cmd.extend(["--skip", str(oci_params["skip"])])
            if oci_params.get("fields"):
                cmd.extend(["--fields", oci_params["fields"]])
            if oci_params.get("labels_query"):
                cmd.extend(["--labels-query", oci_params["labels_query"]])
            if oci_params.get("lastconnectionafter"):
                cmd.extend(["--lastconnectionafter", oci_params["lastconnectionafter"]])
            if oci_params.get("lastconnectionbefore"):
                cmd.extend(["--lastconnectionbefore", oci_params["lastconnectionbefore"]])
            if oci_params.get("lastconnectionok"):
                cmd.extend(["--lastconnectionok", oci_params["lastconnectionok"]])
                
        elif action == "get":
            cmd.extend(["--id", oci_params["id"]])
            
        elif action == "delete":
            cmd.extend(["--id", oci_params["id"]])
            if oci_params.get("force"):
                cmd.append("--force")
                
        elif action == "modify":
            cmd.extend(["--id", oci_params["id"]])
            if oci_params.get("name"):
                cmd.extend(["--name", oci_params["name"]])
            if oci_params.get("tenancy_ocid"):
                cmd.extend(["--tenancy-ocid", oci_params["tenancy_ocid"]])
            if oci_params.get("user_ocid"):
                cmd.extend(["--user-ocid", oci_params["user_ocid"]])
            if oci_params.get("fingerprint"):
                cmd.extend(["--fingerprint", oci_params["fingerprint"]])
            if oci_params.get("private_key"):
                cmd.extend(["--private-key", oci_params["private_key"]])
            if oci_params.get("region"):
                cmd.extend(["--region", oci_params["region"]])
            if oci_params.get("products"):
                cmd.extend(["--products", oci_params["products"]])
            if oci_params.get("description"):
                cmd.extend(["--description", oci_params["description"]])
            if oci_params.get("meta"):
                cmd.extend(["--meta", oci_params["meta"]])
            if oci_params.get("labels"):
                cmd.extend(["--labels", oci_params["labels"]])
            if oci_params.get("json_file"):
                cmd.extend(["--json-file", oci_params["json_file"]])
                
        elif action == "test":
            cmd.extend(["--id", oci_params["id"]])
            
        else:
            raise ValueError(f"Unsupported OCI action: {action}")
        
        # Execute command
        result = self.execute_command(cmd, params.get("domain"), params.get("auth_domain"))
        return result.get("data", result.get("stdout", "")) 