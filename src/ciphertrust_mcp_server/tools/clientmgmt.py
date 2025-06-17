from typing import Optional
from pydantic import BaseModel
from .base import BaseTool

# --- CLIENTS SUBCOMMANDS ---
class ClientListParams(BaseModel):
    ca_id: Optional[str] = None
    client_id: Optional[str] = None
    client_meta_data: Optional[str] = None
    client_mgmt_profile_id: Optional[str] = None
    client_name: Optional[str] = None
    limit: Optional[int] = None
    sha256_fingerprint: Optional[str] = None
    skip: Optional[int] = None
    state: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientGetParams(BaseModel):
    client_id: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientRegisterParams(BaseModel):
    reg_token: str
    csr: Optional[str] = None
    cert_file: Optional[str] = None
    client_type: Optional[str] = None
    client_name: Optional[str] = None
    cn: Optional[str] = None
    csrfile: Optional[str] = None
    dns: Optional[str] = None
    do_not_modify_subject_dn: Optional[bool] = None
    email: Optional[str] = None
    enc_alg: Optional[str] = None
    ips: Optional[str] = None
    names: Optional[str] = None
    pass_: Optional[str] = None
    private_key_file: Optional[str] = None
    size: Optional[int] = None
    subject_dn_field_to_modify: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientDeleteParams(BaseModel):
    client_id: str
    nowarning: Optional[bool] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientRenewParams(BaseModel):
    client_id: str
    alg: Optional[str] = None
    ca_id: Optional[str] = None
    cert_duration: Optional[int] = None
    clientcsr: Optional[str] = None
    cn: Optional[str] = None
    dns: Optional[str] = None
    do_not_modify_subject_dn: Optional[bool] = None
    email: Optional[str] = None
    enc_alg: Optional[str] = None
    ext_cert: Optional[str] = None
    ips: Optional[str] = None
    names: Optional[str] = None
    pass_: Optional[str] = None
    private_key_bytes: Optional[str] = None
    private_key_file: Optional[str] = None
    size: Optional[int] = None
    subject_dn_field_to_modify: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientRevokeParams(BaseModel):
    client_id: str
    revoke_reason: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientSelfParams(BaseModel):
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

# --- PROFILES SUBCOMMANDS ---
class ProfileCreateParams(BaseModel):
    ca_id: Optional[str] = None
    cert_duration: Optional[int] = None
    csr_params_jsonfile: Optional[str] = None
    csr_parameters: Optional[str] = None
    groups: Optional[str] = None
    name: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ProfileDeleteParams(BaseModel):
    profile_id: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ProfileGetParams(BaseModel):
    profile_id: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ProfileListParams(BaseModel):
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ProfileUpdateParams(BaseModel):
    profile_id: str
    ca_id: Optional[str] = None
    cert_duration: Optional[int] = None
    csr_params_jsonfile: Optional[str] = None
    csr_parameters: Optional[str] = None
    groups: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

# --- TOKENS SUBCOMMANDS ---
class TokenCreateParams(BaseModel):
    ca_id: Optional[str] = None
    cert_duration: Optional[int] = None
    client_mgmt_profile_id: Optional[str] = None
    label: Optional[str] = None
    life_time: Optional[str] = None
    max_clients: Optional[int] = None
    name_prefix: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class TokenDeleteParams(BaseModel):
    reg_token: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class TokenGetParams(BaseModel):
    reg_token: str
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class TokenListParams(BaseModel):
    ca_id: Optional[str] = None
    client_mgmt_profile_id: Optional[str] = None
    label: Optional[str] = None
    max_clients: Optional[int] = None
    name_prefix: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class TokenUpdateParams(BaseModel):
    reg_token: str
    ca_id: Optional[str] = None
    cert_duration: Optional[int] = None
    client_mgmt_profile_id: Optional[str] = None
    label: Optional[str] = None
    life_time: Optional[str] = None
    max_clients: Optional[int] = None
    name_prefix: Optional[str] = None
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class TokenWebcertFingerprintParams(BaseModel):
    domain: Optional[str] = None
    auth_domain: Optional[str] = None

