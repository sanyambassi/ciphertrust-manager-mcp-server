from typing import Optional
from pydantic import BaseModel
from .base import BaseTool

class ClusterNewParams(BaseModel):
    host: str
    public_address: Optional[str] = None

class ClusterDeleteParams(BaseModel):
    yes: bool = True

class ClusterInfoParams(BaseModel):
    pass

class ClusterSummaryParams(BaseModel):
    pass

class ClusterJoinParams(BaseModel):
    host: str
    member: str
    cachain: Optional[str] = None
    cafile: Optional[str] = None
    cert: Optional[str] = None
    certfile: Optional[str] = None
    mkek_blob: Optional[str] = None
    public_address: Optional[str] = None
    yes: bool = True

class ClusterNodesListParams(BaseModel):
    allowlist: Optional[str] = None

class ClusterNodesGetParams(BaseModel):
    id: str

class ClusterNodesDeleteParams(BaseModel):
    id: str
    force: Optional[bool] = False
    yes: bool = True

class ClusterManagementTool(BaseTool):
    name = "cluster_management"
    description = "Manage CipherTrust Manager clusters (create, join, delete, info, summary, node management)"

    def get_schema(self):
        return {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": [
                    "new", "delete", "info", "summary", "join", "nodes_list", "nodes_get", "nodes_delete"
                ]},
                "host": {"type": "string"},
                "public_address": {"type": ["string", "null"]},
                "yes": {"type": "boolean"},
                "member": {"type": "string"},
                "cachain": {"type": ["string", "null"]},
                "cafile": {"type": ["string", "null"]},
                "cert": {"type": ["string", "null"]},
                "certfile": {"type": ["string", "null"]},
                "mkek_blob": {"type": ["string", "null"]},
                "allowlist": {"type": ["string", "null"]},
                "id": {"type": "string"},
                "force": {"type": "boolean"},
            },
            "required": ["action"],
        }

    async def execute(self, **kwargs):
        action = kwargs.get("action")
        if action == "new":
            params = ClusterNewParams(**kwargs)
            cmd = ["cluster", "new", "--host", params.host]
            if params.public_address:
                cmd += ["--public-address", params.public_address]
            return self.ksctl.execute(cmd)
        elif action == "delete":
            params = ClusterDeleteParams(**kwargs)
            cmd = ["cluster", "delete"]
            if params.yes:
                cmd.append("-y")
            return self.ksctl.execute(cmd)
        elif action == "info":
            cmd = ["cluster", "info"]
            return self.ksctl.execute(cmd)
        elif action == "summary":
            cmd = ["cluster", "summary"]
            return self.ksctl.execute(cmd)
        elif action == "join":
            params = ClusterJoinParams(**kwargs)
            cmd = ["cluster", "join", "--host", params.host, "--member", params.member]
            if params.cachain:
                cmd += ["--cachain", params.cachain]
            if params.cafile:
                cmd += ["--cafile", params.cafile]
            if params.cert:
                cmd += ["--cert", params.cert]
            if params.certfile:
                cmd += ["--certfile", params.certfile]
            if params.mkek_blob:
                cmd += ["--mkek-blob", params.mkek_blob]
            if params.public_address:
                cmd += ["--public-address", params.public_address]
            if params.yes:
                cmd.append("-y")
            return self.ksctl.execute(cmd)
        elif action == "nodes_list":
            params = ClusterNodesListParams(**kwargs)
            cmd = ["cluster", "nodes", "list"]
            if params.allowlist:
                cmd += ["--allowlist", params.allowlist]
            return self.ksctl.execute(cmd)
        elif action == "nodes_get":
            params = ClusterNodesGetParams(**kwargs)
            cmd = ["cluster", "nodes", "get", "--id", params.id]
            return self.ksctl.execute(cmd)
        elif action == "nodes_delete":
            params = ClusterNodesDeleteParams(**kwargs)
            cmd = ["cluster", "nodes", "delete", "--id", params.id]
            if params.force:
                cmd.append("--force")
            if params.yes:
                cmd.append("-y")
            return self.ksctl.execute(cmd)
        else:
            raise ValueError(f"Unknown action: {action}")

CLUSTER_MANAGEMENT_TOOLS = [ClusterManagementTool] 