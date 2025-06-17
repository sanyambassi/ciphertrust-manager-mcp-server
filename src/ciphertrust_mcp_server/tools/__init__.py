"""CipherTrust MCP tools package with integrated domain support."""

from typing import Type

from .base import BaseTool

# Import domain management tools (administrative domain operations)
from .domains import DOMAIN_TOOLS

# Import existing tools - all now have optional domain/auth_domain parameters
from .akeyless import AKEYLESS_TOOLS     # Akeyless Gateway integration (with domain support)
from .backup import BACKUP_TOOLS         # Backup management (with domain support)
from .backupkeys import BACKUPKEY_TOOLS  # Backup key management (with domain support)
from .groupmaps import GROUPMAP_TOOLS    # Group mappings with domain support
from .groups import GROUP_TOOLS          # Updated with domain support
from .keys import KEY_TOOLS              # Updated with domain support
from .keypolicies import KEY_POLICY_TOOLS  # Key policies with domain support
from .licensing import LICENSING_TOOLS   # System-wide operations
from .metrics import METRICS_TOOLS       # Prometheus metrics (system-wide)
from .mkeks import MKEKS_TOOLS           # Master KEKs (system-wide)
from .network import NETWORK_TOOLS       # Network diagnostics (system-wide)
from .ntp import NTP_TOOLS               # NTP server management (system-wide)
from .properties import PROPERTIES_TOOLS # System properties (system-wide)
from .proxy import PROXY_TOOLS           # Proxy configurations (system-wide)
from .quorum import QUORUM_TOOLS         # Quorum management (with domain support)
from .records import RECORD_TOOLS        # Audit records and alarm configs (system-wide)
from .rotkeys import ROTKEY_TOOLS        # Root of Trust keys (system-wide)
from .scp import SCP_TOOLS               # SCP public key management (with domain support)
from .secrets import SECRET_TOOLS        # Secrets management (with domain support)
from .services import SERVICE_MGMT_TOOLS # Service management (system-wide)
from .system import SYSTEM_TOOLS         # System-wide operations
from .templates import TEMPLATE_TOOLS    # Template management (with domain support)
from .tokens import TOKEN_TOOLS          # Updated with domain support
from .users import USER_TOOLS            # Updated with domain support + password policies

# Import connection management tools
from .connection_management import CONNECTION_TOOLS

# Import authentication connection management tools
from .connections_ldap import CONNECTION_LDAP_TOOLS      # LDAP connection management (with domain support)
from .connections_oidc import CONNECTION_OIDC_TOOLS      # OIDC connection management (with domain support)
from .connections_users import CONNECTION_USERS_TOOLS    # Connection users management (with domain support)

# Import cryptographic operation tools
from .crypto import CRYPTO_TOOLS         # Cryptographic operations (with domain support)

# Import CTE management tools
from .cte_clientgroups import CTE_CLIENTGROUP_TOOLS     # CTE client group management (with domain support)
from .cte_clients import CTE_CLIENT_TOOLS                # CTE client management (with domain support)
from .cte_csi_storagegroups import CTE_CSI_STORAGEGROUP_TOOLS  # CTE CSI StorageGroup management (with domain support)
from .cte_policies import CTE_POLICY_TOOLS               # CTE policy management (with domain support)
from .cte_profiles import CTE_PROFILE_TOOLS             # CTE profile management (with domain support)
from .cte_process_sets import CTE_PROCESS_SET_TOOLS     # CTE process set management (with domain support)
from .cte_user_sets import CTE_USER_SET_TOOLS           # CTE user set management (with domain support)
from .cte_resource_sets import CTE_RESOURCE_SET_TOOLS   # CTE resource set management (with domain support)

# Import cluster management tools
from .cluster_management import CLUSTER_MANAGEMENT_TOOLS
from .clientmgmt import CLIENTMGMT_TOOLS
from .banner_management import BANNER_MANAGEMENT_TOOLS
from .interfaces_management import INTERFACES_MANAGEMENT_TOOLS
from .ddc_management import DDC_MANAGEMENT_TOOLS

