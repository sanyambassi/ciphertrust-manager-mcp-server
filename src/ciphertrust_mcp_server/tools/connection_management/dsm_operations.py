"""DSM connection operations for Connection Management."""

from typing import Any, Dict, List
from .base import ConnectionOperations
from .constants import DSM_PARAMETERS, CONNECTION_OPERATIONS


class DSMOperations(ConnectionOperations):
    """DSM connection operations for Connection Management."""
    
    def get_operations(self) -> List[str]:
        """Return list of supported DSM operations."""
        return CONNECTION_OPERATIONS["dsm"]
    
    def get_schema_properties(self) -> Dict[str, Any]:
        """Return schema properties for DSM operations."""
        return {
            "dsm_params": {
                "type": "object",
                "properties": DSM_PARAMETERS,
                "description": "DSM-specific parameters"
            }
        }
    
    def get_action_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Return action-specific parameter requirements for DSM."""
        return {
            "create": {
                "required": ["name"],
                "optional": ["server_url", "username", "password", "certificate_file", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
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
                "optional": ["name", "server_url", "username", "password", "certificate_file", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
            },
            "test": {
                "required": ["id"],
                "optional": ["domain", "auth_domain"]
            }
        }
    
    async def execute_operation(self, action: str, params: Dict[str, Any]) -> Any:
        """Execute DSM connection operation."""
        dsm_params = params.get("dsm_params", {})
        
        # Build base command
        cmd = ["connectionmgmt", "dsm", action]
        
        # Add action-specific parameters
        if action == "create":
            if dsm_params.get("name"):
                cmd.extend(["--name", dsm_params["name"]])
            if dsm_params.get("server_url"):
                cmd.extend(["--server-url", dsm_params["server_url"]])
            if dsm_params.get("username"):
                cmd.extend(["--username", dsm_params["username"]])
            if dsm_params.get("password"):
                cmd.extend(["--password", dsm_params["password"]])
            if dsm_params.get("certificate_file"):
                cmd.extend(["--certificate-file", dsm_params["certificate_file"]])
            if dsm_params.get("products"):
                cmd.extend(["--products", dsm_params["products"]])
            if dsm_params.get("description"):
                cmd.extend(["--description", dsm_params["description"]])
            if dsm_params.get("meta"):
                cmd.extend(["--meta", dsm_params["meta"]])
            if dsm_params.get("labels"):
                cmd.extend(["--labels", dsm_params["labels"]])
            if dsm_params.get("json_file"):
                cmd.extend(["--json-file", dsm_params["json_file"]])
                
        elif action == "list":
            if dsm_params.get("name"):
                cmd.extend(["--name", dsm_params["name"]])
            if dsm_params.get("cloudname"):
                cmd.extend(["--cloudname", dsm_params["cloudname"]])
            if dsm_params.get("category"):
                cmd.extend(["--category", dsm_params["category"]])
            if dsm_params.get("products"):
                cmd.extend(["--products", dsm_params["products"]])
            if dsm_params.get("limit"):
                cmd.extend(["--limit", str(dsm_params["limit"])])
            if dsm_params.get("skip"):
                cmd.extend(["--skip", str(dsm_params["skip"])])
            if dsm_params.get("fields"):
                cmd.extend(["--fields", dsm_params["fields"]])
            if dsm_params.get("labels_query"):
                cmd.extend(["--labels-query", dsm_params["labels_query"]])
            if dsm_params.get("lastconnectionafter"):
                cmd.extend(["--lastconnectionafter", dsm_params["lastconnectionafter"]])
            if dsm_params.get("lastconnectionbefore"):
                cmd.extend(["--lastconnectionbefore", dsm_params["lastconnectionbefore"]])
            if dsm_params.get("lastconnectionok"):
                cmd.extend(["--lastconnectionok", dsm_params["lastconnectionok"]])
                
        elif action == "get":
            cmd.extend(["--id", dsm_params["id"]])
            
        elif action == "delete":
            cmd.extend(["--id", dsm_params["id"]])
            if dsm_params.get("force"):
                cmd.append("--force")
                
        elif action == "modify":
            cmd.extend(["--id", dsm_params["id"]])
            if dsm_params.get("name"):
                cmd.extend(["--name", dsm_params["name"]])
            if dsm_params.get("server_url"):
                cmd.extend(["--server-url", dsm_params["server_url"]])
            if dsm_params.get("username"):
                cmd.extend(["--username", dsm_params["username"]])
            if dsm_params.get("password"):
                cmd.extend(["--password", dsm_params["password"]])
            if dsm_params.get("certificate_file"):
                cmd.extend(["--certificate-file", dsm_params["certificate_file"]])
            if dsm_params.get("products"):
                cmd.extend(["--products", dsm_params["products"]])
            if dsm_params.get("description"):
                cmd.extend(["--description", dsm_params["description"]])
            if dsm_params.get("meta"):
                cmd.extend(["--meta", dsm_params["meta"]])
            if dsm_params.get("labels"):
                cmd.extend(["--labels", dsm_params["labels"]])
            if dsm_params.get("json_file"):
                cmd.extend(["--json-file", dsm_params["json_file"]])
                
        elif action == "test":
            cmd.extend(["--id", dsm_params["id"]])
            
        else:
            raise ValueError(f"Unsupported DSM action: {action}")
        
        # Execute command
        result = self.execute_command(cmd, params.get("domain"), params.get("auth_domain"))
        return result.get("data", result.get("stdout", "")) 