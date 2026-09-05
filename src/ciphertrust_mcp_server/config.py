"""Configuration management for CipherTrust MCP Server."""

import os
from pathlib import Path
from typing import Optional

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # CipherTrust Manager settings
    ciphertrust_url: str = Field(..., description="CipherTrust Manager URL (required)")
    ciphertrust_user: Optional[str] = None
    ciphertrust_password: Optional[str] = None
    ciphertrust_jwt: Optional[str] = None
    ciphertrust_nosslverify: bool = False
    ciphertrust_timeout: int = 30
    ciphertrust_domain: str = Field(default="root")
    ciphertrust_auth_domain: str = Field(default="root")

    # ksctl settings
    ksctl_download_url: Optional[str] = None
    ksctl_path: Path = Path.home() / ".ciphertrust-mcp" / "ksctl"
    ksctl_config_path: Path = Path.home() / ".ksctl" / "config.yaml"

    # MCP server settings
    mcp_server_name: str = "ciphertrust-manager"
    mcp_server_version: str = "0.2.0"
    
    # Logging
    log_level: str = "INFO"
    debug_mode: bool = False

    @field_validator("ciphertrust_domain", "ciphertrust_auth_domain", mode="before")
    @classmethod
    def empty_domain_is_root(cls, v):
        if v is None or (isinstance(v, str) and not v.strip()):
            return "root"
        return v.strip() if isinstance(v, str) else v

    @field_validator("ciphertrust_url")
    @classmethod
    def validate_url(cls, v: str) -> str:
        """Validate CipherTrust URL."""
        if not v:
            raise ValueError("CIPHERTRUST_URL is required")
        if not v.startswith(("http://", "https://")):
            raise ValueError("CIPHERTRUST_URL must start with http:// or https://")
        return v.rstrip("/")

    @property
    def ksctl_download_url_full(self) -> str:
        """Get the full ksctl download URL."""
        if self.ksctl_download_url:
            return self.ksctl_download_url
        return f"{self.ciphertrust_url}/downloads/ksctl_images.zip"

    def get_ksctl_env(self) -> dict[str, str]:
        """Environment for ksctl. Credentials stay out of argv."""
        env = os.environ.copy()
        for key in ("KSCTL_JWT", "KSCTL_REFRESHTOKEN", "KSCTL_PASSWORD", "KSCTL_USERNAME"):
            env.pop(key, None)

        if self.ciphertrust_user and self.ciphertrust_password:
            env["KSCTL_USERNAME"] = self.ciphertrust_user
            env["KSCTL_PASSWORD"] = self.ciphertrust_password
        elif self.ciphertrust_jwt:
            env["KSCTL_JWT"] = self.ciphertrust_jwt

        env["KSCTL_URL"] = self.ciphertrust_url
        env["KSCTL_NOSSLVERIFY"] = str(self.ciphertrust_nosslverify).lower()
        env["KSCTL_TIMEOUT"] = str(self.ciphertrust_timeout)
        env["KSCTL_DOMAIN"] = self.ciphertrust_domain
        env["KSCTL_AUTH_DOMAIN"] = self.ciphertrust_auth_domain

        isolated_home = self.ksctl_path.parent / "ksctl-home"
        isolated_home.mkdir(parents=True, exist_ok=True)
        env["HOME"] = str(isolated_home)
        env["USERPROFILE"] = str(isolated_home)
        return env


# Global settings instance
settings = Settings()