class ClientMgmtTool(BaseTool):
    name = "clientmgmt"
    description = "CipherTrust Manager client management operations (clients, profiles, tokens)."

    def get_schema(self):
        return {
            "action": {"type": "string", "enum": [
                "clients_list", "clients_get", "clients_register", "clients_delete", "clients_renew", "clients_revoke", "clients_self",
                "profiles_create", "profiles_delete", "profiles_get", "profiles_list", "profiles_update",
                "tokens_create", "tokens_delete", "tokens_get", "tokens_list", "tokens_update", "tokens_webcert_fingerprint"
            ]},
            "params": {"type": "object"}
        }

    async def execute(self, action: str, params: dict):
        if action == "clients_list":
            p = ClientListParams(**params)
            cmd = ["clientmgmt", "clients", "list"]
            if p.ca_id: cmd += ["--ca-id", p.ca_id]
            if p.client_id: cmd += ["--client-id", p.client_id]
            if p.client_meta_data: cmd += ["--client-meta-data", p.client_meta_data]
            if p.client_mgmt_profile_id: cmd += ["--client-mgmt-profile-id", p.client_mgmt_profile_id]
            if p.client_name: cmd += ["--client-name", p.client_name]
            if p.limit is not None: cmd += ["--limit", str(p.limit)]
            if p.sha256_fingerprint: cmd += ["--sha256-fingerprint", p.sha256_fingerprint]
            if p.skip is not None: cmd += ["--skip", str(p.skip)]
            if p.state: cmd += ["--state", p.state]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_get":
            p = ClientGetParams(**params)
            cmd = ["clientmgmt", "clients", "get", "--client-id", p.client_id]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_register":
            p = ClientRegisterParams(**params)
            cmd = ["clientmgmt", "clients", "register", "--reg-token", p.reg_token]
            if p.csr: cmd += ["--csr", p.csr]
            if p.cert_file: cmd += ["--cert-file", p.cert_file]
            if p.client_type: cmd += ["--client-type", p.client_type]
            if p.client_name: cmd += ["--client-name", p.client_name]
            if p.cn: cmd += ["--cn", p.cn]
            if p.csrfile: cmd += ["--csrfile", p.csrfile]
            if p.dns: cmd += ["--dns", p.dns]
            if p.do_not_modify_subject_dn: cmd += ["--do-not-modify-subject-dn"]
            if p.email: cmd += ["--email", p.email]
            if p.enc_alg: cmd += ["--enc-alg", p.enc_alg]
            if p.ips: cmd += ["--ips", p.ips]
            if p.names: cmd += ["--names", p.names]
            if p.pass_: cmd += ["--pass", p.pass_]
            if p.private_key_file: cmd += ["--private-key-file", p.private_key_file]
            if p.size is not None: cmd += ["--size", str(p.size)]
            if p.subject_dn_field_to_modify: cmd += ["--subject-dn-field-to-modify", p.subject_dn_field_to_modify]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_delete":
            p = ClientDeleteParams(**params)
            cmd = ["clientmgmt", "clients", "delete", "--client-id", p.client_id]
            if p.nowarning: cmd += ["--nowarning"]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_renew":
            p = ClientRenewParams(**params)
            cmd = ["clientmgmt", "clients", "renew", "--client-id", p.client_id]
            if p.alg: cmd += ["--alg", p.alg]
            if p.ca_id: cmd += ["--ca-id", p.ca_id]
            if p.cert_duration is not None: cmd += ["--cert-duration", str(p.cert_duration)]
            if p.clientcsr: cmd += ["--clientcsr", p.clientcsr]
            if p.cn: cmd += ["--cn", p.cn]
            if p.dns: cmd += ["--dns", p.dns]
            if p.do_not_modify_subject_dn: cmd += ["--do-not-modify-subject-dn"]
            if p.email: cmd += ["--email", p.email]
            if p.enc_alg: cmd += ["--enc-alg", p.enc_alg]
            if p.ext_cert: cmd += ["--ext-cert", p.ext_cert]
            if p.ips: cmd += ["--ips", p.ips]
            if p.names: cmd += ["--names", p.names]
            if p.pass_: cmd += ["--pass", p.pass_]
            if p.private_key_bytes: cmd += ["--private-key-bytes", p.private_key_bytes]
            if p.private_key_file: cmd += ["--private-key-file", p.private_key_file]
            if p.size is not None: cmd += ["--size", str(p.size)]
            if p.subject_dn_field_to_modify: cmd += ["--subject-dn-field-to-modify", p.subject_dn_field_to_modify]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_revoke":
            p = ClientRevokeParams(**params)
            cmd = ["clientmgmt", "clients", "revoke", "--client-id", p.client_id]
            if p.revoke_reason: cmd += ["--revoke-reason", p.revoke_reason]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "clients_self":
            cmd = ["clientmgmt", "clients", "self"]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        # --- PROFILES ---
        elif action == "profiles_create":
            p = ProfileCreateParams(**params)
            cmd = ["clientmgmt", "profiles", "create", "--name", p.name]
            if p.ca_id: cmd += ["--ca_id", p.ca_id]
            if p.cert_duration is not None: cmd += ["--cert-duration", str(p.cert_duration)]
            if p.csr_params_jsonfile: cmd += ["--csr-params-jsonfile", p.csr_params_jsonfile]
            if p.csr_parameters: cmd += ["--csr_parameters", p.csr_parameters]
            if p.groups: cmd += ["--groups", p.groups]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "profiles_delete":
            p = ProfileDeleteParams(**params)
            cmd = ["clientmgmt", "profiles", "delete", "--profile-id", p.profile_id]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "profiles_get":
            p = ProfileGetParams(**params)
            cmd = ["clientmgmt", "profiles", "get", "--profile-id", p.profile_id]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "profiles_list":
            cmd = ["clientmgmt", "profiles", "list"]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "profiles_update":
            p = ProfileUpdateParams(**params)
            cmd = ["clientmgmt", "profiles", "update", "--profile-id", p.profile_id]
            if p.ca_id: cmd += ["--ca_id", p.ca_id]
            if p.cert_duration is not None: cmd += ["--cert-duration", str(p.cert_duration)]
            if p.csr_params_jsonfile: cmd += ["--csr-params-jsonfile", p.csr_params_jsonfile]
            if p.csr_parameters: cmd += ["--csr_parameters", p.csr_parameters]
            if p.groups: cmd += ["--groups", p.groups]
            if p.name: cmd += ["--name", p.name]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        # --- TOKENS ---
        elif action == "tokens_create":
            p = TokenCreateParams(**params)
            cmd = ["clientmgmt", "tokens", "create"]
            if p.ca_id: cmd += ["--ca-id", p.ca_id]
            if p.cert_duration is not None: cmd += ["--cert-duration", str(p.cert_duration)]
            if p.client_mgmt_profile_id: cmd += ["--client-mgmt-profile-id", p.client_mgmt_profile_id]
            if p.label: cmd += ["--label", p.label]
            if p.life_time: cmd += ["--life-time", p.life_time]
            if p.max_clients is not None: cmd += ["--max-clients", str(p.max_clients)]
            if p.name_prefix: cmd += ["--name-prefix", p.name_prefix]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "tokens_delete":
            p = TokenDeleteParams(**params)
            cmd = ["clientmgmt", "tokens", "delete", "--reg-token", p.reg_token]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "tokens_get":
            p = TokenGetParams(**params)
            cmd = ["clientmgmt", "tokens", "get", "--reg-token", p.reg_token]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "tokens_list":
            cmd = ["clientmgmt", "tokens", "list"]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "tokens_update":
            p = TokenUpdateParams(**params)
            cmd = ["clientmgmt", "tokens", "update", "--reg-token", p.reg_token]
            if p.ca_id: cmd += ["--ca-id", p.ca_id]
            if p.cert_duration is not None: cmd += ["--cert-duration", str(p.cert_duration)]
            if p.client_mgmt_profile_id: cmd += ["--client-mgmt-profile-id", p.client_mgmt_profile_id]
            if p.label: cmd += ["--label", p.label]
            if p.life_time: cmd += ["--life-time", p.life_time]
            if p.max_clients is not None: cmd += ["--max-clients", str(p.max_clients)]
            if p.name_prefix: cmd += ["--name-prefix", p.name_prefix]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        elif action == "tokens_webcert_fingerprint":
            cmd = ["clientmgmt", "tokens", "webcert-fingerprint"]
            self.add_domain_auth_params(cmd, params)
            return self.ksctl.execute(cmd)
        else:
            raise ValueError(f"Unknown action: {action}")

CLIENTMGMT_TOOLS = [ClientMgmtTool] 