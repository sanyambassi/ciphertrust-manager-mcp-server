"""Elasticsearch Log Forwarder connection operations for Connection Management."""

from typing import Any, Dict, List
from .base import ConnectionOperations
from .constants import LOG_FORWARDER_PARAMETERS, CONNECTION_OPERATIONS


class LogForwarderElasticsearchOperations(ConnectionOperations):
    """Elasticsearch Log Forwarder connection operations for Connection Management."""
    
    def get_operations(self) -> List[str]:
        """Return list of supported Elasticsearch Log Forwarder operations."""
        return CONNECTION_OPERATIONS["log_forwarder"]
    
    def get_schema_properties(self) -> Dict[str, Any]:
        """Return schema properties for Elasticsearch Log Forwarder operations."""
        return {
            "log_forwarder_elasticsearch_params": {
                "type": "object",
                "properties": LOG_FORWARDER_PARAMETERS,
                "description": "Elasticsearch Log Forwarder-specific parameters"
            }
        }
    
    def get_action_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Return action-specific parameter requirements for Elasticsearch Log Forwarder."""
        return {
            "create": {
                "required": ["name"],
                "optional": ["host", "port", "http_user", "http_password", "transport", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
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
                "optional": ["name", "host", "port", "http_user", "http_password", "transport", "products", "description", "meta", "labels", "json_file", "domain", "auth_domain"]
            },
            "test": {
                "required": ["id"],
                "optional": ["host", "port", "http_user", "http_password", "transport", "domain", "auth_domain"]
            }
        }
    
    async def execute_operation(self, action: str, params: Dict[str, Any]) -> Any:
        """Execute Elasticsearch Log Forwarder connection operation."""
        log_forwarder_params = params.get("log_forwarder_elasticsearch_params", {})
        
        # Build base command
        cmd = ["connectionmgmt", "log-forwarder", "elasticsearch", action]
        
        # Add action-specific parameters
        if action == "create":
            if log_forwarder_params.get("name"):
                cmd.extend(["--name", log_forwarder_params["name"]])
            if log_forwarder_params.get("host"):
                cmd.extend(["--host", log_forwarder_params["host"]])
            if log_forwarder_params.get("port"):
                cmd.extend(["--port", str(log_forwarder_params["port"])])
            if log_forwarder_params.get("http_user"):
                cmd.extend(["--http-user", log_forwarder_params["http_user"]])
            if log_forwarder_params.get("http_password"):
                cmd.extend(["--http-password", log_forwarder_params["http_password"]])
            if log_forwarder_params.get("transport"):
                cmd.extend(["--transport", log_forwarder_params["transport"]])
            if log_forwarder_params.get("products"):
                cmd.extend(["--products", log_forwarder_params["products"]])
            if log_forwarder_params.get("description"):
                cmd.extend(["--description", log_forwarder_params["description"]])
            if log_forwarder_params.get("meta"):
                cmd.extend(["--meta", log_forwarder_params["meta"]])
            if log_forwarder_params.get("labels"):
                cmd.extend(["--labels", log_forwarder_params["labels"]])
            if log_forwarder_params.get("json_file"):
                cmd.extend(["--json-file", log_forwarder_params["json_file"]])
                
        elif action == "list":
            if log_forwarder_params.get("name"):
                cmd.extend(["--name", log_forwarder_params["name"]])
            if log_forwarder_params.get("cloudname"):
                cmd.extend(["--cloudname", log_forwarder_params["cloudname"]])
            if log_forwarder_params.get("category"):
                cmd.extend(["--category", log_forwarder_params["category"]])
            if log_forwarder_params.get("products"):
                cmd.extend(["--products", log_forwarder_params["products"]])
            if log_forwarder_params.get("limit"):
                cmd.extend(["--limit", str(log_forwarder_params["limit"])])
            if log_forwarder_params.get("skip"):
                cmd.extend(["--skip", str(log_forwarder_params["skip"])])
            if log_forwarder_params.get("fields"):
                cmd.extend(["--fields", log_forwarder_params["fields"]])
            if log_forwarder_params.get("labels_query"):
                cmd.extend(["--labels-query", log_forwarder_params["labels_query"]])
            if log_forwarder_params.get("lastconnectionafter"):
                cmd.extend(["--lastconnectionafter", log_forwarder_params["lastconnectionafter"]])
            if log_forwarder_params.get("lastconnectionbefore"):
                cmd.extend(["--lastconnectionbefore", log_forwarder_params["lastconnectionbefore"]])
            if log_forwarder_params.get("lastconnectionok"):
                cmd.extend(["--lastconnectionok", log_forwarder_params["lastconnectionok"]])
                
        elif action == "get":
            cmd.extend(["--id", log_forwarder_params["id"]])
            
        elif action == "delete":
            cmd.extend(["--id", log_forwarder_params["id"]])
            if log_forwarder_params.get("force"):
                cmd.append("--force")
                
        elif action == "modify":
            cmd.extend(["--id", log_forwarder_params["id"]])
            if log_forwarder_params.get("name"):
                cmd.extend(["--name", log_forwarder_params["name"]])
            if log_forwarder_params.get("host"):
                cmd.extend(["--host", log_forwarder_params["host"]])
            if log_forwarder_params.get("port"):
                cmd.extend(["--port", str(log_forwarder_params["port"])])
            if log_forwarder_params.get("http_user"):
                cmd.extend(["--http-user", log_forwarder_params["http_user"]])
            if log_forwarder_params.get("http_password"):
                cmd.extend(["--http-password", log_forwarder_params["http_password"]])
            if log_forwarder_params.get("transport"):
                cmd.extend(["--transport", log_forwarder_params["transport"]])
            if log_forwarder_params.get("products"):
                cmd.extend(["--products", log_forwarder_params["products"]])
            if log_forwarder_params.get("description"):
                cmd.extend(["--description", log_forwarder_params["description"]])
            if log_forwarder_params.get("meta"):
                cmd.extend(["--meta", log_forwarder_params["meta"]])
            if log_forwarder_params.get("labels"):
                cmd.extend(["--labels", log_forwarder_params["labels"]])
            if log_forwarder_params.get("json_file"):
                cmd.extend(["--json-file", log_forwarder_params["json_file"]])
                
        elif action == "test":
            cmd.extend(["--id", log_forwarder_params["id"]])
            if log_forwarder_params.get("host"):
                cmd.extend(["--host", log_forwarder_params["host"]])
            if log_forwarder_params.get("port"):
                cmd.extend(["--port", str(log_forwarder_params["port"])])
            if log_forwarder_params.get("http_user"):
                cmd.extend(["--http-user", log_forwarder_params["http_user"]])
            if log_forwarder_params.get("http_password"):
                cmd.extend(["--http-password", log_forwarder_params["http_password"]])
            if log_forwarder_params.get("transport"):
                cmd.extend(["--transport", log_forwarder_params["transport"]])
            
        else:
            raise ValueError(f"Unsupported Elasticsearch Log Forwarder action: {action}")
        
        # Execute command
        result = self.execute_command(cmd, params.get("domain"), params.get("auth_domain"))
        return result.get("data", result.get("stdout", "")) 