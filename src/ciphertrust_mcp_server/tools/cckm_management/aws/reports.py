"""AWS Reports operations for CCKM."""
from typing import Any, Dict

def get_reports_operations() -> Dict[str, Any]:
    """Return schema and action requirements for AWS reports operations."""
    return {
        "schema_properties": {
            "aws_reports_params": {
                "type": "object",
                "properties": {
                    "report_type": {"type": "string", "description": "Type of report to generate"},
                    "name": {"type": "string", "description": "Unique name for the report"},
                    "start_time": {"type": "string", "description": "Start time for report generation"},
                    "end_time": {"type": "string", "description": "End time for report generation"},
                    "id": {"type": "string", "description": "Report job ID or resource identifier for filtering"},
                    "create_report_jobs_jsonfile": {"type": "string", "description": "JSON file with report job parameters"},
                    "cloud_watch_params_jsonfile": {"type": "string", "description": "JSON file with CloudWatch parameters"},
                    "cloud_watch_params": {"type": "string", "description": "CloudWatch parameters in JSON format"},
                    "limit": {"type": "integer", "description": "Maximum number of results to return"},
                    "skip": {"type": "integer", "description": "Number of results to skip"},
                    "key_arn": {"type": "string", "description": "Filter by key ARN"},
                    "region": {"type": "string", "description": "Filter by region"},
                    "aws_account_id": {"type": "string", "description": "Filter by AWS account ID"},
                    "cloud_name": {"type": "string", "description": "Filter by cloud name"},
                    "sort": {"type": "string", "description": "Sort parameter"}
                }
            }
        },
        "action_requirements": {
            "reports_list": {"required": [], "optional": ["limit", "skip"]},
            "reports_get": {"required": ["id"], "optional": []},
            "reports_generate": {
                "required": ["report_type", "name", "start_time"], 
                "optional": ["end_time", "create_report_jobs_jsonfile", "cloud_watch_params_jsonfile"]
            },
            "reports_download": {"required": ["id"], "optional": []},
            "reports_delete": {"required": ["id"], "optional": []},
            "reports_get_reports": {
                "required": [], 
                "optional": ["id", "key_arn", "region", "aws_account_id", "cloud_name", "limit", "skip", "sort"]
            }
        }
    }

def build_reports_command(action: str, aws_params: Dict[str, Any]) -> list:
    """Build the ksctl command for a given AWS reports operation."""
    cmd = ["cckm", "aws", "reports"]
    
    # Extract the base operation name (remove 'reports_' prefix)
    base_action = action.replace("reports_", "")
    
    # Simple actions that only need --id parameter
    simple_actions = ["get", "download", "delete"]
    
    if base_action in simple_actions:
        cmd.extend([base_action, "--id", aws_params["id"]])
        return cmd
    
    if base_action == "list":
        cmd.append("list")
        if "limit" in aws_params:
            cmd.extend(["--limit", str(aws_params["limit"])])
        if "skip" in aws_params:
            cmd.extend(["--skip", str(aws_params["skip"])])
            
    elif base_action == "generate":
        cmd.append("generate-report")
        cmd.extend(["--report-type", aws_params["report_type"]])
        cmd.extend(["--name", aws_params["name"]])
        cmd.extend(["--start-time", aws_params["start_time"]])
        
        if "cloud_watch_params_jsonfile" in aws_params:
            cmd.extend(["--cloud-watch-params-jsonfile", aws_params["cloud_watch_params_jsonfile"]])
        if "end_time" in aws_params:
            cmd.extend(["--end-time", aws_params["end_time"]])

        if "create_report_jobs_jsonfile" in aws_params:
            cmd.extend(["--create-report-jobs-jsonfile", aws_params["create_report_jobs_jsonfile"]])
            
    elif base_action == "get_reports":
        cmd.append("get-reports")
        if "id" in aws_params:
            cmd.extend(["--id", aws_params["id"]])
        if "key_arn" in aws_params:
            cmd.extend(["--key-arn", aws_params["key_arn"]])
        if "region" in aws_params:
            cmd.extend(["--region", aws_params["region"]])
        if "aws_account_id" in aws_params:
            cmd.extend(["--aws-account-id", aws_params["aws_account_id"]])
        if "cloud_name" in aws_params:
            cmd.extend(["--cloud-name", aws_params["cloud_name"]])
        if "limit" in aws_params:
            cmd.extend(["--limit", str(aws_params["limit"])])
        if "skip" in aws_params:
            cmd.extend(["--skip", str(aws_params["skip"])])
        if "sort" in aws_params:
            cmd.extend(["--sort", aws_params["sort"]])
    else:
        raise ValueError(f"Unsupported reports action: {action}")
        
    return cmd
