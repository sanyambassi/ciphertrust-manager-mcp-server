"""CipherTrust MCP tools package with integrated domain support."""

from typing import Type

from .base import BaseTool

# Import domain management tools (administrative domain operations)
from .domains import DOMAIN_TOOLS  # Now a single grouped DomainManagementTool

# Import existing tools - all now have optional domain/auth_domain parameters
from .akeyless import AKEYLESS_TOOLS     # Akeyless Gateway integration (with domain support)
from .backup import BACKUP_TOOLS  # Now a single grouped BackupManagementTool
from .backupkeys import BACKUPKEY_TOOLS  # Now a single grouped BackupKeyManagementTool
from .groupmaps import GROUPMAP_TOOLS  # Now a single grouped GroupMapManagementTool
from .groups import GROUP_TOOLS          # Now a single grouped GroupManagementTool
from .keys import KEY_TOOLS              # Now a single grouped KeyManagementTool
from .keypolicies import KEY_POLICY_TOOLS  # Now a single grouped KeyPolicyManagementTool
from .licensing import LICENSING_TOOLS   # System-wide operations
from .metrics import METRICS_TOOLS       # Prometheus metrics (system-wide)
from .mkeks import MKEKS_TOOLS           # Master KEKs (system-wide)
from .network import NETWORK_TOOLS       # Network diagnostics (system-wide)
from .ntp import NTP_TOOLS               # NTP server management (system-wide)
from .properties import PROPERTIES_TOOLS # System properties (system-wide)
from .proxy import PROXY_TOOLS           # Proxy configurations (system-wide)
from .quorum import QUORUM_TOOLS         # Quorum management (with domain support)
from .records import RECORD_TOOLS  # Now a single grouped RecordManagementTool
from .rotkeys import ROTKEY_TOOLS        # Root of Trust keys (system-wide)
from .scp import SCP_TOOLS  # Now a single grouped ScpManagementTool
from .secrets import SECRET_TOOLS  # Now a single grouped SecretsManagementTool
from .services import SERVICE_MGMT_TOOLS # Service management (system-wide)
from .system import SYSTEM_TOOLS         # Now a single grouped SystemInformationTool
from .templates import TEMPLATE_TOOLS    # Template management (with domain support)
from .tokens import TOKEN_TOOLS          # Now a single grouped TokenManagementTool
from .users import USER_TOOLS            # Now two grouped tools: UserManagementTool and PasswordPolicyManagementTool
from .vkeys import VKEYS_TOOLS  # Now a single grouped VKeysManagementTool

# Import connection management tools
from .connection_management import CONNECTION_TOOLS  # Now a single grouped ConnectionManagementTool

# Import authentication connection management tools
from .connections_ldap import CONNECTION_LDAP_TOOLS      # LDAP connection management (with domain support)
from .connections_oidc import CONNECTION_OIDC_TOOLS      # OIDC connection management (with domain support)
from .connections_users import CONNECTION_USERS_TOOLS    # Connection users management (with domain support)

# Import cryptographic operation tools
from .crypto import CRYPTO_TOOLS  # Now a single grouped CryptoOperationsTool

# Import CTE management tools
from .cte_clientgroups import CTE_CLIENTGROUP_TOOLS     # Now a single grouped CTEClientGroupManagementTool
from .cte_clients import CTE_CLIENT_TOOLS                # CTE client management (with domain support)
from .cte_csi_storagegroups import CTE_CSI_STORAGEGROUP_TOOLS  # Now a single grouped CTECSIStorageGroupManagementTool
from .cte_policies import CTE_POLICY_TOOLS               # CTE policy management (with domain support)
from .cte_profiles import CTE_PROFILE_TOOLS             # CTE profile management (with domain support)
from .cte_process_sets import CTE_PROCESS_SET_TOOLS     # CTE process set management (with domain support)
from .cte_user_sets import CTE_USER_SET_TOOLS           # CTE user set management (with domain support)
from .cte_resource_sets import CTE_RESOURCE_SET_TOOLS   # CTE resource set management (with domain support)


