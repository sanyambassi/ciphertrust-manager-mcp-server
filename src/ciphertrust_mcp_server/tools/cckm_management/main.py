"""Main CCKM Management Tool."""

from typing import Any, Dict, List
from ..base import BaseTool
from .constants import COMMON_SCHEMA_PROPERTIES, CLOUD_OPERATIONS
from .aws_operations import AWSOperations
from .azure_operations import AzureOperations
from .oci_operations import OCIOperations
from .google_operations import GoogleOperations
from .microsoft_operations import MicrosoftOperations
from .ekm_operations import EKMOperations
from .gws_operations import GWSOperations


class CCKMManagementTool(BaseTool):
    """Unified CCKM Management Tool that delegates to specialized cloud provider operations.
    
    This tool provides a single interface for all CCKM operations while internally
    organizing functionality by cloud provider for better maintainability.
    """
    
    def __init__(self):
        super().__init__()
        # Initialize all cloud provider operations
        self.cloud_operations = {
            'aws': AWSOperations(self.execute_with_domain),
            'azure': AzureOperations(self.execute_with_domain),
            'oci': OCIOperations(self.execute_with_domain),
            'google': GoogleOperations(self.execute_with_domain),
            'microsoft': MicrosoftOperations(self.execute_with_domain),
            'ekm': EKMOperations(self.execute_with_domain),
            'gws': GWSOperations(self.execute_with_domain),
            # TODO: Add other cloud providers as they are implemented
            # 'sap-dc': SAPDCOperations(self.execute_with_domain),
            # 'salesforce': SalesforceOperations(self.execute_with_domain),
            # 'virtual': VirtualOperations(self.execute_with_domain),
            # 'hsm': HSMOperations(self.execute_with_domain),
            # 'external-cm': ExternalCMOperations(self.execute_with_domain),
            # 'dsm': DSMOperations(self.execute_with_domain),
        }
        
    @property
    def name(self) -> str:
        return "cckm_management"
    
    @property
    def description(self) -> str:
        return (
            "CCKM (CipherTrust Cloud Key Manager) operations for managing cloud keys and related resources across various providers. "
            "Supports comprehensive operations for AWS, Azure, Google Cloud, OCI, SAP Data Custodian, Salesforce, Microsoft DKE, Virtual, HSM, GWS, EKM, External CM, and DSM. "
            "Features include: "
            "AWS: Keys, Custom Key Stores (XKS), IAM management, KMS account management, Reports, Bulk jobs, Log groups; "
            "Azure: Keys, Certificates, Secrets, Vaults, Subscriptions, Reports, Bulk jobs, Synchronization jobs; "
            "Google Cloud: Keys, Key Rings, Projects, Locations, Reports, Synchronization jobs; "
            "OCI: Keys, Compartments, External Vaults, Issuers, Regions, Reports, Tenancy, Vaults; "
            "Microsoft: Keys, DKE endpoints; "
            "EKM: Endpoints; "
            "GWS: Endpoints with wrap/unwrap operations. "
            "Each cloud provider has specific operations and parameters - see action_requirements in schema for details."
        )
    
    def get_schema(self) -> dict[str, Any]:
        """Build complete schema from all cloud providers"""
        # Collect all unique operations across all cloud providers
        all_operations = set()
        for cloud_provider, operations in self.cloud_operations.items():
            for operation in operations.get_operations():
                all_operations.add(operation)
        
        # Start with common properties
        properties = {
            "action": {
                "type": "string",
                "enum": sorted(all_operations),
                "description": "The CCKM operation to perform (e.g., keys_create, keys_list, keys_get). The cloud_provider parameter determines which cloud provider to use."
            },
            **COMMON_SCHEMA_PROPERTIES
        }
        
        # Add properties from each cloud provider
        for cloud_provider, operations in self.cloud_operations.items():
            properties.update(operations.get_schema_properties())
        
        # Collect action requirements from all cloud providers
        action_requirements = {}
        for cloud_provider, operations in self.cloud_operations.items():
            cloud_requirements = operations.get_action_requirements()
            for operation, requirements in cloud_requirements.items():
                # Use generic operation names, not cloud-specific ones
                action_requirements[operation] = requirements
        
        return {
            "type": "object",
            "properties": properties,
            "required": ["action", "cloud_provider"],
            "additionalProperties": True,
            "action_requirements": action_requirements
        }
    
    async def execute(self, action: str, **kwargs: Any) -> Any:
        """Execute CCKM operation by delegating to appropriate cloud provider."""
        # Get cloud provider from parameters
        cloud_provider = kwargs.get("cloud_provider")
        if not cloud_provider:
            return {"error": "Missing required parameter: cloud_provider"}
        
        # Get the appropriate cloud operations handler
        if cloud_provider not in self.cloud_operations:
            return {"error": f"Cloud provider {cloud_provider} not implemented yet"}
        
        cloud_ops = self.cloud_operations[cloud_provider]
        
        # Check if the operation is supported by this cloud provider
        if action not in cloud_ops.get_operations():
            return {"error": f"Operation {action} not supported for cloud provider {cloud_provider}"}
        
        # Validate action-specific requirements using cloud-specific requirements
        if not self._validate_action_params(action, kwargs, cloud_ops):
            cloud_requirements = cloud_ops.get_action_requirements().get(action, {})
            required_params = cloud_requirements.get("required", [])
            return {"error": f"Missing required parameters for {action}: {required_params}"}
        
        # Execute the operation
        try:
            return await cloud_ops.execute_operation(action, kwargs)
        except Exception as e:
            return {"error": f"Failed to execute {action}: {str(e)}"}
    
    def _validate_action_params(self, action: str, params: dict, cloud_ops=None) -> bool:
        """Validate that required parameters are present for the action."""
        if cloud_ops:
            # Use cloud-specific requirements
            requirements = cloud_ops.get_action_requirements().get(action, {})
        else:
            # Fallback to global schema requirements
            schema = self.get_schema()
            requirements = schema.get("action_requirements", {}).get(action, {})
        required_params = requirements.get("required", [])
        
        # Check if all required parameters are present
        for param in required_params:
            # Check in the main params first
            if param in params:
                continue
                
            # Check in cloud-specific params (e.g., aws_params, azure_params, etc.)
            cloud_provider = params.get("cloud_provider")
            if cloud_provider:
                # Generic cloud params pattern (e.g., aws_params)
                cloud_params_key = f"{cloud_provider}_params"
                if cloud_params_key in params and param in params[cloud_params_key]:
                    continue
                
                # Check service-specific params (e.g., aws_kms_params, aws_iam_params, etc.)
                service_specific_keys = [
                    f"{cloud_provider}_kms_params",
                    f"{cloud_provider}_iam_params", 
                    f"{cloud_provider}_key_params",
                    f"{cloud_provider}_keys_params",
                    f"{cloud_provider}_reports_params",
                    f"{cloud_provider}_bulkjob_params",
                    f"{cloud_provider}_custom_key_stores_params",
                    f"{cloud_provider}_logs_params",
                    f"{cloud_provider}_certificates_params",
                    f"{cloud_provider}_vaults_params",
                    f"{cloud_provider}_secrets_params",
                    f"{cloud_provider}_subscriptions_params",
                    f"{cloud_provider}_compartments_params"
                ]
                
                param_found = False
                for service_key in service_specific_keys:
                    if service_key in params and param in params[service_key]:
                        param_found = True
                        break
                
                if param_found:
                    continue
                
                # Special case: Check for alternative parameter names
                if param == "source_key_identifier":
                    # Check for sourceKey_identifier alternative
                    for service_key in service_specific_keys:
                        if service_key in params and "sourceKey_identifier" in params[service_key]:
                            param_found = True
                            break
                    if param_found:
                        continue
                
            # Parameter not found
            return False
        
        return True 