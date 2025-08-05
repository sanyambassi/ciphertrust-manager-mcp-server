"""OCI operations for CCKM."""

from typing import Any, Dict, List
from .base import CCKMOperations
from .constants import CLOUD_OPERATIONS
from .oci import (
    get_key_operations, build_key_command,
    get_vault_operations, build_vault_command,
    get_compartment_operations, build_compartment_command,
    OCISmartIDResolver
)


class OCIOperations(CCKMOperations):
    """Handles OCI operations for CCKM by building and executing ksctl commands."""
    
    def get_operations(self) -> List[str]:
        """Return list of supported OCI operations."""
        return CLOUD_OPERATIONS["oci"]
    
    def get_schema_properties(self) -> Dict[str, Any]:
        """Return schema properties for OCI operations."""
        key_ops = get_key_operations()
        vault_ops = get_vault_operations()
        compartment_ops = get_compartment_operations()
        
        return {
            **key_ops.get("schema_properties", {}),
            **vault_ops.get("schema_properties", {}),
            **compartment_ops.get("schema_properties", {}),
        }

    def get_action_requirements(self) -> Dict[str, Dict[str, Any]]:
        """Return action-specific parameter requirements for OCI."""
        return {
            **get_key_operations()["action_requirements"],
            **get_vault_operations()["action_requirements"],
            **get_compartment_operations()["action_requirements"],
        }

    async def execute_operation(self, action: str, params: Dict[str, Any]) -> Any:
        """Execute OCI operation."""
        # Start with generic oci_params
        oci_params = params.get("oci_params", {}).copy()
        
        # Merge service-specific params into oci_params
        service_specific_keys = [
            "oci_keys_params",
            "oci_vaults_params",
            "oci_compartments_params"
        ]
        
        for service_key in service_specific_keys:
            if service_key in params:
                oci_params.update(params[service_key])
        
        # Create smart resolver for ID resolution
        smart_resolver = OCISmartIDResolver(self)
        
        # Check if this operation needs ID resolution
        if self._needs_id_resolution(action, oci_params):
            await self._resolve_ids(action, oci_params, smart_resolver, params.get("cloud_provider", "oci"))
        
        # Route to appropriate command builder based on operation type
        if action.startswith("keys_"):
            cmd = build_key_command(action, oci_params)
        elif action.startswith("vaults_"):
            cmd = build_vault_command(action, oci_params)
        elif action.startswith("compartments_"):
            cmd = build_compartment_command(action, oci_params)
        else:
            raise ValueError(f"Unsupported OCI action: {action}")
        
        # Execute command
        # Pass domain parameters to execute_command
        result = self.execute_command(cmd, params.get("domain"), params.get("auth_domain"))
        return result
    
    def _needs_id_resolution(self, action: str, oci_params: Dict[str, Any]) -> bool:
        """Check if this operation needs ID resolution."""
        id_operations = [
            "keys_get", "keys_delete", "keys_enable", "keys_disable", "keys_refresh", 
            "keys_restore", "keys_schedule_deletion", "keys_cancel_deletion", 
            "keys_change_compartment", "keys_enable_auto_rotation", "keys_disable_auto_rotation", 
            "keys_delete_backup", "keys_add_version", "keys_get_version", "keys_list_version",
            "keys_schedule_deletion_version", "keys_cancel_schedule_deletion_version",
            "vaults_get", "compartments_get", "compartments_delete"
        ]
        
        return action in id_operations and "id" in oci_params
    
    async def _resolve_ids(self, action: str, oci_params: Dict[str, Any], smart_resolver: OCISmartIDResolver, cloud_provider: str):
        """Resolve IDs in the parameters."""
        if "id" in oci_params:
            original_id = oci_params["id"]
            
            if action.startswith("keys_"):
                resolved_id = await smart_resolver.resolve_key_id(original_id, oci_params, cloud_provider)
            elif action.startswith("vaults_"):
                resolved_id = await smart_resolver.resolve_vault_id(original_id, oci_params, cloud_provider)
            elif action.startswith("compartments_"):
                resolved_id = await smart_resolver.resolve_compartment_id(original_id, oci_params, cloud_provider)
            else:
                resolved_id = original_id
            
            oci_params["id"] = resolved_id 