# CipherTrust MCP Server: Tools Reference

This document lists all grouped tools available in the CipherTrust MCP Server, with their JSON-RPC method names and a short description. Use these method names in your JSON-RPC requests.

---

## System
- **system_information**: Get or set CipherTrust Manager system information. Actions: `get`, `set`.

## Keys
- **key_management**: Key management operations (list, create, get, delete, modify, archive, recover, revoke, reactivate, destroy, export, clone, generate_kcv, alias_add, alias_delete, alias_modify, query, list_labels).

## Users
- **user_management**: User management operations (create, list, get, delete, modify).
- **password_policy_management**: Password policy management operations (pwdpolicy_create, pwdpolicy_list, pwdpolicy_get, pwdpolicy_delete, pwdpolicy_update).

## Groups
- **group_management**: Group management operations (list, create, get, delete, add_user, remove_user, add_client, remove_client).

## Domains
- **domain_management**: Domain management operations (switch, get_current, create, list, get, update, keks_list, keks_get, rotate_kek, retry_kek_rotation, log_forwarders_redirection_enable, log_forwarders_redirection_disable, log_forwarders_redirection_status, syslog_redirection_enable, syslog_redirection_disable, syslog_redirection_status).

## Crypto
- **crypto_operations**: Cryptographic operations (encrypt, decrypt, reencrypt, sign, verify, hide, unhide).

## CTE (CipherTrust Transparent Encryption)
- **cte_clientgroup_management**: CTE client group management (create, list, get, delete, modify, add_clients, remove_client, list_clients, get_client, create_guardpoint, list_guardpoints, get_guardpoint, modify_guardpoint, unguard_guardpoint, unguard_bulk_guardpoints, modify_password, modify_auth_binaries, send_ldt_pause).

---

## Other Major Tool Groups
- **akeyless_management**: Akeyless management operations (config_get, config_modify, config_status, customer_fragment_create, customer_fragment_delete, customer_fragment_list, token_create).
- **groupmap_management**: Group mapping management operations (list, create, get, delete, modify).
- **key_policy_management**: Key policy management operations (list, create, get, update, delete).
- **licensing_management**: Licensing management operations (features_list, licenses_add, licenses_delete, licenses_get, licenses_list, lockdata, trials_activate, trials_deactivate, trials_get, trials_list).
- **metrics_management**: Prometheus metrics operations (status, enable, disable, get, renew_token).
- **network_management**: Network management operations (ping, checkport, lookup, traceroute, interfaces_list).
- **ntp_management**: NTP management operations (status, servers_list, servers_add, servers_get, servers_delete).
- **properties_management**: System properties management operations (list, get, modify, reset).
- **proxy_management**: Proxy and proxy protocol allow proxies management operations (list, add, update, delete, test, protocol_allow_list, protocol_allow_add, protocol_allow_get, protocol_allow_update, protocol_allow_delete, protocol_allow_reset).
- **quorum_management**: Quorum management operations (list, get, activate, approve, deny, revoke, delete, get_resources_list, policy_activate, policy_deactivate, policy_status, profiles_list, profiles_get, profiles_update).
- **record_management**: Audit record and alarm config management operations (record_list, record_get, alarm_config_list, alarm_config_create, alarm_config_get, alarm_config_update, alarm_config_delete).
- **rotkey_management**: Root of Trust key management operations (list, get, rotate, delete).
- **scp_management**: SCP public key management operations (public_key_get, public_key_rotate).
- **secrets_management**: Secret management operations (list, create, get, delete, modify, export, destroy, version, list_version).
- **service_management**: Service management operations (status, restart, reset).
- **template_management**: Template management operations (list, create, get, delete, modify).
- **token_management**: Token management operations (create, list, get, delete, revoke).
- **vkeys_management**: Versioned key management operations (create, list, get, export).

---

> **Tip:** For a full list of actions and parameters for each tool, see the code or use the `get_schema` method if available. 