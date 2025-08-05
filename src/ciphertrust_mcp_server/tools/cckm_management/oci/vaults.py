"""OCI Vaults operations for CCKM."""

from typing import Any, Dict


def get_vault_operations() -> Dict[str, Any]:
    """Return schema and action requirements for OCI vault operations."""
    return {
        "schema_properties": {
            "oci_vaults_params": {
                "type": "object",
                "properties": {
                    # Basic vault parameters  
                    "oci_compartment_id": {"type": "string", "description": "OCI compartment ID"},
                    "connection_identifier": {"type": "string", "description": "Connection identifier"},
                    
                    # Common parameters
                    "id": {"type": "string", "description": "Vault ID"},
                    
                    # List parameters
                    "limit": {"type": "integer", "description": "Maximum number of results"},
                    "skip": {"type": "integer", "description": "Number of results to skip"},
                    "sort": {"type": "string", "description": "Sort field and order"}
                }
            }
        },
        "action_requirements": {
            "vaults_list": {"required": [], "optional": ["limit", "skip", "sort", "oci_compartment_id"]},
            "vaults_get": {"required": ["id"], "optional": []},
            "vaults_get_vaults": {"required": ["oci_compartment_id"], "optional": []},
        }
    }


def build_vault_command(action: str, oci_params: Dict[str, Any]) -> list:
    """Build the ksctl command for a given OCI vault operation."""
    cmd = ["cckm", "oci", "vaults"]
    
    # Extract the base operation name (remove 'vaults_' prefix)  
    base_action = action.replace("vaults_", "")
    
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
            
    elif base_action == "get":
        cmd.extend(["get", "--id", oci_params["id"]])
        
    elif base_action == "get_vaults":
        cmd.extend(["get-vaults", "--oci-compartment-id", oci_params["oci_compartment_id"]])
        
    else:
        raise ValueError(f"Unsupported OCI vaults action: {action}")
    
    return cmd 