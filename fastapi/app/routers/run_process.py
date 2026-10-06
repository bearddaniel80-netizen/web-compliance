import json
from pathlib import Path
import asyncio
import subprocess

def _get_data_type(value):
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "string"
    return "unknown"

def _collect_column_name(response, key_field):
    unique_columns = [
        {
            "key": key,
            "label": key.title(),
            "type": _get_data_type(value)
        }
        for key, value in response.get(key_field, {}).items()
    ]
    response.update({f"{key_field}_columns": unique_columns})

def _collect_column_list_name(response, key_field):
    unique_columns = [
        {
            "key": key,
            "label": key.title(),
            "type": _get_data_type(value)
        }
        for key, value in response[key_field][0].items()
    ]
    response.update({f"{key_field}_columns": unique_columns})

async def run_query(command):
    try:
        result = await asyncio.to_thread(
            subprocess.run,
            command,
            capture_output=True,
            text=True
        )
        return result.stdout
    except:
        return " ".join(command)

async def run_test(command):
    await run_query(command)
    with open(Path.cwd() / "report.json", "r") as f:
        response = json.load(f)
        _collect_column_name(response, "summary")
        _collect_column_list_name(response, "results")
        if "query_performance" in response.keys() and len(response["query_performance"]) > 0:
            _collect_column_list_name(response, "query_performance")
        if "failures" in response.keys() and len(response["failures"]) > 0:
            _collect_column_list_name(response, "failures")
        return response