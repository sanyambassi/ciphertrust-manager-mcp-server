"""OCI Compartments operations for CCKM."""

from typing import Any, Dict


def get_compartment_operations() -> Dict[str, Any]:
    """Return schema and action requirements for OCI compartment operations."""
    return {
        "schema_properties": {
            "oci_compartments_params": {
                "type": "object",
                "properties": {
                    # Basic compartment parameters
                    "connection_identifier": {"type": "string", "description": "Name or ID of the connection"},
                    "oci_compartment_id": {"type": "string", "description": "OCI compartment ID"},
                    
                    # Common parameters
                    "id": {"type": "string", "description": "Compartment resource ID"},
                    
                    # List parameters
                    "limit": {"type": "integer", "description": "Maximum number of results"},
                    "skip": {"type": "integer", "description": "Number of results to skip"},
                    "sort": {"type": "string", "description": "Sort field and order"}
                }
            }
        },
        "action_requirements": {
            "compartments_list": {"required": [], "optional": ["limit", "skip", "sort"]},
            "compartments_get": {"required": ["id"], "optional": []},
            "compartments_add_compartments": {"required": ["connection_identifier", "oci_compartment_id"], "optional": []},
            "compartments_delete": {"required": ["id"], "optional": []},
        }
    }


def build_compartment_command(action: str, oci_params: Dict[str, Any]) -> list:
    """Build the ksctl command for a given OCI compartment operation."""
    cmd = ["cckm", "oci", "compartments"]
    
    # Extract the base operation name (remove 'compartments_' prefix)
    base_action = action.replace("compartments_", "")
    
    if base_action == "list":
        cmd.append("list")
        if "limit" in oci_params:
            cmd.extend(["--limit", str(oci_params["limit"])])
        if "skip" in oci_params:
            cmd.extend(["--skip", str(oci_params["skip"])])
        if "sort" in oci_params:
            cmd.extend(["--sort", oci_params["sort"]])
            
    elif base_action == "get":
        cmd.extend(["get", "--id", oci_params["id"]])
        
    elif base_action == "add_compartments":
        cmd.extend(["add-compartments"])
        cmd.extend(["--connection-identifier", oci_params["connection_identifier"]])
        cmd.extend(["--oci-compartment-id", oci_params["oci_compartment_id"]])
        
    elif base_action == "delete":
        cmd.extend(["delete", "--id", oci_params["id"]])
        
    else:
        raise ValueError(f"Unsupported OCI compartments action: {action}")
    
    return cmd 