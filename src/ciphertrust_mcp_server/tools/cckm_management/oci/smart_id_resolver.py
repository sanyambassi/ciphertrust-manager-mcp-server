"""Smart ID resolver for OCI operations."""

import json
import re
from typing import Any, Dict, Optional, Union


class OCISmartIDResolver:
    """Smart ID resolver for OCI resources (keys, vaults, compartments)."""
    
    def __init__(self, operations):
        self.operations = operations
    
    def is_uuid(self, identifier: str) -> bool:
        """Check if the identifier is a UUID."""
        uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
        return bool(re.match(uuid_pattern, identifier.lower()))
    
    def is_ocid(self, identifier: str) -> bool:
        """Check if the identifier is an OCI OCID."""
        # OCI OCIDs follow pattern: ocid1.<resource-type>.<realm>.[region].<unique-id>
        # Example: ocid1.key.oc1.iad.amaaaaaaexampleuniqueid
        ocid_pattern = r'^ocid1\.[a-z]+\.oc1(\.[a-z0-9]+)?\..*'
        return bool(re.match(ocid_pattern, identifier))
    
    async def resolve_key_id(self, key_identifier: str, oci_params: Dict[str, Any], cloud_provider: str = "oci") -> str:
        """Resolve key identifier to UUID."""
        # If already a UUID, return as is
        if self.is_uuid(key_identifier):
            return key_identifier
        
        # If it's an OCID, return as is (OCI accepts these)
        if self.is_ocid(key_identifier):
            return key_identifier
        
        # Prepare the list parameters for key search
        list_params = {
            "cloud_provider": cloud_provider,
            "oci_keys_params": {}
        }
        
        # Use name filter
        list_params["oci_keys_params"]["key_name"] = key_identifier
        
        # Add any additional filters that might help
        if "oci_compartment_id" in oci_params:
            list_params["oci_keys_params"]["oci_compartment_id"] = oci_params["oci_compartment_id"]
        if "oci_vault" in oci_params:
            list_params["oci_keys_params"]["oci_vault"] = oci_params["oci_vault"]
        
        # Call the list operation
        try:
            result = await self.operations.execute_operation("keys_list", list_params)
            
            # Parse the result
            if isinstance(result, str):
                result_data = json.loads(result)
            else:
                result_data = result
            
            # Look for matching keys
            keys = result_data.get("resources", [])
            if not keys:
                # Try alternative result structure
                keys = result_data.get("data", [])
            
            # Find exact name match
            for key in keys:
                if key.get("name") == key_identifier or key.get("key_name") == key_identifier:
                    return key.get("id", key_identifier)
            
            # If no exact match found, return original identifier
            return key_identifier
            
        except Exception:
            # If resolution fails, return original identifier
            return key_identifier
    
    async def resolve_vault_id(self, vault_identifier: str, oci_params: Dict[str, Any], cloud_provider: str = "oci") -> str:
        """Resolve vault identifier to UUID."""
        # If already a UUID, return as is
        if self.is_uuid(vault_identifier):
            return vault_identifier
        
        # If it's an OCID, return as is
        if self.is_ocid(vault_identifier):
            return vault_identifier
        
        # Prepare the list parameters for vault search
        list_params = {
            "cloud_provider": cloud_provider,
            "oci_vaults_params": {}
        }
        
        # Add compartment filter if available
        if "oci_compartment_id" in oci_params:
            list_params["oci_vaults_params"]["oci_compartment_id"] = oci_params["oci_compartment_id"]
        
        # Call the list operation
        try:
            result = await self.operations.execute_operation("vaults_list", list_params)
            
            # Parse the result
            if isinstance(result, str):
                result_data = json.loads(result)
            else:
                result_data = result
            
            # Look for matching vaults
            vaults = result_data.get("resources", [])
            if not vaults:
                vaults = result_data.get("data", [])
            
            # Find exact name match
            for vault in vaults:
                if vault.get("name") == vault_identifier or vault.get("display_name") == vault_identifier:
                    return vault.get("id", vault_identifier)
            
            # If no exact match found, return original identifier
            return vault_identifier
            
        except Exception:
            # If resolution fails, return original identifier
            return vault_identifier
    
    async def resolve_compartment_id(self, compartment_identifier: str, oci_params: Dict[str, Any], cloud_provider: str = "oci") -> str:
        """Resolve compartment identifier to UUID."""
        # If already a UUID, return as is
        if self.is_uuid(compartment_identifier):
            return compartment_identifier
        
        # If it's an OCID, return as is
        if self.is_ocid(compartment_identifier):
            return compartment_identifier
        
        # Prepare the list parameters for compartment search
        list_params = {
            "cloud_provider": cloud_provider,
            "oci_compartments_params": {}
        }
        
        # Call the list operation
        try:
            result = await self.operations.execute_operation("compartments_list", list_params)
            
            # Parse the result
            if isinstance(result, str):
                result_data = json.loads(result)
            else:
                result_data = result
            
            # Look for matching compartments
            compartments = result_data.get("resources", [])
            if not compartments:
                compartments = result_data.get("data", [])
            
            # Find exact name match
            for compartment in compartments:
                if compartment.get("name") == compartment_identifier or compartment.get("compartment_name") == compartment_identifier:
                    return compartment.get("id", compartment_identifier)
            
            # If no exact match found, return original identifier
            return compartment_identifier
            
        except Exception:
            # If resolution fails, return original identifier
            return compartment_identifier 