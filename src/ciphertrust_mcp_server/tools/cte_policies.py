"""CTE Policies management tools for CipherTrust Manager with built-in domain support."""

from typing import Any, Optional, Literal

from pydantic import BaseModel, Field

from .base import BaseTool


# Policy Parameter Models
class CTEPolicyCreateParams(BaseModel):
    """Parameters for creating a CTE policy."""
    cte_policy_name: str = Field(..., description="Name of the CTE policy")
    policy_type: str = Field(..., description="Policy type: Standard, Cloud_Object_Storage, LDT, IDT, or CSI")
    description: Optional[str] = Field(None, description="Description of the policy")
    never_deny: bool = Field(False, description="Flag to always permit operations in policy")
    # JSON parameters for rules
    security_rules_json: Optional[str] = Field(None, description="SecurityRule parameters in JSON format")
    security_rules_json_file: Optional[str] = Field(None, description="File containing SecurityRule parameters in JSON")
    key_rules_json: Optional[str] = Field(None, description="KeyRule parameters in JSON format")
    key_rules_json_file: Optional[str] = Field(None, description="File containing KeyRule parameters in JSON")
    data_tx_rules_json: Optional[str] = Field(None, description="DataTxRule parameters in JSON format")
    data_tx_rules_json_file: Optional[str] = Field(None, description="File containing DataTxRule parameters in JSON")
    ldt_rules_json: Optional[str] = Field(None, description="LDTRule parameters in JSON format")
    ldt_rules_json_file: Optional[str] = Field(None, description="File containing LDTRule parameters in JSON")
    idt_rules_json: Optional[str] = Field(None, description="IDTRule parameters in JSON format")
    idt_rules_json_file: Optional[str] = Field(None, description="File containing IDTRule parameters in JSON")
    signature_rules_json: Optional[str] = Field(None, description="SignatureRule parameters in JSON format")
    signature_rules_json_file: Optional[str] = Field(None, description="File containing SignatureRule parameters in JSON")
    restrict_update_json: Optional[str] = Field(None, description="RestrictUpdate parameters in JSON format")
    restrict_update_json_file: Optional[str] = Field(None, description="File containing RestrictUpdate parameters in JSON")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to create policy in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListParams(BaseModel):
    """Parameters for listing CTE policies."""
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    cte_policy_name: Optional[str] = Field(None, description="Filter by policy name")
    policy_type: Optional[str] = Field(None, description="Filter by policy type: Standard, Cloud_Object_Storage, LDT, IDT, or CSI")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list policies from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyGetParams(BaseModel):
    """Parameters for getting a CTE policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to get policy from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyDeleteParams(BaseModel):
    """Parameters for deleting a CTE policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to delete policy from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifyParams(BaseModel):
    """Parameters for modifying a CTE policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    description: Optional[str] = Field(None, description="Description of the policy")
    never_deny: Optional[bool] = Field(None, description="Flag to always permit operations in policy")
    force_restrict_update: bool = Field(False, description="Flag to remove restriction of policy for modification")
    restrict_update_json: Optional[str] = Field(None, description="RestrictUpdate parameters in JSON format")
    restrict_update_json_file: Optional[str] = Field(None, description="File containing RestrictUpdate parameters in JSON")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify policy in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Security Rule Parameter Models
class CTEPolicyAddSecurityRuleParams(BaseModel):
    """Parameters for adding a security rule to a policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    effect: str = Field(..., description="Effect: permit, deny, audit, applykey (comma-separated for multiple)")
    action: Optional[str] = Field(None, description="Action: read, write, all_ops, key_op")
    user_set_identifier: Optional[str] = Field(None, description="Identifier for CTE UserSet")
    process_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ProcessSet")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    exclude_user_set: bool = Field(False, description="Exclude the user set from the policy")
    exclude_process_set: bool = Field(False, description="Exclude the process set from the policy")
    exclude_resource_set: bool = Field(False, description="Exclude the resource set from the policy")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add rule to (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicySecurityRuleParams(BaseModel):
    """Parameters for security rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    security_rule_identifier: str = Field(..., description="Identifier for CTE SecurityRule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListSecurityRulesParams(BaseModel):
    """Parameters for listing security rules."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    action: Optional[str] = Field(None, description="Filter by action: read, write, all_ops, key_op")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list rules from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifySecurityRuleParams(BaseModel):
    """Parameters for modifying a security rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    security_rule_identifier: str = Field(..., description="Identifier for CTE SecurityRule")
    effect: Optional[str] = Field(None, description="Effect: permit, deny, audit, applykey (comma-separated)")
    action: Optional[str] = Field(None, description="Action: read, write, all_ops, key_op")
    order_number: Optional[int] = Field(None, description="Order number on CTE Client")
    user_set_identifier: Optional[str] = Field(None, description="Identifier for CTE UserSet")
    process_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ProcessSet")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    exclude_user_set: Optional[bool] = Field(None, description="Exclude the user set from the policy")
    exclude_process_set: Optional[bool] = Field(None, description="Exclude the process set from the policy")
    exclude_resource_set: Optional[bool] = Field(None, description="Exclude the resource set from the policy")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Key Rule Parameter Models
class CTEPolicyAddKeyRuleParams(BaseModel):
    """Parameters for adding a key rule to a policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    key_identifier: str = Field(..., description="Key identifier (name, id, slug, alias, uri, uuid, muid, key_id, or 'clear_key')")
    key_type: Optional[str] = Field(None, description="Key type: name, id, slug, alias, uri, uuid, muid, or key_id")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add rule to (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyKeyRuleParams(BaseModel):
    """Parameters for key rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    key_rule_identifier: str = Field(..., description="Identifier for CTE KeyRule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListKeyRulesParams(BaseModel):
    """Parameters for listing key rules."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list rules from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifyKeyRuleParams(BaseModel):
    """Parameters for modifying a key rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    key_rule_identifier: str = Field(..., description="Identifier for CTE KeyRule")
    key_identifier: Optional[str] = Field(None, description="Key identifier")
    key_type: Optional[str] = Field(None, description="Key type")
    order_number: Optional[int] = Field(None, description="Order number on CTE Client")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Data Tx Rule Parameter Models (same structure as Key Rules)
class CTEPolicyAddDataTxRuleParams(CTEPolicyAddKeyRuleParams):
    """Parameters for adding a data transformation rule to a policy."""
    pass


class CTEPolicyDataTxRuleParams(BaseModel):
    """Parameters for data tx rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    data_tx_rule_identifier: str = Field(..., description="Identifier for CTE DataTxRule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListDataTxRulesParams(CTEPolicyListKeyRulesParams):
    """Parameters for listing data tx rules."""
    pass


class CTEPolicyModifyDataTxRuleParams(BaseModel):
    """Parameters for modifying a data tx rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    data_tx_rule_identifier: str = Field(..., description="Identifier for CTE DataTxRule")
    key_identifier: Optional[str] = Field(None, description="Key identifier")
    key_type: Optional[str] = Field(None, description="Key type")
    order_number: Optional[int] = Field(None, description="Order number on CTE Client")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# LDT Rule Parameter Models
class CTEPolicyAddLDTRuleParams(BaseModel):
    """Parameters for adding an LDT rule to a policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    current_key_json_file: str = Field(..., description="CurrentKey parameters JSON file")
    transform_key_json_file: str = Field(..., description="Transformation Key parameters JSON file")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    is_exclusion_rule: bool = Field(False, description="Whether LDT rule is exclusion rule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add rule to (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyLDTRuleParams(BaseModel):
    """Parameters for LDT rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    ldt_rule_identifier: str = Field(..., description="Identifier for CTE LDT Rule (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListLDTRulesParams(BaseModel):
    """Parameters for listing LDT rules."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list rules from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifyLDTRuleParams(BaseModel):
    """Parameters for modifying an LDT rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    ldt_rule_identifier: str = Field(..., description="Identifier for CTE LDT Rule")
    current_key_json_file: Optional[str] = Field(None, description="CurrentKey parameters JSON file")
    transform_key_json_file: Optional[str] = Field(None, description="Transformation Key parameters JSON file")
    order_number: Optional[int] = Field(None, description="Order number on CTE Client")
    resource_set_identifier: Optional[str] = Field(None, description="Identifier for CTE ResourceSet")
    is_exclusion_rule: Optional[bool] = Field(None, description="Whether LDT rule is exclusion rule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# IDT Rule Parameter Models
class CTEPolicyIDTRuleParams(BaseModel):
    """Parameters for IDT rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    idt_rule_identifier: str = Field(..., description="Identifier for CTE IDT KeyRule (UUID, URI)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListIDTRulesParams(BaseModel):
    """Parameters for listing IDT rules."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list rules from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifyIDTRuleParams(BaseModel):
    """Parameters for modifying an IDT rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    idt_rule_identifier: str = Field(..., description="Identifier for CTE IDT KeyRule")
    idt_current_key: Optional[str] = Field(None, description="CurrentKey parameters")
    idt_current_key_type: Optional[str] = Field(None, description="Current key type")
    idt_transform_key: Optional[str] = Field(None, description="Transformation Key parameters")
    idt_transform_key_type: Optional[str] = Field(None, description="Transformation key type")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


# Signature Rule Parameter Models
class CTEPolicyAddSignatureRuleParams(BaseModel):
    """Parameters for adding a signature rule to a policy."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    signature_set_id_list: str = Field(..., description="Comma-separated list of signature set identifiers")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to add rule to (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicySignatureRuleParams(BaseModel):
    """Parameters for signature rule operations."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    signature_rule_identifier: str = Field(..., description="Identifier for CTE SignatureRule")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to operate in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyListSignatureRulesParams(BaseModel):
    """Parameters for listing signature rules."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    limit: int = Field(10, description="Maximum number of resources to return")
    skip: int = Field(0, description="Index of the first resource to return")
    signature_set_identifier: Optional[str] = Field(None, description="Filter by signature set identifier")
    signature_set_name: Optional[str] = Field(None, description="Filter by signature set name")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to list rules from (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyModifySignatureRuleParams(BaseModel):
    """Parameters for modifying a signature rule."""
    cte_policy_identifier: str = Field(..., description="Identifier for CTE Policy (UUID, URI or Name)")
    signature_rule_identifier: str = Field(..., description="Identifier for CTE SignatureRule")
    signature_set_identifier: str = Field(..., description="Identifier for CTE SignatureSet")
    # Domain support
    domain: Optional[str] = Field(None, description="Domain to modify rule in (defaults to global setting)")
    auth_domain: Optional[str] = Field(None, description="Authentication domain (defaults to global setting)")


class CTEPolicyManagementTool(BaseTool):
    """Manage CTE policies and related operations (grouped)."""

    @property
    def name(self) -> str:
        return "cte_policy_management"

    @property
    def description(self) -> str:
        return "Manage CTE policies and related operations (create, list, get, delete, modify, add/delete/modify rules, etc.)"

    def get_schema(self) -> dict[str, Any]:
        # Provide a schema that includes an 'action' parameter and all possible params for each action
        # For brevity, only a sample is shown; in the real code, merge all params
        return {
            "title": "CTEPolicyManagementTool",
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": [
                        "create", "list", "get", "delete", "modify",
                        "add_security_rule", "delete_security_rule", "get_security_rule", "list_security_rules", "modify_security_rule",
                        "add_key_rule", "delete_key_rule", "get_key_rule", "list_key_rules", "modify_key_rule",
                        "add_data_tx_rule", "delete_data_tx_rule", "get_data_tx_rule", "list_data_tx_rules", "modify_data_tx_rule",
                        "add_ldt_rule", "delete_ldt_rule", "get_ldt_rule", "list_ldt_rules", "modify_ldt_rule",
                        "get_idt_rule", "list_idt_rules", "modify_idt_rule",
                        "add_signature_rule", "delete_signature_rule", "get_signature_rule", "list_signature_rules", "modify_signature_rule"
                    ],
                    "description": "Action to perform"
                },
                # ... merge all params from the old tool classes ...
            },
            "required": ["action"]
        }

    async def execute(self, **kwargs: Any) -> Any:
        action = kwargs.get("action")
        # CTE Policy actions
        if action == "create":
            params = CTEPolicyCreateParams(**kwargs)
            cmd = ["cte", "policy", "create", "--cte-policy-name", params.cte_policy_name, "--policy-type", params.policy_type]
            if params.description:
                cmd.extend(["--description", params.description])
            if params.never_deny:
                cmd.append("--never-deny")
            if params.security_rules_json:
                cmd.extend(["--security-rules-json", params.security_rules_json])
            if params.security_rules_json_file:
                cmd.extend(["--security-rules-json-file", params.security_rules_json_file])
            if params.key_rules_json:
                cmd.extend(["--key-rules-json", params.key_rules_json])
            if params.key_rules_json_file:
                cmd.extend(["--key-rules-json-file", params.key_rules_json_file])
            if params.data_tx_rules_json:
                cmd.extend(["--data-tx-rules-json", params.data_tx_rules_json])
            if params.data_tx_rules_json_file:
                cmd.extend(["--data-tx-rules-json-file", params.data_tx_rules_json_file])
            if params.ldt_rules_json:
                cmd.extend(["--ldt-rules-json", params.ldt_rules_json])
            if params.ldt_rules_json_file:
                cmd.extend(["--ldt-rules-json-file", params.ldt_rules_json_file])
            if params.idt_rules_json:
                cmd.extend(["--idt-rules-json", params.idt_rules_json])
            if params.idt_rules_json_file:
                cmd.extend(["--idt-rules-json-file", params.idt_rules_json_file])
            if params.signature_rules_json:
                cmd.extend(["--signature-rules-json", params.signature_rules_json])
            if params.signature_rules_json_file:
                cmd.extend(["--signature-rules-json-file", params.signature_rules_json_file])
            if params.restrict_update_json:
                cmd.extend(["--restrict-update-json", params.restrict_update_json])
            if params.restrict_update_json_file:
                cmd.extend(["--restrict-update-json-file", params.restrict_update_json_file])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list":
            params = CTEPolicyListParams(**kwargs)
            cmd = ["cte", "policy", "list", "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.cte_policy_name:
                cmd.extend(["--cte-policy-name", params.cte_policy_name])
            if params.policy_type:
                cmd.extend(["--policy-type", params.policy_type])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get":
            params = CTEPolicyGetParams(**kwargs)
            cmd = ["cte", "policy", "get", "--cte-policy-identifier", params.cte_policy_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete":
            params = CTEPolicyDeleteParams(**kwargs)
            cmd = ["cte", "policy", "delete", "--cte-policy-identifier", params.cte_policy_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify":
            params = CTEPolicyModifyParams(**kwargs)
            cmd = ["cte", "policy", "modify", "--cte-policy-identifier", params.cte_policy_identifier]
            if params.description:
                cmd.extend(["--description", params.description])
            if params.never_deny is not None:
                cmd.append("--never-deny" if params.never_deny else "--no-never-deny")
            if params.force_restrict_update:
                cmd.append("--force-restrict-update")
            if params.restrict_update_json:
                cmd.extend(["--restrict-update-json", params.restrict_update_json])
            if params.restrict_update_json_file:
                cmd.extend(["--restrict-update-json-file", params.restrict_update_json_file])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # Security Rule actions
        elif action == "add_security_rule":
            params = CTEPolicyAddSecurityRuleParams(**kwargs)
            cmd = ["cte", "policy", "add-security-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--effect", params.effect]
            if params.action:
                cmd.extend(["--action", params.action])
            if params.user_set_identifier:
                cmd.extend(["--user-set-identifier", params.user_set_identifier])
            if params.process_set_identifier:
                cmd.extend(["--process-set-identifier", params.process_set_identifier])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            if params.exclude_user_set:
                cmd.append("--exclude-user-set")
            if params.exclude_process_set:
                cmd.append("--exclude-process-set")
            if params.exclude_resource_set:
                cmd.append("--exclude-resource-set")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete_security_rule":
            params = CTEPolicySecurityRuleParams(**kwargs)
            cmd = ["cte", "policy", "delete-security-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--security-rule-identifier", params.security_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get_security_rule":
            params = CTEPolicySecurityRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-security-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--security-rule-identifier", params.security_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_security_rules":
            params = CTEPolicyListSecurityRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-security-rules", "--cte-policy-identifier", params.cte_policy_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.action:
                cmd.extend(["--action", params.action])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_security_rule":
            params = CTEPolicyModifySecurityRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-security-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--security-rule-identifier", params.security_rule_identifier]
            if params.effect:
                cmd.extend(["--effect", params.effect])
            if params.action:
                cmd.extend(["--action", params.action])
            if params.order_number is not None:
                cmd.extend(["--order-number", str(params.order_number)])
            if params.user_set_identifier:
                cmd.extend(["--user-set-identifier", params.user_set_identifier])
            if params.process_set_identifier:
                cmd.extend(["--process-set-identifier", params.process_set_identifier])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            if params.exclude_user_set:
                cmd.append("--exclude-user-set")
            if params.exclude_process_set:
                cmd.append("--exclude-process-set")
            if params.exclude_resource_set:
                cmd.append("--exclude-resource-set")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # Key Rule actions
        elif action == "add_key_rule":
            params = CTEPolicyAddKeyRuleParams(**kwargs)
            cmd = ["cte", "policy", "add-key-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--key-identifier", params.key_identifier]
            if params.key_type:
                cmd.extend(["--key-type", params.key_type])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete_key_rule":
            params = CTEPolicyKeyRuleParams(**kwargs)
            cmd = ["cte", "policy", "delete-key-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--key-rule-identifier", params.key_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get_key_rule":
            params = CTEPolicyKeyRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-key-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--key-rule-identifier", params.key_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_key_rules":
            params = CTEPolicyListKeyRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-key-rules", "--cte-policy-identifier", params.cte_policy_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_key_rule":
            params = CTEPolicyModifyKeyRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-key-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--key-rule-identifier", params.key_rule_identifier]
            if params.key_identifier:
                cmd.extend(["--key-identifier", params.key_identifier])
            if params.key_type:
                cmd.extend(["--key-type", params.key_type])
            if params.order_number is not None:
                cmd.extend(["--order-number", str(params.order_number)])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # Data Tx Rule actions
        elif action == "add_data_tx_rule":
            params = CTEPolicyAddDataTxRuleParams(**kwargs)
            cmd = ["cte", "policy", "add-data-tx-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--key-identifier", params.key_identifier]
            if params.key_type:
                cmd.extend(["--key-type", params.key_type])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete_data_tx_rule":
            params = CTEPolicyDataTxRuleParams(**kwargs)
            cmd = ["cte", "policy", "delete-data-tx-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--data-tx-rule-identifier", params.data_tx_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get_data_tx_rule":
            params = CTEPolicyDataTxRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-data-tx-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--data-tx-rule-identifier", params.data_tx_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_data_tx_rules":
            params = CTEPolicyListDataTxRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-data-tx-rules", "--cte-policy-identifier", params.cte_policy_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_data_tx_rule":
            params = CTEPolicyModifyDataTxRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-data-tx-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--data-tx-rule-identifier", params.data_tx_rule_identifier]
            if params.key_identifier:
                cmd.extend(["--key-identifier", params.key_identifier])
            if params.key_type:
                cmd.extend(["--key-type", params.key_type])
            if params.order_number is not None:
                cmd.extend(["--order-number", str(params.order_number)])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # LDT Rule actions
        elif action == "add_ldt_rule":
            params = CTEPolicyAddLDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "add-ldt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--current-key-json-file", params.current_key_json_file, "--transform-key-json-file", params.transform_key_json_file]
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            if params.is_exclusion_rule:
                cmd.append("--is-exclusion-rule")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete_ldt_rule":
            params = CTEPolicyLDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "delete-ldt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--ldt-rule-identifier", params.ldt_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get_ldt_rule":
            params = CTEPolicyLDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-ldt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--ldt-rule-identifier", params.ldt_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_ldt_rules":
            params = CTEPolicyListLDTRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-ldt-rules", "--cte-policy-identifier", params.cte_policy_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_ldt_rule":
            params = CTEPolicyModifyLDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-ldt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--ldt-rule-identifier", params.ldt_rule_identifier]
            if params.current_key_json_file:
                cmd.extend(["--current-key-json-file", params.current_key_json_file])
            if params.transform_key_json_file:
                cmd.extend(["--transform-key-json-file", params.transform_key_json_file])
            if params.order_number is not None:
                cmd.extend(["--order-number", str(params.order_number)])
            if params.resource_set_identifier:
                cmd.extend(["--resource-set-identifier", params.resource_set_identifier])
            if params.is_exclusion_rule is not None:
                cmd.append("--is-exclusion-rule" if params.is_exclusion_rule else "--no-is-exclusion-rule")
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # IDT Rule actions
        elif action == "get_idt_rule":
            params = CTEPolicyIDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-idt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--idt-rule-identifier", params.idt_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_idt_rules":
            params = CTEPolicyListIDTRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-idt-rules", "--cte-policy-identifier", params.cte_policy_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_idt_rule":
            params = CTEPolicyModifyIDTRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-idt-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--idt-rule-identifier", params.idt_rule_identifier]
            if params.idt_current_key:
                cmd.extend(["--idt-current-key", params.idt_current_key])
            if params.idt_current_key_type:
                cmd.extend(["--idt-current-key-type", params.idt_current_key_type])
            if params.idt_transform_key:
                cmd.extend(["--idt-transform-key", params.idt_transform_key])
            if params.idt_transform_key_type:
                cmd.extend(["--idt-transform-key-type", params.idt_transform_key_type])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        # Signature Rule actions
        elif action == "add_signature_rule":
            params = CTEPolicyAddSignatureRuleParams(**kwargs)
            cmd = ["cte", "policy", "add-signature-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--signature-set-id-list", params.signature_set_id_list]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "delete_signature_rule":
            params = CTEPolicySignatureRuleParams(**kwargs)
            cmd = ["cte", "policy", "delete-signature-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--signature-rule-identifier", params.signature_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "get_signature_rule":
            params = CTEPolicySignatureRuleParams(**kwargs)
            cmd = ["cte", "policy", "get-signature-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--signature-rule-identifier", params.signature_rule_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "list_signature_rules":
            params = CTEPolicyListSignatureRulesParams(**kwargs)
            cmd = ["cte", "policy", "list-signature-rules", "--cte-policy-identifier", params.cte_policy_identifier, "--limit", str(params.limit), "--skip", str(params.skip)]
            if params.signature_set_identifier:
                cmd.extend(["--signature-set-identifier", params.signature_set_identifier])
            if params.signature_set_name:
                cmd.extend(["--signature-set-name", params.signature_set_name])
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        elif action == "modify_signature_rule":
            params = CTEPolicyModifySignatureRuleParams(**kwargs)
            cmd = ["cte", "policy", "modify-signature-rule", "--cte-policy-identifier", params.cte_policy_identifier, "--signature-rule-identifier", params.signature_rule_identifier, "--signature-set-identifier", params.signature_set_identifier]
            return self.execute_with_domain(cmd, params.domain, params.auth_domain)
        else:
            raise ValueError(f"Unknown action: {action}")

CTE_POLICY_TOOLS = [CTEPolicyManagementTool]