# Collect all available tools
ALL_TOOLS: list[Type[BaseTool]] = [
    # Core functionality (all tools now support optional domain parameters where applicable)
    *SYSTEM_TOOLS,          # 2 tools - system info (system-wide)
    *SERVICE_MGMT_TOOLS,    # 3 tools - service management (system-wide)
    *TOKEN_TOOLS,           # 5 tools - JWT/refresh tokens (with domain support)
    *USER_TOOLS,            # 10 tools - user management + password policies (with domain support)
    *GROUP_TOOLS,           # 8 tools - group management (with domain support)
    *GROUPMAP_TOOLS,        # 5 tools - group mappings (with domain support)
    *KEY_TOOLS,             # 18 tools - key management (with domain support)
    *KEY_POLICY_TOOLS,      # 5 tools - key policies (with domain support)
    *SECRET_TOOLS,          # 9 tools - secrets management (with domain support)
    *SCP_TOOLS,             # 2 tools - SCP public key management (with domain support)
    *TEMPLATE_TOOLS,        # 5 tools - template management (with domain support)
    *AKEYLESS_TOOLS,        # 7 tools - Akeyless Gateway integration (with domain support)
    *BACKUP_TOOLS,          # 11 tools - backup management (with domain support)
    *BACKUPKEY_TOOLS,       # 8 tools - backup key management (with domain support)
    *LICENSING_TOOLS,       # 10 tools - licensing (system-wide)
    *ROTKEY_TOOLS,          # 4 tools - root of trust keys (system-wide)
    *RECORD_TOOLS,          # 7 tools - audit records & alarm configs (system-wide)
    *METRICS_TOOLS,         # 5 tools - Prometheus metrics (system-wide)
    *MKEKS_TOOLS,           # 3 tools - Master KEKs (system-wide)
    *NETWORK_TOOLS,         # 5 tools - network diagnostics (system-wide)
    *NTP_TOOLS,             # 5 tools - NTP server management (system-wide)
    *PROPERTIES_TOOLS,      # 4 tools - system properties (system-wide)
    *PROXY_TOOLS,           # 11 tools - proxy configurations (system-wide)
    *QUORUM_TOOLS,          # 14 tools - quorum management (with domain support)

    # Domain management (administrative domain operations)
    *DOMAIN_TOOLS,          # 13 tools - domain admin, KEKs, log redirection

    # Connection management
    *CONNECTION_TOOLS,      # 11 clean connection management tools

    # Authentication connection management
    *CONNECTION_LDAP_TOOLS,    # 6 tools - LDAP connection management (with domain support)
    *CONNECTION_OIDC_TOOLS,    # 6 tools - OIDC connection management (with domain support)
    *CONNECTION_USERS_TOOLS,   # 2 tools - Connection users management (with domain support)

    # Cryptographic operations
    *CRYPTO_TOOLS,            # 7 tools - Encryption, signing, FPE operations (with domain support)

    # CTE (CipherTrust Transparent Encryption) management
    *CTE_CLIENTGROUP_TOOLS,   # 18 tools - CTE client group management (with domain support)
    *CTE_CLIENT_TOOLS,            # 31 tools - CTE client management (with domain support)
    *CTE_CSI_STORAGEGROUP_TOOLS,  # 14 tools - CTE CSI StorageGroup management (with domain support)
    *CTE_POLICY_TOOLS,            # 33 tools - CTE policy management (with domain support)
    *CTE_PROFILE_TOOLS,           # 6 tools - CTE profile management (with domain support)
    *CTE_PROCESS_SET_TOOLS,       # 10 tools - CTE process set management (with domain support)
    *CTE_USER_SET_TOOLS,          # 10 tools - CTE user set management (with domain support)
    *CTE_RESOURCE_SET_TOOLS,      # 10 tools - CTE resource set management (with domain support)

    # Additional management tools
    *CLUSTER_MANAGEMENT_TOOLS,
    *CLIENTMGMT_TOOLS,
    *BANNER_MANAGEMENT_TOOLS,
    *INTERFACES_MANAGEMENT_TOOLS,
    *DDC_MANAGEMENT_TOOLS,
]

all = ["BaseTool", "ALL_TOOLS"]