# Collect all available tools
ALL_TOOLS: list[Type[BaseTool]] = [
    *SYSTEM_TOOLS,          # Now a single grouped SystemInformationTool
    *KEY_TOOLS,             # Now a single grouped KeyManagementTool
    *USER_TOOLS,            # UserManagementTool and PasswordPolicyManagementTool
    *GROUP_TOOLS,           # Now a single grouped GroupManagementTool
    *SERVICE_MGMT_TOOLS,
    *LICENSING_TOOLS,
    *MKEKS_TOOLS,
    *PROPERTIES_TOOLS,
    *KEY_POLICY_TOOLS,      # Now a single grouped KeyPolicyManagementTool
    *GROUPMAP_TOOLS,        # Now a single grouped GroupMapManagementTool
    *DOMAIN_TOOLS,          # Now a single grouped DomainManagementTool
    *TOKEN_TOOLS,           # Now a single grouped TokenManagementTool
    *SECRET_TOOLS,          # Now a single grouped SecretsManagementTool
    *SCP_TOOLS,             # Now a single grouped ScpManagementTool
    *TEMPLATE_TOOLS,        # Now a single grouped TemplateManagementTool
    *VKEYS_TOOLS,           # Now a single grouped VKeysManagementTool
    *AKEYLESS_TOOLS,        # Now a single grouped AkeylessManagementTool
    *NETWORK_TOOLS,         # Now a single grouped NetworkManagementTool
    *ROTKEY_TOOLS,          # Now a single grouped RotKeyManagementTool
    *RECORD_TOOLS,          # Now a single grouped RecordManagementTool
    *METRICS_TOOLS,
    *TOKEN_TOOLS,
    *CONNECTION_TOOLS,      # Now a single grouped ConnectionManagementTool
    *CRYPTO_TOOLS,          # Now a single grouped CryptoOperationsTool
    *BACKUP_TOOLS,          # Now a single grouped BackupManagementTool
    *BACKUPKEY_TOOLS,       # Now a single grouped BackupKeyManagementTool
    *QUORUM_TOOLS,          # Now a single grouped QuorumManagementTool
    *PROXY_TOOLS,           # Now a single grouped ProxyManagementTool
    *NTP_TOOLS,             # Now a single grouped NtpManagementTool
    *CONNECTION_LDAP_TOOLS,
    *CONNECTION_OIDC_TOOLS,
    *CONNECTION_USERS_TOOLS,
    *CTE_CLIENTGROUP_TOOLS,
    *CTE_CLIENT_TOOLS,
    *CTE_CSI_STORAGEGROUP_TOOLS,
    *CTE_POLICY_TOOLS,
    *CTE_PROFILE_TOOLS,
    *CTE_PROCESS_SET_TOOLS,
    *CTE_USER_SET_TOOLS,
    *CTE_RESOURCE_SET_TOOLS,
]

all = ["BaseTool", "ALL_TOOLS"]

# Total tool count: 292 tools
# - System: 2 (system-wide operations)
# - Services: 3 (system-wide operations)
# - Tokens: 5 (with domain support)
# - Users: 10 (with domain support + password policies)
# - Groups: 8 (with domain support)
# - GroupMaps: 5 (with domain support)
# - Keys: 18 (with domain support)
# - Key Policies: 5 (with domain support)
# - Secrets: 9 (with domain support)
# - SCP: 2 (with domain support)
# - Templates: 5 (with domain support)
# - Akeyless: 7 (with domain support)
# - Backup: 11 (with domain support)
# - Backup Keys: 8 (with domain support)
# - Licensing: 10 (system-wide operations)
# - RoTKeys: 4 (system-wide operations)
# - Records: 7 (system-wide operations)
# - Metrics: 5 (system-wide operations)
# - Master KEKs: 3 (system-wide operations)
# - Network: 5 (system-wide operations)
# - NTP: 5 (system-wide operations)
# - Properties: 4 (system-wide operations)
# - Proxy: 11 (system-wide operations)
# - Quorum: 14 (with domain support)
# - Domains: 13 (administrative)
# - Connection Management: 11 (from connection_management module)
# - Connection LDAP: 6 (with domain support)
# - Connection OIDC: 6 (with domain support)
# - Connection Users: 2 (with domain support)
# - Crypto: 7 (with domain support)
# - CTE Client Groups: 18 (with domain support)
# - CTE Clients: 31 (with domain support)
# - CTE CSI Storage groups: 14 (with domain support)
# - CTE Policies: 33 (with domain support)
# - CTE Profiles: 6 (with domain support)
# - CTE Process Sets: 10 (with domain support)
# - CTE User Sets: 10 (with domain support)
# - CTE Resource Sets: 10 (with domain support)
# = 292 total tools
